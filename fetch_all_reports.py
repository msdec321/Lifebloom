#!/usr/bin/env python3
"""
Fetch All Reports for Players

Takes a comparison CSV file containing players' "best" reports and fetches
all of their reports for the same encounter.

Usage:
    python fetch_all_reports.py <encounter_id> <comparison_file> <output_file> [--phase N]

Examples:
    python fetch_all_reports.py 725 data/t6/brutallus.csv data/t6/brutallus_all_reports.csv
    python fetch_all_reports.py 727 data/t6/eredar_twins_p1.csv data/t6/eredar_twins_p1_all_reports.csv --phase 1
"""

import sys
import csv
import time
import requests
import os
from datetime import datetime
from auth import get_user_access_token
from analyze_druid import analyze_druid_performance

# API Configuration
API_URL = "https://www.warcraftlogs.com/api/v2/user"

# Rate limiting configuration
BASE_DELAY = 2.0  # Base delay between API calls
SAVE_INTERVAL = 10  # Save every N new entries
RATE_CHECK_INTERVAL = 10  # Check rate limit every N reports
RATE_THRESHOLD = 0.70  # Increase delay if using more than 70% of limit
HIGH_USAGE_THRESHOLD = 0.90  # Pause if usage exceeds 90%
WAIT_INTERVAL = 600  # Wait 10 minutes (600 seconds) before rechecking


def check_rate_limit():
    """
    Query the current rate limit status.

    Returns:
        dict with keys: limitPerHour, pointsSpentThisHour, pointsResetIn, percentUsed
    """
    query = """
    query {
        rateLimitData {
            limitPerHour
            pointsSpentThisHour
            pointsResetIn
        }
    }
    """

    response = requests.post(
        API_URL,
        json={"query": query},
        headers=get_headers()
    )

    if response.status_code == 200:
        result = response.json()
        data = result.get("data", {}).get("rateLimitData", {})
        if data:
            limit = data.get("limitPerHour", 3600)
            spent = data.get("pointsSpentThisHour", 0)
            reset_in = data.get("pointsResetIn", 0)
            percent_used = (spent / limit * 100) if limit > 0 else 0

            return {
                "limitPerHour": limit,
                "pointsSpentThisHour": spent,
                "pointsResetIn": reset_in,
                "percentUsed": percent_used
            }

    # Return default values if query fails
    return {
        "limitPerHour": 3600,
        "pointsSpentThisHour": 0,
        "pointsResetIn": 3600,
        "percentUsed": 0
    }


def wait_for_rate_limit():
    """
    Wait for rate limit usage to drop below HIGH_USAGE_THRESHOLD.

    Checks rate limit every WAIT_INTERVAL (10 minutes) until usage drops below 90%.
    This prevents hitting the hourly rate limit cap.
    """
    while True:
        rate_status = check_rate_limit()
        percent_used = rate_status['percentUsed']

        if percent_used < HIGH_USAGE_THRESHOLD * 100:
            print(f"  ✅ Rate limit OK: {percent_used:.1f}% used. Continuing...")
            return

        # Still over threshold, wait and check again
        minutes = WAIT_INTERVAL / 60
        print(f"  ⏸️  High usage: {percent_used:.1f}% of {rate_status['limitPerHour']} points used")
        print(f"  ⏰ Waiting {minutes:.0f} minutes before rechecking...")

        time.sleep(WAIT_INTERVAL)
        print(f"  🔄 Rechecking rate limit status...")


def get_headers():
    """Get fresh API headers with current access token."""
    access_token = get_user_access_token()
    return {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }


