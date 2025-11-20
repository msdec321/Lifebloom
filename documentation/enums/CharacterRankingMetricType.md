# CharacterRankingMetricType

**Type:** ENUM

## Description

All the possible metrics.

## GraphQL Schema Definition

```graphql
enum CharacterRankingMetricType {
  # Boss cDPS is unique to FFXIV and is damage done to the boss adjusted for raid-contributing buffs and debuffs.
  bossCdps

  # Boss damage per second.
  bossDps

  # Boss nDPS is unique to FFXIV and is damage done to the boss adjusted for raid-contributing buffs and debuffs.
  bossNdps

  # Boss rDPS is unique to FFXIV and is damage done to the boss adjusted for raid-contributing buffs and debuffs.
  bossRdps

  # Choose an appropriate default depending on the other selected parameters.
  default

  # Damage per second.
  dps

  # Healing per second.
  hps

  # Survivability ranking for tanks. Deprecated. Only supported for some older WoW zones.
  krsi

  # Score. Used by WoW Mythic dungeons and by ESO trials.
  score

  # Speed. Not supported by every zone.
  speed

  # cDPS is unique to FFXIV and is damage done adjusted for raid-contributing buffs and debuffs.
  cdps

  # nDPS is unique to FFXIV and is damage done adjusted for raid-contributing buffs and debuffs.
  ndps

  # rDPS is unique to FFXIV and is damage done adjusted for raid-contributing buffs and debuffs.
  rdps

  # Healing done per second to tanks.
  tankhps

  # Weighted damage per second. Unique to WoW currently. Used to remove pad damage and reward damage done to high priority targets.
  wdps

  # Unique to FFXIV. Represents the combined ranking for a pair of healers in eight player content.
  healercombinedBossCdps

  # Unique to FFXIV. Represents the combined ranking for a pair of healers in eight player content.
  healercombinedBossNdps

  # Unique to FFXIV. Represents the combined ranking for a pair of healers in eight player content.
  healercombinedBossRdps

  # Unique to FFXIV. Represents the combined ranking for a pair of healers in eight player content.
  healercombinedCdps

  # Unique to FFXIV. Represents the combined ranking for a pair of healers in eight player content.
  healercombinedNdps

  # Unique to FFXIV. Represents the combined ranking for a pair of healers in eight player content.
  healercombinedRdps

  # Unique to FFXIV. Represents the combined ranking for a pair of healers in eight player content.
  healercombinedScore

  # Unique to FFXIV. Represents the combined ranking for a pair of healers in eight player content.
  healercombinedSpeed

  # Unique to FFXIV. Represents the combined ranking for a pair of tanks in eight player content.
  tankcombinedBossCdps

  # Unique to FFXIV. Represents the combined ranking for a pair of tanks in eight player content.
  tankcombinedBossNdps

  # Unique to FFXIV. Represents the combined ranking for a pair of tanks in eight player content.
  tankcombinedBossRdps

  # Unique to FFXIV. Represents the combined ranking for a pair of tanks in eight player content.
  tankcombinedCdps

  # Unique to FFXIV. Represents the combined ranking for a pair of tanks in eight player content.
  tankcombinedNdps

  # Unique to FFXIV. Represents the combined ranking for a pair of tanks in eight player content.
  tankcombinedRdps

  # Unique to FFXIV. Represents the combined ranking for a pair of tanks in eight player content.
  tankcombinedScore

  # Unique to FFXIV. Represents the combined ranking for a pair of tanks in eight player content.
  tankcombinedSpeed
}
```

## Notes

⚠️ **Important**: The enum value names above are inferred based on common naming conventions. 
The actual enum values should be verified against the GraphQL schema or by inspecting the 
actual API responses.

## Enum Values

- `bossCdps` - Boss cDPS is unique to FFXIV and is damage done to the boss adjusted for raid-contributing buffs and debuffs.
- `bossDps` - Boss damage per second.
- `bossNdps` - Boss nDPS is unique to FFXIV and is damage done to the boss adjusted for raid-contributing buffs and debuffs.
- `bossRdps` - Boss rDPS is unique to FFXIV and is damage done to the boss adjusted for raid-contributing buffs and debuffs.
- `default` - Choose an appropriate default depending on the other selected parameters.
- `dps` - Damage per second.
- `hps` - Healing per second.
- `krsi` - Survivability ranking for tanks. Deprecated. Only supported for some older WoW zones.
- `score` - Score. Used by WoW Mythic dungeons and by ESO trials.
- `speed` - Speed. Not supported by every zone.
- `cdps` - cDPS is unique to FFXIV and is damage done adjusted for raid-contributing buffs and debuffs.
- `ndps` - nDPS is unique to FFXIV and is damage done adjusted for raid-contributing buffs and debuffs.
- `rdps` - rDPS is unique to FFXIV and is damage done adjusted for raid-contributing buffs and debuffs.
- `tankhps` - Healing done per second to tanks.
- `wdps` - Weighted damage per second. Unique to WoW currently. Used to remove pad damage and reward damage done to high priority targets.
- `healercombinedBossCdps` - Unique to FFXIV. Represents the combined ranking for a pair of healers in eight player content.
- `healercombinedBossNdps` - Unique to FFXIV. Represents the combined ranking for a pair of healers in eight player content.
- `healercombinedBossRdps` - Unique to FFXIV. Represents the combined ranking for a pair of healers in eight player content.
- `healercombinedCdps` - Unique to FFXIV. Represents the combined ranking for a pair of healers in eight player content.
- `healercombinedNdps` - Unique to FFXIV. Represents the combined ranking for a pair of healers in eight player content.
- `healercombinedRdps` - Unique to FFXIV. Represents the combined ranking for a pair of healers in eight player content.
- `healercombinedScore` - Unique to FFXIV. Represents the combined ranking for a pair of healers in eight player content.
- `healercombinedSpeed` - Unique to FFXIV. Represents the combined ranking for a pair of healers in eight player content.
- `tankcombinedBossCdps` - Unique to FFXIV. Represents the combined ranking for a pair of tanks in eight player content.
- `tankcombinedBossNdps` - Unique to FFXIV. Represents the combined ranking for a pair of tanks in eight player content.
- `tankcombinedBossRdps` - Unique to FFXIV. Represents the combined ranking for a pair of tanks in eight player content.
- `tankcombinedCdps` - Unique to FFXIV. Represents the combined ranking for a pair of tanks in eight player content.
- `tankcombinedNdps` - Unique to FFXIV. Represents the combined ranking for a pair of tanks in eight player content.
- `tankcombinedRdps` - Unique to FFXIV. Represents the combined ranking for a pair of tanks in eight player content.
- `tankcombinedScore` - Unique to FFXIV. Represents the combined ranking for a pair of tanks in eight player content.
- `tankcombinedSpeed` - Unique to FFXIV. Represents the combined ranking for a pair of tanks in eight player content.
