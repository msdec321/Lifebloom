# GameItem

**Type:** OBJECT

## Description

A single item for the game.

## GraphQL Schema Definition

```graphql
type GameItem {
  # The ID of the item.
  id: Int!
  
  # The icon for the item.
  icon: String
  
  # The localized name of the item. Will be null if no localization information
  # exists for the item.
  name: String
}
```

## Fields

- `id: Int!` - The ID of the item.
- `icon: String` - The icon for the item.
- `name: String` - The localized name of the item. Will be null if no localization information exists for the item.

## Required By

- **GameData** - The game object contains collections of data such as NPCs, classes, abilities, items, maps, etc. Game data only changes when major game patches are released, so you should cache results for as long as possible and only update when new content is released for the game.
- **GameItemPagination**
