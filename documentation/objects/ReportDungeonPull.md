# ReportDungeonPull

**Type:** OBJECT

## Description

The ReportDungeonPull represents a single pull that occurs in a containing dungeon.

## GraphQL Schema Definition

```graphql
type ReportDungeonPull {
  # The bounding box that encloses the positions of all players/enemies in the
  # fight.
  boundingBox: ReportMapBoundingBox

  # The encounter ID of the fight. If the ID is 0, the fight is considered a
  # trash fight.
  encounterID: Int!

  # The end time of the fight. This is a timestamp with millisecond precision
  # that is relative to the start of the report, i.e., the start of the report
  # is considered time 0.
  endTime: Float!

  # Information about enemies involved in the fight. Includes report IDs,
  # instance counts, and instance group counts for each NPC.
  enemyNPCs: ReportDungeonPullNPC]

  # graphs for this fight.
  id: Int!

  # Whether or not the fight was a boss kill, i.e., successful. If this field
  # is false, it means the fight was an incomplete run, etc..
  kill: Boolean

  # All the maps that were involved in a pull.
  maps: ReportMap]

  name: String!

  # The start time of the fight. This is a timestamp with millisecond precision
  # that is relative to the start of the report, i.e., the start of the report
  # is considered time 0.
  startTime: Float!

  # The x position of the first mob damaged in the pull at the time this damage
  # happens. Used to establish a marker position to represent where the pull
  # took place.
  x: Int!

  # The y position of the first mob damaged in the pull at the time this damage
  # happens. Used to establish a marker position to represent where the pull
  # took place.
  y: Int!
}
```

## Fields

### boundingBox

**Type:** `ReportMapBoundingBox`

The bounding box that encloses the positions of all players/enemies in the fight.

### encounterID

**Type:** `Int!`

The encounter ID of the fight. If the ID is 0, the fight is considered a trash fight.

### endTime

**Type:** `Float!`

The end time of the fight. This is a timestamp with millisecond precision that is relative to the start of the report, i.e., the start of the report is considered time 0.

### enemyNPCs

**Type:** `ReportDungeonPullNPC]`

Information about enemies involved in the fight. Includes report IDs, instance counts, and instance group counts for each NPC.

### id

**Type:** `Int!`

graphs for this fight.

### kill

**Type:** `Boolean`

Whether or not the fight was a boss kill, i.e., successful. If this field is false, it means the fight was an incomplete run, etc..

### maps

**Type:** `ReportMap]`

All the maps that were involved in a pull.

### name

**Type:** `String!`

### startTime

**Type:** `Float!`

The start time of the fight. This is a timestamp with millisecond precision that is relative to the start of the report, i.e., the start of the report is considered time 0.

### x

**Type:** `Int!`

The x position of the first mob damaged in the pull at the time this damage happens. Used to establish a marker position to represent where the pull took place.

### y

**Type:** `Int!`

The y position of the first mob damaged in the pull at the time this damage happens. Used to establish a marker position to represent where the pull took place.

