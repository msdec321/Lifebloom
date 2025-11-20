# Lifebloom - A WarcraftLogs Restoration Druid Analyzer

Welcome to **Lifebloom** a retrospective analysis tool for TBC Restoration Druids.
This tool fetches report data from WarcraftLogs via their GraphQL API. It combines report-level data such as HPS, Fight Duration, Number of healers, etc. with rotation pattern analysis in a single unified output.

## Quick Start

### Prerequisites

- Python 3.12+
- WarcraftLogs API credentials ([Get them here](https://www.warcraftlogs.com/api/clients))
- WarcraftLogs Gold tier subscription (for archived report access)

### Setup

1. **Clone the repository**
   ```bash
   cd warcraftlogs
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API credentials**

   Create a `.env` file with your WarcraftLogs API credentials:
   ```
   WARCRAFTLOGS_CLIENT_ID=your_client_id_here
   WARCRAFTLOGS_CLIENT_SECRET=your_client_secret_here
   ```

5. **Authenticate**

   Run the authentication script (one-time setup):
   ```bash
   python auth.py
   ```

   This will open your browser to authorize the application and save your access token.

### Usage

Analyze a specific Restoration Druid's performance and rotation patterns:

```bash
python analyze_druid.py <report_id> <boss_name> <player_name>
```

**Examples:**
```bash
python analyze_druid.py wX7H9RtYJ48P1cdW Brutallus Mercychann
python analyze_druid.py qH6MjfcZdPmn27CF "Kil'jaeden" Healzplz
python analyze_druid.py m329HYcBhMdfJgXz "M'uru" Treeheals
```

This script provides a complete analysis combining:
- **Performance Metrics:** Stats, trinkets, buffs, HPS breakdown, and rankings
- **Cast Timeline:** Chronological view of all casts with active tank tracking
- **Rotation Analysis:** Pattern identification with `[XLB YI ZRG]` notation
- **Pattern Frequency:** Statistical breakdown of rotation patterns
- **Top Patterns:** The most and second-most commonly used rotations

## Extracted Data

The script provides comprehensive Restoration Druid analysis for any boss encounter:

### Encounter Information
- **Date & Time:** Full timestamp of the encounter
- **Duration:** Fight length in minutes and seconds

### Healing Composition
- **Total Healers:** Count of all healers in the raid
- **Breakdown by Spec:**
  - Holy Paladins
  - Holy Priests
  - Discipline Priests
  - Restoration Druids
  - Restoration Shamans

### Restoration Druid Performance

For the specified Restoration Druid, the script extracts:

- **Name-Server (Region):** Full player identification
- **Item Level:** Average item level (or "Unknown" if unavailable)
- **Stats:**
  - Intellect
  - Spirit
  - Haste
  - (Shows "Unknown" if stats are unavailable)
- **Trinkets:** List of equipped trinkets with item IDs
- **Vampiric Touch:** Yes/No - Whether the druid received mana from a Shadow Priest's Vampiric Touch
- **Innervate Count:** Number of times the druid received Innervate during the encounter
- **Received Bloodlust:** Yes/No - Whether the druid received Heroism or Bloodlust during the encounter
- **Nature's Grace:** Yes/No - Whether the druid had the Nature's Grace buff during the encounter
- **Lifebloom Uptime:** Percentage of fight time that Lifebloom was active on at least one target
- **Lifebloom HPS:** Healing per second from Lifebloom and percentage of total HPS
- **Rejuvenation HPS:** Healing per second from Rejuvenation and percentage of total HPS
- **Regrowth HPS:** Healing per second from Regrowth (all ranks combined) and percentage of total HPS, with rank breakdown if multiple ranks used
- **Performance Metrics:**
  - HPS (Healing Per Second)
  - Rank (absolute rank compared to all parses)
  - Total Parses (number of logs for comparison)
  - Percentile (performance percentile)

### Rotation Analysis

The script provides detailed rotation pattern analysis:

- **Cast-by-Cast Timeline:** Chronological list of all casts with:
  - Timestamp (relative to fight start)
  - Spell name and target
  - Active tank at that moment
  - Cast type and action classification
  - Rotation notation markers

- **Identified Rotations:** Table showing each meaningful rotation with:
  - Sequential rotation number
  - Time range (start to end)
  - Rotation notation `[XLB YI ZRG]`

- **Top Rotation Patterns:** Summary of the most common patterns:
  - 1st most common rotation pattern with usage count and percentage
  - 2nd most common rotation pattern with usage count and percentage

## Sample Output

```
======================================================================
ENCOUNTER INFORMATION
======================================================================
Date: 2022-08-05 19:40:20
Duration: 4m 51s

======================================================================
HEALING COMPOSITION
======================================================================

Total Healers: 6

Holy Paladin: 1
  • Samehada
Holy Priest: 2
  • Aêsthetic
  • Zhanghanxiao
Discipline Priest: 0
Restoration Druid: 1
  • Mercychann
Restoration Shaman: 2
  • Tibberz
  • Dankwindfury

======================================================================
RESTORATION DRUID PERFORMANCE
======================================================================
  • Mercychann-Benediction (US)
    Item Level: 150
    Stats: 651 Intellect | 640 Spirit | 204 Haste
    Trinkets:
      • Memento of Tyrande (ID: 32496)
      • Redeemer's Alchemist Stone (ID: 35750)
    Vampiric Touch: No
    Innervate Count: 1
    Received Bloodlust: No
    Nature's Grace: No
    Lifebloom Uptime: 99.4%
    Lifebloom HPS: 1734.25 (78.98% of total)
    Rejuvenation HPS: 177.14 (8.07% of total)
    Regrowth HPS: 53.09 (2.42% of total)
      • Rank 7: 22.17
      • Rank 10: 30.92
    HPS: 2195.88
    Rank: 82 out of 58617 parses (99th percentile)
======================================================================

(Cast-by-cast timeline omitted for brevity)

======================================================================================
IDENTIFIED ROTATIONS ONLY
======================================================================================
Rotation                       Time Range                Notation
--------------------------------------------------------------------------------------
Rotation #1                    7.42s - 13.84s            [1LB 1I 2RG]
Rotation #2                    13.84s - 18.70s           [1LB 1I 2RG]
Rotation #3                    18.70s - 23.58s           [1LB 0I 2RG]
Rotation #4                    23.58s - 28.93s           [1LB 3I 0RG]
...
======================================================================================

======================================================================================
TOP ROTATION PATTERNS
======================================================================================
1st Most Common: [1LB 4I 0RG] - Used 24 times (53.3%)
2nd Most Common: [1LB 3I 0RG] - Used 5 times (11.1%)
======================================================================================
```

## Project Structure

```
warcraftlogs/
├── auth.py                 # OAuth authentication handler
├── analyze_druid.py        # Main script: Combined performance & rotation analysis
├── pull_data.py            # [DEPRECATED] Performance data extraction only
├── query_druid_casts.py    # [DEPRECATED] Rotation analysis only
├── query_report.py         # Basic report query example
├── query_players.py        # Player participation query example
├── requirements.txt        # Python dependencies
├── .env                    # API credentials (not in git)
├── .token.json            # OAuth token cache (not in git)
└── documentation/          # WarcraftLogs API documentation
```

## Technical Details

### Authentication

The project uses OAuth 2.0 Authorization Code flow to authenticate as a user with subscription access. This enables:
- Access to archived reports (2+ years old)
- Full access to player stats and combat data
- Resource event querying for buff/mana tracking

### Vampiric Touch Detection

Vampiric Touch is detected by querying resource events (mana gains) rather than buffs, since WarcraftLogs classifies it as a resource restoration ability. The script:
1. Queries all resource events for the Restoration Druid
2. Filters for ability ID 34919 (Vampiric Touch)
3. Verifies the target matches the druid's player ID

### Innervate Detection

Innervate is tracked by querying buff events to count how many times the druid received this mana regeneration buff. The script:
1. Queries all buff events for the Restoration Druid
2. Filters for ability ID 29166 (Innervate)
3. Counts "applybuff" events to determine how many times Innervate was cast on the druid
4. Reports both whether they received it and the total count

### Heroism/Bloodlust Detection

Heroism and Bloodlust provide the same haste buff but have different ability IDs (Heroism for Alliance, Bloodlust for Horde). The script:
1. Queries all buff events for the fight (not filtered by player to capture raid-wide buffs)
2. Checks for either ability ID 32182 (Heroism) or 2825 (Bloodlust)
3. Reports a single "Received Bloodlust" status (Yes/No) if either buff was applied to the druid

### Nature's Grace Detection

Nature's Grace is a druid damage buff that procs from critical strikes. The script:
1. Queries all buff events for the fight
2. Filters for ability ID 16886 (Nature's Grace)
3. Reports whether the druid had this buff active during the encounter (Yes/No)

### Trinket Detection

Trinket information is extracted from the combatantInfo gear data:
1. Accesses the gear array from combatantInfo
2. Filters for items in slots 12 and 13 (trinket slots)
3. Extracts item ID and name for each trinket
4. Displays both trinkets with their item IDs

### Lifebloom Uptime Calculation

Lifebloom uptime represents the percentage of fight time that the druid had at least one Lifebloom active. The script:
1. Queries buff events for ability ID 33763 (Lifebloom) where sourceID matches the druid
2. Tracks applybuff, refreshbuff, and removebuff events to build time intervals for each instance
3. Merges overlapping intervals (when Lifebloom is on multiple targets simultaneously)
4. Calculates total uptime from merged intervals
5. Divides by fight duration to get the percentage

This correctly handles multiple simultaneous Lifeblooms - if Lifebloom is on 3 targets at once, it counts as one period of uptime, not three.

### HoT Healing Analysis (Lifebloom, Rejuvenation & Regrowth)

Spell-specific healing metrics provide insight into how much of the druid's healing comes from their key HoTs. The script:
1. Queries table data with dataType: Healing filtered by sourceID (the druid)
2. Extracts total healing amounts for:
   - Lifebloom (ability ID 33763)
   - Rejuvenation (ability ID 26982)
   - Regrowth - all ranks (Rank 10: 26980, Rank 9: 9858, Rank 8: 9857, Rank 7: 9856, Rank 6: 9750, Rank 5: 8941)
3. Calculates HPS for each spell by dividing total healing by fight duration
4. Calculates percentage of total HPS by comparing to the druid's overall HPS from rankings

For Regrowth, the script:
- Combines healing from all ranks to show total Regrowth HPS
- If multiple ranks were used, displays a breakdown showing HPS from each rank
- Only displays ranks that were actually used during the encounter

This shows both raw HPS from each spell and what percentage of their total healing output it represents, helping analyze healing breakdown and playstyle.

### Handling Missing Data

The script gracefully handles:
- Missing player stats (shows "Unknown")
- Missing trinket data (shows "Unknown")
- Archived reports (requires Gold subscription)
- Multiple Restoration Druids in one raid
- Encounters without Vampiric Touch

## Rotation Analysis Details

The analyzer provides deep insight into a Restoration Druid's spell usage patterns, rotation structure, and decision-making throughout an encounter.

### Core Concepts

#### Tank Tracking
The script identifies which tank is actively tanking the boss at each moment by:
1. Querying all damage taken events during the fight
2. Filtering for boss melee swings hitting tank players
3. Building a chronological timeline of active tanks
4. Correlating each cast with who was tanking at that timestamp

#### Rotation Definition
A **Rotation** is a sequence of casts that begins when the Druid casts Lifebloom on the Active Tank. A rotation ends when:
- 7.00 seconds pass without Lifebloom being cast on an Active Tank, OR
- A new rotation begins (Lifebloom cast on Active Tank)

Between rotations, the script groups casts into 5-cast sections for analysis.

#### Action Labels
Each cast is categorized with an action:
- **Rotation started** - Lifebloom cast on the Active Tank (begins a rotation)
- **Instant cast** - Lifebloom on non-Active Tank, Rejuvenation, Swiftmend, Nature's Swiftness, Innervate, or Tree of Life
- **Regrowth** - Regrowth begincast events (cast-time heals)

#### Rotation Notation
Each rotation section is summarized using the format **[XLB YI ZRG]** where:
- **X** = Number of Lifeblooms on Active Tank (rotation starts)
- **Y** = Number of Instant casts
- **Z** = Number of Regrowth casts

For example:
- `[1LB 4I 0RG]` = One rotation start + 4 instant casts + no Regrowths
- `[1LB 1I 2RG]` = One rotation start + 1 instant + 2 Regrowths
- `[0LB 5I 0RG]` = No rotation start + 5 instant casts (between rotations)

### Data Filtering

The script intelligently filters casts to focus on meaningful actions:
- **Regrowth:** Only shows begincast events (not completion) to avoid duplicates
- **Healing Touch:** Completely filtered out
- **Restore Mana:** Completely filtered out (mana potion usage)

### Use Cases

This analysis helps answer questions like:
- What is the player's most common rotation pattern?
- How often do they use instant-only rotations vs. weaving in Regrowths?
- Are they pre-hotting tanks before tank swaps?
- How does their rotation adapt during different fight phases?
- What percentage of GCDs are instant casts vs. hardcasts?

---

# WarcraftLogs API Documentation

This repository also contains comprehensive documentation for the WarcraftLogs GraphQL API, covering all available types, queries, and data structures.

## API Overview

The WarcraftLogs API is a GraphQL-based interface for accessing combat log data, character rankings, guild information, and game metadata from World of Warcraft, Final Fantasy XIV, and other supported games.

## Documentation Structure

The documentation is organized into four main categories:

### 📋 Schema (`/documentation/schema/`)
Contains the root `Query` type definition, which serves as the primary entry point for all API requests. The Query type provides access to eight main data domains.

### 📦 Objects (`/documentation/objects/`)
Detailed documentation for complex GraphQL object types, including:
- **Report** - Combat log reports with fights, events, rankings, and analysis data
- **Character** - Player character information, rankings, and recent activity
- **Guild** - Guild data, member rosters, attendance, and rankings
- **GameData** - Static game data (abilities, items, NPCs, achievements, classes, etc.)
- **WorldData** - Game world structure (expansions, zones, encounters, regions, servers)
- **UserData** - Authenticated user information and settings
- **RateLimitData** - API usage and rate limiting information
- **ProgressRaceData** - World first and realm first race tracking

### 🏷️ Enums (`/documentation/enums/`)
Enumeration types that define valid values for various parameters:
- **RoleType** - Tank, Healer, DPS, or Any
- **CharacterRankingMetricType** - DPS, HPS, score, speed, and game-specific metrics
- **KillType** - Kill tracking filters
- **RankingTimeframeType** - Historical vs current rankings
- **EventDataType**, **GraphDataType**, **TableDataType** - Data visualization types
- And many more...

### 📊 Scalars (`/documentation/scalars/`)
Basic scalar types used throughout the API:
- **String** - Text data
- **Int** - Integer values
- **Boolean** - True/false values
- **JSON** - Complex JSON data structures

## Main API Entry Points

The root `Query` type provides access to these main data domains:

### characterData
Retrieve individual characters or filtered collections of characters, including:
- Character rankings and statistics
- Recent combat log appearances
- Guild membership information
- Cached game data (gear, specs, etc.)

### reportData
Access combat log reports uploaded by players:
- Fight breakdowns and timelines
- Event data with advanced filtering
- Rankings and performance metrics
- Player details (gear, talents, specs)
- Graph and table visualizations

### guildData
Query guild information and rosters:
- Guild member lists
- Attendance tracking
- Guild rankings by zone
- Guild tags (raid teams)

### gameData
Static game data that changes only with major patches:
- Abilities and spells
- Items and item sets
- NPCs and encounters
- Classes and specializations
- Achievements
- Game zones and maps

**Note:** Game data should be cached aggressively as it only updates with major game patches.

### worldData
Game world organizational structure:
- Expansions and their zones
- Dungeon and raid encounters
- Regions and subregions
- Servers (realms)

### userData
Retrieve the authenticated user's information (requires authentication with appropriate scopes).

### rateLimitData
Check API usage against rate limits to avoid throttling.

### progressRaceData
Track ongoing world first or realm first progression races. Updates every 30 seconds during active races.

## Key Features

### Advanced Filtering
Most data endpoints support extensive filtering options:
- Time ranges (startTime, endTime)
- Difficulty levels
- Encounter/boss filtering
- Class and spec filtering
- Ability-based filtering
- Custom filter expressions

### Pagination
Collection endpoints support pagination with standardized parameters:
- `limit` - Items per page (typically 1-100, default varies)
- `page` - Page number (default: 1)

### Rankings and Metrics
Comprehensive ranking data with multiple metric types:
- DPS, HPS, tanking metrics
- Game-specific metrics (FFXIV: nDPS, rDPS, cDPS)
- Score-based rankings (Mythic+ dungeons)
- Speed rankings
- Historical vs current comparisons

### Data Visualization
Multiple data representation formats:
- **Events** - Paginated combat log events
- **Graphs** - Time-series data visualization
- **Tables** - Aggregated statistical data
- **JSON** - Flexible structured data

### Archive Access
Reports can be archived after a certain period. Accessing archived report data requires a subscription with archive access.

## Important Notes

### Data Stability
⚠️ Some fields return data that is **not considered frozen** and may change without notice:
- Report events, graphs, tables, and rankings
- Character rankings
- Most analysis and statistical data

Always use these fields with caution in production systems.

### Caching Recommendations
- **GameData**: Cache for extended periods (only changes with game patches)
- **WorldData**: Cache for days/weeks (changes infrequently)
- **Reports**: Cache based on archive status
- **Rankings**: Cache briefly (can change frequently)

### Rate Limiting
Monitor `rateLimitData` to track API usage and avoid hitting rate limits. The API uses a points-based system for rate limiting.

### Authentication
Some endpoints and fields require authentication:
- User profile data
- Private logs access
- Character claiming status
- Guild member-specific data

Use appropriate OAuth scopes when authenticating.

## Use Cases

### Player Performance Analysis
Query reports to analyze player performance, compare rankings, and review combat logs for improvement opportunities.

### Guild Management
Track attendance, monitor member progression, manage raid teams, and analyze guild performance across tiers.

### Theorycrafting
Access game data to build simulators, calculate optimal rotations, or analyze ability interactions.

### Progression Tracking
Monitor world first races, track guild progression through raid tiers, and compare against other guilds.

### Statistical Analysis
Build dashboards, generate reports, and perform meta-analysis on class/spec performance across the playerbase.

## Getting Started

1. Browse the `/documentation/schema/Query.md` file to understand available entry points
2. Explore object types in `/documentation/objects/` for detailed field information
3. Reference enum types in `/documentation/enums/` for valid parameter values
4. Build GraphQL queries using the schema definitions provided

## Additional Resources

For more information about the WarcraftLogs API:
- Official API Documentation: https://www.warcraftlogs.com/api/docs
- GraphQL Playground: https://www.warcraftlogs.com/api/v2/explorer
- OAuth Setup: https://www.warcraftlogs.com/api/clients
