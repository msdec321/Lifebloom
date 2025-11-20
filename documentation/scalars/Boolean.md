# Boolean

**Type:** SCALAR

## Description

The `Boolean` scalar type represents `true` or `false`.

## GraphQL Schema Definition

```graphql
scalar Boolean
```

## Required By

The following types use the Boolean scalar:

- Character - A player character. Characters can earn individual rankings and appear in reports.
- CharacterPagination
- Encounter - A single encounter for the game.
- EncounterPhases
- GameAbilityPagination
- GameAchievementPagination
- GameEnchantPagination
- GameItemPagination
- GameItemSetPagination
- GameMapPagination
- GameNPCPagination
- GameZonePagination
- Guild - A single guild. Guilds earn their own rankings and contain characters. They may correspond to a guild in-game or be a custom guild created just to hold reports and rankings.
- GuildAttendancePagination
- GuildPagination
- Partition - A single partition for a given raid zone. Partitions have an integer value representing the actual partition and a localized name that describes what the partition represents. Partitions contain their own rankings, statistics and all stars.
- PhaseMetadata - Information about a phase from a boss encounter.
- Report - A single report uploaded by a player to a guild or personal logs.
- ReportArchiveStatus - The archival status of a report.
- ReportComponent
- ReportComponentData
- ReportComponentMutation
- ReportData - The ReportData object enables the retrieval of single reports or filtered collections of reports.
- ReportDungeonPull - The ReportDungeonPull represents a single pull that occurs in a containing dungeon.
- ReportFight - The ReportFight represents a single fight that occurs in the report.
- ReportPagination
- ServerPagination
- Zone - A single zone from an expansion that represents a raid, dungeon, arena, etc.
- __Directive - A Directive provides a way to describe alternate runtime execution and type validation behavior in a GraphQL document.
- __EnumValue - One possible value for a given Enum. Enum values are unique values, not a placeholder for a string or numeric value.
- __Field - Object and Interface types are described by a list of Fields, each of which has a name, potentially a list of arguments, and a return type.
- __InputValue - Arguments provided to Fields or Directives and the input fields of an InputObject are represented as Input Values which describe their type and optionally a default value.
- __Type - The fundamental unit of any GraphQL Schema is the type.
