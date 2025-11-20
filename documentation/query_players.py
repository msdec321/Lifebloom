#!/usr/bin/env python3
"""
WarcraftLogs Player Participation Query
Identifies players who participated in boss encounters
"""

import os
import requests
from dotenv import load_dotenv
from auth import get_user_access_token

# Load environment variables from .env file
load_dotenv()

# API Configuration
API_URL = "https://www.warcraftlogs.com/api/v2/user"  # Using user endpoint for subscription access


def query_boss_players(access_token, report_code, boss_name=None, fight_id=None):
    """
    Query players who participated in boss encounters.

    Args:
        access_token: OAuth access token
        report_code: The report code/ID
        boss_name: Optional - filter to a specific boss name
        fight_id: Optional - specific fight ID to query

    Returns:
        Report data with fight and player information
    """
    # GraphQL query to fetch fights and master data (actors)
    # Use table API to get player composition with specs
    if fight_id:
        query = """
        query ($code: String!, $fightIDs: [Int]!) {
          reportData {
            report(code: $code) {
              title
              fights {
                id
                encounterID
                name
                kill
                bossPercentage
                friendlyPlayers
              }
              masterData {
                actors(type: "Player") {
                  id
                  name
                  server
                  type
                  subType
                }
              }
              table(fightIDs: $fightIDs, dataType: Summary)
            }
          }
        }
        """
        variables = {
            "code": report_code,
            "fightIDs": [fight_id]
        }
    else:
        query = """
        query ($code: String!) {
          reportData {
            report(code: $code) {
              title
              fights {
                id
                encounterID
                name
                kill
                bossPercentage
                friendlyPlayers
              }
              masterData {
                actors(type: "Player") {
                  id
                  name
                  server
                  type
                  subType
                }
              }
            }
          }
        }
        """
        variables = {
            "code": report_code
        }

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        API_URL,
        json={"query": query, "variables": variables},
        headers=headers
    )

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Query failed: {response.status_code} - {response.text}")


def main():
    """Main execution function"""
    report_code = "wX7H9RtYJ48P1cdW"
    target_boss = "Brutallus"
    target_class = "Druid"
    target_spec = "Restoration"

    print("Authenticating with WarcraftLogs API (user authentication)...")
    access_token = get_user_access_token()
    print("✓ Authentication successful!\n")

    print(f"Querying report: {report_code}...")
    # First, get the fights without playerDetails to find the fight ID
    result = query_boss_players(access_token, report_code)

    # Check for errors
    if "errors" in result:
        print("Error in query:")
        print(result["errors"])
        return

    # Extract data
    report = result.get("data", {}).get("reportData", {}).get("report")
    if not report:
        print("No report found!")
        return

    fights = report.get("fights", [])

    # Find the target boss fight
    boss_fights = [f for f in fights if f.get("encounterID", 0) > 0]
    if target_boss:
        boss_fights = [f for f in boss_fights if f.get("name") == target_boss]

    if not boss_fights:
        print(f"No boss fights found for '{target_boss}'!")
        return

    fight = boss_fights[0]
    fight_id = fight["id"]

    # Now query again with the specific fight ID to get playerDetails
    print(f"Querying player details for {target_boss} (Fight ID: {fight_id})...")
    result = query_boss_players(access_token, report_code, fight_id=fight_id)

    # Check for errors
    if "errors" in result:
        print("Error in query:")
        print(result["errors"])
        return

    report = result.get("data", {}).get("reportData", {}).get("report")
    actors = report.get("masterData", {}).get("actors", [])
    table_data = report.get("table", {})

    # Create a mapping of actor ID to actor info
    actor_map = {actor["id"]: actor for actor in actors}

    # Display player participation for the boss
    for fight in [fight]:
        print("=" * 70)
        print(f"BOSS: {fight['name']} (Fight ID: {fight['id']})")
        print("=" * 70)

        kill_status = "✓ KILL" if fight.get('kill') else "✗ WIPE"
        boss_pct = fight.get('bossPercentage', 0)
        print(f"Status: {kill_status} | Boss HP: {boss_pct:.1f}%\n")

        player_ids = fight.get("friendlyPlayers", [])

        if not player_ids:
            print("No player data available for this fight.")
            continue

        # Parse table data to get spec information
        print(f"Table data available: {table_data is not None}")

        if table_data and "data" in table_data:
            # The table structure contains composition info
            composition = table_data.get("data", {}).get("composition", [])

            print(f"\n{target_class} players with {target_spec} spec:")
            print("-" * 70)

            # Look through composition for matching class/spec
            found_players = []
            for player_data in composition:
                player_type = player_data.get("type")
                player_specs = player_data.get("specs", [])

                for spec_data in player_specs:
                    spec_name = spec_data.get("spec")
                    if player_type == target_class and spec_name == target_spec:
                        found_players.append({
                            "name": player_data.get("name"),
                            "class": player_type,
                            "spec": spec_name
                        })

            if found_players:
                for player in found_players:
                    print(f"  • {player['name']} ({player['class']} - {player['spec']})")
            else:
                print(f"  No {target_spec} {target_class} found.")
                print("\nShowing all players in composition for debugging:")
                for player_data in composition[:5]:  # Show first 5
                    print(f"  {player_data.get('name')} - {player_data.get('type')} - Specs: {player_data.get('specs', [])}")
        else:
            print("\nTable data not available in expected format.")
            if table_data:
                print("Raw table keys:", table_data.keys())
                import json
                print(json.dumps(table_data, indent=2)[:500])

        print("\n" + "=" * 70)


if __name__ == "__main__":
    main()
