# 🐉 **Monster Family Generator (Fantasy Engine v1.1)**  
*(Integrated Document with JSON Block)*

## 1. 🎯 Purpose  
Define reusable templates for “monster families” that automatically generate individual monsters with coherent stats, abilities, biome affinities, and rarity—ready to feed into zones, factions, and the world‑state function.

---

## 2. 🧬 Family Schema (Conceptual Layer)

Each monster family \(F\) is defined by:

- 🐉 **Family Name**  
- 🌱 **Tier** (minion, elite, boss, apex)  
- 🗺️ **Biome Affinity**  
- 📈 **Level Range**  
- ❤️ **Base Stats**  
- 📈 **Growth Rates**  
- ☠️ **Threat Tag**  
- ✨ **Ability Set**  
- 💎 **Loot Profile**

---

## 3. 📈 Stat Growth Model

For a monster of family \(F\) at level \(L\):

- ❤️ Health  
  \[
  HP_{\max}^F(L) = HP_0^F + g_{HP}^F \cdot L
  \]

- 🔥 Attack  
  \[
  AP^F(L) = AP_0^F + g_{AP}^F \cdot L
  \]

- 🛡️ Defense  
  \[
  DF^F(L) = DF_0^F + g_{DF}^F \cdot L
  \]

- ⚡ Speed  
  \[
  SPD^F(L) = SPD_0^F + g_{SPD}^F \cdot L
  \]

Growth rates define **family identity**:

- brutes → high ❤️, high 🛡️  
- skirmishers → high ⚡  
- casters → high 🔥, special abilities  
- controllers → utility + debuffs  

---

## 4. 🗺️ Biome Affinity

Biome affinity determines:

- spawn regions  
- environmental bonuses  
- zone difficulty scaling  
- loot flavor  

Examples:

- 🌲 forest → evasion, nature magic  
- 🏜️ desert → speed, bleed  
- 🐍 swamp → poison, slow  
- 🏔️ mountain → armor, knockback  
- 🕯️ ruins → curse, fear  
- 🔮 arcane → magic damage  
- ⚫ abyssal → rare, high threat  

---

## 5. ✨ Ability Templates

Abilities are defined as:

- name  
- multiplier  
- tags  

Example templates:

- 🔥 **Brute Smash** — \(M_a = 1.3\), stagger  
- 🩸 **Bleeding Strike** — \(M_a = 1.1\), bleed  
- 🌫️ **Poison Cloud** — AoE DoT  
- 🌀 **Blink Step** — teleport, evasion  

Damage uses your existing formula:

\[
DMG_a = DMG_{\text{base}} \cdot M_a
\]

---

## 6. 💎 Loot Profiles

Loot profiles define:

- rarity bias  
- item tags  
- special drops for elites/bosses  

Zones later use these to build **regional loot tables**.

---

## 7. 🧪 Example Families (Conceptual)

### 🐺 Dire Wolf Pack  
- skirmisher  
- forest biome  
- fast, medium damage  
- abilities: Pounce, Pack Howl, Hamstring  
- loot: pelts, fangs, essence_swiftness  

### 🦴 Bone Legion  
- brute  
- ruins biome  
- high HP + armor  
- abilities: Bone Crush, Shield Wall, Unholy Resilience  
- loot: bone fragments, cursed armor, necrotic essence  

---

# 🧩 **8. JSON Block (Machine‑Readable Layer)**  
*(This is the part you asked to add to the original document.)*

## 📦 Schema

```json
{
  "family_name": "string",
  "tier": "minion | elite | boss | apex",
  "biome_affinity": "forest | desert | swamp | mountain | ruins | arcane | abyssal",
  "level_range": {
    "min": "integer",
    "max": "integer"
  },
  "base_stats": {
    "hp_0": "integer",
    "ap_0": "integer",
    "df_0": "integer",
    "spd_0": "integer"
  },
  "growth": {
    "g_hp": "integer",
    "g_ap": "integer",
    "g_df": "integer",
    "g_spd": "integer"
  },
  "threat_tag": "brute | skirmisher | caster | controller | support | swarm",
  "abilities": [
    {
      "name": "string",
      "multiplier": "float",
      "tags": ["string"]
    }
  ],
  "loot_profile": {
    "rarity_bias": "common | uncommon | rare | epic | legendary",
    "item_tags": ["string"]
  }
}
```

---

## 🐺 Example Payload — Dire Wolf Pack

```json
{
  "family_name": "Dire Wolf Pack",
  "tier": "minion",
  "biome_affinity": "forest",
  "level_range": { "min": 3, "max": 12 },
  "base_stats": { "hp_0": 40, "ap_0": 8, "df_0": 3, "spd_0": 12 },
  "growth": { "g_hp": 6, "g_ap": 2, "g_df": 1, "g_spd": 1 },
  "threat_tag": "skirmisher",
  "abilities": [
    { "name": "Pounce", "multiplier": 1.3, "tags": ["gap-close", "stagger"] },
    { "name": "Pack Howl", "multiplier": 0.0, "tags": ["buff", "pack-synergy"] },
    { "name": "Hamstring", "multiplier": 1.1, "tags": ["slow"] }
  ],
  "loot_profile": {
    "rarity_bias": "common",
    "item_tags": ["pelts", "fangs", "essence_swiftness"]
  }
}
```

---

## 🦴 Example Payload — Bone Legion

```json
{
  "family_name": "Bone Legion",
  "tier": "elite",
  "biome_affinity": "ruins",
  "level_range": { "min": 5, "max": 20 },
  "base_stats": { "hp_0": 60, "ap_0": 10, "df_0": 8, "spd_0": 4 },
  "growth": { "g_hp": 8, "g_ap": 3, "g_df": 2, "g_spd": 0 },
  "threat_tag": "brute",
  "abilities": [
    { "name": "Bone Crush", "multiplier": 1.4, "tags": ["stagger"] },
    { "name": "Shield Wall", "multiplier": 0.0, "tags": ["defense-up"] },
    { "name": "Unholy Resilience", "multiplier": 0.0, "tags": ["self-heal", "curse"] }
  ],
  "loot_profile": {
    "rarity_bias": "uncommon",
    "item_tags": ["bone_fragments", "cursed_armor", "necrotic_essence"]
  }
}
```

---

# 🌈 **Provenance Footer — Monster Family Generator (v1.1)**

```
Artifact: Monster Family Generator (v1.1)
Repository: shared-horizon/healthyambiguity/game-engines/fantasy
Altitude: A5 • Engine Layer • Creature-Ecology Backbone • PRECL-Stable

Purpose:
  Establish a generative template system for monster families within the Fantasy
  Engine Spine. Provides stat baselines, growth curves, biome affinities, threat
  roles, ability templates, and loot profiles. Includes a JSON schema and
  example payloads enabling programmatic integration with zone modeling,
  faction simulation, event engines, and the world-state function W(t).

Membrane:
  Engine-layer. Routable. Safe for IC narrative integration and gameplay
  expansion. No epistemic contamination with NDH-RESEARCH-PILOT.

Anchors:
  - Fantasy Engine Spine (World-State v1.0)
  - Fantasy World-Generation Roadmap (v1.0)
  - Zone Difficulty Model (planned)
  - Faction Simulation Spine (planned)
  - World-State Function W(t)

Maintainer: Borealis S. Hedling
Compiler: Microsoft Copilot
Location: Dublin, Ireland
Timestamp: 06 September 2026 — 23:27 IST
Seal: [ M O N S T E R • F A M I L Y • G E N E R A T O R • v1_1 ]
```

---

