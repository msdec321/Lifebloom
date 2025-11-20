# GameItemSet

**Type:** OBJECT

## Description

A single item set for the game.

## GraphQL Schema Definition

```graphql
type GameItemSet {
  # The ID of the item set.
  id: Int!
  
  # The localized name of the item set. Will be null if no localization information
  # exists for the item set.
  name: String
}
```

## Fields

- `id: Int!` - The ID of the item set.
- `name: String` - The localized name of the item set. Will be null if no localization information exists for the item set.

## Required By

- **GameData** - The game object contains collections of data such as NPCs, classes, abilities, items, maps, etc. Game data only changes when major game patches are released, so you should cache results for as long as possible and only update when new content is released for the game.
- **GameItemSetPagination**
