# EncounterPhases

**Type:** OBJECT

## Description

Phase information for an encounter.

## GraphQL Schema Definition

```graphql
type EncounterPhases {
  # The encounter ID
  encounterID: Int!
  
  # Whether the phases can be used to separate wipes in the report UI.
  separatesWipes: Boolean
  
  # Phase metadata for all phases in this encounter.
  phases: [PhaseMetadata!]
}
```

## Fields

- `encounterID` (Int!) - The encounter ID
- `separatesWipes` (Boolean) - Whether the phases can be used to separate wipes in the report UI.
- `phases` ([PhaseMetadata!]) - Phase metadata for all phases in this encounter.
