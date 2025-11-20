# ReportActor

**Type:** OBJECT

## Description

The ReportActor represents a single player, pet or NPC that occurs in the report.

## GraphQL Schema Definition

```graphql
type ReportActor {
  # The game ID of the actor.
  gameID: Float
  
  # An icon to use for the actor. For pets and NPCs, this will be the icon the site
  # chose to represent that actor.
  icon: String
  
  # The report ID of the actor. This ID is used in events to identify sources and
  # targets.
  id: Int
  
  # The name of the actor.
  name: String
  
  # The report ID of the actor's owner if the actor is a pet.
  petOwner: Int
  
  # The normalized server name of the actor.
  server: String
  
  # The sub-type of the actor, for players it's their class, and for NPCs, they are
  # further subdivided into normal NPCs and bosses.
  subType: String
  
  # The type of the actor, i.e., if it is a player, pet or NPC.
  type: String
}
```

## Fields

- `gameID` - The game ID of the actor.
- `icon` - An icon to use for the actor. For pets and NPCs, this will be the icon the site chose to represent that actor.
- `id` - The report ID of the actor. This ID is used in events to identify sources and targets.
- `name` - The name of the actor.
- `petOwner` - The report ID of the actor's owner if the actor is a pet.
- `server` - The normalized server name of the actor.
- `subType` - The sub-type of the actor, for players it's their class, and for NPCs, they are further subdivided into normal NPCs and bosses.
- `type` - The type of the actor, i.e., if it is a player, pet or NPC.
