# GameData

**Type:** OBJECT

## Description

The game object contains collections of data such as NPCs, classes, abilities, items, maps, etc. Game data only changes when major game patches are released, so you should cache results for as long as possible and only update when new content is released for the game.

## GraphQL Schema Definition

```graphql
type GameData {
  # The player and enemy abilities for the game.
  #
  # Arguments
  # limit: Optional. The number of abilities to retrieve per page.
  # If omitted, defaults to 100. The maximum allowed value is 100, and minimum
  # allowed value is 1.
  # page: Optional. The page of paginated data to retrieve. If
  # omitted, defaults to the first page.
  abilities(limit: Int, page: Int): GameAbilityPagination
  
  # Obtain a single ability for the game.
  #
  # Arguments
  # id: Required. Specify a specific ability to retrieve by its id.
  ability(id: Int): GameAbility
  
  # Obtain a single achievement for the game.
  #
  # Arguments
  # id: Required. Specify a specific achievement to retrieve by its
  # id.
  achievement(id: Int): GameAchievement
  
  # Achievements for the game.
  #
  # Arguments
  # limit: Optional. The number of achievements to retrieve per
  # page. If omitted, defaults to 100. The maximum allowed value is 100, and minimum
  # allowed value is 1.
  # page: Optional. The page of paginated data to retrieve. If
  # omitted, defaults to the first page.
  achievements(limit: Int, page: Int): GameAchievementPagination
  
  # Obtain a single affix for the game.
  #
  # Arguments
  # id: Required. Specify a specific affix to retrieve by its id.
  affix(id: Int): GameAffix
  
  # The affixes for the game.
  affixes: [GameAffix]
  
  # Obtain a single class for the game.
  #
  # Arguments
  # id: Required. Specify a specific class to retrieve by its id.
  # faction_id: Optional. Specify which faction you are retrieving
  # the set of classes for. If the game has faction-specific classes, then the
  # correct slugs and names will be returned for that faction.
  # zone_id: Optional. Specify which zone you are retrieving the
  # set of classes for. The classes that existed at the time the zone was relevant
  # will be returned.
  class(id: Int, faction_id: Int, zone_id: Int): GameClass
  
  # Obtain the supported classes for the game.
  #
  # Arguments
  # faction_id: Optional. Specify which faction you are retrieving
  # the set of classes for. If the game has faction-specific classes, then the
  # correct slugs and names will be returned for that faction.
  # zone_id: Optional. Specify which zone you are retrieving the
  # set of classes for. The classes that existed at the time the zone was relevant
  # will be returned.
  classes(faction_id: Int, zone_id: Int): [GameClass]
  
  # Obtain a single enchant for the game.
  #
  # Arguments
  # id: Required. Specify a specific enchant to retrieve by its id.
  enchant(id: Int): GameEnchant
  
  # Enchants for the game.
  #
  # Arguments
  # limit: Optional. The number of enchants to retrieve per page.
  # If omitted, defaults to 100. The maximum allowed value is 100, and minimum
  # allowed value is 1.
  # page: Optional. The page of paginated data to retrieve. If
  # omitted, defaults to the first page.
  enchants(limit: Int, page: Int): GameEnchantPagination
  
  # Obtain all the factions that guilds and players can belong to.
  factions: [GameFaction]
  
  # Obtain a single item for the game.
  #
  # Arguments
  # id: Required. Specify a specific item to retrieve by its id.
  item(id: Int): GameItem
  
  # Obtain a single item set for the game.
  #
  # Arguments
  # id: Required. Specify a specific item set to retrieve by its
  # id.
  itemSet(id: Int): GameItemSet
  
  # Item sets for the game.
  #
  # Arguments
  # limit: Optional. The number of item sets to retrieve per page.
  # If omitted, defaults to 100. The maximum allowed value is 100, and minimum
  # allowed value is 1.
  # page: Optional. The page of paginated data to retrieve. If
  # omitted, defaults to the first page.
  itemSets(limit: Int, page: Int): GameItemSetPagination
  
  # Items for the game.
  #
  # Arguments
  # limit: Optional. The number of items to retrieve per page. If
  # omitted, defaults to 100. The maximum allowed value is 100, and minimum allowed
  # value is 1.
  # page: Optional. The page of paginated data to retrieve. If
  # omitted, defaults to the first page.
  items(limit: Int, page: Int): GameItemPagination
  
  # Obtain a single map for the game.
  #
  # Arguments
  # id: Required. Specify a specific map to retrieve by its id.
  map(id: Int): GameMap
  
  # Maps for the game.
  #
  # Arguments
  # limit: Optional. The number of maps to retrieve per page. If
  # omitted, defaults to 100. The maximum allowed value is 100, and minimum allowed
  # value is 1.
  # page: Optional. The page of paginated data to retrieve. If
  # omitted, defaults to the first page.
  maps(limit: Int, page: Int): GameMapPagination
  
  # Obtain a single NPC for the game.
  #
  # Arguments
  # id: Required. Specify a specific NPC to retrieve by its id.
  npc(id: Int): GameNPC
  
  # NPCs for the game.
  #
  # Arguments
  # limit: Optional. The number of NPCs to retrieve per page. If
  # omitted, defaults to 100. The maximum allowed value is 100, and minimum allowed
  # value is 1.
  # page: Optional. The page of paginated data to retrieve. If
  # omitted, defaults to the first page.
  npcs(limit: Int, page: Int): GameNPCPagination
  
  # Obtain a single zone for the game, not to be confused with the worldData zones
  # for ranking bosses and dungeons.
  #
  # Arguments
  # id: Required. Specify a specific game zone to retrieve by its
  # id.
  zone(id: Int): GameZone
  
  # Zones for the game.
  #
  # Arguments
  # limit: Optional. The number of game zones to retrieve per page.
  # If omitted, defaults to 100. The maximum allowed value is 100, and minimum
  # allowed value is 1.
  # page: Optional. The page of paginated data to retrieve. If
  # omitted, defaults to the first page.
  zones(limit: Int, page: Int): GameZonePagination
}
```

