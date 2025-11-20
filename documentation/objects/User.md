# User

**Type:** OBJECT

## Description

A single user of the site. Most fields can only be accessed when authenticated as that user with the "view-user-profile" scope.

## GraphQL Schema Definition

```graphql
type User {
  # The ID of the user.
  id: Int!

  # The name of the user.
  name: String!

  # The avatar of the user, typically the main character avatar.
  avatar: String!

  # The list of guilds to which the user belongs. Only accessible via user
  # authentication when you have the "view-user-profile" scope.
  guilds: Guild]

  # when you have the "view-user-profile" scope.
  characters: Character]

  battleTag: String
}
```

## Fields

### id

**Type:** `Int!`

The ID of the user.

### name

**Type:** `String!`

The name of the user.

### avatar

**Type:** `String!`

The avatar of the user, typically the main character avatar.

### guilds

**Type:** `Guild]`

The list of guilds to which the user belongs. Only accessible via user authentication when you have the "view-user-profile" scope.

### characters

**Type:** `Character]`

when you have the "view-user-profile" scope.

### battleTag

**Type:** `String`

