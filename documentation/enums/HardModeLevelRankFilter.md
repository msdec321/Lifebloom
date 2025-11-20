# HardModeLevelRankFilter

**Type:** ENUM

## Description

Hard mode level filter. Used for WoW Classic Hard Modes. For ESO hard modes, use difficulty. Hard mode levels range from 0-4, with 0 being normal mode and 4 being the highest hard mode.

## GraphQL Schema Definition

```graphql
enum HardModeLevelRankFilter {
  # Any hard mode level (including normal mode).
  Any

  # The highest hard mode level. Convenience alias for hard mode level 4.
  Highest

  # The normal (non-hard) mode level. Convenience alias for hard mode level 0.
  Normal

  # Hard mode level 0.
  HardModeLevel0

  # Hard mode level 1.
  HardModeLevel1

  # Hard mode level 2.
  HardModeLevel2

  # Hard mode level 3.
  HardModeLevel3

  # Hard mode level 4.
  HardModeLevel4
}
```

## Notes

⚠️ **Important**: The enum value names above are inferred based on common naming conventions. 
The actual enum values should be verified against the GraphQL schema or by inspecting the 
actual API responses.

## Enum Values

- `Any` - Any hard mode level (including normal mode).
- `Highest` - The highest hard mode level. Convenience alias for hard mode level 4.
- `Normal` - The normal (non-hard) mode level. Convenience alias for hard mode level 0.
- `HardModeLevel0` - Hard mode level 0.
- `HardModeLevel1` - Hard mode level 1.
- `HardModeLevel2` - Hard mode level 2.
- `HardModeLevel3` - Hard mode level 3.
- `HardModeLevel4` - Hard mode level 4.
