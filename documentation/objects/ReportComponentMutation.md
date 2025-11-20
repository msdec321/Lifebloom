# ReportComponentMutation

**Type:** OBJECT

## Description

The ReportComponentMutation object provides mutations for creating, updating, and deleting report components.

## GraphQL Schema Definition

```graphql
type ReportComponentMutation {
  # Create a new (possibly empty) report component. If successful, the KEY of the
  # new component will be returned.
  create(
    # A human-readable name for the component.
    name: String!,
    
    # The (optional) initial contents of the component. Evaluating an empty 
    # component will produce an error.
    contents: String
  ): String
  
  # Update the script contents of a report component, replacing the old contents.
  # True is returned on success, errors are thrown on failure.
  update(
    key: String!,
    
    # The new script contents, in JavaScript.
    contents: String!
  ): Boolean
  
  # Mark (or un-mark) a component as "deletion protected" to prevent accidental
  # deletion. This is a quality of life feature to prevent oopsies, not a security
  # feature.
  setProtection(
    key: String!,
    
    # Whether the component is protected from deletion. Default is `true`.
    protected: Boolean
  ): Boolean
  
  # Delete a report component. Since this is an API call, there is NO CONFIRMATION.
  # Protected components may not be deleted.
  delete(
    key: String!
  ): Boolean
}
```

## Fields

- `create` - Create a new (possibly empty) report component. If successful, the KEY of the new component will be returned.
  - Arguments:
    - `name` (String!, required) - A human-readable name for the component.
    - `contents` (String, optional) - The (optional) initial contents of the component. Evaluating an empty component will produce an error.
- `update` - Update the script contents of a report component, replacing the old contents. True is returned on success, errors are thrown on failure.
  - Arguments:
    - `key` (String!, required) - The component key to update.
    - `contents` (String!, required) - The new script contents, in JavaScript.
- `setProtection` - Mark (or un-mark) a component as "deletion protected" to prevent accidental deletion. This is a quality of life feature to prevent oopsies, not a security feature.
  - Arguments:
    - `key` (String!, required) - The component key to protect/unprotect.
    - `protected` (Boolean, optional) - Whether the component is protected from deletion. Default is `true`.
- `delete` - Delete a report component. Since this is an API call, there is NO CONFIRMATION. Protected components may not be deleted.
  - Arguments:
    - `key` (String!, required) - The component key to delete.

## Notes

⚠️ **Warning**: The `delete` mutation has NO CONFIRMATION. Use with caution. Protected components may not be deleted.

⚠️ **Important**: Some argument descriptions were not available in the source documentation and are marked as [Not documented].
