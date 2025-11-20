# ViewType

**Type:** ENUM

## Description

Whether the view is by source, target, or ability.

## GraphQL Schema Definition

```graphql
enum ViewType {
  # Use the same default that the web site picks based off the other selected
  # parameters.
  default

  # View by ability.
  ability

  # View by source.
  source

  # View by target.
  target
}
```

## Notes

⚠️ **Important**: The enum value names above are inferred based on common naming conventions. 
The actual enum values should be verified against the GraphQL schema or by inspecting the 
actual API responses.

## Enum Values

- `default` - Use the same default that the web site picks based off the other selected parameters.
- `ability` - View by ability.
- `source` - View by source.
- `target` - View by target.
