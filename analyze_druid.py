#!/usr/bin/env python3
"""
Comprehensive Restoration Druid Performance Analysis

Combines performance metrics with rotation analysis for a specific Restoration Druid.

Usage:
    python analyze_druid.py <report_id> <boss_name> <player_name>

Example:
    python analyze_druid.py wX7H9RtYJ48P1cdW Brutallus Mercychann
"""

import sys
import requests
from datetime import datetime
from collections import Counter
from auth import get_user_access_token

# API Configuration
API_URL = "https://www.warcraftlogs.com/api/v2/user"

# Ability IDs
LIFEBLOOM_ID = 33763
REJUVENATION_ID = 26982
TREE_OF_LIFE_ID = 33891
SWIFTMEND_ID = 18562
NATURES_SWIFTNESS_ID = 17116
INNERVATE_ID = 29166
VAMPIRIC_TOUCH_ID = 34919
HEROISM_ID = 32182
BLOODLUST_ID = 2825
NATURES_GRACE_ID = 16886

# Regrowth has multiple ranks
REGROWTH_IDS = {
    26980: "Rank 10",
    9858: "Rank 9",
    9857: "Rank 8",
    9856: "Rank 7",
    9750: "Rank 6",
    8941: "Rank 5"
}

# Rotation tracking constants
ROTATION_TIMEOUT = 7.0  # seconds
CASTS_BETWEEN_SEPARATORS = 5


