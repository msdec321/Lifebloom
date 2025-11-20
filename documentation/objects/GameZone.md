# GameZone

**Type:** OBJECT

## Description

A single zone for the game.

## GraphQL Schema Definition

```graphql
type GameZone {
  # The ID of the zone.
  id: Float!
  
  # The localized name of the zone. Will be null if no localization information
  # exists for the zone.
  name: String
}
```

## Fields

- `id: Float!` - The ID of the zone.
- `name: String` - The localized name of the zone. Will be null if no localization information exists for the zone.

## Required By

- **GameData** - The game object contains collections of data such as NPCs, classes, abilities, items, maps, etc. Game data only changes when major game patches are released, so you should cache results for as long as possible and only update when new content is released for the game.
- **GameZonePagination**
- **ReportFight** - The ReportFight represents a single fight that occurs in the report.
