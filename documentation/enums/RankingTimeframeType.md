# RankingTimeframeType

**Type:** ENUM

## Description

Whether or not rankings are today or historical.

## GraphQL Schema Definition

```graphql
enum RankingTimeframeType {
  # Compare against today's rankings.
  Today

  # Compare against historical rankings.
  Historical
}
```

## Notes

⚠️ **Important**: The enum value names above are inferred based on common naming conventions. 
The actual enum values should be verified against the GraphQL schema or by inspecting the 
actual API responses.

## Enum Values

- `Today` - Compare against today's rankings.
- `Historical` - Compare against historical rankings.
