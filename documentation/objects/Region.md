# Region

**Type:** OBJECT

## Description

A single region for the game.

## GraphQL Schema Definition

```graphql
type Region {
  # The ID of the region.
  id: Int!
  
  # The localized compact name of the region, e.g., US for United States.
  compactName: String!
  
  # The localized name of the region.
  name: String!
  
  # The slug for the region, usable when looking up characters and guilds by server.
  slug: String!
  
  # The subregions found within this region.
  subregions: [Subregion]
  
  # The servers found within this region.
  servers(
    # Optional. The number of servers to retrieve per page. If omitted, defaults 
    # to 100. The maximum allowed value is 5000, and minimum allowed value is 1.
    limit: Int,
    
    # Optional. The page of paginated data to retrieve. If omitted, defaults to 
    # the first page.
    page: Int
  ): ServerPagination
}
```

## Fields

- `id` - The ID of the region.
- `compactName` - The localized compact name of the region, e.g., US for United States.
- `name` - The localized name of the region.
- `slug` - The slug for the region, usable when looking up characters and guilds by server.
- `subregions` - The subregions found within this region.
- `servers` - The servers found within this region.
  - Arguments:
    - `limit` (Int, optional) - The number of servers to retrieve per page. If omitted, defaults to 100. The maximum allowed value is 5000, and minimum allowed value is 1.
    - `page` (Int, optional) - The page of paginated data to retrieve. If omitted, defaults to the first page.

## Related Types

- [Report](report.md) - A single report uploaded by a player to a guild or personal logs.
- [Server](server.md) - A single server. Servers correspond to actual game servers that characters and guilds reside on.
- [Subregion](subregion.md) - A single subregion. Subregions are used to divide a region into sub-categories, such as French or German subregions of a Europe region.
- [WorldData](worlddata.md) - The world data object contains collections of data such as expansions, zones, encounters, regions, subregions, etc.
