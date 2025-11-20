#!/usr/bin/env python3
"""
Find Restoration Druid(s) in Boss Encounters

Usage:
    python find_resto_druid.py <report_id> <boss_name>

Example:
    python find_resto_druid.py wX7H9RtYJ48P1cdW Brutallus
"""

import sys
import requests
from auth import get_user_access_token

# API Configuration
API_URL = "https://www.warcraftlogs.com/api/v2/user"


def find_resto_druids(report_code, boss_name):
    """
    Find Restoration Druid(s) who participated in a specific boss encounter.

    Args:
        report_code: The report code/ID (e.g., "wX7H9RtYJ48P1cdW")
        boss_name: The name of the boss (e.g., "Brutallus")

    Returns:
        List of Restoration Druid names, or empty list if none found
    """
    # Get user access token
    access_token = get_user_access_token()

    # Step 1: Query fights to find the boss encounter
    print(f"Searching for {boss_name} in report {report_code}...")

    fights_query = """
    query ($code: String!) {
      reportData {
        report(code: $code) {
          title
          fights {
            id
            encounterID
            name
            kill
          }
        }
      }
    }
    """

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        API_URL,
        json={"query": fights_query, "variables": {"code": report_code}},
        headers=headers
    )

    if response.status_code != 200:
        raise Exception(f"Query failed: {response.status_code} - {response.text}")

    result = response.json()

    if "errors" in result:
        raise Exception(f"GraphQL errors: {result['errors']}")

    report = result.get("data", {}).get("reportData", {}).get("report")
    if not report:
        raise Exception(f"Report {report_code} not found!")

    fights = report.get("fights", [])

    # Find boss fights with matching name
    boss_fights = [
        f for f in fights
        if f.get("encounterID", 0) > 0 and f.get("name") == boss_name
    ]

    if not boss_fights:
        raise Exception(f"Boss '{boss_name}' not found in report!")

    # Filter for kills only
    boss_kills = [f for f in boss_fights if f.get("kill")]

    if not boss_kills:
        print(f"Warning: Found {len(boss_fights)} {boss_name} fight(s), but no kills.")
        print("Using first encounter (might be a wipe)...")
        target_fight = boss_fights[0]
    else:
        # Use the first kill
        target_fight = boss_kills[0]

    fight_id = target_fight["id"]
    is_kill = target_fight.get("kill", False)

    print(f"✓ Found {boss_name} (Fight ID: {fight_id}, {'KILL' if is_kill else 'WIPE'})")

    # Step 2: Query table data for player composition with specs
    print(f"Querying player composition...")

    composition_query = """
    query ($code: String!, $fightIDs: [Int]!) {
      reportData {
        report(code: $code) {
          table(fightIDs: $fightIDs, dataType: Summary)
        }
      }
    }
    """

    response = requests.post(
        API_URL,
        json={
            "query": composition_query,
            "variables": {"code": report_code, "fightIDs": [fight_id]}
        },
        headers=headers
    )

    if response.status_code != 200:
        raise Exception(f"Query failed: {response.status_code} - {response.text}")

    result = response.json()

    if "errors" in result:
        raise Exception(f"GraphQL errors: {result['errors']}")

    report = result.get("data", {}).get("reportData", {}).get("report")
    table_data = report.get("table", {})

    if not table_data or "data" not in table_data:
        raise Exception("Table data not available (might require subscription for archived reports)")

    composition = table_data.get("data", {}).get("composition", [])

    # Step 3: Find Restoration Druids
    resto_druids = []

    for player_data in composition:
        player_type = player_data.get("type")
        player_name = player_data.get("name")
        player_specs = player_data.get("specs", [])

        # Check if this is a Druid with Restoration spec
        for spec_data in player_specs:
            spec_name = spec_data.get("spec")
            if player_type == "Druid" and spec_name == "Restoration":
                resto_druids.append(player_name)
                break  # Don't add the same player twice

    return resto_druids


def main():
    """Main execution function"""
    # Parse command line arguments
    if len(sys.argv) != 3:
        print("Usage: python find_resto_druid.py <report_id> <boss_name>")
        print("\nExample:")
        print("  python find_resto_druid.py wX7H9RtYJ48P1cdW Brutallus")
        return 1

    report_code = sys.argv[1]
    boss_name = sys.argv[2]

    print("=" * 70)
    print("RESTORATION DRUID FINDER")
    print("=" * 70)
    print()

    try:
        resto_druids = find_resto_druids(report_code, boss_name)

        print()
        print("=" * 70)
        print("RESULTS")
        print("=" * 70)

        if resto_druids:
            if len(resto_druids) == 1:
                print(f"✓ Found 1 Restoration Druid:")
            else:
                print(f"✓ Found {len(resto_druids)} Restoration Druids:")

            for druid in resto_druids:
                print(f"  • {druid}")
        else:
            print("✗ No Restoration Druids found in this encounter.")

        print("=" * 70)
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