def get_character_id_from_report(report_code, fight_id, player_name):
    """
    Get the WarcraftLogs character ID for a player from a report's rankings.

    Args:
        report_code: The report code
        fight_id: The fight ID within the report (optional, will find first matching fight)
        player_name: The player's name to find

    Returns:
        Character ID if found, None otherwise
    """
    query = f"""
    query {{
      reportData {{
        report(code: "{report_code}") {{
          rankings(playerMetric: hps)
        }}
      }}
    }}
    """

    try:
        response = requests.post(
            API_URL,
            json={"query": query},
            headers=get_headers(),
            timeout=30
        )

        if response.status_code != 200:
            return None

        result = response.json()
        rankings_data = result.get("data", {}).get("reportData", {}).get("report", {}).get("rankings", {})

        if not rankings_data or "data" not in rankings_data:
            return None

        # Search through all fights' rankings
        for fight_ranking in rankings_data.get("data", []):
            roles = fight_ranking.get("roles", {})

            # Check healers
            healers = roles.get("healers", {}).get("characters", [])
            for healer in healers:
                if healer.get("name") == player_name:
                    return healer.get("id")

        return None

    except Exception as e:
        print(f"    Error getting character ID: {e}")
        return None


def get_all_parses_for_character(character_id, encounter_id):
    """
    Get all parses for a character on a specific encounter.

    Args:
        character_id: The WarcraftLogs character ID
        encounter_id: The encounter ID (e.g., 725 for Brutallus)

    Returns:
        List of parse info dicts with report_code, fight_id, amount (HPS)
    """
    query = f"""
    query {{
      characterData {{
        character(id: {character_id}) {{
          name
          encounterRankings(encounterID: {encounter_id}, metric: hps)
        }}
      }}
    }}
    """

    try:
        response = requests.post(
            API_URL,
            json={"query": query},
            headers=get_headers(),
            timeout=30
        )

        if response.status_code != 200:
            return []

        result = response.json()
        character = result.get("data", {}).get("characterData", {}).get("character")

        if not character:
            return []

        rankings = character.get("encounterRankings", {})
        if not rankings or "ranks" not in rankings:
            return []

        parses = []
        for rank in rankings.get("ranks", []):
            report = rank.get("report", {})
            parses.append({
                "report_code": report.get("code"),
                "fight_id": report.get("fightID"),
                "amount": rank.get("amount", 0),
                "duration": rank.get("duration", 0),
                "start_time": rank.get("startTime", 0),
                "rank_percent": rank.get("rankPercent", 0)
            })

        return parses

    except Exception as e:
        print(f"    Error getting parses: {e}")
        return []


