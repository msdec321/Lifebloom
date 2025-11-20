# GuildAttendancePagination

**Type:** OBJECT

## Description

Pagination wrapper for GuildAttendance collections.

## GraphQL Schema Definition

```graphql
type GuildAttendancePagination {
  # List of items on the current page
  data: [GuildAttendance]
  
  # Number of total items selected by the query
  total: Int!
  
  # Number of items returned per page
  per_page: Int!
  
  # Current page of the cursor
  current_page: Int!
  
  # Number of the first item returned
  from: Int
  
  # Number of the last item returned
  to: Int
  
  # The last page (number of pages)
  last_page: Int!
  
  # Determines if cursor has more pages after the current page
  has_more_pages: Boolean!
}
```

## Fields

- `data: [GuildAttendance]` - List of items on the current page
- `total: Int!` - Number of total items selected by the query
- `per_page: Int!` - Number of items returned per page
- `current_page: Int!` - Current page of the cursor
- `from: Int` - Number of the first item returned
- `to: Int` - Number of the last item returned
- `last_page: Int!` - The last page (number of pages)
- `has_more_pages: Boolean!` - Determines if cursor has more pages after the current page

## Required By

- **Guild** - A single guild. Guilds earn their own rankings and contain characters. They may correspond to a guild in-game or be a custom guild created just to hold reports and rankings.
