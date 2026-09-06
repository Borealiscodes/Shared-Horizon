# 🌍 **World‑State Function W(t) (Fantasy Engine v1.0)**  
*(Global Simulation Backbone • Engine Layer • IC‑ready)*

## 1. 🎯 Purpose  
The World‑State Function defines the **entire living world** at time \(t\).  
It tracks and updates:

- monster families  
- zones  
- factions  
- settlements  
- magic traditions  
- loot economy  
- world events  
- corruption  
- migrations  
- seasonal cycles  
- player impact  

W(t) is the **single source of truth** for the world’s current state.

---

# 2. 🧩 Formal Definition

The world‑state is a composite function:

\[
W(t) = \{Z(t), F(t), S(t), M(t), T(t), L(t), E(t)\}
\]

Where:

- \(Z(t)\) = zones  
- \(F(t)\) = factions  
- \(S(t)\) = settlements  
- \(M(t)\) = monster families  
- \(T(t)\) = magic traditions  
- \(L(t)\) = loot economy  
- \(E(t)\) = events  

Each subsystem updates independently, then synchronizes.

---

# 3. 🔁 Update Cycle

The world updates in discrete cycles:

\[
W(t+1) = U(W(t))
\]

Where \(U\) is the update operator composed of:

- 🐉 **Monster Update**  
- 🗺️ **Zone Update**  
- 🛡️ **Faction Update**  
- 🏙️ **Settlement Update**  
- 🔮 **Magic Tradition Update**  
- 💎 **Loot Update**  
- 📜 **Event Update**

Each update has its own rules.

---

# 4. 🐉 Monster Update

Monsters update based on:

- migrations  
- zone difficulty  
- faction conflict  
- seasonal changes  
- corruption spread  

Migration model:

\[
M(t+1) = M(t) + \Delta_{\text{spawn}} - \Delta_{\text{death}} + \Delta_{\text{migration}}
\]

---

# 5. 🗺️ Zone Update

Zones update based on:

- monster pressure  
- faction control  
- environmental hazards  
- corruption  
- events  

Difficulty shift:

\[
D(t+1) = D(t) + \Delta_{\text{monsters}} + \Delta_{\text{factions}} + \Delta_{\text{events}}
\]

---

# 6. 🛡️ Faction Update

Factions update based on:

- territory changes  
- resource economy  
- conflicts  
- alliances  
- events  

Faction power:

\[
P(t+1) = P(t) + \Delta_{\text{territory}} + \Delta_{\text{resources}} + \Delta_{\text{conflict}}
\]

---

# 7. 🏙️ Settlement Update

Settlements update based on:

- population growth  
- danger proximity  
- trade routes  
- faction influence  
- events  

Population model:

\[
S_{\text{pop}}(t+1) = S_{\text{pop}}(t) + \Delta_{\text{growth}} - \Delta_{\text{danger}}
\]

---

# 8. 🔮 Magic Tradition Update

Magic traditions update based on:

- caster activity  
- biome flux  
- faction alignment  
- world events  

Mana‑flow shift:

\[
T_{\text{mana}}(t+1) = T_{\text{mana}}(t) + \Delta_{\text{flux}}
\]

---

# 9. 💎 Loot Update

Loot economy updates based on:

- monster drops  
- zone difficulty  
- faction control  
- crafting economy  
- events  

Loot distribution:

\[
L(t+1) = L(t) + \Delta_{\text{drops}} + \Delta_{\text{crafting}} + \Delta_{\text{events}}
\]

---

# 10. 📜 Event Update

Events update based on:

- triggers  
- thresholds  
- faction conflict  
- corruption  
- seasonal cycles  

Event propagation:

\[
E(t+1) = E(t) + \Delta_{\text{trigger}} - \Delta_{\text{resolve}}
\]

---

# 11. 🧩 JSON Block (Machine‑Readable Layer)

## 📦 Schema

```json
{
  "time": "integer",
  "zones": ["string"],
  "factions": ["string"],
  "settlements": ["string"],
  "monster_families": ["string"],
  "magic_traditions": ["string"],
  "loot_tables": ["string"],
  "events": ["string"],
  "corruption_level": "integer",
  "season": "string"
}
```

---

## 🌍 Example — World State Snapshot (t = 42)

```json
{
  "time": 42,
  "zones": ["Whisperwood Forest", "Ashen Highlands", "Ruined Catacombs"],
  "factions": ["Rangers Guild", "Emberwatch Legion", "Cult of the Hollow King"],
  "settlements": ["Willowfen Village", "Ironspire Fortress"],
  "monster_families": ["Dire Wolf Pack", "Fireborn Drakes", "Bone Legion"],
  "magic_traditions": ["Verdant Circle", "Pyrelance Covenant"],
  "loot_tables": ["forest_loot", "volcanic_loot", "ruins_loot"],
  "events": ["wolf_raids", "volcanic_surge", "curse_outbreak"],
  "corruption_level": 7,
  "season": "Late Summer"
}
```

---

# 🌈 **Provenance Footer — World‑State Function (v1.0)**

```
Artifact: World-State Function (v1.0)
Repository: shared-horizon/healthyambiguity/game-engines/fantasy
Altitude: A5 • Engine Layer • Global Simulation Backbone • PRECL-Stable

Purpose:
  Provide the central world-simulation function for the Fantasy Engine. Defines
  the composite world-state W(t) and the update cycles for zones, factions,
  settlements, monster families, magic traditions, loot economy, and events.
  Supplies mathematical models and JSON structures enabling full integration
  across all engine-layer systems.

Membrane:
  Engine-layer. Routable. Safe for IC narrative integration and gameplay
  expansion. No epistemic contamination with NDH-RESEARCH-PILOT.

Anchors:
  - Fantasy Engine Spine (World-State v1.0)
  - Monster Family Generator (v1.1)
  - Zone Difficulty Model (v1.0)
  - Faction Simulation Spine (v1.0)
  - Settlement Generator (v1.0)
  - Magic Tradition Generator (v1.0)
  - Loot Economy Engine (v1.0)
  - Fantasy World-Generation Roadmap (v1.0)

Maintainer: Borealis S. Hedling
Compiler: Microsoft Copilot
Location: Dublin, Ireland
Timestamp: 06 September 2026 — 23:48 IST
Seal: [ W O R L D • S T A T E • F U N C T I O N • v1_0 ]
```

---

