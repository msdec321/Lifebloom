# GameMapPagination

**Type:** OBJECT

## Description

Pagination wrapper for GameMap collections.

## GraphQL Schema Definition

```graphql
type GameMapPagination {
  # List of items on the current page
  data: [GameMap]
  
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

- `data: [GameMap]` - List of items on the current page
- `total: Int!` - Number of total items selected by the query
- `per_page: Int!` - Number of items returned per page
- `current_page: Int!` - Current page of the cursor
- `from: Int` - Number of the first item returned
- `to: Int` - Number of the last item returned
- `last_page: Int!` - The last page (number of pages)
- `has_more_pages: Boolean!` - Determines if cursor has more pages after the current page

## Required By

- **GameData** - The game object contains collections of data such as NPCs, classes, abilities, items, maps, etc. Game data only changes when major game patches are released.
