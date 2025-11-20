# Character

**Type:** OBJECT

## Description

A player character. Characters can earn individual rankings and appear in reports.

## GraphQL Schema Definition

```graphql
type Character {
  # The canonical ID of the character. If a character renames or transfers, then the
  # canonical id can be used to identify the most recent version of the character.
  canonicalID: Int!
  
  # Whether this character is claimed by the current user. Only accessible if
  # accessed via the user API with the "view-user-profile" scope.
  claimed: Boolean
  
  # The class id of the character.
  classID: Int!
  
  # Encounter rankings information for a character, filterable to specific zones,
  # bosses, metrics, etc. This data is not considered frozen, and it can change
  # without notice. Use at your own risk.
  encounterRankings(
    byBracket: Boolean
    className: String
    compare: RankingCompareType
    difficulty: Int
    encounterID: Int
    includeCombatantInfo: Boolean
    includeOtherPlayers: Boolean
    includeHistoricalGraph: Boolean
    includePrivateLogs: Boolean
    metric: CharacterRankingMetricType
    partition: Int
    role: RoleType
    size: Int
    specName: String
    timeframe: RankingTimeframeType
  ): JSON
  
  # The faction of the character.
  faction: GameFaction!
  
  # Cached game data such as gear for the character. This data was fetched from the
  # appropriate source (Blizzard APIs for WoW, Lodestone for FF). This call will
  # only return a cached copy of the data if it exists already. It will not go out
  # to Blizzard or Lodestone to fetch a new copy.
  gameData(
    specID: Int
    forceUpdate: Boolean
  ): JSON
  
  # The guild rank of the character in their primary guild. This is not the user
  # rank on the site, but the rank according to the game data, e.g., a Warcraft
  # guild rank or an FFXIV Free Company rank.
  guildRank: Int!
  
  # All guilds that the character belongs to.
  guilds: [Guild]
  
  # Whether or not the character has all its rankings hidden.
  hidden: Boolean!
  
  # The ID of the character.
  id: Int!
  
  # The level of the character.
  level: Int!
  
  # The name of the character.
  name: String!
  
  # Recent reports for the character.
  recentReports(
    limit: Int
    page: Int
  ): ReportPagination
  
  # The server that the character belongs to.
  server: Server!
  
  # Rankings information for a character, filterable to specific zones, bosses,
  # metrics, etc. This data is not considered frozen, and it can change without
  # notice. Use at your own risk.
  zoneRankings(
    byBracket: Boolean
    className: String
    compare: RankingCompareType
    difficulty: Int
    includePrivateLogs: Boolean
    metric: CharacterRankingMetricType
    partition: Int
    role: RoleType
    size: Int
    specName: String
    timeframe: RankingTimeframeType
    zoneID: Int
  ): JSON
}
```

## Fields

### canonicalID
**Type:** Int!

The canonical ID of the character. If a character renames or transfers, then the canonical id can be used to identify the most recent version of the character.

### claimed
**Type:** Boolean

Whether this character is claimed by the current user. Only accessible if accessed via the user API with the "view-user-profile" scope.

### classID
**Type:** Int!

The class id of the character.

### encounterRankings
**Type:** JSON

Encounter rankings information for a character, filterable to specific zones, bosses, metrics, etc. This data is not considered frozen, and it can change without notice. Use at your own risk.

**Arguments:**
- `byBracket` (Boolean) - Optional. Whether or not to use bracket rankings instead of overall rankings. For WoW, brackets are item levels or keystones. For FF, brackets are patches.
- `className` (String) - Optional. The slug for a specific class. Whether or not to filter rankings to a specific class. Only used by games that support multiple classes on a single character.
- `compare` (RankingCompareType) - Optional. Whether or not to compare against rankings (best scores across the entire tier) or two weeks worth of parses (more representative of real-world performance).
- `difficulty` (Int) - Optional. Whether or not to filter the rankings to a specific difficulty. If omitted, the highest difficulty is used.
- `encounterID` (Int) - Required. The specific encounter whose rankings should be fetched.
- `includeCombatantInfo` (Boolean) - Optional. Whether or not to include detailed combatant info such as gear in the results.
- `includeOtherPlayers` (Boolean) - Optional. Whether to include the other characters you cleared with in the results.
- `includeHistoricalGraph` (Boolean) - Optional. Whether to include the historical graph with the results.
- `includePrivateLogs` (Boolean) - Optional. Whether or not to include private logs in the results. This option is only available if using the user GraphQL endpoint.
- `metric` (CharacterRankingMetricType) - Optional. You can filter to a specific character metric like dps or hps. If omitted, an appropriate default metric for the zone will be chosen.
- `partition` (Int) - Optional. Whether or not to filter the rankings to a specific partition. By default, the latest partition is chosen. A special value of -1 can be passed to fetch data from all partitions.
- `role` (RoleType) - Optional. The slug for a specific role. This allow you to only fetch ranks for the healing role, dps role or tank role.
- `size` (Int) - Optional. Whether or not to filter rankings to a specific size. If omitted, the first valid raid size will be used.
- `specName` (String) - Optional. The slug for a specific spec. Whether or not to filter rankings to a specific spec. If omitted, data for all specs will be used.
- `timeframe` (RankingTimeframeType) - Optional. Whether or not the returned report rankings should be compared against today's rankings or historical rankings around the time the fight occurred.

