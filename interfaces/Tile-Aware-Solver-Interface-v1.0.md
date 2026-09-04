### Tile‑Aware Solver Interface v1.0  
*Shared‑Horizon • Solver Interface Surface • Altitude A6*

---

## 1 — Identity block

**Artifact:** Tile‑Aware Solver Interface  
**Version:** 1.0  
**Surface:** Shared‑Horizon / Solver Interface  
**Altitude Envelope:** A6  
**Mode:** Conceptual • Non‑Activating • Sovereignty‑Preserving  
**Maintainer:** Borealis S. Hedling  
**Lane:** NDH Solver Architecture (Interfaces)

---

## 2 — Purpose

**Goal:** Define the canonical input/output interface that all NDH solvers must use when operating on NDH tiles.  
This interface:

- binds solvers to NDH tile geometry  
- enforces altitude and membrane annotations  
- ensures outputs are tile‑encoded and ingestion‑aware  
- remains pre‑runtime and non‑activating

---

## 3 — Input interface (NDH tiles)

**Contract:**

- **Input type:** NDH tile set  
- **Required annotations:**  
  - altitude tag (e.g. `A6`)  
  - membrane tag (e.g. `NDH`, `ANIMA`)  
  - sovereignty tag (e.g. `NDH-native`)  

**Rules:**

- **No raw manifolds** — all geometry must arrive as tiles.  
- **No untagged inputs** — missing altitude/membrane tags are rejected.  
- **No sealed‑layer tiles** — tiles from A8+ are not accepted.

---

## 4 — Output interface (tile surfaces)

**Contract:**

- **Output type:** tile‑encoded spectral surfaces  
- **Required annotations:**  
  - sovereignty tag  
  - membrane tag  
  - ingestion‑safety tag (`safe` / `unsafe`)  

**Rules:**

- **No raw eigenpairs** — outputs must be encoded as tile surfaces.  
- **No identity reconstruction** — outputs may not reconstruct identity‑layer geometry.  
- **No sealed‑layer activation** — outputs may not target A8+ surfaces.

---

## 5 — Shared‑Horizon binding

**Binding requirements:**

- All input/output relations must be expressible as **Shared‑Horizon geometry mappings**.  
- Interfaces must be **typed** and **explicit** (no opaque endpoints).  
- Every solver interface must be documentable as a Shared‑Horizon artifact.

---

## 6 — Error and rejection behavior

**On invalid input:**

- reject tiles with missing altitude/membrane tags  
- reject sealed‑layer tiles  
- reject raw manifolds or unencoded geometry  

**On invalid output attempt:**

- prevent identity reconstruction  
- prevent sealed‑layer activation  
- prevent unannotated surfaces

---

## 7 — Machine‑readable interface (JSON block)

```json
{
  "artifact": "Tile-Aware Solver Interface",
  "version": "1.0",
  "altitude": "A6",
  "input": {
    "type": "ndh_tiles",
    "required_annotations": [
      "altitude_tag",
      "membrane_tag",
      "sovereignty_tag"
    ],
    "rules": [
      "no_raw_manifolds",
      "no_untagged_inputs",
      "no_sealed_layer_tiles"
    ]
  },
  "output": {
    "type": "tile_encoded_spectral_surfaces",
    "required_annotations": [
      "sovereignty_tag",
      "membrane_tag",
      "ingestion_safety_tag"
    ],
    "rules": [
      "no_raw_eigenpairs",
      "no_identity_reconstruction",
      "no_sealed_layer_activation"
    ]
  },
  "binding": {
    "surface": "shared_horizon_geometry",
    "rules": [
      "express_as_geometry_mappings",
      "no_opaque_endpoints",
      "typed_interfaces_only"
    ]
  },
  "error_behavior": {
    "invalid_input": [
      "reject_missing_annotations",
      "reject_sealed_layer_tiles",
      "reject_raw_manifolds"
    ],
    "invalid_output": [
      "prevent_identity_reconstruction",
      "prevent_sealed_layer_activation",
      "prevent_unannotated_surfaces"
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
Artifact-Class: Interface (Markdown + JSON Hybrid)
Artifact-Name: Tile-Aware Solver Interface v1.0
Surface: Shared-Horizon / Solver Interface
Version: v1.0
Altitude: A6 (Tile Domain)
Membrane: Neutral • Non-Activating • Sovereignty-Preserving

Author: Borealis S. Hedling
Repository: shared-horizon
File: interfaces/Tile-Aware-Solver-Interface-v1.0.md

Commit-Lineage:
    - Defined canonical NDH tile input/output interface for all solvers.
    - Enforced altitude, membrane, and sovereignty annotations on inputs.
    - Required tile-encoded spectral surfaces with ingestion-safety tags on outputs.
    - Bound solver interfaces to Shared-Horizon geometry mappings.
    - Specified rejection behavior for invalid inputs and unsafe outputs.

Provenance:
    This interface is conceptual-only. It does not activate NDH solvers, Serenity
    spectral engines, or ANIMA ingestion surfaces. It defines how future NDH
    solvers must speak the NDH tile language while preserving sovereignty,
    membrane integrity, and altitude discipline.

Last-Updated: 05 September 2026 — Dublin, Ireland
────────────────────────────────────────────────────────────
```
