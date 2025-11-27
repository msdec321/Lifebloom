# Restoration Druid Haste Breakpoints Guide

## Introduction: Understanding Rotations

As a Restoration Druid maintaining Lifebloom on a tank, your healing follows a **rotation cycle** - the sequence of spells you cast between Lifebloom refreshes. Since Lifebloom has a 7-second duration, you have a limited window to weave in additional heals before needing to refresh it.

**Why does haste matter?** Spell haste rating reduces both your Global Cooldown (GCD) and Regrowth's cast time, allowing you to fit more spells into each 7-second Lifebloom cycle. This creates distinct **breakpoints** where new rotation patterns become possible.

---

## Rotation Mechanics

**Key Parameters:**
- **Lifebloom Duration**: 7.0 seconds (fixed)
- **Base GCD** (0 haste): 1.5 seconds
- **Base Regrowth Cast Time** (0 haste): 2.0 seconds
- **Rotation Window**: 7.0s - GCD ≈ 5.5s at 0 haste

**Haste Formulas:**
```
GCD = 1.5 / (1 + Haste Rating / 1577)
Regrowth Cast Time = 2.0 / (1 + Haste Rating / 1577)
Rotation Window = 7.0 - GCD
```

**Spell Categories:**
- **Lifebloom (LB)**: The anchor spell that starts each rotation cycle when cast on the active tank
- **Instant Casts (I)**: Rejuvenation, Swiftmend, Nature's Swiftness, Innervate, Lifebloom on non-tanks
  - Each consumes 1 GCD (1.5s at 0 haste)
- **Regrowth (RG)**: Your primary direct heal with a cast time
  - Takes 2.0s at 0 haste

**Rotation Notation:**
We use the format **[XLB YI ZRG]** where:
- X = Number of Lifebloom casts on tank
- Y = Number of instant-cast spells
- Z = Number of Regrowth casts

Example: **[1LB 2I 1RG]** = 1 Lifebloom on tank, 2 instant casts, 1 Regrowth

---

## 0 Haste (0 Spell Haste Rating)

**GCD:** 1.5 seconds
**Regrowth Cast Time:** 2.0 seconds
**Rotation Window:** 5.5 seconds

### Viable Rotations

At 0 haste, you can fit the following rotations within the 5.5-second window:

| Rotation | Instants | Regrowths | Time Used | Buffer | Notes |
|----------|----------|-----------|-----------|--------|-------|
| **[1LB 3I 0RG]** | 3 | 0 | 4.5s | 1.0s | Pure HoT/instant healing - maximum mobility |
| **[1LB 2I 1RG]** | 2 | 1 | 5.0s | 0.5s | Balanced rotation with one direct heal |
| **[1LB 1I 2RG]** | 1 | 2 | 5.5s | 0.0s | Maximum throughput - fills entire window (tight!) |
| **[1LB 2I 0RG]** | 2 | 0 | 3.0s | 2.5s | Conservative instant-only rotation |
| **[1LB 1I 1RG]** | 1 | 1 | 3.5s | 2.0s | Light healing rotation with flexibility |
| **[1LB 0I 2RG]** | 0 | 2 | 4.0s | 1.5s | Pure Regrowth spam (uncommon) |

### The Ping Problem: Latency Kills Rotations

**In theory**, 6 rotations are possible at 0 haste. **In practice**, latency (ping) drastically limits your options.

When you cast a spell, you must wait for the server to register it before your next cast. This creates an **effective "Server GCD"**:

```
Server GCD = 1.5s + Ping
Rotation Window = 7.0s - Server GCD
```

#### Rotation Viability by Ping

| Rotation | 0ms Ping | 50ms Ping | 100ms Ping | 150ms Ping |
|----------|----------|-----------|------------|------------|
| **[1LB 3I 0RG]** | ✅ | ✅ | ✅ | ✅ |
| **[1LB 2I 1RG]** | ✅ | ✅ | ✅ | ❌ **Impossible** |
| **[1LB 1I 2RG]** | ✅ (0.0s buffer!) | ❌ **Impossible** | ❌ | ❌ |
| **[1LB 2I 0RG]** | ✅ | ✅ | ✅ | ✅ |
| **[1LB 1I 1RG]** | ✅ | ✅ | ✅ | ✅ |
| **[1LB 0I 2RG]** | ✅ | ✅ | ✅ | ✅ |

**Key Findings:**
- **[1LB 1I 2RG]** is **theoretical only** - even 50ms ping makes it impossible to execute
- **[1LB 2I 1RG]** requires excellent ping (<150ms) to work reliably
- Players with 150ms+ ping lose access to the most efficient rotations

**Practical Recommendations:**
- **Low Ping (<100ms)**: Use **[1LB 2I 1RG]** as your primary rotation - best balance of throughput and safety
- **High Ping (150ms+)**: Stick to **[1LB 3I 0RG]** or lighter rotations - Regrowth-heavy patterns will clip your Lifebloom
- **All Players**: Avoid **[1LB 1I 2RG]** unless on LAN - the 0.0s buffer is unrealistic in real gameplay

This is why **spell haste is critically important** - it expands your rotation window, making efficient rotations accessible even with higher ping!

---

## Next: Haste Breakpoints

*Stay tuned for analysis of higher haste tiers where new rotations become possible!*

---

*Analysis based on data from Lifebloom (tbc-lifebloom.com) - TBC Classic Restoration Druid performance analytics*
