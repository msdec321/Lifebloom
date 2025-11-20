# ReportComponentFilter

**Type:** INPUT_OBJECT

## Description

A broad filter for a report component. This is primarily intended to allow callers to invoke a component on a single fight and/or actor without having to encode these values in their script. If multiple fields are specified, they are treated as ANDs (so a timestamp range with a fight ID includes only events within the timestamp range AND within the fight).

## GraphQL Schema Definition

```graphql
input ReportComponentFilter {
  # Filter input events to those from these fight IDs.
  fightIDs: [Int!]

  # Filter input events to those that include the `actorID` and their pets.
  actorID: Int

  # Filter input events to those within this range.
  componentRange: ReportComponentRangeFilter

  # Filter input events to those from fights having this encounter ID. 0 is used for
  # trash fights and very short boss pulls (typically less than 20s).
  encounterID: Int

  # Filter input events to a specific phase index. Note that if multiple different
  # encounters are included, the phase index will be applied to *each encounter
  # separately* which is probably not what you want.
  phaseIndex: Int

  # Filter input events to only those prior to the `deathCutoff`-th death in each
  # fight.
  #
  # ## Special Values
  #
  # - End after a Called Wipe: -1
  #
  deathCutoff: Int

  # Filter to only include kills, wipes, encounters, or trash. Note: if set to
  # `Trash`, this will override `encounterID`.
  killType: KillType

  # Filter to fights that have the specified difficulty ID. Difficulty IDs are game-
  # and sometimes zone-specific. Use the `difficulties` field of a `Zone` object to
  # retrieve a list of all valid IDs. Trash does not have a difficulty.
  difficulty: Int
}
```

## Fields

- `fightIDs: [Int!]` - Filter input events to those from these fight IDs.
- `actorID: Int` - Filter input events to those that include the specified actorID and their pets.
- `componentRange: ReportComponentRangeFilter` - Filter input events to those within this range.
- `encounterID: Int` - Filter input events to those from fights having this encounter ID. 0 is used for trash fights and very short boss pulls (typically less than 20s).
- `phaseIndex: Int` - Filter input events to a specific phase index. Note that if multiple different encounters are included, the phase index will be applied to each encounter separately which is probably not what you want.
- `deathCutoff: Int` - Filter input events to only those prior to the deathCutoff-th death in each fight. Special value: -1 means end after a Called Wipe.
- `killType: KillType` - Filter to only include kills, wipes, encounters, or trash. Note: if set to Trash, this will override encounterID.
- `difficulty: Int` - Filter to fights that have the specified difficulty ID. Difficulty IDs are game- and sometimes zone-specific. Use the difficulties field of a Zone object to retrieve a list of all valid IDs. Trash does not have a difficulty.
