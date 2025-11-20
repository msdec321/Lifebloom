# Subregion

**Type:** OBJECT

## Description

A single subregion. Subregions are used to divide a region into sub-categories, such as French or German subregions of a Europe region.

## GraphQL Schema Definition

```graphql
type Subregion {
  # The ID of the subregion.
  id: Int!

  # The localized name of the subregion.
  name: String!

  # The region that this subregion is found in.
  region: Region!

  # The servers found within this region. Arguments limit: Optional. The number
  # of servers to retrieve per page. If omitted, defaults to 100. The maximum
  # allowed value is 100, and minimum allowed value is 1. page: Optional. The
  # page of paginated data to retrieve. If omitted, defaults to the first page.
  limit: Int, page
}
```

## Fields

### id

**Type:** `Int!`

The ID of the subregion.

### name

**Type:** `String!`

The localized name of the subregion.

### region

**Type:** `Region!`

The region that this subregion is found in.

### limit

**Type:** `Int, page`

The servers found within this region.  Arguments limit: Optional. The number of servers to retrieve per page. If omitted, defaults to 100. The maximum allowed value is 100, and minimum allowed value is 1. page: Optional. The page of paginated data to retrieve. If omitted, defaults to the first page.

