#!/usr/bin/env python3
"""
WarcraftLogs API Query Script
Queries report data using the GraphQL API
"""

import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Configuration
TOKEN_URL = "https://www.warcraftlogs.com/oauth/token"
API_URL = "https://www.warcraftlogs.com/api/v2/client"

CLIENT_ID = os.getenv("WARCRAFTLOGS_CLIENT_ID")
CLIENT_SECRET = os.getenv("WARCRAFTLOGS_CLIENT_SECRET")


def get_access_token():
    """
    Authenticate with WarcraftLogs API using OAuth client credentials flow.
    Returns an access token.
    """
    response = requests.post(
        TOKEN_URL,
        data={
            "grant_type": "client_credentials"
        },
        auth=(CLIENT_ID, CLIENT_SECRET)
    )

    if response.status_code == 200:
        token_data = response.json()
        return token_data["access_token"]
    else:
        raise Exception(f"Failed to get access token: {response.status_code} - {response.text}")


def query_report(access_token, report_code):
    """
    Query a specific report by its code.

    Args:
        access_token: OAuth access token
        report_code: The report code/ID (e.g., "wX7H9RtYJ48P1cdW")

    Returns:
        Report data as a dictionary
    """
    # GraphQL query to fetch basic report information
    query = """
    query ($code: String!) {
      reportData {
        report(code: $code) {
          code
          title
          startTime
          endTime
          owner {
            name
          }
          guild {
            name
            server {
              name
              region {
                name
              }
            }
          }
          zone {
            name
          }
          fights {
            id
            encounterID
            name
            difficulty
            kill
            bossPercentage
            fightPercentage
            startTime
            endTime
            size
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

    print("Authenticating with WarcraftLogs API...")
    access_token = get_access_token()
    print("✓ Authentication successful!\n")

    print(f"Querying report: {report_code}...")
    result = query_report(access_token, report_code)

    # Check for errors in the response
    if "errors" in result:
        print("Error in query:")
        print(result["errors"])
        return

    # Extract report data
    report = result.get("data", {}).get("reportData", {}).get("report")

    if not report:
        print("No report found!")
        return

    # Display report information
    print("✓ Query successful!\n")
    print("=" * 60)
    print("REPORT INFORMATION")
    print("=" * 60)
    print(f"Code: {report['code']}")
    print(f"Title: {report['title']}")
    print(f"Zone: {report['zone']['name'] if report['zone'] else 'N/A'}")

    if report['guild']:
        guild = report['guild']
        server = guild['server']
        region = server['region']
        print(f"Guild: <{guild['name']}> - {server['name']} ({region['name']})")

    if report['owner']:
        print(f"Owner: {report['owner']['name']}")

    print(f"\nStart Time: {report['startTime']} (Unix timestamp)")
    print(f"End Time: {report['endTime']} (Unix timestamp)")

    # Separate boss fights from trash
    boss_fights = [f for f in report['fights'] if f.get('encounterID', 0) > 0]
    trash_fights = [f for f in report['fights'] if f.get('encounterID', 0) == 0]

    # Display boss fights
    if boss_fights:
        print(f"\n{'=' * 60}")
        print(f"BOSS ENCOUNTERS ({len(boss_fights)} bosses)")
        print("=" * 60)
        for fight in boss_fights:
            kill_status = "✓ KILL" if fight.get('kill') else "✗ WIPE"
            boss_pct = fight.get('bossPercentage', 0)
            fight_pct = fight.get('fightPercentage', 0)
            size = fight.get('size', 'N/A')

            # Calculate fight duration in minutes and seconds
            duration_ms = fight['endTime'] - fight['startTime']
            duration_sec = duration_ms / 1000
            minutes = int(duration_sec // 60)
            seconds = int(duration_sec % 60)

            print(f"  [{fight['id']}] {fight.get('name', 'Unknown')}")
            print(f"       Status: {kill_status} | Boss HP: {boss_pct:.1f}% | Duration: {minutes}m {seconds}s | Size: {size}")

    # Display summary of trash fights
    if trash_fights:
        print(f"\n{'=' * 60}")
        print(f"TRASH FIGHTS: {len(trash_fights)} encounters")
        print("=" * 60)

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
