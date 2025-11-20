# __DirectiveLocation

**Type:** ENUM

## Description

A Directive can be adjacent to many parts of the GraphQL language, a __DirectiveLocation describes one such possible adjacencies.

## GraphQL Schema Definition

```graphql
enum __DirectiveLocation {
  # Location adjacent to a query operation.
  QUERY

  # Location adjacent to a mutation operation.
  MUTATION

  # Location adjacent to a subscription operation.
  SUBSCRIPTION

  # Location adjacent to a field.
  FIELD

  # Location adjacent to a fragment definition.
  FRAGMENT_DEFINITION

  # Location adjacent to a fragment spread.
  FRAGMENT_SPREAD

  # Location adjacent to an inline fragment.
  INLINE_FRAGMENT

  # Location adjacent to a variable definition.
  VARIABLE_DEFINITION

  # Location adjacent to a schema definition.
  SCHEMA

  # Location adjacent to a scalar definition.
  SCALAR

  # Location adjacent to an object type definition.
  OBJECT

  # Location adjacent to a field definition.
  FIELD_DEFINITION

  # Location adjacent to an argument definition.
  ARGUMENT_DEFINITION

  # Location adjacent to an interface definition.
  INTERFACE

  # Location adjacent to a union definition.
  UNION

  # Location adjacent to an enum definition.
  ENUM

  # Location adjacent to an enum value definition.
  ENUM_VALUE

  # Location adjacent to an input object type definition.
  INPUT_OBJECT

  # Location adjacent to an input object field definition.
  INPUT_FIELD_DEFINITION
}
```

## Notes

⚠️ **Important**: The enum value names above are inferred based on common naming conventions. 
The actual enum values should be verified against the GraphQL schema or by inspecting the 
actual API responses.

This is a standard GraphQL introspection type used to describe where directives can be placed in a GraphQL schema.

## Enum Values

- `QUERY` - Location adjacent to a query operation.
- `MUTATION` - Location adjacent to a mutation operation.
- `SUBSCRIPTION` - Location adjacent to a subscription operation.
- `FIELD` - Location adjacent to a field.
- `FRAGMENT_DEFINITION` - Location adjacent to a fragment definition.
- `FRAGMENT_SPREAD` - Location adjacent to a fragment spread.
- `INLINE_FRAGMENT` - Location adjacent to an inline fragment.
- `VARIABLE_DEFINITION` - Location adjacent to a variable definition.
- `SCHEMA` - Location adjacent to a schema definition.
- `SCALAR` - Location adjacent to a scalar definition.
- `OBJECT` - Location adjacent to an object type definition.
- `FIELD_DEFINITION` - Location adjacent to a field definition.
- `ARGUMENT_DEFINITION` - Location adjacent to an argument definition.
- `INTERFACE` - Location adjacent to an interface definition.
- `UNION` - Location adjacent to a union definition.
- `ENUM` - Location adjacent to an enum definition.
- `ENUM_VALUE` - Location adjacent to an enum value definition.
- `INPUT_OBJECT` - Location adjacent to an input object type definition.
- `INPUT_FIELD_DEFINITION` - Location adjacent to an input object field definition.
