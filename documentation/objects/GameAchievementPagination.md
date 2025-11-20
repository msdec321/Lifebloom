# GameAchievementPagination

**Type:** OBJECT

## Description

Pagination object for GameAchievement results.

## GraphQL Schema Definition

```graphql
type GameAchievementPagination {
  # List of items on the current page
  data: [GameAchievement]
  
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

- `data` - List of [GameAchievement](GameAchievement.md) items on the current page
- `total` - Number of total items selected by the query
- `per_page` - Number of items returned per page
- `current_page` - Current page of the cursor
- `from` - Number of the first item returned
- `to` - Number of the last item returned
- `last_page` - The last page (number of pages)
- `has_more_pages` - Determines if cursor has more pages after the current page
