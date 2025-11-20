# Bracket

**Type:** OBJECT

## Description

A bracket description for a given raid zone. Brackets have a minimum value, maximum value, and a bucket that can be used to establish all of the possible brackets. The type field indicates what the brackets represent, e.g., item levels or game patches, etc.

## GraphQL Schema Definition

```graphql
type Bracket {
  # An integer representing the minimum value used by bracket number 1, etc.
  min: Float!
  
  # An integer representing the value used by bracket N when there are a total of N
  # brackets, etc.
  max: Float!
  
  # A float representing the value to increment when moving from bracket 1 to
  # bracket N, etc.
  bucket: Float!
  
  # The localized name of the bracket type.
  type: String
}
```

## Fields

- `min` (Float!) - An integer representing the minimum value used by bracket number 1, etc.
- `max` (Float!) - An integer representing the value used by bracket N when there are a total of N brackets, etc.
- `bucket` (Float!) - A float representing the value to increment when moving from bracket 1 to bracket N, etc.
- `type` (String) - The localized name of the bracket type.
