# SubscriptionStatus

**Type:** ENUM

## Description

The type of Subscription.

## GraphQL Schema Definition

```graphql
enum SubscriptionStatus {
  # Silver Tier subscription
  Silver

  # Gold Tier subscription
  Gold

  # Platinum Tier subscription
  Platinum

  # Legacy Silver Tier subscription
  LegacySilver
  @deprecated(reason: "Legacy Silver subscriptions are not available for new users.")

  # Legacy Gold Tier subscription
  LegacyGold
  @deprecated(reason: "Legacy Gold subscriptions are not available for new users.")

  # Legacy Platinum Tier subscription
  LegacyPlatinum
  @deprecated(reason: "Legacy Platinum subscriptions are not available for new users.")

  # Alchemical Society Tier subscription
  AlchemicalSociety
}
```

## Notes

⚠️ **Important**: The enum value names above are inferred based on common naming conventions. 
The actual enum values should be verified against the GraphQL schema or by inspecting the 
actual API responses.

**Deprecation Notice**: Legacy subscription tiers (LegacySilver, LegacyGold, LegacyPlatinum) are deprecated and not available for new users.

## Enum Values

- `Silver` - Silver Tier subscription
- `Gold` - Gold Tier subscription
- `Platinum` - Platinum Tier subscription
- `LegacySilver` - Legacy Silver Tier subscription *(deprecated - not available for new users)*
- `LegacyGold` - Legacy Gold Tier subscription *(deprecated - not available for new users)*
- `LegacyPlatinum` - Legacy Platinum Tier subscription *(deprecated - not available for new users)*
- `AlchemicalSociety` - Alchemical Society Tier subscription
