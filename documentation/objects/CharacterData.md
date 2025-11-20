# CharacterData

**Type:** OBJECT

## Description

The CharacterData object enables the retrieval of single characters or filtered collections of characters.

## GraphQL Schema Definition

```graphql
type CharacterData {
  # Obtain a specific character either by id or by name/server_slug/server_region.
  #
  # Arguments
  # id: Optional. The ID of a single character to retrieve.
  # name: Optional. The name of a specific character. Must be used
  # in conjunction with serverSlug and serverRegion to uniquely identify a
  # character.
  # serverSlug: Optional. The slug of a specific server. Must be
  # used in conjunction with name and serverRegion to uniquely identify a character.
  # serverRegion: Optional. The region for a specific character.
  # Must be used in conjunction with name and serverRegion to uniquely identify a
  # character.
  character(
    id: Int,
    name: String,
    serverSlug: String,
    serverRegion: String
  ): Character
  
  # A collection of characters for a specific guild.
  #
  # Arguments
  # guildID: Required. The ID of a specific guild. Characters from
  # that guild will be fetched.
  # limit: Optional. The number of characters to retrieve per page.
  # If omitted, defaults to 100. The maximum allowed value is 100, and minimum
  # allowed value is 1.
  # page: Optional. The page of paginated data to retrieve. If
  # omitted, defaults to the first page.
  characters(
    guildID: Int,
    limit: Int,
    page: Int
  ): CharacterPagination
}
```

## Fields

### character

Obtain a specific character either by id or by name/server_slug/server_region.

**Arguments:**
- `id` (Int) - Optional. The ID of a single character to retrieve.
- `name` (String) - Optional. The name of a specific character. Must be used in conjunction with serverSlug and serverRegion to uniquely identify a character.
- `serverSlug` (String) - Optional. The slug of a specific server. Must be used in conjunction with name and serverRegion to uniquely identify a character.
- `serverRegion` (String) - Optional. The region for a specific character. Must be used in conjunction with name and serverRegion to uniquely identify a character.

**Returns:** Character

### characters

A collection of characters for a specific guild.

**Arguments:**
- `guildID` (Int) - Required. The ID of a specific guild. Characters from that guild will be fetched.
- `limit` (Int) - Optional. The number of characters to retrieve per page. If omitted, defaults to 100. The maximum allowed value is 100, and minimum allowed value is 1.
- `page` (Int) - Optional. The page of paginated data to retrieve. If omitted, defaults to the first page.

**Returns:** CharacterPagination
