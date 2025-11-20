# Server

**Type:** OBJECT

## Description

A single server. Servers correspond to actual game servers that characters and guilds reside on.

## GraphQL Schema Definition

```graphql
type Server {
  # The ID of the server.
  id: Int!

  # The name of the server in the locale of the subregion that the server
  # belongs to.
  name: String!

  # The normalized name is a transformation of the name, dropping spaces. It is
  # how the server appears in a World of Warcraft log file.
  normalizedName: String!

  # The server slug, also a transformation of the name following Blizzard
  # rules. For retail World of Warcraft realms, this slug will be in English.
  # For all other games, the slug is just a transformation of the name field.
  slug: String!

  # The region that this server belongs to.
  region: Region!

  # The subregion that this server belongs to.
  subregion: Subregion!

  # The guilds found on this server (and any servers connected to this one.
  # Arguments limit: Optional. The number of guilds to retrieve per page. The
  # maximum allowed value is 100, and minimum allowed value is 1. page:
  # Optional. The page of paginated data to retrieve. If omitted, defaults to
  # the first page.
  limit: Int, page

  # Arguments limit: Optional. The number of characters to retrieve per page.
  # The maximum allowed value is 100, and minimum allowed value is 1. page:
  # Optional. The page of paginated data to retrieve. If omitted, defaults to
  # the first page.
  limit: Int, page

  serverID: Int!

  # The connected realm ID of the server.
  connectedRealmID: Int!

  # The season ID of the server.
  seasonID: Int!
}
```

## Fields

### id

**Type:** `Int!`

The ID of the server.

### name

**Type:** `String!`

The name of the server in the locale of the subregion that the server belongs to.

### normalizedName

**Type:** `String!`

The normalized name is a transformation of the name, dropping spaces. It is how the server appears in a World of Warcraft log file.

### slug

**Type:** `String!`

The server slug, also a transformation of the name following Blizzard rules. For retail World of Warcraft realms, this slug will be in English. For all other games, the slug is just a transformation of the name field.

### region

**Type:** `Region!`

The region that this server belongs to.

### subregion

**Type:** `Subregion!`

The subregion that this server belongs to.

### limit

**Type:** `Int, page`

The guilds found on this server (and any servers connected to this one.  Arguments limit: Optional. The number of guilds to retrieve per page. The maximum allowed value is 100, and minimum allowed value is 1. page: Optional. The page of paginated data to retrieve. If omitted, defaults to the first page.

### limit

**Type:** `Int, page`

 Arguments limit: Optional. The number of characters to retrieve per page. The maximum allowed value is 100, and minimum allowed value is 1. page: Optional. The page of paginated data to retrieve. If omitted, defaults to the first page.

### serverID

**Type:** `Int!`

### connectedRealmID

**Type:** `Int!`

The connected realm ID of the server.

### seasonID

**Type:** `Int!`

The season ID of the server.

