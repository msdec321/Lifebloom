# ReportMasterData

**Type:** OBJECT

## Description

The ReporMastertData object contains information about the log version of a report, as well as the actors and abilities used in the report.

## GraphQL Schema Definition

```graphql
type ReportMasterData {
  # The version of the client parser that was used to parse and upload this log
  # file.
  logVersion: Int!

  # The version of the game that generated the log file. Used to distinguish
  # Classic and Retail Warcraft primarily.
  gameVersion: Int

  # The auto-detected locale of the report. This is the source language of the
  # original log file.
  lang: String

  # A list of every ability that occurs in the report.
  abilities: ReportAbility]

  # Arguments type: Optional. A filter on the actors in a report. If the type
  # field of the actor matches the specified type field, it will be included.
  # subType: Optional. A filter on the actors in a report. If the subType field
  # of the actor matches the specified subType field, it will be included.
  type: String, subType
}
```

## Fields

### logVersion

**Type:** `Int!`

The version of the client parser that was used to parse and upload this log file.

### gameVersion

**Type:** `Int`

The version of the game that generated the log file. Used to distinguish Classic and Retail Warcraft primarily.

### lang

**Type:** `String`

The auto-detected locale of the report. This is the source language of the original log file.

### abilities

**Type:** `ReportAbility]`

A list of every ability that occurs in the report.

### type

**Type:** `String, subType`

 Arguments type: Optional. A filter on the actors in a report. If the type field of the actor matches the specified type field, it will be included. subType: Optional. A filter on the actors in a report. If the subType field of the actor matches the specified subType field, it will be included.

