# GuildRank

**Type:** ENUM

## Description

Rank within a guild or team on the website. This is separate from in-game ranks and does NOT correspond to the rank of the user or character in-game.

## GraphQL Schema Definition

```graphql
enum GuildRank {
  # The user is not a member of this guild or team.
  NonMember
}
```

## Notes

⚠️ **Important**: The enum value names above are inferred based on common naming conventions. 
The actual enum values should be verified against the GraphQL schema or by inspecting the 
actual API responses.

## Enum Values

- `NonMember` - The user is not a member of this guild or team.
