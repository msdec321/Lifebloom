"""
TBC Classic Spell Haste Rating Lookup Table

This table contains all items with Spell Haste Rating in TBC Classic.
Items are keyed by Item ID (which is consistent across all languages).

Format:
    ITEM_ID: (SPELL_HASTE_RATING, "Item Name"),

Usage:
    from tbc_haste_items import TBC_HASTE_ITEMS, get_item_haste

    haste = TBC_HASTE_ITEMS.get(34554, (0, "Unknown"))[0]  # Returns haste rating
    # or
    haste = get_item_haste(34554)  # Returns 0 if not found
"""

# =============================================================================
# TBC CLASSIC SPELL HASTE ITEMS
# =============================================================================
# Key: Item ID
# Value: (Spell Haste Rating, "Item Name for reference")
# =============================================================================

TBC_HASTE_ITEMS = {
    # =========================================================================
    # HEAD
    # =========================================================================
    34202: (33, "Shawl of Wonderment"), # Eredar Twins
    34339: (30, "Cowl of Light's Purity"), # Kil'jaeden
    34340: (30, "Dark Conjuror's Collar"), # Kil'jaeden

    # =========================================================================
    # NECK
    # =========================================================================
    34184: (20, "Brooch of the Highborne"), # Felmyst
    34204: (32, "Amulet of Unfettered Magics"), # Eredar Twins
    33281: (33, "Brooch of Nature's Mercy"), # Akil'zon (Zul'Aman)
    33466: (27, "Loop of Cursed Bones"), # Zul'jin (Zul'Aman)
    34360: (25, "Amulet of Flowing Life"), # Jewelcrafting
    34359: (25, "Pendant of Sunfire"), # Jewelcrafting
    37929: (26, "Guardian's Pendant of Reprieve"), # PVP
    37928: (24, "Guardian's Pendant of Subjugation"), # PVP
    35319: (21, "Vindicator's Pendant of Subjugation"), # PVP
    35317: (23, "Vindicator's Pendant of Reprieve"), # PVP

    # =========================================================================
    # SHOULDER
    # =========================================================================
    34209: (30, "Spaulders of Reclamation"), # Eredar Twins
    34210: (30, "Amice of the Convoker"), # Eredar Twins
    32583: (38, "Shoulderpads of Renewed Life"), # Leatherworking
    32585: (27, "Swiftheal Mantle"), # Tailoring

    # =========================================================================
    # BACK
    # =========================================================================
    33592: (25, "Cloak of Ancient Rituals"), # Hex Lord Malacrass (Zul'Aman)
    34242: (32, "Tattered Cape of Antonidas"), # Kil'jaeden
    32524: (32, "Shroud of the Highborne"), # Illidan
    35321: (16, "Cloak of Arcane Alacrity"), # Badge of Justice
    34702: (18, "Cloak of Swift Mending"), # Magister's Terrace
    35324: (16, "Cloak of Swift Reprieve"), # Badge of Justice

    # =========================================================================
    # CHEST
    # =========================================================================
    34212: (33, "Sunglow Vest"), # M'uru
    34233: (32, "Robes of Faltered Light"), # M'uru
    34232: (33, "Fel Conquerer Raiments"), # M'uru
    33317: (35, "Robe of Departed Spirits"), # Halazzi (Zul'Aman)
    34365: (40, "Robe of Eternal Light"), # Tailoring
    34364: (40, "Sunfire Robe"), # Tailoring

    # =========================================================================
    # WRIST
    # =========================================================================
    34445: (12, "Thunderheart Bracers"), # Tier 6, Kalecgos, Eredar Twins
    33588: (25, "Runed Spell-cuffs"), # Badge of Justice
    34697: (18, "Bindings of Raging Fire"), # Magister's Terrace
    32582: (28, "Bracers of Renewed Life"), # Leatherworking
    32584: (28, "Swiftheal Wraps"), # Tailoring

    # =========================================================================
    # HANDS
    # =========================================================================
    34342: (27, "Handguards of the Dawn"), # Kil'jaeden
    34344: (36, "Handguards of Defiled Worlds"), # Kil'jaeden
    34406: (36,  "Gloves of Tyri's Power"), # Kil'jaeden + Sunmote
    32328: (37, "Botanist's Gloves of Growth"), # Teron Gorefiend
    33974: (25, "Grasp of the Moonkin"), # Badge of Justice
    34372: (38, "Leather Gauntlets of the Sun"), # Leatherworking

    # =========================================================================
    # BELT
    # =========================================================================
    34554: (13, "Thunderheart Belt"), # Tier 6, Brutallus, Eredar Twins
    32256: (32, "Waistwrap of Infinity"), # Supremus
    32339: (37, "Belt of Primal Majesty"), # Gurtogg Bloodboil
    30895: (37, "Angelista's Sash"), # Kaz'rogal
    30914: (36, "Belt of the Crescent Moon"), # Kaz'rogal

    # =========================================================================
    # LEGS
    # =========================================================================
    34181: (32, "Leggings of Calamity"), # Brutallus
    33585: (45, "Achromic Trousers of the Naaru"), # Badge of Justice
    33584: (45, "Pantaloons of Arcane Annihilation"), # Badge of Justice
    34386: (42, "Pantaloons of Growing Strife"), # Kalecgos + Sunmote

    # =========================================================================
    # FEET
    # =========================================================================
    34571: (19, "Thunderheart Boots"), # Tier 6, Felmyst, Eredar Twins
    33357: (25, "Footpads of Madness"), # Jan'alai (Zul'Aman)

    # =========================================================================
    # RINGS
    # =========================================================================
    34166: (22, "Band of Lucent Beams"), # Kalecgos
    34230: (31, "Ring of Omnipotence"), # M'uru
    33498: (30, "Signet of the Quiet Forest"), # Zul'Aman
    32528: (30, "Blessed Band of Karabor"), # Black temple trash
    32527: (31, "Ring of Ancient Knowledge"), # Black temple trash
    34704: (18, "Band of Arcane Alacrity"), # Magister's Terrace
    34625: (14, "Kharmaa's Ring of Fate"), # Magister's Terrace
    34362: (30, "Loop of Forged Power"), # Jewelcrafting
    34363: (30, "Ring of Flowing Life"), # Jewelcrafting
    35129: (14, "Guardian's Band of Dominance"), # PVP
    35320: (30, "Vindicator's Band of Subjugation"), # PVP
    37927: (34, "Guardian's Band of Subjugation"), # PVP

    # =========================================================================
    # TRINKETS
    # =========================================================================
    34429: (54, "Shifting Naaru Sliver"), # M'uru
    35326: (40, "Battlemaster's Alacrity"), # Badge of Justice
    35327: (40, "Battlemaster's Alacrity"), # PVP

    # =========================================================================
    # MAIN HAND / ONE-HAND WEAPONS
    # =========================================================================
    34335: (23, "Hammer of Sanctification"), # Kil'jaeden
    34176: (30, "Reign of Misery"), # Brutallus
    34336: (23, "Sunflare"), # Kil'jaeden
    33468: (30, "Dark Blessing"), # Zul'jin (Zul'Aman)
    34604: (18, "Jaded Crystal Dagger"), # Magister's Terrace
    34790: (15, "Battle-mace of the High Priestess"), # Magister's Terrace

    # =========================================================================
    # OFF-HAND
    # =========================================================================
    34206: (22, "Book of Highborne Hymns"), # Eredar Twins
    34179: (32, "Heart of the Pit"), # Brutallus
    33334: (17, "Fetish of the Primal Gods"), # Badge of Justice

    # =========================================================================
    # TWO-HAND WEAPONS
    # =========================================================================
    34337: (32, "Golden Staff of the Sin'dorei"), # Kil'jaeden
    32374: (55, "Zhar'doom, Greatstaff of the Devourer") # Illidan

    # =========================================================================
    # IDOLS 
    # =========================================================================
    # None
}


