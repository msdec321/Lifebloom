# ExternalBuffRankFilter

**Type:** ENUM

## Description

Whether to include ranks with major external buffs. Not all metrics, zones and games support this. It will be ignored if unsupported.

## GraphQL Schema Definition

```graphql
enum ExternalBuffRankFilter {
  # Include all ranks, regardless of external buffs.
  Any

  # Only include ranks that DO CONTAIN external buffs.
  With

  # Only include ranks that DO NOT CONTAIN external buffs.
  Without
}
```

## Notes

⚠️ **Important**: The enum value names above are inferred based on common naming conventions. 
The actual enum values should be verified against the GraphQL schema or by inspecting the 
actual API responses.

## Enum Values

- `Any` - Include all ranks, regardless of external buffs.
- `With` - Only include ranks that DO CONTAIN external buffs.
- `Without` - Only include ranks that DO NOT CONTAIN external buffs.
