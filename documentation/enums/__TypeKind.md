# __TypeKind

**Type:** ENUM

## Description

An enum describing what kind of type a given __Type is.

## GraphQL Schema Definition

```graphql
enum __TypeKind {
  # Indicates this type is a scalar.
  SCALAR

  # Indicates this type is an object. `fields` and `interfaces` are valid fields.
  OBJECT

  # Indicates this type is an interface. `fields`, `interfaces`, and `possibleTypes`
  # are valid fields.
  INTERFACE

  # Indicates this type is a union. `possibleTypes` is a valid field.
  UNION

  # Indicates this type is an enum. `enumValues` is a valid field.
  ENUM

  # Indicates this type is an input object. `inputFields` is a valid field.
  INPUT_OBJECT

  # Indicates this type is a list. `ofType` is a valid field.
  LIST

  # Indicates this type is a non-null. `ofType` is a valid field.
  NON_NULL
}
```

## Notes

⚠️ **Important**: The enum value names above are inferred based on common naming conventions. 
The actual enum values should be verified against the GraphQL schema or by inspecting the 
actual API responses.

This is a standard GraphQL introspection type used to describe the kind of a given type in the GraphQL schema.

## Enum Values

- `SCALAR` - Indicates this type is a scalar.
- `OBJECT` - Indicates this type is an object. `fields` and `interfaces` are valid fields.
- `INTERFACE` - Indicates this type is an interface. `fields`, `interfaces`, and `possibleTypes` are valid fields.
- `UNION` - Indicates this type is a union. `possibleTypes` is a valid field.
- `ENUM` - Indicates this type is an enum. `enumValues` is a valid field.
- `INPUT_OBJECT` - Indicates this type is an input object. `inputFields` is a valid field.
- `LIST` - Indicates this type is a list. `ofType` is a valid field.
- `NON_NULL` - Indicates this type is a non-null. `ofType` is a valid field.