# =============================================================================
# GEMS WITH SPELL HASTE
# =============================================================================
# Key: Gem ID
# Value: (Spell Haste Rating, "Gem Name for reference")
# =============================================================================

TBC_HASTE_GEMS = {
    # =========================================================================
    # YELLOW GEMS
    # =========================================================================
    35761: (10, "Quick Lionseye"), 

    # =========================================================================
    # ORANGE GEMS (Red + Yellow)
    # =========================================================================
    35760: (5, "Reckless Pyrestone"),

    # =========================================================================
    # GREEN GEMS (Yellow + Blue)
    # =========================================================================
    35759: (5, "Forceful Seaspray Emerald")
}


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def get_item_haste(item_id):
    """
    Get the spell haste rating for an item.

    Args:
        item_id: The item's ID number

    Returns:
        int: Spell haste rating, or 0 if item not in table
    """
    entry = TBC_HASTE_ITEMS.get(item_id)
    return entry[0] if entry else 0


def get_gem_haste(gem_id):
    """
    Get the spell haste rating for a gem.

    Args:
        gem_id: The gem's ID number

    Returns:
        int: Spell haste rating, or 0 if gem not in table
    """
    entry = TBC_HASTE_GEMS.get(gem_id)
    return entry[0] if entry else 0


def get_item_name(item_id):
    """
    Get the reference name for an item.

    Args:
        item_id: The item's ID number

    Returns:
        str: Item name, or "Unknown" if not in table
    """
    entry = TBC_HASTE_ITEMS.get(item_id)
    return entry[1] if entry else "Unknown"


