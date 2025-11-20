# Report

**Type:** OBJECT

## Description

A single report uploaded by a player to a guild or personal logs.

## GraphQL Schema Definition

```graphql
type Report {
  # The report code, a unique value used to identify the report.
  code: String!
  
  # The end time of the report. This is a UNIX timestamp representing the timestamp
  # of the last event contained in the report.
  endTime: Float!
  
  # A set of paginated report events, filterable via arguments like type, source,
  # target, ability, etc. This data is not considered frozen, and it can change
  # without notice. Use at your own risk.
  events(
    abilityID: Float,
    dataType: EventDataType,
    death: Int,
    difficulty: Int,
    encounterID: Int,
    endTime: Float,
    fightIDs: [Int],
    filterExpression: String,
    hostilityType: HostilityType,
    includeResources: Boolean,
    killType: KillType,
    limit: Int,
    sourceAurasAbsent: String,
    sourceAurasPresent: String,
    sourceClass: String,
    sourceID: Int,
    sourceInstanceID: Int,
    startTime: Float,
    targetAurasAbsent: String,
    targetAurasPresent: String,
    targetClass: String,
    targetID: Int,
    targetInstanceID: Int,
    translate: Boolean,
    useAbilityIDs: Boolean,
    useActorIDs: Boolean,
    viewOptions: Int,
    wipeCutoff: Int
  ): ReportEventPaginator
  
  # The number of exported segments in the report. This is how many segments have
  # been processed for rankings.
  exportedSegments: Int!
  
  # A set of fights with details about participating players.
  fights(
    difficulty: Int,
    encounterID: Int,
    fightIDs: [Int],
    killType: KillType,
    translate: Boolean
  ): [ReportFight]
  
  # A graph of information for a report, filterable via arguments like type, source,
  # target, ability, etc. This data is not considered frozen, and it can change
  # without notice. Use at your own risk.
  graph(
    abilityID: Float,
    dataType: GraphDataType,
    death: Int,
    difficulty: Int,
    encounterID: Int,
    endTime: Float,
    fightIDs: [Int],
    filterExpression: String,
    hostilityType: HostilityType,
    killType: KillType,
    sourceAurasAbsent: String,
    sourceAurasPresent: String,
    sourceClass: String,
    sourceID: Int,
    sourceInstanceID: Int,
    startTime: Float,
    targetAurasAbsent: String,
    targetAurasPresent: String,
    targetClass: String,
    targetID: Int,
    targetInstanceID: Int,
    translate: Boolean,
    viewOptions: Int,
    viewBy: ViewType,
    wipeCutoff: Int
  ): JSON
  
  # The guild that the report belongs to. If this is null, then the report was
  # uploaded to the user's personal logs.
  guild: Guild
  
  # The guild tag that the report belongs to. If this is null, then the report was
  # not tagged.
  guildTag: GuildTag
  
  # The user that uploaded the report.
  owner: User
  
  # Data from the report's master file. This includes version info, all of the
  # players, NPCs and pets that occur in the report, and all the game abilities used
  # in the report.
  masterData(
    # Optional. Whether or not the actors and abilities in the master data should 
    # be auto-translated. Defaults to true. Set to false if speed is a priority, 
    # and you do not care about the names of abilities and actors.
    translate: Boolean
  ): ReportMasterData
  
  # A table of information for the players of a report, including their specs,
  # talents, gear, etc. This data is not considered frozen, and it can change
  # without notice. Use at your own risk.
  playerDetails(
    difficulty: Int,
    encounterID: Int,
    endTime: Float,
    fightIDs: [Int],
    killType: KillType,
    startTime: Float,
    translate: Boolean,
    includeCombatantInfo: Boolean
  ): JSON
  
  # A list of all characters that ranked on kills in the report.
  rankedCharacters: [Character]
  
  # Rankings information for a report, filterable to specific fights, bosses,
  # metrics, etc. This data is not considered frozen, and it can change without
  # notice. Use at your own risk.
  rankings(
    compare: RankingCompareType,
    difficulty: Int,
    encounterID: Int,
    fightIDs: [Int],
    playerMetric: ReportRankingMetricType,
    timeframe: RankingTimeframeType
  ): JSON
  
  # The region of the report.
  region: Region
  
  # The revision of the report. This number is increased when reports get
  # re-exported.
  revision: Int!
  
  # The number of uploaded segments in the report.
  segments: Int!
  
  # The start time of the report. This is a UNIX timestamp representing the
  # timestamp of the first event contained in the report.
  startTime: Float!
  
  # A table of information for a report, filterable via arguments like type, source,
  # target, ability, etc. This data is not considered frozen, and it can change
  # without notice. Use at your own risk.
  table(
    abilityID: Float,
    dataType: TableDataType,
    death: Int,
    difficulty: Int,
    encounterID: Int,
    endTime: Float,
    fightIDs: [Int],
    filterExpression: String,
    hostilityType: HostilityType,
    killType: KillType,
    sourceAurasAbsent: String,
    sourceAurasPresent: String,
    sourceClass: String,
    sourceID: Int,
    sourceInstanceID: Int,
    startTime: Float,
    targetAurasAbsent: String,
    targetAurasPresent: String,
    targetClass: String,
    targetID: Int,
    targetInstanceID: Int,
    translate: Boolean,
    viewOptions: Int,
    viewBy: ViewType,
    wipeCutoff: Int
  ): JSON
  
  # A title for the report.
  title: String!
  
  # The visibility level of the report. The possible values are 'public', 'private',
  # and 'unlisted'.
  visibility: String!
  
  # The principal zone that the report contains fights for. Null if no supported
  # zone exists.
  zone: Zone
  
  # Whether this report has been archived. Events, tables, and graphs for archived
  # reports are inaccessible unless the retrieving user has a subscription including
  # archive access.
  archiveStatus: ReportArchiveStatus
  
  # Phase information for all boss encounters observed in this report. This requires
  # loading fight data, but does not double-charge API points if you load fights and
  # phases.
  phases: [EncounterPhases]!
}
```

