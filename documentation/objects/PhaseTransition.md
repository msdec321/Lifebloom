# PhaseTransition

**Type:** OBJECT

## Description

A spartan representation of phase transitions during a fight.

## GraphQL Schema Definition

```graphql
type PhaseTransition {
  # The 1-indexed id of the phase. Phase IDs are absolute within a fight: phases
  # with the same ID correspond to the same semantic phase.
  id: Int!
  
  # The report-relative timestamp of the transition into the phase. The phase ends
  # at the beginning of the next phase, or at the end of the fight.
  startTime: Int!
}
```

## Fields

- `id` - The 1-indexed id of the phase. Phase IDs are absolute within a fight: phases with the same ID correspond to the same semantic phase.
- `startTime` - The report-relative timestamp of the transition into the phase. The phase ends at the beginning of the next phase, or at the end of the fight.
