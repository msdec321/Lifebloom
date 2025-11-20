# ReportComponentResult

**Type:** OBJECT

## Description

The result of evaluating a report component script.

## GraphQL Schema Definition

```graphql
type ReportComponentResult {
  # The return value of the component as a JSON string. If the component throws an
  # error, this will be null
  result: JSON
  
  # When evaluated with `debug: True`, this includes the `console.log` output as a
  # string.
  debugOutput: String
  
  # The description of the exception the component threw (if it threw one). Note
  # that component failures DO NOT produce standard GraphQL errors.
  error: String
}
```

## Fields

- `result` - The return value of the component as a JSON string. If the component throws an error, this will be null.
- `debugOutput` - When evaluated with `debug: True`, this includes the `console.log` output as a string.
- `error` - The description of the exception the component threw (if it threw one). Note that component failures DO NOT produce standard GraphQL errors.

## Notes

⚠️ **Important**: Component failures DO NOT produce standard GraphQL errors. Check the `error` field to detect failures.
