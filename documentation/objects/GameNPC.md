# GameNPC

**Type:** OBJECT

## Description

A single NPC for the game.

## GraphQL Schema Definition

```graphql
type GameNPC {
  # The ID of the NPC.
  id: Int!
  
  # The localized name of the NPC. Will be null if no localization information
  # exists for the NPC.
  name: String
}
```

## Fields

- `id: Int!` - The ID of the NPC.
- `name: String` - The localized name of the NPC. Will be null if no localization information exists for the NPC.

## Required By

- **GameData** - The game object contains collections of data such as NPCs, classes, abilities, items, maps, etc. Game data only changes when major game patches are released, so you should cache results for as long as possible and only update when new content is released for the game.
- **GameNPCPagination**
