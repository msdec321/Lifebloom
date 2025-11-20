# ServerPagination

**Type:** OBJECT

## Description



## GraphQL Schema Definition

```graphql
type ServerPagination {
  # List of items on the current page
  data: Server]

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

### data

**Type:** `Server]`

List of items on the current page

### total

**Type:** `Int!`

### per_page

**Type:** `Int!`

Number of items returned per page

### current_page

**Type:** `Int!`

Current page of the cursor

### from

**Type:** `Int`

Number of the first item returned

### to

**Type:** `Int`

Number of the last item returned

### last_page

**Type:** `Int!`

The last page (number of pages)

### has_more_pages

**Type:** `Boolean!`

Determines if cursor has more pages after the current page

