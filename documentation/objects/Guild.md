# Guild

**Type:** OBJECT

## Description

A single guild. Guilds earn their own rankings and contain characters. They may correspond to a guild in-game or be a custom guild created just to hold reports and rankings.

## GraphQL Schema Definition

```graphql
type Guild {
  # Arguments
  # guildTagID: Optional. Whether or not to filter the attendance
  # to a specific guild tag.
  # limit: Optional. The number of reports to retrieve per page. If
  # omitted, defaults to 16. The maximum allowed value is 25, and minimum allowed
  # value is 1.
  # page: Optional. The page of paginated data to retrieve. If
  # omitted, defaults to the first page.
  # zoneID: Optional. Whether or not to filter the attendance table
  # to a specific zone.
  attendance(guildTagID: Int, limit: Int, page: Int, zoneID: Int): GuildAttendancePagination!

  # Whether or not the guild has competition mode enabled.
  competitionMode: Boolean!

  # The description for the guild that is displayed with the guild name on the site.
  description: String!

  # The faction of the guild.
  faction: GameFaction!

  # The ID of the guild.
  id: Int!

  # The name of the guild.
  name: String!

  # The server that the guild belongs to.
  server: Server!

  # Whether or not the guild has stealth mode enabled.
  stealth: Boolean!

  # The tags used to label reports. In the site UI, these are called raid teams.
  tags: [GuildTag]

  # The member roster for a specific guild. The result of this query is a paginated
  # list of characters. This query only works for games where the guild roster is
  # verifiable, e.g., it does not work for Classic Warcraft.
  #
  # Arguments
  # limit: Optional. The number of characters to retrieve per page.
  # If omitted, defaults to 100. The maximum allowed value is 100, and minimum
  # allowed value is 1.
  # page: Optional. The page of paginated data to retrieve. If
  # omitted, defaults to the first page.
  zoneRankedCharacters(limit: Int, page: Int): CharacterPagination!

  # The current user's rank within the guild. Only accessible via user
  # authentication with the "view-user-profile" scope.
  zoneRankings: GuildRank

  # The guild's ranking for a zone. If `zoneId` is unset or null, uses the latest
  # zone.
  #
  # Arguments
  # zoneId: [Not documented]
  zoneRanking(zoneId: Int): GuildZoneRankings!
}
```

## Fields

- `attendance` - Paginated attendance data for the guild. Can be filtered by guild tag and zone.
- `competitionMode` - Whether or not the guild has competition mode enabled.
- `description` - The description for the guild that is displayed with the guild name on the site.
- `faction` - The faction of the guild.
- `id` - The ID of the guild.
- `name` - The name of the guild.
- `server` - The server that the guild belongs to.
- `stealth` - Whether or not the guild has stealth mode enabled.
- `tags` - The tags used to label reports. In the site UI, these are called raid teams.
- `zoneRankedCharacters` - The member roster for a specific guild. The result of this query is a paginated list of characters. This query only works for games where the guild roster is verifiable.
- `zoneRankings` - The current user's rank within the guild. Only accessible via user authentication with the "view-user-profile" scope.
- `zoneRanking` - The guild's ranking for a zone. If `zoneId` is unset or null, uses the latest zone.
