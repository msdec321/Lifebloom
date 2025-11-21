#!/usr/bin/env python3
"""
Test script to verify rate limit monitoring is working
"""

from analyze_top_rankings import check_rate_limit

def main():
    print("Testing Rate Limit Monitoring")
    print("=" * 50)

    # Check current rate limit status
    status = check_rate_limit()

    print(f"Limit per hour: {status['limitPerHour']} points")
    print(f"Points spent this hour: {status['pointsSpentThisHour']} points")
    print(f"Points reset in: {status['pointsResetIn']} seconds")
    print(f"Percentage used: {status['percentUsed']:.2f}%")

    # Show tier information
    tier = "Unknown"
    if status['limitPerHour'] == 3600:
        tier = "Standard (Free)"
    elif status['limitPerHour'] == 9000:
        tier = "Gold"
    elif status['limitPerHour'] == 18000:
        tier = "Platinum"
    elif status['limitPerHour'] == 36000:
        tier = "Premium"

    print(f"Subscription tier: {tier}")

    # Calculate estimated capacity
    points_per_player = 10  # Rough estimate
    remaining = status['limitPerHour'] - status['pointsSpentThisHour']
    estimated_players = remaining // points_per_player

    print(f"\nEstimated remaining capacity: ~{estimated_players} players")

if __name__ == "__main__":
    main()