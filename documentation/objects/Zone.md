# Zone

**Type:** OBJECT

## Description

A single zone from an expansion that represents a raid, dungeon, arena, etc.

## GraphQL Schema Definition

```graphql
type Zone {
  # The ID of the zone.
  id: Int!

  # The bracket information for this zone. This field will be null if the zone does
  # not support brackets.
  bracket: Bracket

  # A list of all the difficulties supported for this zone.
  difficulties: [Difficulty]

  # The encounters found within this zone.
  encounters: [Encounter]

  # The expansion that this zone belongs to.
  expansion: Expansion!

  # Whether or not the entire zone (including all its partitions) is permanently
  # frozen. When a zone is frozen, data involving that zone will never change and
  # can be cached forever.
  frozen: Boolean!

  # The name of the zone.
  name: String!

  # A list of all the partitions supported for this zone.
  partitions: [Partition]
}
```

## Fields

- `id: Int!` - The ID of the zone (required).
- `bracket: Bracket` - The bracket information for this zone. This field will be null if the zone does not support brackets.
- `difficulties: [Difficulty]` - A list of all the difficulties supported for this zone.
- `encounters: [Encounter]` - The encounters found within this zone.
- `expansion: Expansion!` - The expansion that this zone belongs to (required).
- `frozen: Boolean!` - Whether or not the entire zone (including all its partitions) is permanently frozen. When a zone is frozen, data involving that zone will never change and can be cached forever (required).
- `name: String!` - The name of the zone (required).
- `partitions: [Partition]` - A list of all the partitions supported for this zone.

## Required By

- **Encounter** - A single encounter for the game.
- **Expansion** - A single expansion for the game.
- **GuildAttendance** - Attendance for a specific report within a guild.
- **Report** - A single report uploaded by a player to a guild or personal logs.
- **WorldData** - The world data object contains collections of data such as expansions, zones, encounters, regions, subregions, etc.
