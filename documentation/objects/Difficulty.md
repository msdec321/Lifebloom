# Difficulty

**Type:** OBJECT

## Description

A single difficulty for a given raid zone. Difficulties have an integer value representing the actual difficulty, a localized name that describes the difficulty level, and a list of valid sizes for the difficulty level.

## GraphQL Schema Definition

```graphql
type Difficulty {
  # An integer representing a specific difficulty level within a zone. For example,
  # in World of Warcraft, this could be Mythic. In FF, it could be Savage, etc.
  id: Int!
  
  # The localized name for the difficulty level.
  name: String!
  
  # A list of supported sizes for the difficulty level. An empty result means that
  # the difficulty level has a flexible raid size.
  sizes: [Int]
}
```

## Fields

- `id` (Int!) - An integer representing a specific difficulty level within a zone. For example, in World of Warcraft, this could be Mythic. In FF, it could be Savage, etc.
- `name` (String!) - The localized name for the difficulty level.
- `sizes` ([Int]) - A list of supported sizes for the difficulty level. An empty result means that the difficulty level has a flexible raid size.
