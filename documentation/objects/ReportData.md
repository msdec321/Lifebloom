# ReportData

**Type:** OBJECT

## Description

The ReportData object enables the retrieval of single reports or filtered collections of reports.

## GraphQL Schema Definition

```graphql
type ReportData {
  # Obtain a specific report by its code.
  report(
    # Required. The code of a single report to retrieve.
    code: String,
    
    # Optional. Whether to allow viewing of unlisted logs. If you have a multi-user 
    # application where you cache codes, set this to true to avoid accidentally 
    # giving away unlisted codes to unauthorized users.
    allowUnlisted: Boolean
  ): Report
  
  # A set of reports for a specific guild, guild tag, or user.
  reports(
    # Optional. A UNIX timestamp with millisecond precision representing the end 
    # time for a report range. If omitted, defaults to the current time in milliseconds.
    endTime: Float,
    
    # Optional. The ID of a specific guild. Reports from that guild will be fetched.
    guildID: Int,
    
    # Optional. The name of a specific guild. Must be used in conjunction with 
    # guildServerSlug and guildServerRegion to uniquely identify a guild.
    guildName: String,
    
    # Optional. The name of a specific guild. Must be used in conjunction with 
    # guildName and guildServerRegion to uniquely identify a guild.
    guildServerSlug: String,
    
    # Optional. The region for a specific guild. Must be used in conjunction with 
    # guildName and guildServerRegion to uniquely identify a guild.
    guildServerRegion: String,
    
    # Optional. The ID of a specific guild tag. Reports from that guild tag will be 
    # fetched. This will take precedence over all other guild arguments.
    guildTagID: Int,
    
    # Optional. The ID of a specific user. Reports from that user's personal logs 
    # will be fetched.
    userID: Int,
    
    # Optional. The number of characters to retrieve per page. If omitted, defaults 
    # to 100. The maximum allowed value is 100, and minimum allowed value is 1.
    limit: Int,
    
    # Optional. The page of paginated data to retrieve. If omitted, defaults to the 
    # first page.
    page: Int,
    
    # Optional. A UNIX timestamp with millisecond precision representing a start 
    # time for a report range. If omitted, defaults to 0.
    startTime: Float,
    
    # Optional. The ID of a specific zone to filter to. Reports with that zone as 
    # their default will be included.
    zoneID: Int,
    
    # Optional. The ID of a specific game zone to filter reports to.
    gameZoneID: Int
  ): ReportPagination
}
```

## Fields

- `report` - Obtain a specific report by its code.
  - Arguments:
    - `code` (String, required) - The code of a single report to retrieve.
    - `allowUnlisted` (Boolean, optional) - Whether to allow viewing of unlisted logs. If you have a multi-user application where you cache codes, set this to true to avoid accidentally giving away unlisted codes to unauthorized users.
- `reports` - A set of reports for a specific guild, guild tag, or user.
  - Arguments:
    - `endTime` (Float, optional) - A UNIX timestamp with millisecond precision representing the end time for a report range. If omitted, defaults to the current time in milliseconds.
    - `guildID` (Int, optional) - The ID of a specific guild. Reports from that guild will be fetched.
    - `guildName` (String, optional) - The name of a specific guild. Must be used in conjunction with guildServerSlug and guildServerRegion to uniquely identify a guild.
    - `guildServerSlug` (String, optional) - The name of a specific guild. Must be used in conjunction with guildName and guildServerRegion to uniquely identify a guild.
    - `guildServerRegion` (String, optional) - The region for a specific guild. Must be used in conjunction with guildName and guildServerRegion to uniquely identify a guild.
    - `guildTagID` (Int, optional) - The ID of a specific guild tag. Reports from that guild tag will be fetched. This will take precedence over all other guild arguments.
    - `userID` (Int, optional) - The ID of a specific user. Reports from that user's personal logs will be fetched.
    - `limit` (Int, optional) - The number of characters to retrieve per page. If omitted, defaults to 100. The maximum allowed value is 100, and minimum allowed value is 1.
    - `page` (Int, optional) - The page of paginated data to retrieve. If omitted, defaults to the first page.
    - `startTime` (Float, optional) - A UNIX timestamp with millisecond precision representing a start time for a report range. If omitted, defaults to 0.
    - `zoneID` (Int, optional) - The ID of a specific zone to filter to. Reports with that zone as their default will be included.
    - `gameZoneID` (Int, optional) - The ID of a specific game zone to filter reports to.

## Notes

⚠️ **Important**: When using guild arguments, you can either use `guildID` alone, or use `guildName`, `guildServerSlug`, and `guildServerRegion` together to uniquely identify a guild. The `guildTagID` takes precedence over all other guild arguments.