def analyze_druid_performance(report_code, boss_name, player_name):
    """
    Comprehensive analysis combining performance metrics and rotation data.

    Args:
        report_code: The report code/ID
        boss_name: The name of the boss
        player_name: The name of the Restoration Druid to analyze

    Returns:
        Dictionary containing all performance and rotation data
    """
    access_token = get_user_access_token()
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    print(f"Searching for {boss_name} in report {report_code}...")

    # ===== STEP 1: Get fight and player information =====
    fights_query = """
    query ($code: String!) {
      reportData {
        report(code: $code) {
          title
          startTime
          fights {
            id
            encounterID
            name
            kill
            startTime
            endTime
          }
          masterData {
            actors {
              id
              name
              type
              subType
              gameID
            }
          }
        }
      }
    }
    """

    response = requests.post(
        API_URL,
        json={"query": fights_query, "variables": {"code": report_code}},
        headers=headers
    )

    if response.status_code != 200:
        raise Exception(f"Query failed: {response.status_code} - {response.text}")

    result = response.json()
    if "errors" in result:
        raise Exception(f"GraphQL errors: {result['errors']}")

    report = result.get("data", {}).get("reportData", {}).get("report")
    if not report:
        raise Exception(f"Report {report_code} not found!")

    fights = report.get("fights", [])
    master_data = report.get("masterData", {})
    report_start_time = report.get("startTime")

    # Build actor mapping
    actor_names = {}
    player_ids = set()
    all_actors = master_data.get("actors", [])

    for actor in all_actors:
        actor_id = actor.get("id")
        actor_name = actor.get("name", "Unknown")
        actor_type = actor.get("type", "")
        actor_names[actor_id] = actor_name

        if actor_type == "Player":
            player_ids.add(actor_id)

    # Find the specified player
    player_id = None
    for actor in all_actors:
        if actor.get("name") == player_name:
            player_id = actor.get("id")
            print(f"✓ Found player {player_name} (ID: {player_id})")
            break

    if not player_id:
        raise Exception(f"Player '{player_name}' not found in report!")

    # Find boss fight
    boss_fights = [
        f for f in fights
        if f.get("encounterID", 0) > 0 and f.get("name") == boss_name
    ]

    if not boss_fights:
        raise Exception(f"Boss '{boss_name}' not found in report!")

    boss_kills = [f for f in boss_fights if f.get("kill")]
    target_fight = boss_kills[0] if boss_kills else boss_fights[0]

    fight_id = target_fight["id"]
    is_kill = target_fight.get("kill", False)
    fight_start_time = target_fight.get("startTime")
    fight_end_time = target_fight.get("endTime")

    fight_duration_ms = fight_end_time - fight_start_time
    fight_duration_seconds = fight_duration_ms / 1000
    duration_minutes = int(fight_duration_seconds // 60)
    duration_seconds = int(fight_duration_seconds % 60)

    fight_absolute_timestamp = report_start_time + fight_start_time

    print(f"✓ Found {boss_name} (Fight ID: {fight_id}, {'KILL' if is_kill else 'WIPE'})")

    # ===== STEP 2: Get healing composition and player details =====
    print("Querying healing composition and player details...")

    composition_query = f"""
    query {{
      reportData {{
        report(code: "{report_code}") {{
          table(fightIDs: {[fight_id]}, dataType: Summary)
          rankings(fightIDs: {[fight_id]}, playerMetric: hps)
          playerDetails(fightIDs: {[fight_id]}, includeCombatantInfo: true)
        }}
      }}
    }}
    """

    response = requests.post(API_URL, json={"query": composition_query}, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Query failed: {response.status_code} - {response.text}")

    result = response.json()
    if "errors" in result:
        raise Exception(f"GraphQL errors: {result['errors']}")

    report_data = result.get("data", {}).get("reportData", {}).get("report")
    table_data = report_data.get("table", {})
    rankings_data = report_data.get("rankings", {})
    player_details_data = report_data.get("playerDetails", {})

    if not table_data or "data" not in table_data:
        raise Exception("Table data not available (might require subscription for archived reports)")

    composition = table_data.get("data", {}).get("composition", [])

    # Extract healing composition
    healer_composition = {
        "Holy Paladin": [],
        "Holy Priest": [],
        "Discipline Priest": [],
        "Restoration Druid": [],
        "Restoration Shaman": []
    }

    for player_data in composition:
        player_type = player_data.get("type")
        player_comp_name = player_data.get("name")
        player_specs = player_data.get("specs", [])

        for spec_data in player_specs:
            spec_name = spec_data.get("spec")

            if player_type == "Paladin" and spec_name == "Holy":
                healer_composition["Holy Paladin"].append(player_comp_name)
            elif player_type == "Priest" and spec_name == "Holy":
                healer_composition["Holy Priest"].append(player_comp_name)
            elif player_type == "Priest" and spec_name == "Discipline":
                healer_composition["Discipline Priest"].append(player_comp_name)
            elif player_type == "Druid" and spec_name == "Restoration":
                healer_composition["Restoration Druid"].append(player_comp_name)
            elif player_type == "Shaman" and spec_name == "Restoration":
                healer_composition["Restoration Shaman"].append(player_comp_name)

    total_healers = sum(len(healers) for healers in healer_composition.values())

    # Extract player stats and trinkets for the specified druid
    player_stats = {}
    player_trinkets = {}

    if player_details_data and "data" in player_details_data:
        player_details = player_details_data.get("data", {}).get("playerDetails", {})
        healers = player_details.get("healers", [])

        for healer in healers:
            healer_name = healer.get("name")
            if healer_name == player_name:
                combatant_info = healer.get("combatantInfo", {})

                if combatant_info and isinstance(combatant_info, dict):
                    stats = combatant_info.get("stats", {})

                    intellect = stats.get("Intellect", {}).get("max", 0) if stats.get("Intellect") else 0
                    spirit = stats.get("Spirit", {}).get("max", 0) if stats.get("Spirit") else 0
                    haste = stats.get("Haste", {}).get("max", 0) if stats.get("Haste") else 0
                    item_level = stats.get("Item Level", {}).get("max", 0) if stats.get("Item Level") else 0

                    player_stats = {
                        "intellect": intellect,
                        "spirit": spirit,
                        "haste": haste,
                        "item_level": item_level,
                        "has_stats": bool(intellect or spirit or haste or item_level)
                    }

                    # Extract trinkets
                    gear = combatant_info.get("gear", [])
                    trinkets = []

                    for item in gear:
                        slot = item.get("slot")
                        if slot in [12, 13]:
                            trinket_info = {
                                "id": item.get("id"),
                                "name": item.get("name", "Unknown Trinket"),
                                "quality": item.get("quality", 0),
                                "icon": item.get("icon", "")
                            }
                            trinkets.append(trinket_info)

                    player_trinkets = {
                        "trinkets": trinkets,
                        "has_trinkets": len(trinkets) > 0
                    }
                break

    # ===== STEP 3: Get buff and resource events =====
    print("Querying buffs and resource events...")

    buff_query = f"""
    query {{
      reportData {{
        report(code: "{report_code}") {{
          events(fightIDs: {[fight_id]}, dataType: Buffs, limit: 10000) {{
            data
          }}
        }}
      }}
    }}
    """

    response = requests.post(API_URL, json={"query": buff_query}, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Query failed: {response.status_code} - {response.text}")

    result = response.json()
    all_buff_events = result.get("data", {}).get("reportData", {}).get("report", {}).get("events", {}).get("data", [])

    # Check for Innervate
    innervate_events = [
        event for event in all_buff_events
        if event.get("abilityGameID") == INNERVATE_ID and
           event.get("type") == "applybuff" and
           event.get("targetID") == player_id
    ]
    innervate_count = len(innervate_events)

    # Check for Bloodlust/Heroism
    has_bloodlust = any(
        event.get("abilityGameID") in [HEROISM_ID, BLOODLUST_ID] and
        event.get("type") == "applybuff" and
        event.get("targetID") == player_id
        for event in all_buff_events
    )

    # Check for Nature's Grace
    has_natures_grace = any(
        event.get("abilityGameID") == NATURES_GRACE_ID and
        event.get("type") == "applybuff" and
        event.get("targetID") == player_id
        for event in all_buff_events
    )

    # Query Vampiric Touch (resource events)
    vt_query = f"""
    query {{
      reportData {{
        report(code: "{report_code}") {{
          events(fightIDs: {[fight_id]}, dataType: Resources, targetID: {player_id}, limit: 500) {{
            data
          }}
        }}
      }}
    }}
    """

    response = requests.post(API_URL, json={"query": vt_query}, headers=headers)

    has_vampiric_touch = False
    if response.status_code == 200:
        result = response.json()
        all_events = result.get("data", {}).get("reportData", {}).get("report", {}).get("events", {}).get("data", [])
        has_vampiric_touch = any(
            event.get("abilityGameID") == VAMPIRIC_TOUCH_ID and
            event.get("targetID") == player_id
            for event in all_events
        )

    # ===== STEP 4: Calculate Lifebloom uptime =====
    print("Calculating Lifebloom uptime...")

    lifebloom_query = f"""
    query {{
      reportData {{
        report(code: "{report_code}") {{
          events(fightIDs: {[fight_id]}, dataType: Buffs, sourceID: {player_id}, abilityID: {LIFEBLOOM_ID}, limit: 10000) {{
            data
          }}
        }}
      }}
    }}
    """

    response = requests.post(API_URL, json={"query": lifebloom_query}, headers=headers)

    lifebloom_uptime_percent = 0
    if response.status_code == 200:
        result = response.json()
        lifebloom_events = result.get("data", {}).get("reportData", {}).get("report", {}).get("events", {}).get("data", [])

        intervals = []
        active_instances = {}

        for event in sorted(lifebloom_events, key=lambda e: e.get("timestamp", 0)):
            event_type = event.get("type")
            target_id = event.get("targetID")
            timestamp = event.get("timestamp")

            if event_type in ["applybuff", "refreshbuff"]:
                if target_id in active_instances:
                    intervals.append((active_instances[target_id], timestamp))
                active_instances[target_id] = timestamp
            elif event_type == "removebuff":
                if target_id in active_instances:
                    intervals.append((active_instances[target_id], timestamp))
                    del active_instances[target_id]

        for target_id, apply_time in active_instances.items():
            intervals.append((apply_time, fight_end_time))

        if intervals:
            intervals.sort()
            merged_intervals = [intervals[0]]

            for current_start, current_end in intervals[1:]:
                last_start, last_end = merged_intervals[-1]

                if current_start <= last_end:
                    merged_intervals[-1] = (last_start, max(last_end, current_end))
                else:
                    merged_intervals.append((current_start, current_end))

            total_uptime_ms = sum(end - start for start, end in merged_intervals)
            lifebloom_uptime_percent = (total_uptime_ms / fight_duration_ms * 100) if fight_duration_ms > 0 else 0

    # ===== STEP 5: Get healing breakdown =====
    print("Querying healing breakdown...")

    healing_query = f"""
    query {{
      reportData {{
        report(code: "{report_code}") {{
          table(fightIDs: {[fight_id]}, dataType: Healing, sourceID: {player_id})
        }}
      }}
    }}
    """

    response = requests.post(API_URL, json={"query": healing_query}, headers=headers)

    lifebloom_hps = 0
    rejuvenation_hps = 0
    regrowth_total_hps = 0
    regrowth_by_rank = {}

    if response.status_code == 200:
        result = response.json()
        healing_table = result.get("data", {}).get("reportData", {}).get("report", {}).get("table", {})

        if healing_table and "data" in healing_table:
            healing_data = healing_table.get("data", {})
            entries = healing_data.get("entries", [])

            for entry in entries:
                ability_id = entry.get("abilityGameID") or entry.get("guid")
                if ability_id == LIFEBLOOM_ID:
                    lifebloom_healing = entry.get("total", 0)
                    lifebloom_hps = (lifebloom_healing / fight_duration_seconds) if fight_duration_seconds > 0 else 0
                elif ability_id == REJUVENATION_ID:
                    rejuvenation_healing = entry.get("total", 0)
                    rejuvenation_hps = (rejuvenation_healing / fight_duration_seconds) if fight_duration_seconds > 0 else 0
                elif ability_id in REGROWTH_IDS:
                    rank_name = REGROWTH_IDS[ability_id]
                    healing = entry.get("total", 0)
                    rank_hps = (healing / fight_duration_seconds) if fight_duration_seconds > 0 else 0
                    regrowth_by_rank[rank_name] = rank_hps

            total_regrowth_healing = sum(
                entry.get("total", 0) for entry in entries
                if (entry.get("abilityGameID") or entry.get("guid")) in REGROWTH_IDS
            )
            regrowth_total_hps = (total_regrowth_healing / fight_duration_seconds) if fight_duration_seconds > 0 else 0

    # ===== STEP 6: Get rankings =====
    print("Querying rankings...")

    player_ranking = {}
    if rankings_data and "data" in rankings_data:
        for fight_ranking in rankings_data.get("data", []):
            if isinstance(fight_ranking, dict):
                roles = fight_ranking.get("roles", {})
                healers = roles.get("healers", {})

                if healers and "characters" in healers:
                    for character in healers["characters"]:
                        char_name = character.get("name")

                        if char_name == player_name:
                            rank = character.get("rank")
                            rank_percent = character.get("rankPercent")
                            total_parses = character.get("totalParses")
                            hps = character.get("amount", 0)

                            server_info = character.get("server", {})
                            server_name = server_info.get("name", "Unknown")
                            server_region = server_info.get("region", "Unknown")

                            if rank and isinstance(rank, str):
                                rank = rank.replace("~", "").strip()
                                try:
                                    rank = int(rank)
                                except ValueError:
                                    rank = None

                            player_ranking = {
                                "rank": rank,
                                "rankPercent": rank_percent,
                                "totalParses": total_parses,
                                "hps": hps,
                                "server": server_name,
                                "region": server_region
                            }
                            break

    # ===== STEP 7: Identify tanks =====
    print("Identifying tanks...")

    combatant_query = f"""
    query {{
      reportData {{
        report(code: "{report_code}") {{
          playerDetails(fightIDs: {[fight_id]})
        }}
      }}
    }}
    """

    response = requests.post(API_URL, json={"query": combatant_query}, headers=headers)

    tanks = []
    tank_ids = set()

    if response.status_code == 200:
        result = response.json()
        player_details_data = result.get("data", {}).get("reportData", {}).get("report", {}).get("playerDetails", {})
        player_details = player_details_data.get("data", {}).get("playerDetails", {}) if isinstance(player_details_data, dict) else {}

        if isinstance(player_details, dict):
            tanks_list = player_details.get("tanks", [])
            if tanks_list:
                for tank in tanks_list:
                    tank_name = tank.get("name", "Unknown")
                    tank_id = tank.get("id")
                    tanks.append({"name": tank_name, "id": tank_id})
                    tank_ids.add(tank_id)

    print(f"✓ Identified {len(tanks)} tanks")

    # ===== STEP 8: Build tank timeline from damage events =====
    print("Building tank timeline from boss melee swings...")

    damage_query = f"""
    query {{
      reportData {{
        report(code: "{report_code}") {{
          events(fightIDs: {[fight_id]}, dataType: DamageTaken, limit: 10000) {{
            data
          }}
        }}
      }}
    }}
    """

    response = requests.post(API_URL, json={"query": damage_query}, headers=headers)

    tank_timeline = []
    if response.status_code == 200:
        result = response.json()
        damage_events = result.get("data", {}).get("reportData", {}).get("report", {}).get("events", {}).get("data", [])

        for event in damage_events:
            source_id = event.get("sourceID")
            target_id = event.get("targetID")

            if source_id not in player_ids and event.get("type") == "damage" and target_id in tank_ids:
                tank_timeline.append({
                    "timestamp": event.get("timestamp"),
                    "tank_id": target_id,
                    "tank_name": actor_names.get(target_id, "Unknown")
                })

        tank_timeline.sort(key=lambda x: x["timestamp"])

    print(f"✓ Built tank timeline with {len(tank_timeline)} melee swings")

    # ===== STEP 9: Get cast events =====
    print(f"Querying cast events for {player_name}...")

    casts_query = f"""
    query {{
      reportData {{
        report(code: "{report_code}") {{
          events(fightIDs: {[fight_id]}, dataType: Casts, sourceID: {player_id}, limit: 10000) {{
            data
          }}
        }}
      }}
    }}
    """

    response = requests.post(API_URL, json={"query": casts_query}, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Query failed: {response.status_code} - {response.text}")

    result = response.json()
    cast_events = result.get("data", {}).get("reportData", {}).get("report", {}).get("events", {}).get("data", [])

    print(f"✓ Found {len(cast_events)} cast events")

    # Get ability names
    ability_ids = set(event.get("abilityGameID") for event in cast_events if event.get("abilityGameID"))

    print(f"Querying names for {len(ability_ids)} unique abilities...")
    ability_names = {}

    for ability_id in ability_ids:
        ability_query = f"""
        query {{
          gameData {{
            ability(id: {ability_id}) {{
              name
              icon
            }}
          }}
        }}
        """

        response = requests.post(API_URL, json={"query": ability_query}, headers=headers)

        if response.status_code == 200:
            result = response.json()
            ability_data = result.get("data", {}).get("gameData", {}).get("ability")
            if ability_data:
                ability_names[ability_id] = ability_data.get("name", f"Unknown ({ability_id})")
            else:
                ability_names[ability_id] = f"Unknown ({ability_id})"

    # ===== STEP 10: Process cast events with rotation tracking =====
    print("Processing cast events and rotation patterns...\n")

    def get_active_tank_at_time(timestamp, timeline):
        """Find the active tank at a given timestamp."""
        active_tank_name = None
        active_tank_id = None
        for swing in timeline:
            if swing["timestamp"] <= timestamp:
                active_tank_name = swing["tank_name"]
                active_tank_id = swing["tank_id"]
            else:
                break
        return active_tank_name if active_tank_name else "Unknown", active_tank_id

    cast_data = []
    rotation_count = 0

    for event in cast_events:
        timestamp = event.get("timestamp", 0)
        ability_id = event.get("abilityGameID", "?")
        ability_name = ability_names.get(ability_id, f"Unknown ({ability_id})")
        event_type = event.get("type", "unknown")
        target_id = event.get("targetID")

        # Filter out specific casts
        if "Regrowth" in ability_name and event_type == "cast":
            continue
        if "Restore Mana" in ability_name:
            continue
        if "Healing Touch" in ability_name:
            continue

        target_name = actor_names.get(target_id, f"Unknown (ID: {target_id})") if target_id else "-"
        active_tank_name, active_tank_id = get_active_tank_at_time(timestamp, tank_timeline)
        relative_time = (timestamp - fight_start_time) / 1000.0

        is_rotation_start = (
            ability_id == LIFEBLOOM_ID and
            event_type == "cast" and
            target_id == active_tank_id and
            active_tank_id is not None
        )

        is_instant_cast = (
            (ability_id == LIFEBLOOM_ID and event_type == "cast" and target_id != active_tank_id) or
            (ability_id == REJUVENATION_ID and event_type == "cast") or
            (ability_id == TREE_OF_LIFE_ID and event_type == "cast") or
            (ability_id == SWIFTMEND_ID and event_type == "cast") or
            (ability_id == NATURES_SWIFTNESS_ID and event_type == "cast") or
            (ability_id == INNERVATE_ID and event_type == "cast")
        )

        if is_rotation_start:
            rotation_count += 1

        cast_data.append({
            "time": relative_time,
            "spell": ability_name,
            "target": target_name,
            "active_tank": active_tank_name,
            "type": event_type,
            "ability_id": ability_id,
            "rotation_start": is_rotation_start,
            "instant_cast": is_instant_cast,
            "rotation_number": rotation_count if is_rotation_start else None
        })

    cast_data.sort(key=lambda x: x["time"])

    # Build rotation sections
    rotation_sections = []
    section_start_time = 0
    section_type = "Rotation #1"
    section_lb_count = 0
    section_i_count = 0
    section_rg_count = 0
    last_rotation_time = None
    in_rotation = False
    first_rotation_seen = False
    casts_since_rotation_end = 0

    for i, cast in enumerate(cast_data):
        # Determine abbreviation
        if cast['rotation_start']:
            abbr_str = "LB"
        elif cast['instant_cast']:
            abbr_str = "I"
        elif "Regrowth" in cast['spell']:
            abbr_str = "RG"
        else:
            abbr_str = ""

        # Add separator before first rotation
        if cast['rotation_start'] and not first_rotation_seen:
            rotation_sections.append({
                "type": section_type,
                "start_time": section_start_time,
                "end_time": cast['time'],
                "lb": section_lb_count,
                "i": section_i_count,
                "rg": section_rg_count
            })
            first_rotation_seen = True
            section_start_time = cast['time']
            section_type = f"Rotation #{len(rotation_sections) + 1}"
            section_lb_count = 0
            section_i_count = 0
            section_rg_count = 0

        # Check if we need to end the previous rotation
        if in_rotation and last_rotation_time is not None:
            time_since_last_rotation = cast['time'] - last_rotation_time

            if time_since_last_rotation >= ROTATION_TIMEOUT or cast['rotation_start']:
                rotation_sections.append({
                    "type": section_type,
                    "start_time": section_start_time,
                    "end_time": cast['time'],
                    "lb": section_lb_count,
                    "i": section_i_count,
                    "rg": section_rg_count
                })
                in_rotation = False
                casts_since_rotation_end = 0
                section_start_time = cast['time']
                section_type = f"Rotation #{len(rotation_sections) + 1}"
                section_lb_count = 0
                section_i_count = 0
                section_rg_count = 0

        # When not in a rotation, add separator every 5 casts
        if not in_rotation and first_rotation_seen and not cast['rotation_start']:
            if casts_since_rotation_end > 0 and casts_since_rotation_end % CASTS_BETWEEN_SEPARATORS == 0:
                rotation_sections.append({
                    "type": section_type,
                    "start_time": section_start_time,
                    "end_time": cast['time'],
                    "lb": section_lb_count,
                    "i": section_i_count,
                    "rg": section_rg_count
                })
                section_start_time = cast['time']
                section_type = f"Rotation #{len(rotation_sections) + 1}"
                section_lb_count = 0
                section_i_count = 0
                section_rg_count = 0

        # Update section counts
        if abbr_str == "LB":
            section_lb_count += 1
        elif abbr_str == "I":
            section_i_count += 1
        elif abbr_str == "RG":
            section_rg_count += 1

        # Update rotation tracking
        if cast['rotation_start']:
            last_rotation_time = cast['time']
            in_rotation = True
            casts_since_rotation_end = 0
            if first_rotation_seen:
                section_type = f"Rotation #{len(rotation_sections) + 1}"
        elif not in_rotation:
            casts_since_rotation_end += 1

    # Save final section
    if section_lb_count > 0 or section_i_count > 0 or section_rg_count > 0:
        rotation_sections.append({
            "type": section_type,
            "start_time": section_start_time,
            "end_time": cast_data[-1]['time'] if cast_data else 0,
            "lb": section_lb_count,
            "i": section_i_count,
            "rg": section_rg_count
        })

    # Filter out uninteresting rotations
    actual_rotations = [
        s for s in rotation_sections
        if not (
            (s['lb'] == 1 and s['i'] == 0 and s['rg'] == 0) or
            (s['lb'] == 0 and s['i'] == 1 and s['rg'] == 0)
        )
    ]

    # Calculate rotation pattern frequencies
    rotation_patterns = [f"[{s['lb']}LB {s['i']}I {s['rg']}RG]" for s in actual_rotations]
    pattern_counts = Counter(rotation_patterns)
    sorted_patterns = sorted(pattern_counts.items(), key=lambda x: x[1], reverse=True)

    # Return all collected data
    return {
        "fight_id": fight_id,
        "is_kill": is_kill,
        "timestamp": fight_absolute_timestamp,
        "duration_minutes": duration_minutes,
        "duration_seconds": duration_seconds,
        "total_healers": total_healers,
        "healer_composition": healer_composition,
        "player_name": player_name,
        "player_stats": player_stats,
        "player_trinkets": player_trinkets,
        "has_vampiric_touch": has_vampiric_touch,
        "innervate_count": innervate_count,
        "has_bloodlust": has_bloodlust,
        "has_natures_grace": has_natures_grace,
        "lifebloom_uptime_percent": round(lifebloom_uptime_percent, 2),
        "lifebloom_hps": round(lifebloom_hps, 2),
        "rejuvenation_hps": round(rejuvenation_hps, 2),
        "regrowth_total_hps": round(regrowth_total_hps, 2),
        "regrowth_by_rank": regrowth_by_rank,
        "player_ranking": player_ranking,
        "tanks": tanks,
        "cast_data": cast_data,
        "rotation_count": rotation_count,
        "rotation_sections": rotation_sections,
        "actual_rotations": actual_rotations,
        "sorted_patterns": sorted_patterns,
        "fight_start_time": fight_start_time
    }


def display_results(data):
    """Display all analysis results in formatted output."""

    # Convert timestamp to readable date
    encounter_date = datetime.fromtimestamp(data['timestamp'] / 1000)
    date_str = encounter_date.strftime("%Y-%m-%d %H:%M:%S")

    # ===== ENCOUNTER INFORMATION =====
    print()
    print("=" * 70)
    print("ENCOUNTER INFORMATION")
    print("=" * 70)
    print(f"Date: {date_str}")
    print(f"Duration: {data['duration_minutes']}m {data['duration_seconds']}s")
    print()

    # ===== HEALING COMPOSITION =====
    print("=" * 70)
    print("HEALING COMPOSITION")
    print("=" * 70)
    print(f"\nTotal Healers: {data['total_healers']}")
    print()

    for healer_type, players in data['healer_composition'].items():
        count = len(players)
        print(f"{healer_type}: {count}")
        if players:
            for player in players:
                print(f"  • {player}")

    print()

    # ===== RESTORATION DRUID STATS =====
    print("=" * 70)
    print("RESTORATION DRUID PERFORMANCE")
    print("=" * 70)

    player_name = data['player_name']
    stats = data['player_stats']
    trinkets_data = data['player_trinkets']
    ranking = data['player_ranking']

    if ranking:
        server = ranking.get("server", "Unknown")
        region = ranking.get("region", "Unknown")
        print(f"  • {player_name}-{server} ({region})")
    else:
        print(f"  • {player_name}")

    # Display stats
    if stats.get("has_stats"):
        print(f"    Item Level: {stats.get('item_level', 0)}")
        print(f"    Stats: {stats.get('intellect', 0)} Intellect | {stats.get('spirit', 0)} Spirit | {stats.get('haste', 0)} Haste")
    else:
        print(f"    Item Level: Unknown")
        print(f"    Stats: Unknown")

    # Display trinkets
    if trinkets_data.get("has_trinkets"):
        print(f"    Trinkets:")
        for trinket in trinkets_data.get("trinkets", []):
            trinket_name = trinket.get("name", "Unknown")
            trinket_id = trinket.get("id", "?")
            print(f"      • {trinket_name} (ID: {trinket_id})")
    else:
        print(f"    Trinkets: Unknown")

    # Display buffs
    vt_status = "Yes" if data['has_vampiric_touch'] else "No"
    print(f"    Vampiric Touch: {vt_status}")
    print(f"    Innervate Count: {data['innervate_count']}")

    bloodlust_status = "Yes" if data['has_bloodlust'] else "No"
    print(f"    Received Bloodlust: {bloodlust_status}")

    ng_status = "Yes" if data['has_natures_grace'] else "No"
    print(f"    Nature's Grace: {ng_status}")

    # Display Lifebloom uptime
    print(f"    Lifebloom Uptime: {data['lifebloom_uptime_percent']}%")

    # Display spell HPS
    if ranking and ranking.get("hps", 0) > 0:
        total_hps = ranking.get("hps", 0)

        lb_hps = data['lifebloom_hps']
        lb_percent = (lb_hps / total_hps) * 100
        print(f"    Lifebloom HPS: {lb_hps:.2f} ({lb_percent:.2f}% of total)")

        rej_hps = data['rejuvenation_hps']
        rej_percent = (rej_hps / total_hps) * 100
        print(f"    Rejuvenation HPS: {rej_hps:.2f} ({rej_percent:.2f}% of total)")

        rg_hps = data['regrowth_total_hps']
        rg_percent = (rg_hps / total_hps) * 100
        print(f"    Regrowth HPS: {rg_hps:.2f} ({rg_percent:.2f}% of total)")

        if len(data['regrowth_by_rank']) > 1:
            for rank_name in sorted(data['regrowth_by_rank'].keys(), reverse=True):
                rank_hps = data['regrowth_by_rank'][rank_name]
                if rank_hps > 0:
                    print(f"      • {rank_name}: {rank_hps:.2f}")
    else:
        print(f"    Lifebloom HPS: {data['lifebloom_hps']:.2f}")
        print(f"    Rejuvenation HPS: {data['rejuvenation_hps']:.2f}")
        print(f"    Regrowth HPS: {data['regrowth_total_hps']:.2f}")

    # Display rankings
    if ranking:
        rank = ranking.get("rank")
        rank_percent = ranking.get("rankPercent")
        total_parses = ranking.get("totalParses")
        hps = ranking.get("hps", 0)

        print(f"    HPS: {hps:.2f}")
        if rank is not None and total_parses is not None:
            print(f"    Rank: {rank} out of {total_parses} parses ({rank_percent}th percentile)")
        elif rank_percent is not None:
            print(f"    Percentile: {rank_percent}th")
        else:
            print(f"    Rank: Not ranked (no valid parse)")

    print("=" * 70)
    print()

    # ===== CAST-BY-CAST TIMELINE =====
    print("=" * 150)
    print(f"RESTORATION DRUID CASTS WITH TANK TRACKING - {player_name.upper()}")
    print("=" * 150)
    print(f"{'Time':<10} {'Spell Name':<30} {'Target':<25} {'Active Tank':<20} {'Type':<12} {'Action':<20} {'Abbr':<6}")
    print("-" * 150)

    last_rotation_time = None
    in_rotation = False
    first_rotation_seen = False
    casts_since_rotation_end = 0
    section_lb_count = 0
    section_i_count = 0
    section_rg_count = 0

    for i, cast in enumerate(data['cast_data']):
        time_str = f"{cast['time']:.2f}s"

        # Determine action string
        if cast['rotation_start']:
            action_str = "Rotation started"
        elif cast['instant_cast']:
            action_str = "Instant cast"
        elif "Regrowth" in cast['spell']:
            action_str = "Regrowth"
        else:
            action_str = ""

        # Determine abbreviation
        if cast['rotation_start']:
            abbr_str = "LB"
        elif cast['instant_cast']:
            abbr_str = "I"
        elif "Regrowth" in cast['spell']:
            abbr_str = "RG"
        else:
            abbr_str = ""

        # Add separator before first rotation
        if cast['rotation_start'] and not first_rotation_seen:
            print(f"[{section_lb_count}LB {section_i_count}I {section_rg_count}RG]")
            print("-" * 150)
            first_rotation_seen = True
            section_lb_count = 0
            section_i_count = 0
            section_rg_count = 0

        # Check if we need to end the previous rotation
        if in_rotation and last_rotation_time is not None:
            time_since_last_rotation = cast['time'] - last_rotation_time

            if time_since_last_rotation >= ROTATION_TIMEOUT or cast['rotation_start']:
                print(f"[{section_lb_count}LB {section_i_count}I {section_rg_count}RG]")
                print("-" * 150)
                in_rotation = False
                casts_since_rotation_end = 0
                section_lb_count = 0
                section_i_count = 0
                section_rg_count = 0

        # When not in a rotation, add separator every 5 casts
        if not in_rotation and first_rotation_seen and not cast['rotation_start']:
            if casts_since_rotation_end > 0 and casts_since_rotation_end % CASTS_BETWEEN_SEPARATORS == 0:
                print(f"[{section_lb_count}LB {section_i_count}I {section_rg_count}RG]")
                print("-" * 150)
                section_lb_count = 0
                section_i_count = 0
                section_rg_count = 0

        # Print the cast
        print(f"{time_str:<10} {cast['spell']:<30} {cast['target']:<25} {cast['active_tank']:<20} {cast['type']:<12} {action_str:<20} {abbr_str:<6}")

        # Update section counts
        if abbr_str == "LB":
            section_lb_count += 1
        elif abbr_str == "I":
            section_i_count += 1
        elif abbr_str == "RG":
            section_rg_count += 1

        # Update rotation tracking
        if cast['rotation_start']:
            last_rotation_time = cast['time']
            in_rotation = True
            casts_since_rotation_end = 0
        elif not in_rotation:
            casts_since_rotation_end += 1

    print("=" * 150)
    print(f"Total casts: {len(data['cast_data'])}")
    print(f"Total Rotations: {data['rotation_count']} (Lifebloom cast on Active Tank)")
    print("=" * 150)
    print()

    # ===== IDENTIFIED ROTATIONS ONLY =====
    actual_rotations = data['actual_rotations']

    if actual_rotations:
        print("=" * 150)
        print("IDENTIFIED ROTATIONS ONLY")
        print("=" * 150)
        print(f"{'Rotation':<30} {'Time Range':<25} {'Notation':<30}")
        print("-" * 150)

        for idx, section in enumerate(actual_rotations, 1):
            section_name = f"Rotation #{idx}"
            time_range = f"{section['start_time']:.2f}s - {section['end_time']:.2f}s"
            notation = f"[{section['lb']}LB {section['i']}I {section['rg']}RG]"
            print(f"{section_name:<30} {time_range:<25} {notation:<30}")

        print("=" * 150)
        print()

    # ===== TOP ROTATION PATTERNS =====
    sorted_patterns = data['sorted_patterns']
    total_rotations = len(actual_rotations)

    if sorted_patterns:
        print("=" * 150)
        print("TOP ROTATION PATTERNS")
        print("=" * 150)

        if len(sorted_patterns) >= 2:
            first_pattern, first_count = sorted_patterns[0]
            first_pct = (first_count / total_rotations * 100) if total_rotations > 0 else 0
            print(f"1st Most Common: {first_pattern} - Used {first_count} times ({first_pct:.1f}%)")

            second_pattern, second_count = sorted_patterns[1]
            second_pct = (second_count / total_rotations * 100) if total_rotations > 0 else 0
            print(f"2nd Most Common: {second_pattern} - Used {second_count} times ({second_pct:.1f}%)")
        elif len(sorted_patterns) == 1:
            first_pattern, first_count = sorted_patterns[0]
            first_pct = (first_count / total_rotations * 100) if total_rotations > 0 else 0
            print(f"1st Most Common: {first_pattern} - Used {first_count} times ({first_pct:.1f}%)")
            print(f"2nd Most Common: N/A (only one unique pattern)")

        print("=" * 150)


def main():
    """Main execution function"""
    if len(sys.argv) != 4:
        print("Usage: python analyze_druid.py <report_id> <boss_name> <player_name>")
        print("\nExample:")
        print("  python analyze_druid.py wX7H9RtYJ48P1cdW Brutallus Mercychann")
        return 1

    report_code = sys.argv[1]
    boss_name = sys.argv[2]
    player_name = sys.argv[3]

    print("=" * 70)
    print("WARCRAFTLOGS RESTORATION DRUID ANALYSIS")
    print("=" * 70)
    print()

    try:
        data = analyze_druid_performance(report_code, boss_name, player_name)
        display_results(data)
        return 0
    except Exception as e:
        print()
        print("=" * 70)
        print("ERROR")
        print("=" * 70)
        print(f"{e}")
        print("=" * 70)
        return 1


if __name__ == "__main__":
    exit(main())
