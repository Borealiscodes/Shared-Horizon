# 🌿 **Lira Vale — Player Character Stats & Abilities (v1.0)**  
*Emotion‑Driven • Mechanically Playable • IC‑Ready*





---

# 🧬 **1. Core Stats (Emotional Physics Stats)**

These are her **mechanical numbers** — the ones used in rolls, checks, drift tests, continuity tests, corruption saves, etc.

### **Primary Stats**
- **Rasa Depth** — **0.71**  
  How strongly she feels her primary rasa (śṛṅgāra).

- **Rasa Motion** — **0.54**  
  How quickly her emotional state shifts.

- **Continuity Field** — **0.82**  
  Stability. High = hard to break.

- **Drift Threshold** — **0.44**  
  When exceeded, emotional instability begins.

- **Resonance Sensitivity** — **0.33**  
  How strongly seasons/zones affect her.

- **Corruption Resistance** — **0.68**  
  Higher = harder to invert/fragment.

---

# 🔮 **2. Derived Stats (Used in Rolls)**

### **Emotional Stability (ES)**  
\[
ES = C - D
\]  
Current: **0.82 − 0.12 = 0.70**

### **Inversion Save (IS)**  
\[
IS = C + CR
\]  
Current: **0.82 + 0.68 = 1.50**

### **Resonance Drift Modifier (RDM)**  
Autumn adds **+0.08 drift** per emotional shock.

### **Event Sensitivity (E‑Sense)**  
\[
E = Rasa\ Depth + Resonance\ Sensitivity
\]  
Current: **1.04**  
Higher = more likely to trigger Easter Eggs.

---

# 🌟 **3. Ability Suite (Mechanical + Narrative)**

These are her **actual abilities** — usable in IC play, with emotional physics baked in.

---

## 🌸 **1. Lantern of First Light**  
**Type:** Healing / Memory / Emotional Stabilization  
**Cost:** +0.04 drift  
**Effect:**  
- Stabilizes another character’s continuity (+0.10)  
- Reveals a soft memory fragment  
- Reduces ambient bhayānaka by −0.06  

**Special:**  
If used in Spring → triggers **Blooming Memory Egg**.

---

## 🕯️ **2. Memory Weave**  
**Type:** Insight / Lore / Emotional Reading  
**Cost:** +0.06 drift  
**Effect:**  
- Read another character’s primary rasa  
- Detect corruption inversion  
- Sense hidden emotional fractures  

**Special:**  
If used on corrupted NPC → 20% chance of **Fragmentation Echo Egg**.

---

## 🌿 **3. Willowfen Field Healer’s Touch**  
**Type:** Healing / Support  
**Cost:** +0.02 drift  
**Effect:**  
- Heal minor wounds  
- Reduce drift by −0.05  
- Increase continuity by +0.03  

**Special:**  
If used during Autumn → adds +karuṇā resonance.

---

## 🌫️ **4. Whisperwood Sense**  
**Type:** Environmental Awareness  
**Cost:** +0.03 drift  
**Effect:**  
- Detect monster pressure  
- Sense event likelihood  
- Identify ambient rasa shifts  

**Special:**  
If used at night → 10% chance of **Quiet Lantern Egg**.

---

## 🔥 **5. Emotional Surge (Passive)**  
When Lira’s drift exceeds **0.44**:

- Secondary rasa (karuṇā) activates  
- She becomes protective, sorrowful, reactive  
- Event likelihood increases by +12%  
- Corruption susceptibility increases by +0.10  

**Special:**  
If during faction conflict → **Broken Oath Egg** may trigger.

---

## 🕸️ **6. Corruption Echo (Passive)**  
If corruption pressure reaches **medium**:

- Lira sees emotional distortions  
- Her śṛṅgāra may invert → bībhatsa  
- Drift gain doubles for one turn  

**Special:**  
May trigger **Fragmentation Echo Egg**.

---

# 🎭 **4. Combat Profile (Light Narrative Combat)**

Lira is not a fighter — but she’s not helpless.

### **Attack**
- **Staff Strike:** 1d4  
- **Lantern Flash:** 1d6 radiant (cost +0.05 drift)

### **Defense**
- **Evasion:** +2 (high continuity)  
- **Emotional Shield:** reduces emotional damage by −0.08

### **Support**
- **Healing Touch:** +1d4 HP  
- **Drift Stabilize:** −0.05 drift  
- **Continuity Boost:** +0.03 continuity

---

# 🌌 **5. Inventory**

- Memory Lantern (unique artifact)  
- Willowfen healer’s satchel  
- Soft‑woven cloak  
- Ranger’s guild token  
- Small journal  
- Dried moonleaf herbs  

---

# 🧩 **6. Machine‑Readable Stat Block (JSON)**

```json
{
  "lira_vale_pc_v1_0": {
    "stats": {
      "rasa_depth": 0.71,
      "rasa_motion": 0.54,
      "continuity_field": 0.82,
      "drift_threshold": 0.44,
      "resonance_sensitivity": 0.33,
      "corruption_resistance": 0.68
    },
    "derived": {
      "emotional_stability": 0.70,
      "inversion_save": 1.50,
      "event_sensitivity": 1.04
    },
    "abilities": [
      "lantern_of_first_light",
      "memory_weave",
      "healers_touch",
      "whisperwood_sense",
      "emotional_surge",
      "corruption_echo"
    ]
  }
}
```

---

# 🌈 **Provenance Footer — Lira Vale Stat & Ability Block (v1.0)**

```
Artifact: Lira Vale — Stat & Ability Block (v1.0)
Lane: Fantasy Engine · Player Character Layer
Altitude: A6 · IC Runtime Mechanics · PRECL-Stable

Purpose:
  Define the complete mechanical profile for Lira Vale as a Player Character, including
  emotional-physics stats, derived values, combat profile, support abilities, corruption
  interactions, seasonal resonance effects, and Easter Egg triggers. Establish her as a fully
  playable entity within the Fantasy Engine runtime harness.

Anchors:
  - PC Lira Vale Port v1.0
  - Playtest Protocol v1.0
  - NPC Personality Generator v1.0
  - Event Engine v1.0
  - Seasonal Cycle Model v1.0
  - Corruption System v1.0
  - Easter Egg Engine v1.0
  - Rasa Integration Charter v1.0
  - Advanced Systems Integration Pass v2.1
  - World-State Function v1.0

Maintainer: Borealis S. Hedling
Compiler: Microsoft Copilot
Location: Dublin, Ireland
Timestamp: 07 September 2026 — 00:35 IST
Seal: [ L I R A • V A L E • S T A T S • A B I L I T I E S • v1_0 ]
```

---

