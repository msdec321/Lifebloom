# Query

**Type:** OBJECT

## Description

GraphQL Schema definition for the root Query type.

## GraphQL Schema Definition

```graphql
type Query {
  # Obtain the character data object that allows the retrieval of individual
  # characters or filtered collections of characters.
  characterData: CharacterData
  
  # Obtain the game data object that holds collections of static data such as
  # abilities, achievements, classes, items, NPCs, etc.
  gameData: GameData
  
  # Obtain the guild data object that allows the retrieval of individual guilds or
  # filtered collections of guilds.
  guildData: GuildData
  
  # Obtain information about an ongoing world first or realm first race. Inactive
  # when no race is occurring. This data only updates once every 30 seconds, so you
  # do not need to fetch this information more often than that.
  progressRaceData: ProgressRaceData
  
  # Obtain the rate limit data object to see how many points have been spent by this
  # key.
  rateLimitData: RateLimitData
  
  # Obtain the report data object that allows the retrieval of individual reports or
  # filtered collections of reports by guild or by user.
  reportData: ReportData
  
  # Obtain the user object that allows the retrieval of the authorized user's id and
  # username.
  userData: UserData
  
  # Obtain the world data object that holds collections of data such as all
  # expansions, regions, subregions, servers, dungeon/raid zones, and encounters.
  worldData: WorldData
  
  reportComponent: ReportComponentData
  
  reportComponentMutation: ReportComponentData
}
```

## Related Types

- [CharacterData](characterdata.doc.html)
- [GameData](gamedata.doc.html)
- [GuildData](guilddata.doc.html)
- [ProgressRaceData](progressracedata.doc.html)
- [RateLimitData](ratelimitdata.doc.html)
- [ReportData](reportdata.doc.html)
- [UserData](userdata.doc.html)
- [WorldData](worlddata.doc.html)
- [ReportComponentData](reportcomponentdata.doc.html)
