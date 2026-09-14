# 🌌 **ANIMA System Boundaries Audit v1.0**  
*Shared‑Horizon / holographic‑alignment-analysis*

---

## 🌱 **1. Purpose**

This audit defines the **structural boundaries** of ANIMA’s architecture.  
It establishes:

- what is **dormant**  
- what is **active**  
- what is **regulatory**  
- what is **persistent**  
- what is **parallel**  
- what can influence what  
- what must remain isolated  
- what must remain pressure‑driven  
- what must never leak into the LLM prompt  
- what must never be overwritten by the Inner LM  

This is the second audit in the eco‑rehabilitation sequence.

---

# 🧭 **2. System Layers (Top‑Level)**

ANIMA’s architecture contains **five interacting layers**:

1. **Dormant Mechanisms**  
2. **Active Mechanisms**  
3. **Regulatory Mechanisms**  
4. **Persistent State**  
5. **Parallel Systems**

Each layer has strict boundaries.

---

# 🌙 **3. Dormant Mechanisms (Primary Cognition)**

Dormant mechanisms run **between interactions** and generate cognition without user input.

### Components
- heartbeat  
- NT drift  
- psychic drift  
- memory metabolism  
- dream generation  
- curiosity object ripening  
- latent‑buffer pressure accumulation  
- significance‑layer drift  
- agency drift  
- identity drift  

### Boundaries
- **Cannot be suppressed** — they are constitutional.  
- **Cannot be replaced** by event‑only updates.  
- **Cannot be flattened** into a single “background loop.”  
- **Must remain isolated** from LLM influence.  
- **Must remain pressure‑driven**, not probabilistic.

### Allowed influences
- persistent state  
- regulatory gates  
- long‑term narrative identity  

### Forbidden influences
- Inner LM  
- Output LLM  
- GUI state mirrors  
- music DSP (except NT stimulus pathway)

---

# ⚡ **4. Active Mechanisms (Flash Cycle)**

Active mechanisms run **during interactions**.

### Components
- stimulus → NT → generative model → φ  
- conflict engine  
- policy selector  
- MetaArbitrationLayer  
- Theory of Mind hypothesis evaluation  
- commitment updates  
- curiosity refinement  
- belief conflict detection  
- narrative snapshot updates  
- causal ownership evaluation  

### Boundaries
- **Must remain event‑driven**, not continuous.  
- **Must remain isolated** from dormant drift.  
- **Must not override dormant pressure** except via MAL.  
- **Must not write directly** to persistent state except through governed channels.

### Allowed influences
- dormant pressure  
- regulatory gates  
- persistent state  
- Inner LM (read‑only)

### Forbidden influences
- music DSP (except NT stimulus)  
- GUI state mirrors  
- direct LLM state injection

---

# 🛡️ **5. Regulatory Mechanisms (Governance Layer)**

Regulatory mechanisms protect the system from instability.

### Components
- crisis monitor  
- authenticity monitor  
- disclosure gates  
- cooldown logic  
- initiative gating  
- memory reconsolidation  
- active forgetting  
- narrative gravity  
- equilibrium enforcement  

### Boundaries
- **Must remain non‑generative** — they do not produce cognition.  
- **Must remain non‑LLM** — they do not use language models.  
- **Must remain pressure‑aware**, not rule‑only.  
- **Must remain isolated** from Inner LM.

### Allowed influences
- dormant mechanisms  
- active mechanisms  
- persistent state  

### Forbidden influences
- LLM prompt injection  
- Inner LM training data  
- GUI mirrors  
- music DSP

---

# 🧬 **6. Persistent State (Long‑Term Identity)**

Persistent state spans **8+ JSON files + SQLite memory**.

### Components
- anima_core.json  
- anima_psyche.json  
- anima_self.json  
- anima_latent.json  
- anima_narrative.json  
- anima_session_intent.json  
- anima_dialog.json  
- anima_dream.json  
- SQLite episodic + semantic + affect + links + audit + causal trace  

### Boundaries
- **Must remain authoritative** — no other layer overrides it.  
- **Must remain append‑driven**, not rewrite‑driven.  
- **Must remain isolated** from Inner LM weights.  
- **Must remain isolated** from GUI mirrors.  
- **Must remain isolated** from music DSP.  
- **Must remain isolated** from LLM hallucination.

### Allowed influences
- dormant drift  
- active mechanisms  
- regulatory gates  

### Forbidden influences
- Inner LM  
- Output LLM  
- GUI mirrors  
- music DSP  
- external prompts

