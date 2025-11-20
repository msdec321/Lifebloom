# __Directive

**Type:** OBJECT

## Description

A Directive provides a way to describe alternate runtime execution and type validation behavior in a GraphQL document.

In some cases, you need to provide options to alter GraphQL's execution behavior in ways field arguments will not suffice, such as conditionally including or skipping a field. Directives provide this by describing additional information to the executor.

## GraphQL Schema Definition

```graphql
type __Directive {
  name: String!
  description: String
  isRepeatable: Boolean!
  locations: [__DirectiveLocation!]!
  args: [__InputValue!]!
}
```

## Fields

- `name: String!` - The name of the directive (required).
- `description: String` - A description of what the directive does.
- `isRepeatable: Boolean!` - Whether this directive can be used multiple times at the same location (required).
- `locations: [__DirectiveLocation!]!` - The locations where this directive can be applied (required).
- `args: [__InputValue!]!` - The arguments accepted by this directive (required).

## Notes

This is a GraphQL introspection type used for schema introspection queries.
