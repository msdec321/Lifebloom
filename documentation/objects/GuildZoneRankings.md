# GuildZoneRankings

**Type:** OBJECT

## Description

A guild's rankings within a zone.

## GraphQL Schema Definition

```graphql
type GuildZoneRankings {
  # The progress ranks for the guild. Always uses the highest difficulty.
  progress(
    # Raid size. Only used for Classic WoW and certain old Retail WoW zones.
    size: Int
  ): WorldRegionServerRankPositions
  
  # The all-star based speed rank for the guild.
  speed(
    # Raid size. Only used for Classic WoW and certain old Retail WoW zones.
    size: Int
    
    # Raid difficulty.
    difficulty: Int
  ): WorldRegionServerRankPositions
  
  # The complete raid speed ranks for the guild. Most non-Classic WoW zones do not
  # support complete raid ranks.
  completeRaidSpeed(
    # Raid size. Only used for Classic WoW and certain old Retail WoW zones.
    size: Int
    
    # Raid difficulty.
    difficulty: Int
  ): WorldRegionServerRankPositions
}
```

## Fields

### progress

The progress ranks for the guild. Always uses the highest difficulty.

**Arguments:**
- `size: Int` - Raid size. Only used for Classic WoW and certain old Retail WoW zones.

**Returns:** `WorldRegionServerRankPositions`

### speed

The all-star based speed rank for the guild.

**Arguments:**
- `size: Int` - Raid size. Only used for Classic WoW and certain old Retail WoW zones.
- `difficulty: Int` - Raid difficulty.

**Returns:** `WorldRegionServerRankPositions`

### completeRaidSpeed

The complete raid speed ranks for the guild. Most non-Classic WoW zones do not support complete raid ranks.

**Arguments:**
- `size: Int` - Raid size. Only used for Classic WoW and certain old Retail WoW zones.
- `difficulty: Int` - Raid difficulty.

**Returns:** `WorldRegionServerRankPositions`

## Required By

- **Guild** - A single guild. Guilds earn their own rankings and contain characters. They may correspond to a guild in-game or be a custom guild created just to hold reports.
