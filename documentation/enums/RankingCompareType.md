# RankingCompareType

**Type:** ENUM

## Description

Whether or not rankings are compared against best scores for the entire tier or against all parses in a two week window.

## GraphQL Schema Definition

```graphql
enum RankingCompareType {
  # Compare against rankings.
  Rankings

  # Compare against all parses in a two week window.
  Parses
}
```

## Notes

⚠️ **Important**: The enum value names above are inferred based on common naming conventions. 
The actual enum values should be verified against the GraphQL schema or by inspecting the 
actual API responses.

## Enum Values

- `Rankings` - Compare against rankings.
- `Parses` - Compare against all parses in a two week window.
