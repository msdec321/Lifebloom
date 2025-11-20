# ReportDungeonPullNPC

**Type:** OBJECT

## Description

The ReportDungeonPullNPC represents participation info within a single dungeon pull for an NPC.

## GraphQL Schema Definition

```graphql
type ReportDungeonPullNPC {
  # The report ID of the actor. This ID is used in events to identify sources
  # and targets.
  id: Int

  # The game ID of the actor, e.g., so it can be looked up on external Web
  # sites.
  gameID: Int

  # The lowest instance ID seen during the pull.
  minimumInstanceID: Int

  # The highest instance ID seen during the pull.
  maximumInstanceID: Int

  # The lowest instance group ID seen during the pull.
  minimumInstanceGroupID: Int

  # The highest instance group ID seen during the pull.
  maximumInstanceGroupID: Int
}
```

## Fields

### id

**Type:** `Int`

The report ID of the actor. This ID is used in events to identify sources and targets.

### gameID

**Type:** `Int`

The game ID of the actor, e.g., so it can be looked up on external Web sites.

### minimumInstanceID

**Type:** `Int`

The lowest instance ID seen during the pull.

### maximumInstanceID

**Type:** `Int`

The highest instance ID seen during the pull.

### minimumInstanceGroupID

**Type:** `Int`

The lowest instance group ID seen during the pull.

### maximumInstanceGroupID

**Type:** `Int`

The highest instance group ID seen during the pull.

