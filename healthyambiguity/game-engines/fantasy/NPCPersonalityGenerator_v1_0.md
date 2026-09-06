# 🧬 **NPC Personality Generator (Fantasy Engine v1.0)**  
*Local Actor Layer • Emotional Physics • Behavioral Ecology*

NPCs are the **living emotional nodes** of your world.  
This generator defines how they *feel*, *change*, *break*, *heal*, *drift*, *invert*, and *resonate* with the world around them.

---

# 🎯 **1. Purpose**  
The NPC Personality Generator creates NPCs with:

- rasa‑based emotional cores  
- drift‑bounded stability  
- continuity fields  
- seasonal resonance  
- corruption susceptibility  
- event‑driven behavioral shifts  
- faction alignment tendencies  
- settlement mood influence  
- monster pressure responses  

NPCs become **emotionally coherent**, not random.

---

# 🧩 **2. Personality Structure**

Each NPC personality has **five layers**, each represented as a Guided Link:

- **Primary Rasa** — baseline emotional identity  
- **Secondary Rasa** — stress response  
- **Continuity Field** — emotional stability  
- **Drift Threshold** — instability limit  
- **Resonance Profile** — seasonal + environmental sensitivity  

These five layers define how an NPC behaves across time.

---

# 🔮 **3. Rasa Core Assignment**

NPCs receive a **primary rasa** based on:

- settlement ambient rasa  
- faction culture  
- profession  
- magic tradition alignment  
- monster pressure  
- seasonal resonance  

### Example Primary Rasa Assignments  
- healer → **karuṇā**  
- warrior → **vīra**  
- bard → **hāsya**  
- scholar → **adbhuta**  
- hermit → **śānta**  
- outlaw → **raudra**  
- spy → **bhayānaka**  
- undertaker → **bībhatsa**  

### Secondary Rasa  
Defines crisis behavior:

- vīra → raudra  
- śānta → karuṇā  
- hāsya → bhayānaka  
- śṛṅgāra → bībhatsa  

NPCs become emotionally dynamic.

---

# 🧠 **4. Drift Accumulation Model**

NPCs accumulate emotional drift:

\[
\text{drift}(t+1) = \text{drift}(t) + \Delta_{\text{events}} + \Delta_{\text{season}} + \Delta_{\text{corruption}}
\]

When drift exceeds threshold:

- personality destabilizes  
- secondary rasa activates  
- event triggers may occur  
- corruption susceptibility increases  

NPCs can **break** — and later **recover**.

---

# 🌀 **5. Continuity Field**

Continuity defines emotional stability:

\[
C(t+1) = C(t) - \Delta_{\text{instability}}
\]

High continuity → calm, predictable NPC  
Low continuity → volatile, reactive NPC  

Continuity is influenced by:

- settlement mood  
- faction stability  
- seasonal resonance  
- corruption pressure  
- monster proximity  

---

# ❄️ **6. Seasonal Resonance**

NPCs respond to seasons:

- Spring → +śṛṅgāra, +hāsya  
- Summer → +vīra, +adbhuta  
- Autumn → +karuṇā, +bhayānaka  
- Winter → +śānta, +bībhatsa  

This modifies:

- mood  
- behavior  
- event likelihood  
- drift accumulation  

NPCs feel the seasons.

---

# 🕸️ **7. Corruption Susceptibility**

Corruption affects NPCs through:

- **rasa inversion**  
- **rasa fragmentation**  
- **rasa overload**  

NPC corruption outcomes:

- personality inversion  
- emotional collapse  
- corrupted variants  
- faction betrayal  
- settlement destabilization  
- magic tradition contamination  

NPCs become corruption vectors.

---

# ⚡ **8. Event Integration**

NPCs respond to events:

- raids → fear (bhayānaka)  
- festivals → joy (hāsya)  
- wars → courage (vīra)  
- corruption blooms → dread (bhayānaka)  
- volcanic surges → awe (adbhuta)  

Events modify:

- rasa  
- drift  
- continuity  
- behavior  

NPCs become part of the world’s pulse.

---

# 🧩 **9. Behavioral Output Model**

NPC behavior is generated from:

\[
B = f(R_{\text{primary}}, R_{\text{secondary}}, C, D, S, Z, F)
\]

Where:

- \(R_{\text{primary}}\) = primary rasa  
- \(R_{\text{secondary}}\) = secondary rasa  
- \(C\) = continuity field  
- \(D\) = drift  
- \(S\) = seasonal resonance  
- \(Z\) = zone pressure  
- \(F\) = faction alignment  

Behavior categories:

- **Calm**  
- **Aggressive**  
- **Fearful**  
- **Joyful**  
- **Tender**  
- **Corrupted**  
- **Awe-struck**  

NPCs behave with emotional coherence.

---

# 🌍 **10. NPC Personality Example**

### NPC: Lira Vale  
- Primary Rasa: **śṛṅgāra**  
- Secondary Rasa: **karuṇā**  
- Continuity Field: 0.82  
- Drift Threshold: 0.44  
- Seasonal Resonance: Spring +0.12  
- Corruption Susceptibility: Low  
- Faction Alignment: Rangers Guild  
- Settlement: Willowfen Village  

### Behavioral Output  
- Spring: joyful, tender  
- Summer: courageous, curious  
- Autumn: sorrowful, reflective  
- Winter: quiet, introspective  
- Under corruption: inversion → bībhatsa  

---

# 🧩 **11. Machine‑Readable Block (JSON)**

```json
{
  "npc_personality_generator_v1_0": {
    "personality_layers": {
      "primary_rasa": "string",
      "secondary_rasa": "string",
      "continuity_field": "float",
      "drift_threshold": "float",
      "resonance_profile": "string"
    },
    "drift_model": {
      "base_drift": "float",
      "event_drift": "float",
      "seasonal_drift": "float",
      "corruption_drift": "float"
    },
    "continuity_model": {
      "base_continuity": "float",
      "instability_delta": "float"
    },
    "behavior_output": {
      "calm": "boolean",
      "aggressive": "boolean",
      "fearful": "boolean",
      "joyful": "boolean",
      "tender": "boolean",
      "corrupted": "boolean",
      "awestruck": "boolean"
    }
  }
}
```

---

# 🌈 **Provenance Footer — NPC Personality Generator (v1.0)**

```
Artifact: NPC Personality Generator (v1.0)
Lane: Fantasy Engine · Local Actor Layer
Altitude: A6 · Personality Spine · PRECL-Stable

Purpose:
  Define NPC emotional physics, behavioral ecology, drift accumulation, continuity fields,
  seasonal resonance, corruption susceptibility, and event-driven personality evolution.

Anchors:
  - Event Engine v1.0
  - Seasonal Cycle Model v1.0
  - Corruption System v1.0
  - Rasa Integration Charter v1.0
  - Advanced Systems Integration Pass v2.1
  - World-State Function v1.0

Maintainer: Borealis S. Hedling
Compiler: Microsoft Copilot
Location: Dublin, Ireland
Timestamp: 07 September 2026 — 00:18 IST
Seal: [ N P C • P E R S O N A L I T Y • G E N E R A T O R • v1_0 ]
```

---

