# LeaderboardRank

**Type:** ENUM

## Description

Source of the rank. Most ranks only support log ranks, but some games (ESO) and content types (Retail WoW M+) support leaderboard ranks with no backing log.

## GraphQL Schema Definition

```graphql
enum LeaderboardRank {
  # All ranks are included.
  All

  # Only include ranks with a backing log.
  LogOnly
}
```

## Notes

⚠️ **Important**: The enum value names above are inferred based on common naming conventions. 
The actual enum values should be verified against the GraphQL schema or by inspecting the 
actual API responses.

## Enum Values

- `All` - All ranks are included.
- `LogOnly` - Only include ranks with a backing log.
