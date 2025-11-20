# ReportComponentData

**Type:** OBJECT

## Description

The ReportComponentData object provides access to report components and the ability to evaluate them.

## GraphQL Schema Definition

```graphql
type ReportComponentData {
  # List all report components attached to the user owning the current API key.
  components: [ReportComponent]!
  
  # Get a report component by its ID.
  component(
    # The report component ID
    key: String!
  ): ReportComponent
  
  # Evaluate a report component script directly, without creating an object first.
  evaluate(
    contents: String!,
    filter: ReportComponentFilter,
    debug: Boolean,
    reportCode: String!
  ): ReportComponentResult
}
```

## Fields

- `components` - List all report components attached to the user owning the current API key.
- `component` - Get a report component by its ID.
  - Arguments:
    - `key` (String!, required) - The report component ID
- `evaluate` - Evaluate a report component script directly, without creating an object first.
  - Arguments:
    - `contents` (String!, required) - The component script contents.
    - `filter` (ReportComponentFilter) - Filter to apply when evaluating.
    - `debug` (Boolean) - Whether to include debug output.
    - `reportCode` (String!, required) - The report code to evaluate against.

## Notes

⚠️ **Important**: Some argument descriptions were not available in the source documentation and are marked as [Not documented].
