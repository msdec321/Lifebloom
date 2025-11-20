# WorldData

**Type:** OBJECT

## Description

The world data object contains collections of data such as expansions, zones, encounters, regions, subregions, etc.

## GraphQL Schema Definition

```graphql
type WorldData {
  # Obtain a specific encounter by id.
  #
  # Arguments
  # id: Required. Specify a single encounter ID to retrieve.
  encounter(id: Int): Encounter

  # A single expansion obtained by ID.
  #
  # Arguments
  # id: Required. The ID of a single expansion to retrieve.
  expansion(id: Int): Expansion

  # The set of all expansions supported by the site.
  expansions: [Expansion]

  # Obtain a specific region by its ID.
  #
  # Arguments
  # id: Required. The ID of a single region to retrieve.
  region(id: Int): Region

  # The set of all regions supported by the site.
  regions: [Region]

  # Obtain a specific server either by id or by slug and region.
  #
  # Arguments
  # id: Optional. The ID of a single server to retrieve.
  # region: Optional. The compact English abbreviation for a
  # specific region (e.g., "US"). Use in conjunction with the server slug to
  # retrieve a single server.
  # slug: Optional. A server slug. Use in conjunction with the
  # server region to retrieve a single server.
  server(id: Int, region: String, slug: String): Server

  # Obtain a specific subregion by its ID.
  #
  # Arguments
  # id: Required. The ID of a single subregion to retrieve.
  subregion(id: Int): Subregion

  # Obtain a specific zone by its ID.
  #
  # Arguments
  # id: Required. The ID of a specific zone.
  zone(id: Int): Zone

  # Obtain a set of all zones supported by the site.
  #
  # Arguments
  # expansion_id: Optional. The ID of a specific expansion. If
  # omitted, the zones from all expansions will be retrieved.
  zones(expansion_id: Int): [Zone]
}
```

## Fields

- `encounter(id: Int): Encounter` - Obtain a specific encounter by id. The id argument is required and specifies a single encounter ID to retrieve.
- `expansion(id: Int): Expansion` - A single expansion obtained by ID. The id argument is required and specifies the ID of a single expansion to retrieve.
- `expansions: [Expansion]` - The set of all expansions supported by the site.
- `region(id: Int): Region` - Obtain a specific region by its ID. The id argument is required and specifies the ID of a single region to retrieve.
- `regions: [Region]` - The set of all regions supported by the site.
- `server(id: Int, region: String, slug: String): Server` - Obtain a specific server either by id or by slug and region. Arguments include: id (optional, the ID of a single server), region (optional, the compact English abbreviation for a specific region like "US"), and slug (optional, a server slug to use with region).
- `subregion(id: Int): Subregion` - Obtain a specific subregion by its ID. The id argument is required and specifies the ID of a single subregion to retrieve.
- `zone(id: Int): Zone` - Obtain a specific zone by its ID. The id argument is required and specifies the ID of a specific zone.
- `zones(expansion_id: Int): [Zone]` - Obtain a set of all zones supported by the site. The expansion_id argument is optional; if omitted, zones from all expansions will be retrieved.
