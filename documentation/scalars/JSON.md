# JSON

**Type:** SCALAR

## Description

The `JSON` scalar type represents JSON data.

## GraphQL Schema Definition

```graphql
scalar JSON
```

## Required By

The following types use the JSON scalar:

- ArchonViewModels
- Character - A player character. Characters can earn individual rankings and appear in reports.
- Encounter - A single encounter for the game.
- ProgressRaceData - A way to obtain data for the top guilds involved in an ongoing world first or realm first progress race.
- Report - A single report uploaded by a player to a guild or personal logs.
- ReportComponentResult
- ReportEventPaginator - The ReportEventPaginator represents a paginated list of report events.
