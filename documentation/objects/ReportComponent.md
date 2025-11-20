# ReportComponent

**Type:** OBJECT

## Description

A report component represents a custom script that can be evaluated against report data.

## GraphQL Schema Definition

```graphql
type ReportComponent {
  # The component's unique key.
  key: String!
  
  # The human-readable name of the component
  name: String!
  
  # Whether the component is currently protected from deletion.
  protected: Boolean!
  
  # The contents of the component script.
  contents: String
  
  # Evaluate a report component against report data, returning the result.
  evaluate(
    filter: ReportComponentFilter,
    debug: Boolean,
    reportCode: String!
  ): ReportComponentResult
}
```

## Fields

- `key` - The component's unique key.
- `name` - The human-readable name of the component.
- `protected` - Whether the component is currently protected from deletion.
- `contents` - The contents of the component script.
- `evaluate` - Evaluate a report component against report data, returning the result.
  - Arguments:
    - `filter` (ReportComponentFilter) - Filter to apply when evaluating the component.
    - `debug` (Boolean) - Whether to include debug output.
    - `reportCode` (String!, required) - The report code to evaluate against.

## Notes

⚠️ **Important**: Some argument descriptions were not available in the source documentation and are marked as [Not documented].
