# FightRankingMetricType

**Type:** ENUM

## Description

All the possible metrics.

## GraphQL Schema Definition

```graphql
enum FightRankingMetricType {
  # Choose an appropriate default depending on the other selected parameters.
  default

  # A metric that rewards minimizing deaths and damage taken.
  execution

  # Feats of strength in WoW or Challenges in FF.
  feats

  # For Mythic+ dungeons in WoW, represents the team's score. Used for ESO trials and dungeons also.
  score

  # Speed metric, based off the duration of the fight.
  speed

  # Progress metric, based off when the fight was defeated.
  progress
}
```

## Notes

⚠️ **Important**: The enum value names above are inferred based on common naming conventions. 
The actual enum values should be verified against the GraphQL schema or by inspecting the 
actual API responses.

## Enum Values

- `default` - Choose an appropriate default depending on the other selected parameters.
- `execution` - A metric that rewards minimizing deaths and damage taken.
- `feats` - Feats of strength in WoW or Challenges in FF.
- `score` - For Mythic+ dungeons in WoW, represents the team's score. Used for ESO trials and dungeons also.
- `speed` - Speed metric, based off the duration of the fight.
- `progress` - Progress metric, based off when the fight was defeated.
