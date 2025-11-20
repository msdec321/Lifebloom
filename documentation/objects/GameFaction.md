# GameFaction

**Type:** OBJECT

## Description

A faction that a player or guild can belong to. Factions have an integer id used to identify them throughout the API and a localized name describing the faction.

## Required By

- [Character](Character.md) - A player character. Characters can earn individual rankings and appear in reports.
- [GameData](GameData.md) - The game object contains collections of data such as NPCs, classes, abilities, items, maps, etc. Game data only changes when major game patches are released, so you should cache results for as long as possible and only update when new content is released for the game.
- [Guild](Guild.md) - A single guild. Guilds earn their own rankings and contain characters. They may correspond to a guild in-game or be a custom guild created just to hold reports and rankings.

## Notes

⚠️ **Important**: The specific fields for this object type were not fully available in the documentation page. Please refer to the complete GraphQL schema or API responses for field details.

Factions are identified by:
- An integer `id`
- A localized `name` describing the faction
