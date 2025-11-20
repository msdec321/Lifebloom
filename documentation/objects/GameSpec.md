# GameSpec

**Type:** OBJECT

## Description

A spec for a given player class.

## GraphQL Schema Definition

```graphql
type GameSpec {
  # An integer used to identify the spec.
  id: Int!
  
  # The player class that the spec belongs to.
  class: GameClass
  
  # The localized name of the class.
  name: String!
  
  # A slug used to identify the spec.
  slug: String!
}
```

## Fields

- `id: Int!` - An integer used to identify the spec.
- `class: GameClass` - The player class that the spec belongs to.
- `name: String!` - The localized name of the class.
- `slug: String!` - A slug used to identify the spec.

## Required By

- **GameClass** - A single player class for the game.
