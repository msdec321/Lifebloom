# ReportFightNPC

**Type:** OBJECT

## Description

The ReportFightNPC represents participation info within a single fight for an NPC.

## GraphQL Schema Definition

```graphql
type ReportFightNPC {
  # The game ID of the actor. This ID is used in events to identify sources and
  # targets.
  gameID: Int

  # The report ID of the actor. This ID is used in events to identify sources
  # and targets.
  id: Int

  # How many instances of the NPC were seen during the fight.
  instanceCount: Int

  # How many packs of the NPC were seen during the fight.
  groupCount: Int

  # The report ID of the actor that owns this NPC (if it is a pet). This ID is
  # used in events to identify sources and targets.
  petOwner: Int
}
```

## Fields

### gameID

**Type:** `Int`

The game ID of the actor. This ID is used in events to identify sources and targets.

### id

**Type:** `Int`

The report ID of the actor. This ID is used in events to identify sources and targets.

### instanceCount

**Type:** `Int`

How many instances of the NPC were seen during the fight.

### groupCount

**Type:** `Int`

How many packs of the NPC were seen during the fight.

### petOwner

**Type:** `Int`

The report ID of the actor that owns this NPC (if it is a pet). This ID is used in events to identify sources and targets.

