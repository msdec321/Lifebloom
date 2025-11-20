# RoleType

**Type:** ENUM

## Description

Used to specify a tank, healer or DPS role.

## GraphQL Schema Definition

```graphql
enum RoleType {
  # Fetch any role.
  Any

  # Fetch the DPS role only.
  DPS

  # Fetch the healer role only.
  Healer

  # Fetch the tanking role only.
  Tank
}
```

## Notes

⚠️ **Important**: The enum value names above are inferred based on common naming conventions. 
The actual enum values should be verified against the GraphQL schema or by inspecting the 
actual API responses.

## Enum Values

- `Any` - Fetch any role.
- `DPS` - Fetch the DPS role only.
- `Healer` - Fetch the healer role only.
- `Tank` - Fetch the tanking role only.
