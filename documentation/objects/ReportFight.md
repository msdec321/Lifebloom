# ReportFight

**Type:** OBJECT

## Description

The ReportFight represents a single fight that occurs in the report.

## GraphQL Schema Definition

```graphql
type ReportFight {
  # The average item level of the players in the fight.
  averageItemLevel: Float

  # The percentage health of the active boss or bosses at the end of a fight.
  bossPercentage: Float

  # The bounding box that encloses the positions of all players/enemies in the
  # fight.
  boundingBox: ReportMapBoundingBox

  # The season ID of a Classic fight. Will only be nonzero for Season of
  # Mastery in Vanilla for now.
  classicSeasonID: Int

  # Whether or not a fight represents an entire raid from start to finish,
  # e.g., in Classic WoW a complete run of Blackwing Lair.
  completeRaid: Boolean!

  # The difficulty setting for the raid, dungeon, or arena. Null for trash.
  difficulty: Int

  # For a dungeon, a list of pulls that occurred in the dungeon. Pulls have
  # details such as the enemies involved in the pull and map info showing where
  # the pull took place.
  dungeonPulls: ReportDungeonPull]

  # fight.
  encounterID: Int!

  # The end time of the fight. This is a timestamp with millisecond precision
  # that is relative to the start of the report, i.e., the start of the report
  # is considered time 0.
  endTime: Float!

  # Information about enemy NPCs involved in the fight. Includes report IDs,
  # instance counts, and instance group counts for each NPC.
  enemyNPCs: ReportFightNPC]

  # instance counts, and instance group counts for each pet.
  enemyPets: ReportFightNPC]

  # the master data actors table to get detailed information about each
  # participant.
  enemyPlayers: Int]

  # indicate how far into a fight a wipe was, since fights can be complicated
  # and have multiple bosses, no bosses, bosses that heal, etc.
  fightPercentage: Float

  # Information about friendly NPCs involved in the fight. Includes report IDs,
  # instance counts, and instance group counts for each NPC.
  friendlyNPCs: ReportFightNPC]

  # instance counts, and instance group counts for each pet.
  friendlyPets: ReportFightNPC]

  # the master data actors table to get detailed information about each
  # participant.
  friendlyPlayers: Int]

  # zones used by the sites for rankings. This is the actual in-game zone info.
  gameZone: GameZone

  # The hard mode level of the fight. Most fights don't support optional hard
  # modes. This only applies to bosses like Sartharion.
  hardModeLevel: Int

  # The report ID of the fight. This ID can be used to fetch only events,
  # tables or graphs for this fight.
  id: Int!

  # Whether or not the fight is still in progress. If this field is false, it
  # means the entire fight has been uploaded.
  inProgress: Boolean

  # The affixes for a Mythic+ dungeon.
  keystoneAffixes: Int]

  # pushing of Mythic+ keys. It has the values 1, 2, and 3.
  keystoneBonus: Int

  # The keystone level for a Mythic+ dungeon.
  keystoneLevel: Int

  # The completion time for a Challenge Mode or Mythic+ Dungeon. This is the
  # official time used on Blizzard leaderboards.
  keystoneTime: Int

  # Whether or not the fight was a boss kill, i.e., successful. If this field
  # is false, it means the fight was a wipe or a failed run, etc..
  kill: Boolean

  # The phase that the encounter was in when the fight ended. Counts up from 1
  # based off the phase type (i.e., normal phase vs intermission).
  lastPhase: Int

  # The phase that the encounter was in when the fight ended. Always increases
  # from 0, so a fight with three real phases and two intermissions would count
  # up from 0 to 4.
  lastPhaseAsAbsoluteIndex: Int

  # Whether or not the phase that the encounter was in when the fight ended was
  # an intermission or not.
  lastPhaseIsIntermission: Boolean

  # The layer of a Torghast run.
  layer: Int

  # All the maps that were involved in a fight. For single bosses this will
  # usually be a single map, but for dungeons it will typically be multiple
  # maps.
  maps: ReportMap]

  name: String!

  # Some boss fights may be converted to trash fights (encounterID = 0). When
  # this occurs, `originalEncounterID` contains the original ID of the
  # encounter.
  originalEncounterID: Int

  # List of observed phase transitions during the fight.
  phaseTransitions: PhaseTransition!]

  rating: Float

  # The group size for the raid, dungeon, or arena. Null for trash.
  size: Int

  # The start time of the fight. This is a timestamp with millisecond precision
  # that is relative to the start of the report, i.e., the start of the report
  # is considered time 0.
  startTime: Float!

  # The import/export code for a Retail Dragonflight talent build. Will be null
  # for a classic or pre-Dragonflight fight. Arguments actorID: The friendly
  # player actor to generate talents for. Result will be null for unknown or
  # non-player actors. Use the ReportMasterData or the friendlyPlayers field on
  # this type to get the list of friendly player actor IDs.
  actorID: Int!)

  # contain the time. This is a timestamp with millisecond precision that is
  # relative to the start of the report, i.e., the start of the report is
  # considered time 0.
  wipeCalledTime: Float
}
```

