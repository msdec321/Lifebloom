# ReportArchiveStatus

**Type:** OBJECT

## Description

The archival status of a report.

## GraphQL Schema Definition

```graphql
type ReportArchiveStatus {
  # Whether the report has been archived.
  isArchived: Boolean!
  
  # Whether the current user can access the report. Always true if the report is not
  # archived, and always false if not using user authentication.
  isAccessible: Boolean!
  
  # The date on which the report was archived (if it has been archived).
  archiveDate: Int
}
```

## Fields

- `isArchived` - Whether the report has been archived.
- `isAccessible` - Whether the current user can access the report. Always true if the report is not archived, and always false if not using user authentication.
- `archiveDate` - The date on which the report was archived (if it has been archived).