def load_existing_reports(output_file):
    """Load existing report IDs from output file."""
    existing_reports = set()

    if os.path.exists(output_file):
        with open(output_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                existing_reports.add(row.get('ReportID'))

    return existing_reports


def load_comparison_file(comparison_file):
    """Load players from comparison CSV file."""
    players = []

    with open(comparison_file, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            players.append({
                'name': row.get('Name'),
                'server': row.get('Server'),
                'region': row.get('Region'),
                'report_id': row.get('ReportID'),
                'hps': float(row.get('HPS', 0))
            })

    return players


def save_data(output_file, data, fieldnames):
    """Sort by HPS descending, recompute ranks, and save to CSV."""
    # Sort by HPS descending
    data.sort(key=lambda x: float(x.get('HPS', 0) or 0), reverse=True)

    # Recompute ranks
    for i, row in enumerate(data, start=1):
        row['Rank'] = i

    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def main():
    """Main execution function."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Fetch all reports for players from a comparison CSV",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python fetch_all_reports.py 725 data/t6/brutallus.csv data/t6/brutallus_all_reports.csv
    python fetch_all_reports.py 727 data/t6/eredar_twins_p1.csv data/t6/eredar_twins_p1_all_reports.csv --phase 1
    python fetch_all_reports.py 727 data/t6/eredar_twins_p2.csv data/t6/eredar_twins_p2_all_reports.csv -p 2

Common Sunwell Plateau encounter IDs:
    725 - Brutallus
    726 - Felmyst
    727 - The Eredar Twins (use --phase 1 or --phase 2)
    728 - M'uru
    729 - Kil'jaeden
        """
    )

    parser.add_argument("encounter_id", type=int, help="WarcraftLogs encounter ID")
    parser.add_argument("comparison_file", help="Input CSV with players' best reports")
    parser.add_argument("output_file", help="Output CSV for all reports")
    parser.add_argument("--phase", "-p", type=int, choices=[1, 2],
                        help="Phase number for multi-phase encounters (e.g., Eredar Twins)")
    parser.add_argument("--limit", "-l", type=int, default=None,
                        help="Limit number of players to process (for testing)")

    args = parser.parse_args()

    encounter_id = args.encounter_id
    comparison_file = args.comparison_file
    output_file = args.output_file
    phase = args.phase
    player_limit = args.limit

    # Validate comparison file exists
    if not os.path.exists(comparison_file):
        print(f"Error: Comparison file '{comparison_file}' not found!")
        return 1

    print("=" * 80)
    print("FETCH ALL REPORTS FOR PLAYERS")
    print("=" * 80)
    print(f"Encounter ID: {encounter_id}")
    if phase:
        print(f"Phase: {phase}")
    print(f"Comparison file: {comparison_file}")
    print(f"Output file: {output_file}")
    print()

    # Load existing data
    existing_reports = load_existing_reports(output_file)
    print(f"Found {len(existing_reports)} existing reports in output file")

    # Load existing output data for appending
    existing_data = []
    if os.path.exists(output_file):
        with open(output_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            existing_data = list(reader)

    # Load players from comparison file
    players = load_comparison_file(comparison_file)
    print(f"Found {len(players)} players in comparison file")

    if player_limit:
        players = players[:player_limit]
        print(f"Limited to first {player_limit} players")
    print()

    # Get encounter name
    encounter_query = f"""
    query {{
      worldData {{
        encounter(id: {encounter_id}) {{
          name
        }}
      }}
    }}
    """

    response = requests.post(API_URL, json={"query": encounter_query}, headers=get_headers())
    encounter_name = "Unknown"
    if response.status_code == 200:
        result = response.json()
        encounter_name = result.get("data", {}).get("worldData", {}).get("encounter", {}).get("name", "Unknown")

    print(f"Encounter: {encounter_name}")
    print()

    # Check initial rate limit status
    rate_status = check_rate_limit()
    print(f"Rate Limit Status: {rate_status['pointsSpentThisHour']}/{rate_status['limitPerHour']} points used ({rate_status['percentUsed']:.1f}%)")
    print(f"Points reset in: {rate_status['pointsResetIn']} seconds")
    print()

    # CSV fieldnames (same as analyze_top_rankings.py)
    fieldnames = [
        'Rank', 'Name', 'Server', 'Region', 'Date', 'Duration', 'ReportID', 'ReportLink', 'HPS',
        'HasteSummary', 'HasteGear', 'Spirit', 'Intellect', 'TotalHealers',
        'nDruid', 'nPaladin', 'nHPriest', 'nDPriest', 'nShaman',
        'RaidDamageTakenPerSecond',
        'VampiricTouch', 'InnervateCount', 'Bloodlust', 'NaturesGrace',
        'Trinket1', 'Trinket2',
        'LifebloomUptime', 'LifebloomHPS', 'LifebloomPercentHPS',
        'RejuvenationHPS', 'RejuvenationPercentHPS',
        'RegrowthHPS', 'RegrowthPercentHPS',
        'Rotation1', 'Rotation1Percent', 'Rotation2', 'Rotation2Percent',
        'TankRotationPercent', 'RotatingOnTank'
    ]

    # Track progress
    new_reports_count = 0
    skipped_reports_count = 0
    failed_players_count = 0
    processed_characters = set()  # Track by character ID to avoid duplicates

    for idx, player in enumerate(players):
        player_name = player['name']
        player_server = player['server']
        player_region = player['region']
        player_report = player['report_id']

        print(f"[{idx + 1}/{len(players)}] Processing {player_name} ({player_server}-{player_region})...")

        # Get character ID from their known report
        print(f"  Looking up character ID from report {player_report}...")
        character_id = get_character_id_from_report(player_report, None, player_name)

        if not character_id:
            print(f"  Could not find character ID, skipping...")
            failed_players_count += 1
            continue

        # Skip if we've already processed this character
        if character_id in processed_characters:
            print(f"  Already processed this character (ID: {character_id}), skipping...")
            continue

        processed_characters.add(character_id)
        print(f"  Found character ID: {character_id}")

        # Get all parses for this character
        time.sleep(BASE_DELAY)
        print(f"  Fetching all parses for encounter {encounter_id}...")
        parses = get_all_parses_for_character(character_id, encounter_id)

        if not parses:
            print(f"  No parses found, skipping...")
            continue

        print(f"  Found {len(parses)} total parses")

        # Process each parse
        for parse in parses:
            report_code = parse['report_code']

            # Check if we already have this report
            if report_code in existing_reports:
                skipped_reports_count += 1
                continue

            print(f"    Analyzing report {report_code}...")

            try:
                time.sleep(BASE_DELAY)
                data = analyze_druid_performance(report_code, encounter_name, player_name, phase)

                # Extract stats
                stats = data['player_stats']
                trinkets_data = data['player_trinkets']
                ranking_data = data['player_ranking']

                trinket_list = trinkets_data.get('trinkets', [])
                trinket1 = trinket_list[0].get('name', '') if len(trinket_list) > 0 else ''
                trinket2 = trinket_list[1].get('name', '') if len(trinket_list) > 1 else ''

                total_hps = ranking_data.get('hps', 0)

                # Calculate percentages
                lifebloom_hps = data['lifebloom_hps']
                lifebloom_percent = (lifebloom_hps / total_hps * 100) if total_hps > 0 else 0

                rejuvenation_hps = data['rejuvenation_hps']
                rejuvenation_percent = (rejuvenation_hps / total_hps * 100) if total_hps > 0 else 0

                regrowth_hps = data['regrowth_total_hps']
                regrowth_percent = (regrowth_hps / total_hps * 100) if total_hps > 0 else 0

                # Rotation patterns
                sorted_patterns = data['sorted_patterns']
                rotation1 = sorted_patterns[0][0] if len(sorted_patterns) > 0 else ''
                rotation1_count = sorted_patterns[0][1] if len(sorted_patterns) > 0 else 0
                total_rotations = len(data['actual_rotations'])
                rotation1_percent = (rotation1_count / total_rotations * 100) if total_rotations > 0 else 0

                rotation2 = sorted_patterns[1][0] if len(sorted_patterns) > 1 else ''
                rotation2_count = sorted_patterns[1][1] if len(sorted_patterns) > 1 else 0
                rotation2_percent = (rotation2_count / total_rotations * 100) if total_rotations > 0 else 0

                # Healer composition
                healer_comp = data['healer_composition']
                n_druid = len(healer_comp.get('Restoration Druid', []))
                n_paladin = len(healer_comp.get('Holy Paladin', []))
                n_hpriest = len(healer_comp.get('Holy Priest', []))
                n_dpriest = len(healer_comp.get('Discipline Priest', []))
                n_shaman = len(healer_comp.get('Restoration Shaman', []))

                # Build row
                encounter_date = datetime.fromtimestamp(data['timestamp'] / 1000)
                date_str = encounter_date.strftime("%Y-%m-%d %H:%M:%S")
                duration_str = f"{data['duration_minutes']}m {data['duration_seconds']}s"

                row = {
                    'Rank': 0,  # Will be recomputed on save
                    'Name': player_name,
                    'Server': player_server,
                    'Region': player_region,
                    'Date': date_str,
                    'Duration': duration_str,
                    'ReportID': report_code,
                    'ReportLink': f"https://classic.warcraftlogs.com/reports/{report_code}?fight={data['fight_id']}&source={data['player_id']}&type=healing",
                    'HPS': round(total_hps, 2),
                    'HasteSummary': stats.get('haste_summary', 0) if stats.get('has_stats') else 0,
                    'HasteGear': stats.get('haste_gear', 0) if stats.get('has_stats') else 0,
                    'Spirit': stats.get('spirit', 0) if stats.get('has_stats') else 0,
                    'Intellect': stats.get('intellect', 0) if stats.get('has_stats') else 0,
                    'TotalHealers': data['total_healers'],
                    'nDruid': n_druid,
                    'nPaladin': n_paladin,
                    'nHPriest': n_hpriest,
                    'nDPriest': n_dpriest,
                    'nShaman': n_shaman,
                    'RaidDamageTakenPerSecond': round(data['raid_damage_taken_per_second'], 2),
                    'VampiricTouch': 'Yes' if data['has_vampiric_touch'] else 'No',
                    'InnervateCount': data['innervate_count'],
                    'Bloodlust': 'Yes' if data['has_bloodlust'] else 'No',
                    'NaturesGrace': 'Yes' if data['has_natures_grace'] else 'No',
                    'Trinket1': trinket1,
                    'Trinket2': trinket2,
                    'LifebloomUptime': round(data['lifebloom_uptime_percent'], 2),
                    'LifebloomHPS': round(lifebloom_hps, 2),
                    'LifebloomPercentHPS': round(lifebloom_percent, 2),
                    'RejuvenationHPS': round(rejuvenation_hps, 2),
                    'RejuvenationPercentHPS': round(rejuvenation_percent, 2),
                    'RegrowthHPS': round(regrowth_hps, 2),
                    'RegrowthPercentHPS': round(regrowth_percent, 2),
                    'Rotation1': rotation1,
                    'Rotation1Percent': round(rotation1_percent, 2),
                    'Rotation2': rotation2,
                    'Rotation2Percent': round(rotation2_percent, 2),
                    'TankRotationPercent': round(data['tank_rotation_percent'], 2),
                    'RotatingOnTank': 'Yes' if data['rotating_on_tank'] else 'No'
                }

                existing_data.append(row)
                existing_reports.add(report_code)
                new_reports_count += 1

                print(f"      Added: {total_hps:.2f} HPS")

                # Save periodically
                if new_reports_count % SAVE_INTERVAL == 0:
                    print(f"  Saving progress ({len(existing_data)} total entries)...")
                    save_data(output_file, existing_data, fieldnames)

                # Check rate limit periodically
                if new_reports_count % RATE_CHECK_INTERVAL == 0:
                    rate_status = check_rate_limit()
                    percent_used = rate_status['percentUsed']
                    print(f"  📊 Rate check: {rate_status['pointsSpentThisHour']}/{rate_status['limitPerHour']} ({percent_used:.1f}%)")

                    # If we're at or over 90%, wait until usage drops
                    if percent_used >= HIGH_USAGE_THRESHOLD * 100:
                        print(f"  🛑 Usage at {percent_used:.1f}% - pausing to avoid hitting rate limit")
                        wait_for_rate_limit()

            except Exception as e:
                print(f"      Error analyzing report: {e}")
                continue

    # Final save
    print()
    print(f"Saving final results...")
    save_data(output_file, existing_data, fieldnames)

    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Players processed: {len(players)}")
    print(f"Players failed: {failed_players_count}")
    print(f"Unique characters: {len(processed_characters)}")
    print(f"New reports added: {new_reports_count}")
    print(f"Reports skipped (already exist): {skipped_reports_count}")
    print(f"Total reports in output: {len(existing_data)}")
    print("=" * 80)

    return 0


if __name__ == "__main__":
    exit(main())
