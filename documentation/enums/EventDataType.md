# EventDataType

**Type:** ENUM

## Description

The type of events or tables to examine.

## GraphQL Schema Definition

```graphql
enum EventDataType {
  # All Events
  All

  # Buffs.
  Buffs

  # Casts.
  Casts

  # Combatant info events (includes gear).
  CombatantInfo

  # Damage done.
  DamageDone

  # Damage taken.
  DamageTaken

  # Deaths.
  Deaths

  # Debuffs.
  Debuffs

  # Dispels.
  Dispels

  # Healing done.
  Healing

  # Interrupts.
  Interrupts

  # Resources.
  Resources

  # Summons
  Summons

  # Threat.
  Threat
}
```

## Notes

⚠️ **Important**: The enum value names above are inferred based on common naming conventions. 
The actual enum values should be verified against the GraphQL schema or by inspecting the 
actual API responses.

## Enum Values

- `All` - All Events
- `Buffs` - Buffs.
- `Casts` - Casts.
- `CombatantInfo` - Combatant info events (includes gear).
- `DamageDone` - Damage done.
- `DamageTaken` - Damage taken.
- `Deaths` - Deaths.
- `Debuffs` - Debuffs.
- `Dispels` - Dispels.
- `Healing` - Healing done.
- `Interrupts` - Interrupts.
- `Resources` - Resources.
- `Summons` - Summons
- `Threat` - Threat.
