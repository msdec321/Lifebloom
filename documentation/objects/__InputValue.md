# __InputValue

**Type:** OBJECT

## Description

Arguments provided to Fields or Directives and the input fields of an InputObject are represented as Input Values which describe their type and optionally a default value.

## GraphQL Schema Definition

```graphql
type __InputValue {
  # Note: Complete field definitions were not available from the documentation page
  # Typical fields for __InputValue include:
  # name: String!
  # description: String
  # type: __Type!
  # defaultValue: String
}
```

## Notes

⚠️ **Important**: The complete schema definition was not available from the documentation page.

This is a GraphQL introspection type used for schema introspection queries.

## Required By

- **__Directive** - A Directive provides a way to describe alternate runtime execution and type validation behavior in a GraphQL document.
- **__Field** - Object and Interface types are described by a list of Fields, each of which has a name, potentially a list of arguments, and a return type.
- **__Type** - The fundamental unit of any GraphQL Schema is the type.
