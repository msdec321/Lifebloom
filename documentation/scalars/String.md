# String

**Type:** SCALAR

## Description

The `String` scalar type represents textual data, represented as UTF-8 character sequences. The String type is most often used by GraphQL to represent free-form human-readable text.

## GraphQL Schema Definition

```graphql
scalar String
```

## Required By

The following types use the String scalar:

- ArchonViewModels
- Bracket - A bracket description for a given raid zone. Brackets have a minimum value, maximum value, and a bucket that can be used to establish all of the possible brackets. The type field indicates what the brackets represent, e.g., item levels or game patches, etc.
- Character - A player character. Characters can earn individual rankings and appear in reports.
- CharacterData - The CharacterData object enables the retrieval of single characters or filtered collections of characters.
- Difficulty - A single difficulty for a given raid zone. Difficulties have an integer value representing the actual difficulty, a localized name that describes the difficulty level, and a list of valid sizes for the difficulty level.
- Encounter - A single encounter for the game.
- Expansion - A single expansion for the game.
- GameAbility - A single ability for the game.
- GameAchievement - A single achievement for the game.
- GameAffix - A single affix for Mythic Keystone dungeons.
- GameClass - A single player class for the game.
- GameEnchant - A single enchant for the game.
- GameFaction - A faction that a player or guild can belong to. Factions have an integer id used to identify them throughout the API and a localized name describing the faction.
- GameItem - A single item for the game.
- GameItemSet - A single item set for the game.
- GameMap - A single map for the game.
- GameNPC - A single NPC for the game.
- GameSpec - A spec for a given player class.
- GameZone - A single zone for the game.
- Guild - A single guild. Guilds earn their own rankings and contain characters. They may correspond to a guild in-game or be a custom guild created just to hold reports and rankings.
- GuildAttendance - Attendance for a specific report within a guild.
- GuildData - The GuildData object enables the retrieval of single guilds or filtered collections of guilds.
- GuildTag - The tag for a specific guild. Tags can be used to categorize reports within a guild. In the site UI, they are referred to as report tags.
- Partition - A single partition for a given raid zone. Partitions have an integer value representing the actual partition and a localized name that describes what the partition represents. Partitions contain their own rankings, statistics and all stars.
- PhaseMetadata - Information about a phase from a boss encounter.
- PlayerAttendance - Attendance for a specific player on a specific raid night.
- ProgressRaceData - A way to obtain data for the top guilds involved in an ongoing world first or realm first progress race.
- Rank
- Region - A single region for the game.
- Report - A single report uploaded by a player to a guild or personal logs.
- ReportAbility - The ReportAbility represents a single ability that occurs in the report.
- ReportActor - The ReportActor represents a single player, pet or NPC that occurs in the report.
- ReportComponent
- ReportComponentData
- ReportComponentMutation
- ReportComponentResult
- ReportData - The ReportData object enables the retrieval of single reports or filtered collections of reports.
- ReportDungeonPull - The ReportDungeonPull represents a single pull that occurs in a containing dungeon.
- ReportFight - The ReportFight represents a single fight that occurs in the report.
- ReportMasterData - The ReporMastertData object contains information about the log version of a report, as well as the actors and abilities used in the report.
- Server - A single server. Servers correspond to actual game servers that characters and guilds reside on.
- Subregion - A single subregion. Subregions are used to divide a region into sub-categories, such as French or German subregions of a Europe region.
- User - A single user of the site. Most fields can only be accessed when authenticated as that user with the "view-user-profile" scope.
- WorldData - The world data object contains collections of data such as expansions, zones, encounters, regions, subregions, etc.
- Zone - A single zone from an expansion that represents a raid, dungeon, arena, etc.
- __Directive - A Directive provides a way to describe alternate runtime execution and type validation behavior in a GraphQL document.
- __EnumValue - One possible value for a given Enum. Enum values are unique values, not a placeholder for a string or numeric value.
- __Field - Object and Interface types are described by a list of Fields, each of which has a name, potentially a list of arguments, and a return type.
- __InputValue - Arguments provided to Fields or Directives and the input fields of an InputObject are represented as Input Values which describe their type and optionally a default value.
- __Type - The fundamental unit of any GraphQL Schema is the type.
