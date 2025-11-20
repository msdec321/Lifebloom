# GameMap

**Type:** OBJECT

## Description

A single map for the game.

## GraphQL Schema Definition

```graphql
type GameMap {
  # The ID of the map.
  id: Int!
  
  # The localized name of the map. Will be null if no localization information
  # exists for the map.
  name: String
}
```

## Fields

- `id: Int!` - The ID of the map.
- `name: String` - The localized name of the map. Will be null if no localization information exists for the map.

## Required By

- **GameData** - The game object contains collections of data such as NPCs, classes, abilities, items, maps, etc. Game data only changes when major game patches are released, so you should cache results for as long as possible and only update when new content is released for the game.
- **GameMapPagination**