def get_gem_name(gem_id):
    """
    Get the reference name for a gem.

    Args:
        gem_id: The gem's ID number

    Returns:
        str: Gem name, or "Unknown" if not in table
    """
    entry = TBC_HASTE_GEMS.get(gem_id)
    return entry[1] if entry else "Unknown"


def calculate_gear_haste(gear_list):
    """
    Calculate total spell haste from a player's gear.

    Args:
        gear_list: List of gear dicts from WarcraftLogs API
                   Each dict should have 'id' and optionally 'gems' keys

    Returns:
        dict with:
            - total_haste: Total spell haste rating
            - item_haste: Haste from items only
            - gem_haste: Haste from gems only
            - breakdown: List of (source, haste, name) tuples
            - missing_items: List of item IDs not in lookup table
            - missing_gems: List of gem IDs not in lookup table
    """
    item_haste = 0
    gem_haste = 0
    breakdown = []
    missing_items = []
    missing_gems = []

    for item in gear_list:
        item_id = item.get("id", 0)

        # Skip empty slots
        if item_id == 0:
            continue

        # Check item haste
        if item_id in TBC_HASTE_ITEMS:
            haste, name = TBC_HASTE_ITEMS[item_id]
            if haste > 0:
                item_haste += haste
                breakdown.append((item_id, haste, name))
        else:
            missing_items.append(item_id)

        # Check gems
        gems = item.get("gems", [])
        for gem in gems:
            gem_id = gem.get("id", 0)
            if gem_id == 0:
                continue

            if gem_id in TBC_HASTE_GEMS:
                haste, name = TBC_HASTE_GEMS[gem_id]
                if haste > 0:
                    gem_haste += haste
                    breakdown.append((gem_id, haste, f"Gem: {name}"))
            else:
                missing_gems.append(gem_id)

    return {
        "total_haste": item_haste + gem_haste,
        "item_haste": item_haste,
        "gem_haste": gem_haste,
        "breakdown": breakdown,
        "missing_items": missing_items,
        "missing_gems": missing_gems,
    }


# =============================================================================
# TEST / VERIFICATION
# =============================================================================

if __name__ == "__main__":
    print("TBC Classic Spell Haste Lookup Table")
    print("=" * 60)
    print(f"\nItems with haste: {len(TBC_HASTE_ITEMS)}")
    print(f"Gems with haste:  {len(TBC_HASTE_GEMS)}")

    print("\n" + "-" * 60)
    print("ITEMS")
    print("-" * 60)
    for item_id, (haste, name) in sorted(TBC_HASTE_ITEMS.items(), key=lambda x: x[1][1]):
        print(f"  {item_id:>6}: {haste:>3} haste - {name}")

    print("\n" + "-" * 60)
    print("GEMS")
    print("-" * 60)
    for gem_id, (haste, name) in sorted(TBC_HASTE_GEMS.items(), key=lambda x: x[1][1]):
        print(f"  {gem_id:>6}: {haste:>3} haste - {name}")

    # Test with sample gear
    print("\n" + "=" * 60)
    print("TEST: Mercychann's Gear")
    print("=" * 60)

    sample_gear = [
        {"id": 34245, "gems": [{"id": 25897}, {"id": 32195}]},  # Head
        {"id": 34677, "gems": []},  # Neck
        {"id": 34209, "gems": [{"id": 32195}, {"id": 32195}]},  # Shoulder
        {"id": 34212, "gems": [{"id": 32195}, {"id": 32195}, {"id": 32195}]},  # Chest
        {"id": 34554, "gems": [{"id": 32195}]},  # Belt
        {"id": 34384, "gems": [{"id": 32195}, {"id": 32195}, {"id": 32195}]},  # Legs
        {"id": 34571, "gems": [{"id": 32195}]},  # Feet
        {"id": 34445, "gems": [{"id": 32195}]},  # Wrist
        {"id": 34342, "gems": [{"id": 32195}, {"id": 32195}]},  # Hands
        {"id": 35733, "gems": []},  # Ring 1
        {"id": 29309, "gems": []},  # Ring 2
        {"id": 32496, "gems": []},  # Trinket 1
        {"id": 35750, "gems": []},  # Trinket 2
        {"id": 33592, "gems": []},  # Back
        {"id": 34335, "gems": [{"id": 32195}]},  # Main Hand
        {"id": 34206, "gems": []},  # Off Hand
        {"id": 27886, "gems": []},  # Relic
    ]

    result = calculate_gear_haste(sample_gear)

    print(f"\nItem Haste:  {result['item_haste']}")
    print(f"Gem Haste:   {result['gem_haste']}")
    print(f"Total Haste: {result['total_haste']}")

    if result['breakdown']:
        print("\nBreakdown:")
        for item_id, haste, name in result['breakdown']:
            print(f"  [{item_id}] +{haste} - {name}")

    print(f"\nExpected: 204")
    print(f"Missing:  {204 - result['total_haste']} (items not yet in table)")
