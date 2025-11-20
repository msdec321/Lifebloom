# Int

**Type:** SCALAR

## Description

The `Int` scalar type represents non-fractional signed whole numeric values. Int can represent values between -(2^31) and 2^31 - 1.

## GraphQL Schema Definition

```graphql
scalar Int
```

## Required By

The following types use the Int scalar:

- ArchonViewModels
- Character - A player character. Characters can earn individual rankings and appear in reports.
- CharacterData - The CharacterData object enables the retrieval of single characters or filtered collections of characters.
- CharacterPagination
- Difficulty - A single difficulty for a given raid zone. Difficulties have an integer value representing the actual difficulty, a localized name that describes the difficulty level, and a list of valid sizes for the difficulty level.
- Encounter - A single encounter for the game.
- EncounterPhases
- Expansion - A single expansion for the game.
- GameAbility - A single ability for the game.
- GameAbilityPagination
- GameAchievement - A single achievement for the game.
- GameAchievementPagination
- GameAffix - A single affix for Mythic Keystone dungeons.
- GameClass - A single player class for the game.
- GameData - The game object contains collections of data such as NPCs, classes, abilities, items, maps, etc. Game data only changes when major game patches are released, so you should cache results for as long as possible and only update when new content is released for the game.
- GameEnchant - A single enchant for the game.
- GameEnchantPagination
- GameFaction - A faction that a player or guild can belong to. Factions have an integer id used to identify them throughout the API and a localized name describing the faction.
- GameItem - A single item for the game.
- GameItemPagination
- GameItemSet - A single item set for the game.
- GameItemSetPagination
- GameMap - A single map for the game.
- GameMapPagination
- GameNPC - A single NPC for the game.
- GameNPCPagination
- GameSpec - A spec for a given player class.
- GameZonePagination
- Guild - A single guild. Guilds earn their own rankings and contain characters. They may correspond to a guild in-game or be a custom guild created just to hold reports and rankings.
- GuildAttendancePagination
- GuildData - The GuildData object enables the retrieval of single guilds or filtered collections of guilds.
- GuildPagination
- GuildTag - The tag for a specific guild. Tags can be used to categorize reports within a guild. In the site UI, they are referred to as report tags.
- GuildZoneRankings - A guild's rankings within a zone.
- Partition - A single partition for a given raid zone. Partitions have an integer value representing the actual partition and a localized name that describes what the partition represents. Partitions contain their own rankings, statistics and all stars.
- PhaseMetadata - Information about a phase from a boss encounter.
- PhaseTransition - A spartan representation of phase transitions during a fight.
- PlayerAttendance - Attendance for a specific player on a specific raid night.
- ProgressRaceData - A way to obtain data for the top guilds involved in an ongoing world first or realm first progress race.
- Rank
- RateLimitData - A way to obtain your current rate limit usage.
- Region - A single region for the game.
- Report - A single report uploaded by a player to a guild or personal logs.
- ReportActor - The ReportActor represents a single player, pet or NPC that occurs in the report.
- ReportArchiveStatus - The archival status of a report.
- ReportComponentFilter - A broad filter for a report component. This is primarily intended to allow callers to invoke a component on a single fight and/or actor without having to encode these values in their script.
- ReportComponentRangeFilter - Filter input events of a report component to a range of time within a report.
- ReportData - The ReportData object enables the retrieval of single reports or filtered collections of reports.
- ReportDungeonPull - The ReportDungeonPull represents a single pull that occurs in a containing dungeon.
- ReportDungeonPullNPC - The ReportDungeonPullNPC represents participation info within a single dungeon pull for an NPC.
- ReportFight - The ReportFight represents a single fight that occurs in the report.
- ReportFightNPC - The ReportFightNPC represents participation info within a single fight for an NPC.
- ReportMap - The ReportMap represents a single map that a fight can occur on.
- ReportMapBoundingBox - The ReportMapBoundingBox is a box that encloses the positions of all players and enemies in a fight or dungeon pull.
- ReportMasterData - The ReporMastertData object contains information about the log version of a report, as well as the actors and abilities used in the report.
- ReportPagination
- Server - A single server. Servers correspond to actual game servers that characters and guilds reside on.
- ServerPagination
- Subregion - A single subregion. Subregions are used to divide a region into sub-categories, such as French or German subregions of a Europe region.
- User - A single user of the site. Most fields can only be accessed when authenticated as that user with the "view-user-profile" scope.
- UserData - The user data object contains basic information about users and lets you retrieve specific users (or the current user if using the user endpoint).
- WorldData - The world data object contains collections of data such as expansions, zones, encounters, regions, subregions, etc.
- Zone - A single zone from an expansion that represents a raid, dungeon, arena, etc.
