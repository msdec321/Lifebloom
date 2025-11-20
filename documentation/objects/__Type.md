# __Type

**Type:** OBJECT

## Description

The fundamental unit of any GraphQL Schema is the type. There are many kinds of types in GraphQL as represented by the `__TypeKind` enum.

Depending on the kind of a type, certain fields describe information about that type. Scalar types provide no information beyond a name and description, while Enum types provide their values. Object and Interface types provide the fields they describe. Abstract types, Union and Interface, provide the Object types possible at runtime. List and NonNull types compose other types.

## GraphQL Schema Definition

```graphql
type __Type {
  kind: __TypeKind!
  name: String
  description: String
  
  # Arguments
  # includeDeprecated: [Not documented]
  fields(includeDeprecated: Boolean): [__Field!]
  
  interfaces: [__Type!]
  possibleTypes: [__Type!]
  
  # Arguments
  # includeDeprecated: [Not documented]
  enumValues(includeDeprecated: Boolean): [__EnumValue!]
  
  # Arguments
  # includeDeprecated: [Not documented]
  inputFields(includeDeprecated: Boolean): [__InputValue!]
  
  ofType: __Type
}
```

## Fields

- `kind: __TypeKind!` - The kind of type (required). Can be SCALAR, OBJECT, INTERFACE, UNION, ENUM, INPUT_OBJECT, LIST, or NON_NULL.
- `name: String` - The name of the type.
- `description: String` - A description of the type.
- `fields(includeDeprecated: Boolean): [__Field!]` - The fields available on this type. Only available for OBJECT and INTERFACE types. The includeDeprecated argument controls whether deprecated fields are included.
- `interfaces: [__Type!]` - The interfaces implemented by this type. Only available for OBJECT types.
- `possibleTypes: [__Type!]` - The possible types for this abstract type. Only available for INTERFACE and UNION types.
- `enumValues(includeDeprecated: Boolean): [__EnumValue!]` - The possible values for this enum type. Only available for ENUM types. The includeDeprecated argument controls whether deprecated values are included.
- `inputFields(includeDeprecated: Boolean): [__InputValue!]` - The input fields for this input object type. Only available for INPUT_OBJECT types. The includeDeprecated argument controls whether deprecated fields are included.
- `ofType: __Type` - The underlying type for LIST and NON_NULL wrapper types.

## Notes

This is a GraphQL introspection type used for schema introspection queries.

## Required By

- **__Field** - Object and Interface types are described by a list of Fields, each of which has a name, potentially a list of arguments, and a return type.
- **__InputValue** - Arguments provided to Fields or Directives and the input fields of an InputObject are represented as Input Values which describe their type and optionally a default value.
- **__Schema** - A GraphQL Schema defines the capabilities of a GraphQL server.
- **__Type** - The fundamental unit of any GraphQL Schema is the type (self-reference).