## Fields

### averageItemLevel

**Type:** `Float`

The average item level of the players in the fight.

### bossPercentage

**Type:** `Float`

The percentage health of the active boss or bosses at the end of a fight.

### boundingBox

**Type:** `ReportMapBoundingBox`

The bounding box that encloses the positions of all players/enemies in the fight.

### classicSeasonID

**Type:** `Int`

The season ID of a Classic fight. Will only be nonzero for Season of Mastery in Vanilla for now.

### completeRaid

**Type:** `Boolean!`

Whether or not a fight represents an entire raid from start to finish, e.g., in Classic WoW a complete run of Blackwing Lair.

### difficulty

**Type:** `Int`

The difficulty setting for the raid, dungeon, or arena. Null for trash.

### dungeonPulls

**Type:** `ReportDungeonPull]`

For a dungeon, a list of pulls that occurred in the dungeon. Pulls have details such as the enemies involved in the pull and map info showing where the pull took place.

### encounterID

**Type:** `Int!`

fight.

### endTime

**Type:** `Float!`

The end time of the fight. This is a timestamp with millisecond precision that is relative to the start of the report, i.e., the start of the report is considered time 0.

### enemyNPCs

**Type:** `ReportFightNPC]`

Information about enemy NPCs involved in the fight. Includes report IDs, instance counts, and instance group counts for each NPC.

### enemyPets

**Type:** `ReportFightNPC]`

instance counts, and instance group counts for each pet.

### enemyPlayers

**Type:** `Int]`

the master data actors table to get detailed information about each participant.

### fightPercentage

**Type:** `Float`

indicate how far into a fight a wipe was, since fights can be complicated and have multiple bosses, no bosses, bosses that heal, etc.

### friendlyNPCs

**Type:** `ReportFightNPC]`

Information about friendly NPCs involved in the fight. Includes report IDs, instance counts, and instance group counts for each NPC.

### friendlyPets

**Type:** `ReportFightNPC]`

instance counts, and instance group counts for each pet.

### friendlyPlayers

**Type:** `Int]`

the master data actors table to get detailed information about each participant.

### gameZone

**Type:** `GameZone`

zones used by the sites for rankings. This is the actual in-game zone info.

### hardModeLevel

**Type:** `Int`

The hard mode level of the fight. Most fights don't support optional hard modes. This only applies to bosses like Sartharion.

### id

**Type:** `Int!`

The report ID of the fight. This ID can be used to fetch only events, tables or graphs for this fight.

### inProgress

**Type:** `Boolean`

Whether or not the fight is still in progress. If this field is false, it means the entire fight has been uploaded.

### keystoneAffixes

**Type:** `Int]`

The affixes for a Mythic+ dungeon.

### keystoneBonus

**Type:** `Int`

pushing of Mythic+ keys. It has the values 1, 2, and 3.

### keystoneLevel

**Type:** `Int`

The keystone level for a Mythic+ dungeon.

### keystoneTime

**Type:** `Int`

The completion time for a Challenge Mode or Mythic+ Dungeon. This is the official time used on Blizzard leaderboards.

### kill

**Type:** `Boolean`

Whether or not the fight was a boss kill, i.e., successful. If this field is false, it means the fight was a wipe or a failed run, etc..

### lastPhase

**Type:** `Int`

The phase that the encounter was in when the fight ended. Counts up from 1 based off the phase type (i.e., normal phase vs intermission).

### lastPhaseAsAbsoluteIndex

**Type:** `Int`

The phase that the encounter was in when the fight ended. Always increases from 0, so a fight with three real phases and two intermissions would count up from 0 to 4.

### lastPhaseIsIntermission

**Type:** `Boolean`

Whether or not the phase that the encounter was in when the fight ended was an intermission or not.

### layer

**Type:** `Int`

The layer of a Torghast run.

### maps

**Type:** `ReportMap]`

All the maps that were involved in a fight. For single bosses this will usually be a single map, but for dungeons it will typically be multiple maps.

### name

**Type:** `String!`

### originalEncounterID

**Type:** `Int`

Some boss fights may be converted to trash fights (encounterID = 0). When this occurs, `originalEncounterID` contains the original ID of the encounter.

### phaseTransitions

**Type:** `PhaseTransition!]`

List of observed phase transitions during the fight.

### rating

**Type:** `Float`

### size

**Type:** `Int`

The group size for the raid, dungeon, or arena. Null for trash.

### startTime

**Type:** `Float!`

The start time of the fight. This is a timestamp with millisecond precision that is relative to the start of the report, i.e., the start of the report is considered time 0.

### actorID

**Type:** `Int!)`

The import/export code for a Retail Dragonflight talent build. Will be null for a classic or pre-Dragonflight fight.  Arguments actorID: The friendly player actor to generate talents for. Result will be null for unknown or non-player actors. Use the ReportMasterData or the friendlyPlayers field on this type to get the list of friendly player actor IDs.

### wipeCalledTime

**Type:** `Float`

contain the time. This is a timestamp with millisecond precision that is relative to the start of the report, i.e., the start of the report is considered time 0.

