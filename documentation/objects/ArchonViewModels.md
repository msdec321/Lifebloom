# ArchonViewModels

**Type:** OBJECT

## Description

View models for Archon-related operations.

## GraphQL Schema Definition

```graphql
type ArchonViewModels {
  # Desktop client authentication token
  desktopClientToken(desktopClientToken: String!): JSON
  
  # View models by keys
  viewModelsByKeys(keys: [String]): JSON
  
  # Trending classes view model
  trendingClassesViewModel(gameSlug: String): JSON
  
  # Various archon view models
  archonViewModels: JSON
  adFreeViewModel: JSON
  subscriberViewModel: JSON
  gameArchonViewModel: JSON
  upgradeViewModel: JSON
  recentReportsViewModel: JSON
  liveLogsViewModel: JSON
  recentCharacterLogsViewModel: JSON
  helpersViewModel: JSON
  feedbackViewModel: JSON
  tournamentsViewModel: JSON
  standingsViewModel: JSON
  livePreviewViewModel: JSON
  
  # Rankings view model with multiple filter options
  rankingsViewModel(
    gameSlug: String
    rankingsSlug: String
    zoneTypeSlug: String
    difficultySlug: String
    encounterSlug: String
    affixesSlug: String
  ): JSON
  
  # Character rankings view model with multiple filter options
  characterRankingsViewModel(
    gameSlug: String
    classSlug: String
    specSlug: String
    zoneTypeSlug: String
    categorySlug: String
    difficultySlug: String
    encounterSlug: String
    affixesSlug: String
  ): JSON
  
  # Trending reports view model
  trendingReportsViewModel(gameSlug: String): JSON
  
  # Leaderboard view model
  leaderboardViewModel(id: Int): JSON
  
  # Article categories view model
  articleCategoriesViewModel(articleCategorySlug: String): JSON
  
  # Navigation view model
  navigationViewModel: JSON
  
  # Articles view model with optional filters
  articlesViewModel(
    articleCategorySlug: String
    siteName: String
  ): JSON
  
  # Single article view model
  articleViewModel(
    articleSlug: String
    articleCategorySlug: String
    siteName: String
  ): JSON
  
  # Article breadcrumbs view model
  articleBreadcrumbsViewModel(currentSlug: String): JSON
  
  # Articles by page view model
  articlesByPageViewModel(
    articleCategorySlug: String
    pageNumber: Int
    siteName: String
  ): JSON
  
  # Snippets view model
  snippetsViewModel(snippetSlugs: [String]): JSON
  
  # Armory view model
  armoryViewModel: JSON
  
  # Armory character view model
  armoryCharacterViewModel: JSON
  
  # Report view models
  reportViewModel: JSON
  
  # Report navigation view model with detailed parameters
  reportNavigationViewModel(
    userId: Int
    gameSlug: String!
    reportSlug: String!
  ): JSON
  
  # Report section view model with detailed parameters
  reportSectionViewModel(
    userId: Int
    gameSlug: String!
    reportSlug: String!
    fightSlug: String!
    categorySlug: String!
    phaseSlug: String
    playerSlug: String
    cutoffSlug: Int
    throughputSlug: String
    deathSlug: Int
  ): JSON
  
  # Report sections view model with section component names
  reportSectionsViewModel(
    sectionComponentNames: [String!]!
    userId: Int
    gameSlug: String!
    reportSlug: String!
    fightSlug: String!
    categorySlug: String!
    phaseSlug: String
    playerSlug: String
    cutoffSlug: Int
    throughputSlug: String
    deathSlug: Int
  ): JSON
  
  # Character navigation view model
  characterNavigationViewModel(
    userId: Int
    gameSlug: String!
  ): JSON
  
  # Character section view model
  characterSectionViewModel(
    userId: Int
    gameSlug: String!
    characterSlug: String!
    categorySlug: String!
    zoneSlug: String
  ): JSON
  
  # Character sections view model with section component names
  characterSectionsViewModel(
    sectionComponentNames: [String!]!
    userId: Int
    gameSlug: String!
    characterSlug: String!
    categorySlug: String!
    zoneSlug: String
  ): JSON
}
```

## Notes

⚠️ **Important**: Many fields in this object return JSON and have minimal documentation. The actual structure and usage should be verified against the API responses or additional documentation.