### faction
**Type:** GameFaction!

The faction of the character.

### gameData
**Type:** JSON

Cached game data such as gear for the character. This data was fetched from the appropriate source (Blizzard APIs for WoW, Lodestone for FF). This call will only return a cached copy of the data if it exists already. It will not go out to Blizzard or Lodestone to fetch a new copy.

**Arguments:**
- `specID` (Int) - Optional. A specific spec ID to retrieve information for. If omitted, the last observed spec on Armory (WoW) or Lodestone (FF) will be used.
- `forceUpdate` (Boolean) - Optional. Whether or not to force the updating of the character before returning the game data.

### guildRank
**Type:** Int!

The guild rank of the character in their primary guild. This is not the user rank on the site, but the rank according to the game data, e.g., a Warcraft guild rank or an FFXIV Free Company rank.

### guilds
**Type:** [Guild]

All guilds that the character belongs to.

### hidden
**Type:** Boolean!

Whether or not the character has all its rankings hidden.

### id
**Type:** Int!

The ID of the character.

### level
**Type:** Int!

The level of the character.

### name
**Type:** String!

The name of the character.

### recentReports
**Type:** ReportPagination

Recent reports for the character.

**Arguments:**
- `limit` (Int) - Optional. The number of recent reports to retrieve. If omitted, defaults to 10. The maximum allowed value is 100, and minimum allowed value is 1.
- `page` (Int) - Optional. The page of paginated data to retrieve. If omitted, defaults to the first page.

### server
**Type:** Server!

The server that the character belongs to.

### zoneRankings
**Type:** JSON

Rankings information for a character, filterable to specific zones, bosses, metrics, etc. This data is not considered frozen, and it can change without notice. Use at your own risk.

**Arguments:**
- `byBracket` (Boolean) - Optional. Whether or not to use bracket rankings instead of overall rankings. For WoW, brackets are item levels or keystones. For FF, brackets are patches.
- `className` (String) - Optional. The slug for a specific class. Whether or not to filter rankings to a specific class. Only used by games that support multiple classes on a single character.
- `compare` (RankingCompareType) - Optional. Whether or not to compare against rankings (best scores across the entire tier) or two weeks worth of parses (more representative of real-world performance).
- `difficulty` (Int) - Optional. Whether or not to filter the rankings to a specific difficulty. If omitted, the highest difficulty is used.
- `includePrivateLogs` (Boolean) - Optional. Whether or not to include private logs in the results. This option is only available if using the user GraphQL endpoint.
- `metric` (CharacterRankingMetricType) - Optional. You can filter to a specific character metric like dps or hps. If omitted, an appropriate default metric for the zone will be chosen.
- `partition` (Int) - Optional. Whether or not to filter the rankings to a specific partition. By default, the latest partition is chosen. A special value of -1 can be passed to fetch data from all partitions.
- `role` (RoleType) - Optional. The slug for a specific role. This allow you to only fetch ranks for the healing role, dps role or tank role.
- `size` (Int) - Optional. Whether or not to filter rankings to a specific size. If omitted, the first valid raid size will be used.
- `specName` (String) - Optional. The slug for a specific spec. Whether or not to filter rankings to a specific spec. If omitted, data for all specs will be used.
- `timeframe` (RankingTimeframeType) - Optional. Whether or not the returned report rankings should be compared against today's rankings or historical rankings around the time the fight occurred.
- `zoneID` (Int) - Optional. If not specified, the latest unfrozen zone will be used.

## Required By

- CharacterData - The CharacterData object enables the retrieval of single characters or filtered collections of characters.
- CharacterPagination
- Report - A single report uploaded by a player to a guild or personal logs.
- User - A single user of the site. Most fields can only be accessed when authenticated as that user with the "view-user-profile" scope.
