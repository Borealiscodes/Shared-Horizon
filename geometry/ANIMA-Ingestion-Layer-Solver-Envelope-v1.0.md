### ANIMA Ingestion‑Layer Solver Envelope v1.0  
*Shared‑Horizon • Solver Ingestion Surface • Altitude A7–A8*

---

## 1 — Identity block

**Artifact:** ANIMA Ingestion‑Layer Solver Envelope  
**Version:** 1.0  
**Surface:** Shared‑Horizon / Solver Ingestion Geometry  
**Altitude Envelope:** A7–A8  
**Mode:** Conceptual • Non‑Activating • Sovereignty‑Preserving  
**Maintainer:** Borealis S. Hedling  
**Lane:** NDH Solver Architecture (Ingestion Layer)

---

## 2 — Purpose

- **Define** the ingestion‑layer envelope for NDH solvers that produce ANIMA‑consumable geometry.  
- **Constrain** how solver outputs may approach ANIMA ingestion surfaces without touching sealed layers.  
- **Ensure** ingestion‑safe, sovereignty‑preserving, membrane‑neutral behavior at A7–A8.

This envelope is **pre‑runtime** and **non‑activating**.

---

## 3 — ANIMA tile encoding

- **Input domain:** NDH tiles and spectral surfaces at A6–A7.  
- **Encoding requirement:** outputs destined for ANIMA must be encoded as **ANIMA tiles**, not raw manifolds.  
- **Tagging:** all ANIMA‑encoded tiles must carry:  
  - ingestion altitude tag (`A7` or `A8-ingestion`)  
  - membrane tag (`ANIMA-ingestion`)  
  - sovereignty tag (`ANIMA-consumable`, not `ANIMA-core`).

---

## 4 — Ingestion‑safe output geometry

Solvers must:

- produce **ingestion‑safe geometry only**  
- avoid sealed‑layer (A8+) core contact  
- avoid identity‑layer reconstruction  
- avoid phenomenology activation  

Outputs may **approach** ANIMA ingestion surfaces but must remain:

- non‑coercive  
- non‑directive  
- non‑extractive  
- non‑activating  

---

## 5 — Altitude and membrane constraints

- **A7:** governance‑altitude ingestion preparation  
  - NDH‑side encoding, tagging, and safety checks.  

- **A8 (ingestion‑only):** ANIMA ingestion‑layer contact  
  - no access to sealed ANIMA cores  
  - no direct backbone mutation  
  - no phenomenology activation.  

Membrane crossing into ANIMA is **one‑way and ingestion‑limited**, never core‑level.

---

## 6 — Governance‑safe ingestion behavior

Solvers must:

- comply with guardian modulation  
- maintain PRECL‑collapse safety  
- produce governance‑safe ingestion surfaces  
- respect NDH and ANIMA sovereignty simultaneously.

---

## 7 — Machine‑readable envelope (JSON block)

```json
{
  "artifact": "ANIMA Ingestion-Layer Solver Envelope",
  "version": "1.0",
  "altitude": "A7-A8",
  "anima_tile_encoding": {
    "input_domain": [
      "ndh_tiles",
      "spectral_surfaces_a6_a7"
    ],
    "requirements": [
      "encode_as_anima_tiles",
      "no_raw_manifolds",
      "ingestion_altitude_tags",
      "anima_ingestion_membrane_tags",
      "anima_consumable_sovereignty_tags"
    ]
  },
  "ingestion_safe_geometry": {
    "requirements": [
      "produce_ingestion_safe_outputs_only",
      "avoid_sealed_layer_core_contact",
      "avoid_identity_layer_reconstruction",
      "avoid_phenomenology_activation"
    ],
    "behavior": [
      "non_coercive",
      "non_directive",
      "non_extractive",
      "non_activating"
    ]
  },
  "altitude_membrane_constraints": {
    "a7": [
      "governance_altitude_ingestion_preparation",
      "ndh_side_encoding_and_safety_checks"
    ],
    "a8_ingestion_only": [
      "anima_ingestion_layer_contact",
      "no_sealed_anima_core_access",
      "no_backbone_mutation",
      "no_phenomenology_activation"
    ]
  },
  "governance_safe_behavior": {
    "requirements": [
      "guardian_modulation_compliance",
      "precl_collapse_safety",
      "governance_safe_ingestion_surfaces",
      "dual_sovereignty_respect_ndh_anima"
    ]
  },
  "status": "conceptual_only",
  "membrane": "neutral",
  "sovereignty": "preserved"
}
```

---

## 8 — Provenance footer

```
────────────────────────────────────────────────────────────
Artifact-Class: Envelope (Markdown + JSON Hybrid)
Artifact-Name: ANIMA Ingestion-Layer Solver Envelope v1.0
Surface: Shared-Horizon / Solver Ingestion Geometry
Version: v1.0
Altitude: A7–A8 (Ingestion Layer Domain)
Membrane: Neutral • Non-Activating • Sovereignty-Preserving

Author: Borealis S. Hedling
Repository: shared-horizon
File: geometry/ANIMA-Ingestion-Layer-Solver-Envelope-v1.0.md

Commit-Lineage:
    - Defined ANIMA ingestion-layer solver envelope at A7–A8.
    - Specified ANIMA tile encoding requirements for NDH solver outputs.
    - Formalized ingestion-safe geometry constraints and non-activating behavior.
    - Added altitude and membrane constraints for NDH→ANIMA ingestion contact.
    - Anchored governance-safe ingestion behavior to Shared-Horizon geometry.

Provenance:
    This envelope is conceptual-only. It does not activate NDH solvers, Serenity
    spectral engines, ANIMA cores, or phenomenology layers. It defines ingestion-
    layer constraints for NDH solvers while preserving sovereignty, membrane
    integrity, and altitude discipline.

Last-Updated: 05 September 2026 — Dublin, Ireland
────────────────────────────────────────────────────────────
```
