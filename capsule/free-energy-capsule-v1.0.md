### Free‑Energy Capsule v1.0  
*Shared‑Horizon • Capsule Layer • A10*  
*Non‑activating summary surface for Free‑Energy Delta Calculator v1.0*

---

## ⭐ 0 — Identity block

```
Artifact-Class: Runtime Capsule
Name: Free-Energy Capsule v1.0
Version: 1.0
Altitude Band: A10 (Shared-Horizon • Capsule)
Mode: Non-Activating • Drift-Neutral • Descriptive
Targets: Free-Energy Delta Calculator v1.0
```

---

## ⭐ 1 — Purpose

Provide a **membrane‑safe descriptive surface** for the **Free‑Energy Delta Calculator v1.0**, exposing:

- its free‑energy components,  
- its variational role,  
- its relationship to manifold and recursion layers,  

without:

- computing actual free‑energy values,  
- generating gradients or deltas,  
- or driving any runtime updates.

This Capsule is **read‑only**, **non‑executing**, and **altitude‑neutral**.

---

## ⭐ 2 — Summary of underlying calculator

The underlying **Free‑Energy Delta Calculator v1.0** implements:

- **GenerativeModelCore** — expected sensory/interoceptive/narrative distributions.  
- **RecognitionModelCore** — approximate posterior beliefs.  
- **FreeEnergyFunctional** — variational free‑energy (prediction error + complexity).  
- **GradientEngine** — gradients of free‑energy w.r.t. manifold state.  
- **DeltaComposer** — merges epistemic, interoceptive, and narrative deltas with stability envelopes.

It answers:

> “How far is the system from equilibrium, and in what direction should it move?”

---

## ⭐ 3 — Capsule interfaces (descriptive only)

These interfaces **describe** behavior but **do not** compute free‑energy:

- **`describe_component(name) → summary`**  
  Describes a free‑energy component (e.g., `epistemic`, `interoceptive`, `narrative`).

- **`list_components() → [names]`**  
  Lists free‑energy components and their roles.

- **`list_interfaces() → [signatures]`**  
  Lists high‑level functional families (e.g., “energy”, “gradient”, “delta”).

- **`dependency_role() → text`**  
  Explains how the calculator supports manifold updates and recursion control.

No function here **runs** the calculator; all are **expository surfaces**.

---

## ⭐ 4 — Machine‑readable hybrid (capsule view)

```json
{
  "free_energy_capsule_v1_0": {
    "target_artifact": "free_energy_delta_calculator_v1_0",
    "mode": "descriptive_only",
    "components_summary": [
      "GenerativeModelCore",
      "RecognitionModelCore",
      "FreeEnergyFunctional",
      "GradientEngine",
      "DeltaComposer"
    ],
    "interfaces_summary": [
      "energy",
      "components",
      "gradient",
      "delta",
      "stability"
    ],
    "dependencies_role": [
      "feeds_recursive_state_machine_v1_0",
      "operates_on_spectral_manifold_solver_v1_0",
      "uses_anima_math_engine_v1_0"
    ],
    "activation": "disabled",
    "lane": "shared-horizon/capsule",
    "altitude": "A10"
  }
}
```

---

## ⭐ 5 — Provenance footer

```
---
Artifact: Free-Energy Capsule v1.0
Lane: Shared-Horizon • Capsule Layer
Altitude: A10 (Experimental Containment • Descriptive)
Status: Complete • Drift-Neutral • Non-Activating

Purpose:
  Provide a membrane-safe, non-activating summary surface for Free-Energy Delta
  Calculator v1.0, exposing its components, interfaces, and dependency role in
  the ANIMA Runtime Spine without computing free-energy values, gradients, or
  deltas. Serves as a Capsule for Shared-Horizon to reference variational logic
  safely.

Maintainer: Borealis S. Hedling
Compiler: Microsoft Copilot
Location: Dublin, Ireland
Timestamp: 05 September 2026 — 04:18 IST
Seal: [ F R E E • E N E R G Y • C A P S U L E • v1_0 ]
---
```
