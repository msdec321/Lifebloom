#!/usr/bin/env python3
"""
Analyze Top Rankings for Restoration Druids

Fetches top rankings for a boss and analyzes each player's performance,
saving comprehensive data to a CSV file.

Usage:
    python analyze_top_rankings.py <encounter_id> <start_rank> <end_rank> <output_file>

Example:
    python analyze_top_rankings.py 725 1 100 brutallus_top100.csv
"""

import sys
import csv
import time
import requests
from datetime import datetime
from collections import Counter
from auth import get_user_access_token

# API Configuration
API_URL = "https://www.warcraftlogs.com/api/v2/user"

# Import the analysis function from analyze_druid
from analyze_druid import analyze_druid_performance

# Rate limiting configuration
BASE_DELAY = 2.0  # Base delay between players in seconds
MAX_DELAY = 10.0  # Maximum delay in seconds
RATE_CHECK_INTERVAL = 10  # Check rate limit every N players
RATE_THRESHOLD = 0.70  # Increase delay if using more than 70% of limit
HIGH_USAGE_THRESHOLD = 0.90  # Pause if usage exceeds 90%
WAIT_INTERVAL = 600  # Wait 10 minutes (600 seconds) before rechecking


def check_rate_limit():
    """
    Query the current rate limit status.

    Returns:
        dict with keys: limitPerHour, pointsSpentThisHour, pointsResetIn, percentUsed
    """
    access_token = get_user_access_token()
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

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
        headers=headers
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


