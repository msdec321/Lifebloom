# GuildTag

**Type:** OBJECT

## Description

The tag for a specific guild. Tags can be used to categorize reports within a guild. In the site UI, they are referred to as report tags.

## GraphQL Schema Definition

```graphql
type GuildTag {
  # The ID of the tag.
  id: Float
  
  # The name of the tag.
  name: String
}
```

## Fields

- `id` - The ID of the tag.
- `name` - The name of the tag.
