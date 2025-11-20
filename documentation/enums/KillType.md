# KillType

**Type:** ENUM

## Description

A filter for kills vs wipes and encounters vs trash.

## GraphQL Schema Definition

```graphql
enum KillType {
  # Include trash and encounters.
  All

  # Only include encounters (kills and wipes).
  Encounters

  # Only include encounters that end in a kill.
  Kills

  # Only include trash.
  Trash

  # Only include encounters that end in a wipe.
  Wipes
}
```

## Notes

⚠️ **Important**: The enum value names above are inferred based on common naming conventions. 
The actual enum values should be verified against the GraphQL schema or by inspecting the 
actual API responses.

## Enum Values

- `All` - Include trash and encounters.
- `Encounters` - Only include encounters (kills and wipes).
- `Kills` - Only include encounters that end in a kill.
- `Trash` - Only include trash.
- `Wipes` - Only include encounters that end in a wipe.