def fetch_rankings(encounter_id, start_rank=1, end_rank=100):
    """
    Fetch rankings for a specific encounter within a rank range.

    Returns: (rankings_list, encounter_name)
    """
    access_token = get_user_access_token()
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    page_size = 100  # WarcraftLogs API returns 100 items per page, not 50!
    # WarcraftLogs API uses 1-indexed pages:
    # Page 1 = ranks 1-100, Page 2 = ranks 101-200, etc.
    start_page = ((start_rank - 1) // page_size) + 1
    end_page = ((end_rank - 1) // page_size) + 1

    all_rankings = []
    encounter_name = None

    # Calculate the first rank that will be in all_rankings
    # For 1-indexed pages: page N contains ranks ((N-1)*100+1) to (N*100)
    first_rank_in_list = (start_page - 1) * page_size + 1

    for page in range(start_page, end_page + 1):
        print(f"Fetching rankings page {page}...")

        query = """
        query ($encounterId: Int!, $page: Int!) {
          worldData {
            encounter(id: $encounterId) {
              id
              name
              characterRankings(
                className: "Druid"
                specName: "Restoration"
                metric: hps
                page: $page
              )
            }
          }
        }
        """

        variables = {
            "encounterId": encounter_id,
            "page": page
        }

        response = requests.post(
            API_URL,
            json={"query": query, "variables": variables},
            headers=headers
        )

        if response.status_code != 200:
            raise Exception(f"Query failed: {response.status_code} - {response.text}")

        result = response.json()
        if "errors" in result:
            raise Exception(f"GraphQL errors: {result['errors']}")

        encounter_data = result.get("data", {}).get("worldData", {}).get("encounter")
        if not encounter_data:
            raise Exception(f"Encounter {encounter_id} not found!")

        if encounter_name is None:
            encounter_name = encounter_data.get("name", "Unknown")

        rankings_json = encounter_data.get("characterRankings")
        if not rankings_json:
            break

        if isinstance(rankings_json, dict):
            rankings = rankings_json.get("rankings", [])
            # Keep ALL rankings including Anonymous - we'll filter later
            all_rankings.extend(rankings)

            has_more = rankings_json.get("hasMorePages", False)
            if not has_more:
                break

    # Fetch additional pages if needed to get enough ranks
    # We need enough rankings to cover up to end_rank
    needed_count = end_rank - first_rank_in_list + 1
    while len(all_rankings) < needed_count and has_more:
        page += 1
        print(f"Fetching additional page {page}...")

        response = requests.post(
            API_URL,
            json={"query": query, "variables": {
                "encounterId": encounter_id,
                "page": page
            }},
            headers=headers
        )

        if response.status_code == 200:
            result = response.json()
            encounter_data = result.get("data", {}).get("worldData", {}).get("encounter")
            rankings_json = encounter_data.get("characterRankings")

            if rankings_json and isinstance(rankings_json, dict):
                rankings = rankings_json.get("rankings", [])
                # Keep ALL rankings including Anonymous
                all_rankings.extend(rankings)
                has_more = rankings_json.get("hasMorePages", False)
            else:
                break

    # Slice to get the desired rank range
    # Calculate correct indices: all_rankings starts from first_rank_in_list, not rank 1
    start_index = start_rank - first_rank_in_list
    end_index = end_rank - first_rank_in_list + 1
    result = all_rankings[start_index:end_index]

    # Add the actual rank to each ranking before filtering
    for i, ranking in enumerate(result):
        ranking['actual_rank'] = start_rank + i

    # NOW filter out Anonymous players from the result
    result = [r for r in result if r.get("name") != "Anonymous"]

    return result, encounter_name


def analyze_ranking(ranking, rank_number, encounter_name):
    """
    Analyze a single ranking entry and return CSV row data.

    Returns: dict with all CSV columns
    """
    # Extract basic info from ranking
    player_name = ranking.get("name", "Unknown")
    report_info = ranking.get("report", {})
    report_code = report_info.get("code", "Unknown")
    fight_id = report_info.get("fightID")

    server_info = ranking.get("server", {})
    server_name = server_info.get("name", "Unknown")
    server_region = server_info.get("region", "Unknown")

    print(f"  Analyzing Rank #{rank_number}: {player_name} (Report: {report_code}, Fight: {fight_id})")

    try:
        # Run the full analysis
        data = analyze_druid_performance(report_code, encounter_name, player_name)

        # Extract date and duration
        encounter_date = datetime.fromtimestamp(data['timestamp'] / 1000)
        date_str = encounter_date.strftime("%Y-%m-%d %H:%M:%S")
        duration_str = f"{data['duration_minutes']}m {data['duration_seconds']}s"

        # Extract stats
        stats = data['player_stats']
        intellect = stats.get('intellect', 0) if stats.get('has_stats') else 0
        spirit = stats.get('spirit', 0) if stats.get('has_stats') else 0
        haste_summary = stats.get('haste_summary', 0) if stats.get('has_stats') else 0
        haste_gear = stats.get('haste_gear', 0) if stats.get('has_stats') else 0

        # Extract trinkets
        trinkets_data = data['player_trinkets']
        trinket_list = trinkets_data.get('trinkets', [])
        trinket1 = trinket_list[0].get('name', '') if len(trinket_list) > 0 else ''
        trinket2 = trinket_list[1].get('name', '') if len(trinket_list) > 1 else ''

        # Extract HPS data
        ranking_data = data['player_ranking']
        total_hps = ranking_data.get('hps', 0)

        lifebloom_hps = data['lifebloom_hps']
        lifebloom_percent = (lifebloom_hps / total_hps * 100) if total_hps > 0 else 0

        rejuvenation_hps = data['rejuvenation_hps']
        rejuvenation_percent = (rejuvenation_hps / total_hps * 100) if total_hps > 0 else 0

        regrowth_hps = data['regrowth_total_hps']
        regrowth_percent = (regrowth_hps / total_hps * 100) if total_hps > 0 else 0

        # Extract rotation patterns
        sorted_patterns = data['sorted_patterns']
        rotation1 = sorted_patterns[0][0] if len(sorted_patterns) > 0 else ''
        rotation1_count = sorted_patterns[0][1] if len(sorted_patterns) > 0 else 0
        total_rotations = len(data['actual_rotations'])
        rotation1_percent = (rotation1_count / total_rotations * 100) if total_rotations > 0 else 0

        rotation2 = sorted_patterns[1][0] if len(sorted_patterns) > 1 else ''
        rotation2_count = sorted_patterns[1][1] if len(sorted_patterns) > 1 else 0
        rotation2_percent = (rotation2_count / total_rotations * 100) if total_rotations > 0 else 0

        # Extract healer composition counts
        healer_comp = data['healer_composition']
        n_druid = len(healer_comp.get('Restoration Druid', []))
        n_paladin = len(healer_comp.get('Holy Paladin', []))
        n_hpriest = len(healer_comp.get('Holy Priest', []))
        n_dpriest = len(healer_comp.get('Discipline Priest', []))
        n_shaman = len(healer_comp.get('Restoration Shaman', []))

        # Build report link
        fight_id = data['fight_id']
        player_id = data['player_id']
        report_link = f"https://classic.warcraftlogs.com/reports/{report_code}?fight={fight_id}&source={player_id}&type=healing"

        # Build CSV row
        row = {
            'Rank': rank_number,
            'Name': player_name,
            'Server': server_name,
            'Region': server_region,
            'Date': date_str,
            'Duration': duration_str,
            'ReportID': report_code,
            'ReportLink': report_link,
            'HPS': round(total_hps, 2),
            'HasteSummary': haste_summary,
            'HasteGear': haste_gear,
            'Spirit': spirit,
            'Intellect': intellect,
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

        return row

    except Exception as e:
        print(f"    ERROR analyzing {player_name}: {e}")
        # Return a row with basic info and error indicators
        return {
            'Rank': rank_number,
            'Name': player_name,
            'Server': server_name,
            'Region': server_region,
            'Date': '',
            'Duration': '',
            'ReportID': report_code,
            'ReportLink': '',
            'HPS': 0,
            'HasteSummary': 0,
            'HasteGear': 0,
            'Spirit': 0,
            'Intellect': 0,
            'TotalHealers': 0,
            'nDruid': 0,
            'nPaladin': 0,
            'nHPriest': 0,
            'nDPriest': 0,
            'nShaman': 0,
            'RaidDamageTakenPerSecond': 0,
            'VampiricTouch': 'ERROR',
            'InnervateCount': 0,
            'Bloodlust': 'ERROR',
            'NaturesGrace': 'ERROR',
            'Trinket1': '',
            'Trinket2': '',
            'LifebloomUptime': 0,
            'LifebloomHPS': 0,
            'LifebloomPercentHPS': 0,
            'RejuvenationHPS': 0,
            'RejuvenationPercentHPS': 0,
            'RegrowthHPS': 0,
            'RegrowthPercentHPS': 0,
            'Rotation1': '',
            'Rotation1Percent': 0,
            'Rotation2': '',
            'Rotation2Percent': 0,
            'TankRotationPercent': 0,
            'RotatingOnTank': 'ERROR'
        }


def main():
    """Main execution function"""
    if len(sys.argv) != 5:
        print("Usage: python analyze_top_rankings.py <encounter_id> <start_rank> <end_rank> <output_file>")
        print("\nExample:")
        print("  python analyze_top_rankings.py 725 1 100 brutallus_top100.csv")
        print("  python analyze_top_rankings.py 729 1 50 kiljaeden_top50.csv")
        print("\nCommon Sunwell Plateau encounter IDs:")
        print("  725 - Brutallus")
        print("  726 - Felmyst")
        print("  727 - The Eredar Twins")
        print("  728 - M'uru")
        print("  729 - Kil'jaeden")
        return 1

    encounter_id = int(sys.argv[1])
    start_rank = int(sys.argv[2])
    end_rank = int(sys.argv[3])
    output_file = sys.argv[4]

    if start_rank < 1:
        print("Error: start_rank must be at least 1")
        return 1

    if end_rank < start_rank:
        print("Error: end_rank must be greater than or equal to start_rank")
        return 1

    print("=" * 80)
    print("WARCRAFTLOGS TOP RANKINGS ANALYSIS")
    print("=" * 80)
    print()

    try:
        # Fetch rankings
        print(f"Fetching rankings {start_rank}-{end_rank} for encounter {encounter_id}...")
        rankings, encounter_name = fetch_rankings(encounter_id, start_rank, end_rank)
        print(f"\n✓ Found {len(rankings)} rankings for {encounter_name}")
        print()

        # Prepare CSV
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

        # Load existing data if CSV exists
        existing_data = []
        existing_report_ids = set()

        import os
        if os.path.exists(output_file):
            print(f"✓ Found existing CSV file: {output_file}")
            print(f"  Loading existing data...")

            with open(output_file, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    existing_data.append(row)
                    existing_report_ids.add(row['ReportID'])

            print(f"  Loaded {len(existing_data)} existing entries")
            print()
        else:
            print(f"✓ Creating new CSV file: {output_file}")
            print()

        # Analyze each ranking
        print(f"Analyzing {len(rankings)} players...")

        # Check initial rate limit status
        rate_status = check_rate_limit()
        print(f"  📊 Rate Limit Status: {rate_status['pointsSpentThisHour']}/{rate_status['limitPerHour']} points used ({rate_status['percentUsed']:.1f}%)")
        print(f"  ⏰ Points reset in: {rate_status['pointsResetIn']} seconds")
        print()

        new_count = 0
        skipped_count = 0
        SAVE_INTERVAL = 10  # Save every 10 new entries
        current_delay = BASE_DELAY  # Start with base delay

        def save_progress():
            """Sort and save all data to CSV"""
            print(f"  💾 Saving progress... ({len(existing_data)} total entries)")
            existing_data.sort(key=lambda x: int(x['Rank']))
            with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for row in existing_data:
                    writer.writerow(row)

        for idx, ranking in enumerate(rankings):
            # Use the actual rank that we added during fetch (before Anonymous filtering)
            rank_number = ranking.get("actual_rank", start_rank + idx)
            report_info = ranking.get("report", {})
            report_code = report_info.get("code", "Unknown")

            # Check if this report already exists
            if report_code in existing_report_ids:
                player_name = ranking.get("name", "Unknown")
                print(f"  Skipping Rank #{rank_number}: {player_name} (Report: {report_code}) - already exists")
                skipped_count += 1
                continue

            # Analyze new player
            row_data = analyze_ranking(ranking, rank_number, encounter_name)
            existing_data.append(row_data)
            existing_report_ids.add(report_code)  # Add to set to prevent duplicates in same run
            new_count += 1

            # Check rate limit periodically and adjust delay
            if new_count % RATE_CHECK_INTERVAL == 0:
                rate_status = check_rate_limit()
                percent_used = rate_status['percentUsed']

                print(f"  📊 Rate check after {new_count} players: {rate_status['pointsSpentThisHour']}/{rate_status['limitPerHour']} ({percent_used:.1f}%)")

                # If we're at or over 90%, wait until usage drops
                if percent_used >= HIGH_USAGE_THRESHOLD * 100:
                    print(f"  🛑 Usage at {percent_used:.1f}% - pausing to avoid hitting rate limit")
                    wait_for_rate_limit()
                    current_delay = BASE_DELAY  # Reset delay after waiting

                # Adjust delay based on usage
                elif percent_used > RATE_THRESHOLD * 100:
                    # Calculate new delay proportional to usage
                    scale_factor = percent_used / (RATE_THRESHOLD * 100)
                    current_delay = min(BASE_DELAY * scale_factor, MAX_DELAY)
                    print(f"  ⚠️  High usage detected! Increasing delay to {current_delay:.1f}s")
                elif percent_used < (RATE_THRESHOLD * 100 * 0.5):
                    # If usage is low, we can reduce delay
                    current_delay = max(BASE_DELAY * 0.5, 1.0)
                    print(f"  ✅ Low usage, reducing delay to {current_delay:.1f}s")
                else:
                    current_delay = BASE_DELAY

            # Save progress every 10 new entries
            if new_count % SAVE_INTERVAL == 0:
                save_progress()

            # Apply delay between players (except for the last one)
            if idx < len(rankings) - 1 and not (report_code in existing_report_ids):
                time.sleep(current_delay)

        print()
        print(f"✓ Analysis complete: {new_count} new entries, {skipped_count} skipped")
        print()

        # Final save if there are unsaved changes
        if new_count % SAVE_INTERVAL != 0 or new_count == 0:
            print("Saving final results...")
            save_progress()
        else:
            print("All data already saved!")

        print(f"✓ Total entries in CSV: {len(existing_data)}")

        print()
        print("=" * 80)
        print(f"✓ Analysis complete! Data saved to {output_file}")
        print("=" * 80)
        return 0

    except Exception as e:
        print()
        print("=" * 70)
        print("ERROR")
        print("=" * 70)
        print(f"{e}")
        print("=" * 70)
        return 1


if __name__ == "__main__":
    exit(main())
