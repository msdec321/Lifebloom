# GameEnchant

**Type:** OBJECT

## Description

A single enchant for the game.

## GraphQL Schema Definition

```graphql
type GameEnchant {
  # The ID of the enchant.
  id: Int!
  
  # The localized name of the enchant. Will be null if no localization information
  # exists for the enchant.
  name: String
}
```

## Fields

- `id: Int!` - The ID of the enchant.
- `name: String` - The localized name of the enchant. Will be null if no localization information exists for the enchant.

## Required By

- **GameData** - The game object contains collections of data such as NPCs, classes, abilities, items, maps, etc. Game data only changes when major game patches are released, so you should cache results for as long as possible and only update when new content is released for the game.
- **GameEnchantPagination**
