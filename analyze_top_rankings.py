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
import requests
from datetime import datetime
from collections import Counter
from auth import get_user_access_token

# API Configuration
API_URL = "https://www.warcraftlogs.com/api/v2/user"

# Import the analysis function from analyze_druid
from analyze_druid import analyze_druid_performance


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

    page_size = 50
    start_page = ((start_rank - 1) // page_size) + 1
    end_page = ((end_rank - 1) // page_size) + 1

    all_rankings = []
    encounter_name = None

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
            for ranking in rankings:
                # Filter out Anonymous players
                if ranking.get("name") != "Anonymous":
                    all_rankings.append(ranking)

            has_more = rankings_json.get("hasMorePages", False)
            if not has_more:
                break

    # Fetch additional pages if needed due to filtering
    while len(all_rankings) < end_rank and has_more:
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
                for ranking in rankings:
                    if ranking.get("name") != "Anonymous":
                        all_rankings.append(ranking)
                has_more = rankings_json.get("hasMorePages", False)
            else:
                break

    result = all_rankings[start_rank - 1:end_rank]
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
        haste = stats.get('haste', 0) if stats.get('has_stats') else 0

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

        # Build CSV row
        row = {
            'Rank': rank_number,
            'Name': player_name,
            'Server': server_name,
            'Date': date_str,
            'Duration': duration_str,
            'ReportID': report_code,
            'HPS': round(total_hps, 2),
            'Haste': haste,
            'Spirit': spirit,
            'Intellect': intellect,
            'TotalHealers': data['total_healers'],
            'VampiricTouch': 'Yes' if data['has_vampiric_touch'] else 'No',
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
            'Rotation2Percent': round(rotation2_percent, 2)
        }

        return row

    except Exception as e:
        print(f"    ERROR analyzing {player_name}: {e}")
        # Return a row with basic info and error indicators
        return {
            'Rank': rank_number,
            'Name': player_name,
            'Server': server_name,
            'Date': '',
            'Duration': '',
            'ReportID': report_code,
            'HPS': 0,
            'Haste': 0,
            'Spirit': 0,
            'Intellect': 0,
            'TotalHealers': 0,
            'VampiricTouch': 'ERROR',
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
            'Rotation2Percent': 0
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
            'Rank', 'Name', 'Server', 'Date', 'Duration', 'ReportID', 'HPS',
            'Haste', 'Spirit', 'Intellect', 'TotalHealers',
            'VampiricTouch', 'Bloodlust', 'NaturesGrace',
            'Trinket1', 'Trinket2',
            'LifebloomUptime', 'LifebloomHPS', 'LifebloomPercentHPS',
            'RejuvenationHPS', 'RejuvenationPercentHPS',
            'RegrowthHPS', 'RegrowthPercentHPS',
            'Rotation1', 'Rotation1Percent', 'Rotation2', 'Rotation2Percent'
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
        print()

        new_count = 0
        skipped_count = 0
        SAVE_INTERVAL = 10  # Save every 10 new entries

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
            rank_number = start_rank + idx
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

            # Save progress every 10 new entries
            if new_count % SAVE_INTERVAL == 0:
                save_progress()

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