## Fields

### Query Fields

- `abilities(limit: Int, page: Int)` - The player and enemy abilities for the game. Returns [GameAbilityPagination](GameAbilityPagination.md)
- `ability(id: Int)` - Obtain a single ability for the game by its id. Returns [GameAbility](GameAbility.md)
- `achievement(id: Int)` - Obtain a single achievement for the game by its id. Returns [GameAchievement](GameAchievement.md)
- `achievements(limit: Int, page: Int)` - Achievements for the game. Returns [GameAchievementPagination](GameAchievementPagination.md)
- `affix(id: Int)` - Obtain a single affix for the game by its id. Returns [GameAffix](GameAffix.md)
- `affixes` - The affixes for the game. Returns [[GameAffix](GameAffix.md)]
- `class(id: Int, faction_id: Int, zone_id: Int)` - Obtain a single class for the game. Returns [GameClass](GameClass.md)
- `classes(faction_id: Int, zone_id: Int)` - Obtain the supported classes for the game. Returns [[GameClass](GameClass.md)]
- `enchant(id: Int)` - Obtain a single enchant for the game by its id. Returns [GameEnchant](GameEnchant.md)
- `enchants(limit: Int, page: Int)` - Enchants for the game. Returns [GameEnchantPagination](GameEnchantPagination.md)
- `factions` - Obtain all the factions that guilds and players can belong to. Returns [[GameFaction](GameFaction.md)]
- `item(id: Int)` - Obtain a single item for the game by its id. Returns [GameItem](GameItem.md)
- `itemSet(id: Int)` - Obtain a single item set for the game by its id. Returns [GameItemSet](GameItemSet.md)
- `itemSets(limit: Int, page: Int)` - Item sets for the game. Returns [GameItemSetPagination](GameItemSetPagination.md)
- `items(limit: Int, page: Int)` - Items for the game. Returns [GameItemPagination](GameItemPagination.md)
- `map(id: Int)` - Obtain a single map for the game by its id. Returns [GameMap](GameMap.md)
- `maps(limit: Int, page: Int)` - Maps for the game. Returns [GameMapPagination](GameMapPagination.md)
- `npc(id: Int)` - Obtain a single NPC for the game by its id. Returns [GameNPC](GameNPC.md)
- `npcs(limit: Int, page: Int)` - NPCs for the game. Returns [GameNPCPagination](GameNPCPagination.md)
- `zone(id: Int)` - Obtain a single zone for the game (not to be confused with worldData zones for ranking bosses and dungeons). Returns [GameZone](GameZone.md)
- `zones(limit: Int, page: Int)` - Zones for the game. Returns [GameZonePagination](GameZonePagination.md)

## Notes

### Pagination Parameters

Most collection endpoints support pagination with these optional parameters:
- `limit` - The number of items to retrieve per page (default: 100, min: 1, max: 100)
- `page` - The page of paginated data to retrieve (default: 1)

### Caching

⚠️ **Important**: Game data only changes when major game patches are released. You should cache results for as long as possible and only update when new content is released for the game.
