# __Field

**Type:** OBJECT

## Description

Object and Interface types are described by a list of Fields, each of which has a name, potentially a list of arguments, and a return type.

## GraphQL Schema Definition

```graphql
type __Field {
  # Note: Complete field definitions were not available from the documentation page
  # Typical fields for __Field include:
  # name: String!
  # description: String
  # args: [__InputValue!]!
  # type: __Type!
  # isDeprecated: Boolean!
  # deprecationReason: String
}
```

## Notes

⚠️ **Important**: The complete schema definition was not available from the documentation page.

This is a GraphQL introspection type used for schema introspection queries.

## Required By

- **__Type** - The fundamental unit of any GraphQL Schema is the type.
