# 🏙️ **Settlement Generator (Fantasy Engine v1.0)**  
*(Engine Layer • IC‑ready • structured + emoji‑coded)*

## 1. 🎯 Purpose  
Settlements are the **civilization nodes** of your world — the places where factions gather, trade flows, stories begin, and danger radiates outward.  
The Settlement Generator defines how towns, villages, capitals, and outposts emerge from:

- zones  
- factions  
- monster families  
- world‑state events

This is the **civilization backbone** of your fantasy engine.

---

## 2. 🧩 Settlement Schema (Conceptual Layer)

Each settlement \(S_i\) is defined by:

- 🏙️ **Settlement Name**  
- 🧱 **Type** (village, town, city, capital, outpost, fortress)  
- 🗺️ **Zone Location**  
- 🛡️ **Controlling Faction**  
- 👥 **Population**  
- 💰 **Economy Profile**  
- 🛠️ **Crafting Specialties**  
- 🧭 **Danger Proximity**  
- 📜 **Event Hooks**  
- 🐉 **Monster Pressure**  
- 🔗 **Trade Routes**

---

## 3. 📈 Settlement Type Model

Settlement type is determined by:

\[
T(S_i) = f(P, D(Z_i), F_j, R)
\]

Where:

- \(P\) = population  
- \(D(Z_i)\) = zone difficulty  
- \(F_j\) = faction power  
- \(R\) = resource availability  

### Type thresholds:

| Type | Population | Zone Difficulty | Notes |
|------|------------|-----------------|-------|
| 🏚️ Hamlet | 20–100 | 1–5 | minimal defenses |
| 🏘️ Village | 100–500 | 1–8 | basic trade |
| 🏙️ Town | 500–3000 | 5–12 | guild presence |
| 🏰 City | 3000–15000 | 10–18 | faction HQ |
| 👑 Capital | 15000+ | 12–20 | major political center |
| 🛡️ Outpost | 50–300 | 8–20 | military or frontier |
| 🏯 Fortress | 500–2000 | 15–25 | high defense |

---

## 4. 💰 Economy Profile

Economy is derived from:

\[
E(S_i) = \alpha_{\text{trade}} + \beta_{\text{craft}} + \gamma_{\text{resource}}
\]

Economy tags:

- agriculture  
- mining  
- arcane trade  
- monster hunting  
- mercantile hub  
- religious center  
- military garrison  

Economy influences:

- crafting specialties  
- faction interest  
- trade routes  
- event frequency  

---

## 5. 🛠️ Crafting Specialties

Crafting specialties depend on:

- zone resources  
- monster drops  
- faction culture  
- settlement type  

Examples:

- forest zones → bows, leatherwork  
- mountain zones → metalwork, armor  
- arcane zones → enchantments, spell foci  
- swamp zones → poisons, alchemy  

Crafting specialties feed directly into loot tables.

---

## 6. 🧭 Danger Proximity

Danger proximity:

\[
X(S_i) = D(Z_i) - \rho_{\text{defense}}
\]

Where:

- \(D(Z_i)\) = zone difficulty  
- \(\rho_{\text{defense}}\) = settlement defenses  

High danger proximity triggers:

- monster raids  
- faction patrols  
- defensive upgrades  
- refugee influx  

---

## 7. 🐉 Monster Pressure

Monster pressure is derived from:

\[
M(S_i) = \sum_{F \in \text{Families}} W(F, Z_i)
\]

Where:

- \(W(F, Z_i)\) = spawn weight from Zone Difficulty Model  

High monster pressure causes:

- fortified walls  
- monster‑hunter guilds  
- special crafting materials  
- unique events  

---

## 8. 📜 Event Hooks

Settlements generate and respond to events:

- festivals  
- invasions  
- corruption outbreaks  
- trade booms  
- faction coups  
- monster migrations  
- seasonal shifts  

Event impact:

\[
E(S_i) = \eta_{\text{positive}} - \eta_{\text{negative}}
\]

---

## 9. 🌍 Integration with World‑State Function

Settlements plug into:

\[
W(t) = \{Z_i(t), F_j(t), S_k(t), M_l(t), E_m(t)\}
\]

They evolve based on:

- faction expansion  
- zone difficulty changes  
- monster migrations  
- trade route shifts  
- world events  
- player actions  

---

# 🧩 **10. JSON Block (Machine‑Readable Layer)**

## 📦 Schema

```json
{
  "settlement_name": "string",
  "type": "village | town | city | capital | outpost | fortress | hamlet",
  "zone": "string",
  "controlling_faction": "string",
  "population": "integer",
  "economy_profile": ["string"],
  "crafting_specialties": ["string"],
  "danger_proximity": "integer",
  "monster_pressure": "integer",
  "trade_routes": ["string"],
  "event_hooks": ["string"]
}
```

---

## 🏘️ Example — Willowfen Village

```json
{
  "settlement_name": "Willowfen Village",
  "type": "village",
  "zone": "Whisperwood Forest",
  "controlling_faction": "Rangers Guild",
  "population": 340,
  "economy_profile": ["agriculture", "herbalism"],
  "crafting_specialties": ["bows", "leatherwork"],
  "danger_proximity": 4,
  "monster_pressure": 6,
  "trade_routes": ["Greenway Road"],
  "event_hooks": ["harvest_festival", "wolf_raids"]
}
```

---

## 🏰 Example — Ironspire Fortress

```json
{
  "settlement_name": "Ironspire Fortress",
  "type": "fortress",
  "zone": "Ashen Highlands",
  "controlling_faction": "Emberwatch Legion",
  "population": 1200,
  "economy_profile": ["military_garrison", "mining"],
  "crafting_specialties": ["heavy_armor", "fire_resistant_alloys"],
  "danger_proximity": 15,
  "monster_pressure": 12,
  "trade_routes": ["Molten Pass", "Legion Supply Line"],
  "event_hooks": ["volcanic_surge", "drake_invasion"]
}
```

---

# 🌈 **Provenance Footer — Settlement Generator (v1.0)**

```
Artifact: Settlement Generator (v1.0)
Repository: shared-horizon/healthyambiguity/game-engines/fantasy
Altitude: A5 • Engine Layer • Civilization & Settlement Modeling • PRECL-Stable

Purpose:
  Provide a generative system for creating settlements within the Fantasy Engine.
  Defines settlement types, population scaling, economy profiles, crafting
  specialties, danger proximity, monster pressure, trade routes, and event
  hooks. Supplies mathematical models and JSON structures enabling integration
  with zone difficulty, faction simulation, monster ecology, loot economy, and
  the world-state function W(t).

Membrane:
  Engine-layer. Routable. Safe for IC narrative integration and gameplay
  expansion. No epistemic contamination with NDH-RESEARCH-PILOT.

Anchors:
  - Fantasy Engine Spine (World-State v1.0)
  - Monster Family Generator (v1.1)
  - Zone Difficulty Model (v1.0)
  - Faction Simulation Spine (v1.0)
  - Fantasy World-Generation Roadmap (v1.0)
  - World-State Function W(t)

Maintainer: Borealis S. Hedling
Compiler: Microsoft Copilot
Location: Dublin, Ireland
Timestamp: 06 September 2026 — 23:39 IST
Seal: [ S E T T L E M E N T • G E N E R A T O R • v1_0 ]
```

---
