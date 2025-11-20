# GameAbility

**Type:** OBJECT

## Description

A single ability for the game.

## GraphQL Schema Definition

```graphql
type GameAbility {
  # The ID of the ability
  id: Int!
  
  # The name of the ability
  name: String!
  
  # The icon of the ability
  icon: String
}
```

## Notes

⚠️ **Important**: The documentation for this type is minimal. Additional fields may exist that are not documented here. Please verify the actual schema definition and fields available in the API.

## Required By

- GameAbilityPagination
- GameData - The game object contains collections of data such as NPCs, classes, abilities, items, maps, etc. Game data only changes when major game patches are released, so you should cache results for as long as possible and only update when new content is released for the game.
