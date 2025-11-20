# ProgressRaceData

**Type:** OBJECT

## Description

A way to obtain data for the top guilds involved in an ongoing world first or realm first progress race.

## GraphQL Schema Definition

```graphql
type ProgressRaceData {
  # Progress race information including best percentages, pull counts and streams
  # for top guilds. This API is only active when there is an ongoing race. The
  # format of this JSON may change without notice and is not considered frozen.
  progressRace(
    # Optional. The short name of a region to filter to. If paired with a server slug, 
    # will uniquely identify a server. If used by itself, rankings for that specific 
    # region will be fetched.
    serverRegion: String,
    
    # Optional. The short name of a subregion to filter to. Must be paired with 
    # serverRegion. Rankings for that specific subregion will be fetched.
    serverSubregion: String,
    
    # Optional. The slug for a specific server. Whether or not to filter rankings to 
    # a specific server. If omitted, data for all servers will be used.
    serverSlug: String,
    
    # Optional. If not specified, the latest zone will be used.
    zoneID: Int,
    
    # Optional. If not specified, the race to world first competition will be used.
    competitionID: Int,
    
    # Optional. If not specified, the highest difficulty will be used.
    difficulty: Int,
    
    # Optional. If not specified, the default size for the highest difficulty will be used.
    size: Int,
    
    # Optional. The ID of a single guild to retrieve.
    guildID: Int,
    
    # Optional. The name of a specific guild. Must be used in conjunction with 
    # serverSlug and serverRegion to uniquely identify a guild.
    guildName: String
  ): JSON
  
  # Detailed composition data for a given guild and encounter.
  detailedComposition(
    # Optional. If not specified, the race to world first competition will be used.
    competitionID: Int,
    
    # Optional. The ID of a single guild to retrieve.
    guildID: Int,
    
    # Optional. The name of a specific guild. Must be used in conjunction with 
    # serverSlug and serverRegion to uniquely identify a guild.
    guildName: String,
    
    # Optional. The name of a specific guild. Must be used in conjunction with 
    # name and serverRegion to uniquely identify a guild.
    serverSlug: String,
    
    # Optional. The region for a specific guild. Must be used in conjunction with 
    # name and serverRegion to uniquely identify a guild.
    serverRegion: String,
    
    # Optional. If not specified, the current boss that is being pulled will be used.
    encounterID: Int,
    
    # Optional. If not specified, the highest difficulty will be used.
    difficulty: Int,
    
    # Optional. If not specified, the default size for the highest difficulty will be used.
    size: Int
  ): JSON
}
```

## Fields

- `progressRace` - Progress race information including best percentages, pull counts and streams for top guilds. This API is only active when there is an ongoing race. The format of this JSON may change without notice and is not considered frozen.
  - Arguments:
    - `serverRegion` (String, optional) - The short name of a region to filter to. If paired with a server slug, will uniquely identify a server. If used by itself, rankings for that specific region will be fetched.
    - `serverSubregion` (String, optional) - The short name of a subregion to filter to. Must be paired with serverRegion. Rankings for that specific subregion will be fetched.
    - `serverSlug` (String, optional) - The slug for a specific server. Whether or not to filter rankings to a specific server. If omitted, data for all servers will be used.
    - `zoneID` (Int, optional) - If not specified, the latest zone will be used.
    - `competitionID` (Int, optional) - If not specified, the race to world first competition will be used.
    - `difficulty` (Int, optional) - If not specified, the highest difficulty will be used.
    - `size` (Int, optional) - If not specified, the default size for the highest difficulty will be used.
    - `guildID` (Int, optional) - The ID of a single guild to retrieve.
    - `guildName` (String, optional) - The name of a specific guild. Must be used in conjunction with serverSlug and serverRegion to uniquely identify a guild.
- `detailedComposition` - Detailed composition data for a given guild and encounter.
  - Arguments:
    - `competitionID` (Int, optional) - If not specified, the race to world first competition will be used.
    - `guildID` (Int, optional) - The ID of a single guild to retrieve.
    - `guildName` (String, optional) - The name of a specific guild. Must be used in conjunction with serverSlug and serverRegion to uniquely identify a guild.
    - `serverSlug` (String, optional) - The name of a specific guild. Must be used in conjunction with name and serverRegion to uniquely identify a guild.
    - `serverRegion` (String, optional) - The region for a specific guild. Must be used in conjunction with name and serverRegion to uniquely identify a guild.
    - `encounterID` (Int, optional) - If not specified, the current boss that is being pulled will be used.
    - `difficulty` (Int, optional) - If not specified, the highest difficulty will be used.
    - `size` (Int, optional) - If not specified, the default size for the highest difficulty will be used.

## Notes

⚠️ **Important**: The format of the JSON returned by these fields may change without notice and is not considered frozen. Use at your own risk.
