# Partition

**Type:** OBJECT

## Description

A single partition for a given raid zone. Partitions have an integer value representing the actual partition and a localized name that describes what the partition represents. Partitions contain their own rankings, statistics and all stars.

## GraphQL Schema Definition

```graphql
type Partition {
  # An integer representing a specific partition within a zone.
  id: Int!
  
  # The localized name for partition.
  name: String!
  
  # The compact localized name for the partition. Typically an abbreviation to
  # conserve space.
  compactName: String!
  
  # Whether or not the partition is the current default when viewing rankings or
  # statistics for the zone.
  default: Boolean!
}
```

## Fields

- `id` - An integer representing a specific partition within a zone.
- `name` - The localized name for partition.
- `compactName` - The compact localized name for the partition. Typically an abbreviation to conserve space.
- `default` - Whether or not the partition is the current default when viewing rankings or statistics for the zone.
