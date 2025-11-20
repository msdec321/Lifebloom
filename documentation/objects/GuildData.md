# GuildData

**Type:** OBJECT

## Description

The GuildData object enables the retrieval of single guilds or filtered collections of guilds.

## GraphQL Schema Definition

```graphql
type GuildData {
  # Obtain a specific guild either by id or by name/serverSlug/serverRegion.
  guild(
    # The ID of a single guild to retrieve.
    id: Int
    
    # The name of a specific guild. Must be used in conjunction with serverSlug 
    # and serverRegion to uniquely identify a guild.
    name: String
    
    # The name of a specific guild. Must be used in conjunction with name and 
    # serverRegion to uniquely identify a guild.
    serverSlug: String
    
    # The region for a specific guild. Must be used in conjunction with name and 
    # serverSlug to uniquely identify a guild.
    serverRegion: String
  ): Guild
  
  # The set of all guilds supported by the site. Can be optionally filtered to a
  # specific server id.
  guilds(
    # The number of guilds to retrieve per page. If omitted, defaults to 100. 
    # The maximum allowed value is 100, and minimum allowed value is 1.
    limit: Int
    
    # The page of paginated data to retrieve. If omitted, defaults to the first page.
    page: Int
    
    # The ID of a specific server. If present, only guilds from that server 
    # (and any connected servers) will be fetched.
    serverID: Int
    
    # The slug for a specific server. Must be used in conjunction with serverRegion 
    # to uniquely identify a server. Only guilds from that server (and any connected 
    # servers) will be fetched.
    serverSlug: String
    
    # The region for a specific server. Must be used in conjunction with serverSlug 
    # to uniquely identify a server. Only guilds from that server (and any connected 
    # servers) will be fetched.
    serverRegion: String
  ): GuildPagination
}
```

## Fields

### guild

Obtain a specific guild either by id or by name/serverSlug/serverRegion.

**Arguments:**
- `id: Int` - Optional. The ID of a single guild to retrieve.
- `name: String` - Optional. The name of a specific guild. Must be used in conjunction with serverSlug and serverRegion to uniquely identify a guild.
- `serverSlug: String` - Optional. The name of a specific guild. Must be used in conjunction with name and serverRegion to uniquely identify a guild.
- `serverRegion: String` - Optional. The region for a specific guild. Must be used in conjunction with name and serverSlug to uniquely identify a guild.

**Returns:** `Guild`

### guilds

The set of all guilds supported by the site. Can be optionally filtered to a specific server id.

**Arguments:**
- `limit: Int` - Optional. The number of guilds to retrieve per page. If omitted, defaults to 100. The maximum allowed value is 100, and minimum allowed value is 1.
- `page: Int` - Optional. The page of paginated data to retrieve. If omitted, defaults to the first page.
- `serverID: Int` - Optional. The ID of a specific server. If present, only guilds from that server (and any connected servers) will be fetched.
- `serverSlug: String` - Optional. The slug for a specific server. Must be used in conjunction with serverRegion to uniquely identify a server. Only guilds from that server (and any connected servers) will be fetched.
- `serverRegion: String` - Optional. The region for a specific server. Must be used in conjunction with serverSlug to uniquely identify a server. Only guilds from that server (and any connected servers) will be fetched.

**Returns:** `GuildPagination`

## Required By

- **Query**