## Fields

- `code` - The report code, a unique value used to identify the report.
- `endTime` - The end time of the report. This is a UNIX timestamp representing the timestamp of the last event contained in the report.
- `events` - A set of paginated report events, filterable via arguments like type, source, target, ability, etc. This data is not considered frozen, and it can change without notice. Use at your own risk.
- `exportedSegments` - The number of exported segments in the report. This is how many segments have been processed for rankings.
- `fights` - A set of fights with details about participating players.
- `graph` - A graph of information for a report, filterable via arguments. This data is not considered frozen, and it can change without notice. Use at your own risk.
- `guild` - The guild that the report belongs to. If this is null, then the report was uploaded to the user's personal logs.
- `guildTag` - The guild tag that the report belongs to. If this is null, then the report was not tagged.
- `owner` - The user that uploaded the report.
- `masterData` - Data from the report's master file. This includes version info, all of the players, NPCs and pets that occur in the report, and all the game abilities used in the report.
- `playerDetails` - A table of information for the players of a report, including their specs, talents, gear, etc. This data is not considered frozen, and it can change without notice. Use at your own risk.
- `rankedCharacters` - A list of all characters that ranked on kills in the report.
- `rankings` - Rankings information for a report, filterable to specific fights, bosses, metrics, etc. This data is not considered frozen, and it can change without notice. Use at your own risk.
- `region` - The region of the report.
- `revision` - The revision of the report. This number is increased when reports get re-exported.
- `segments` - The number of uploaded segments in the report.
- `startTime` - The start time of the report. This is a UNIX timestamp representing the timestamp of the first event contained in the report.
- `table` - A table of information for a report, filterable via arguments. This data is not considered frozen, and it can change without notice. Use at your own risk.
- `title` - A title for the report.
- `visibility` - The visibility level of the report. The possible values are 'public', 'private', and 'unlisted'.
- `zone` - The principal zone that the report contains fights for. Null if no supported zone exists.
- `archiveStatus` - Whether this report has been archived. Events, tables, and graphs for archived reports are inaccessible unless the retrieving user has a subscription including archive access.
- `phases` - Phase information for all boss encounters observed in this report. This requires loading fight data, but does not double-charge API points if you load fights and phases.

## Notes

⚠️ **Important**: Many fields in this type return data that is not considered frozen and can change without notice. Use at your own risk. This includes: events, graph, playerDetails, rankings, and table.