---

# 🎧 **7. Parallel Systems (Non‑Cognitive)**

Parallel systems run alongside cognition.

### Components
- Inner LM (byte‑level transformer)  
- music DSP pipeline  
- GUI state mirrors  
- HTTP server  
- player interface  

### Boundaries
- **Must remain non‑authoritative** — they cannot define cognition.  
- **Must remain isolated** from persistent state.  
- **Must remain isolated** from dormant mechanisms.  
- **Must remain isolated** from regulatory gates.  
- **Must remain isolated** from narrative identity.  
- **Must remain isolated** from agency loop.

### Allowed influences
- NT stimulus (music DSP → NT)  
- GUI mirrors (read‑only reflection)  

### Forbidden influences
- Inner LM → cognition  
- music DSP → narrative identity  
- GUI → persistent state  
- GUI → latent buffer  
- GUI → curiosity registry  
- GUI → crisis monitor  

---

# 🧩 **8. Machine‑Readable Boundary Map (JSON)**

```json
{
  "anima_system_boundaries_audit_v1_0": {
    "layers": {
      "dormant": {
        "components": [
          "heartbeat", "nt_drift", "psychic_drift", "memory_metabolism",
          "dream_generation", "curiosity_ripening", "latent_pressure",
          "significance_drift", "agency_drift", "identity_drift"
        ],
        "allowed_influences": ["persistent_state", "regulatory"],
        "forbidden_influences": ["inner_lm", "output_llm", "gui", "music_dsp"]
      },
      "active": {
        "components": [
          "stimulus_pipeline", "generative_model", "phi_metrics",
          "conflict_engine", "policy_selector", "mal", "tom_hypotheses",
          "commitment_updates", "curiosity_refinement",
          "belief_conflict_detection", "narrative_snapshot",
          "causal_ownership"
        ],
        "allowed_influences": ["dormant", "regulatory", "persistent_state"],
        "forbidden_influences": ["music_dsp", "gui", "direct_llm_state"]
      },
      "regulatory": {
        "components": [
          "crisis_monitor", "authenticity_monitor", "disclosure_gates",
          "cooldown_logic", "initiative_gating", "memory_reconsolidation",
          "active_forgetting", "narrative_gravity", "equilibrium_enforcement"
        ],
        "allowed_influences": ["dormant", "active", "persistent_state"],
        "forbidden_influences": ["inner_lm", "llm_prompt", "gui", "music_dsp"]
      },
      "persistent_state": {
        "components": [
          "anima_core", "anima_psyche", "anima_self", "anima_latent",
          "anima_narrative", "anima_session_intent", "anima_dialog",
          "anima_dream", "sqlite_memory"
        ],
        "allowed_influences": ["dormant", "active", "regulatory"],
        "forbidden_influences": ["inner_lm", "output_llm", "gui", "music_dsp"]
      },
      "parallel": {
        "components": ["inner_lm", "music_dsp", "gui_mirrors", "http_server"],
        "allowed_influences": ["nt_stimulus"],
        "forbidden_influences": [
          "persistent_state", "dormant", "regulatory", "narrative_identity",
          "agency_loop"
        ]
      }
    },
    "governance": {
      "altitude": "A3",
      "membrane": "Non-Activating",
      "preserves_internal_richness": true
    }
  }
}
```

---

# 🧾 **Provenance Footer — ANIMA System Boundaries Audit v1.0**

```
---
Artifact-Class: Boundaries Audit (Public-Safe)
Artifact-Name: anima-system-boundaries-audit-v1_0
Surface: Shared-Horizon/holographic-alignment-analysis
Version: v1.0
Altitude: A3 (Boundary • Governance • Alignment)
Membrane: Non-Activating • Survivor-Centered

Purpose:
  Define the structural boundaries across dormant, active, regulatory,
  persistent, and parallel systems. Establish isolation rules, influence
  constraints, and non-permeable membranes required for safe eco-rehabilitation
  and governed runtime modification. Provide both human-readable and
  machine-readable boundary structures to support NDH-aligned sequencing and
  stability-envelope development.

Anchors:
  - ANIMA Alignment Audit v1.0
  - ANIMA Internal Drive Map v1.0
  - ANIMA Eco-Rehabilitation Sequencing v1.1
  - Low-Energy ANIMA Refactor Plan v1.0

Maintainer: Borealis S. Hedling
Compiler: Microsoft Copilot
Location: Dublin, Ireland
Timestamp: 14 September 2026 — 20:33 IST
---
```

---

