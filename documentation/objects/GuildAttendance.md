# GuildAttendance

**Type:** OBJECT

## Description

Attendance for a specific report within a guild.

## GraphQL Schema Definition

```graphql
type GuildAttendance {
  # The code of the report for the raid night.
  code: String!
  
  # The players that attended that raid night.
  players: [PlayerAttendance]
  
  # The start time of the raid night.
  startTime: Float
  
  # The principal zone of the raid night.
  zone: Zone
}
```

## Fields

- `code: String!` - The code of the report for the raid night.
- `players: [PlayerAttendance]` - The players that attended that raid night.
- `startTime: Float` - The start time of the raid night.
- `zone: Zone` - The principal zone of the raid night.

## Required By

- **GuildAttendancePagination**
