# NDH Solver Stack Metaschema v1.0  
### Shared‑Horizon • Architecture • Metastructural  
### Altitude Band: A8 (Metaschema)

---

## 1 — Identity block

**Artifact:** NDH Solver Stack Metaschema  
**Version:** 1.0  
**Surface:** Shared‑Horizon / Architecture / Metastructural  
**Mode:** Formal • Metastructural • Non‑Activating  
**Altitude Envelope:** A7–A8  
**Maintainer:** Borealis S. Hedling  
**Purpose:** Define how NDH schemas describe, version, and govern themselves  
**Companion Artifacts:**  
- NDH-Solver-Stack-Schema-v1.0.md  
- NDH Visual Grammar v1.0  
- Ontology & Taxonomy v1.0 + Explainers  

---

## 2 — Purpose of the metaschema

**Goal:** Provide a **schema‑of‑schemas** for the NDH Solver Stack.

The Metaschema defines:

- how schemas are identified  
- how schemas are versioned  
- how schemas declare altitude and lane  
- how schemas bind to visual grammar primitives  
- how schemas expose machine‑readable metadata  
- how schemas participate in governance and sovereignty

It is the **formal contract** that every NDH schema must satisfy.

---

## 3 — Core metaschema concepts

**SchemaIdentity**

- **fields:** `name`, `version`, `namespace`, `altitude`, `lane`  
- **constraints:** `name` unique within `namespace`; `version` semantic (MAJOR.MINOR.PATCH)

**SchemaProvenance**

- **fields:** `author`, `repository`, `file_path`, `created_at`, `updated_at`  
- **constraints:** `file_path` must map to architecture lane; timestamps monotonic

**SchemaVisualBinding**

- **fields:** `altitude_glyph_id`, `lane_shape_id`  
- **constraints:** must reference IDs from NDH Visual Grammar machine‑readable section

**SchemaGovernance**

- **fields:** `sovereignty_tag`, `membrane_tag`, `governance_scope`  
- **constraints:** sovereignty + membrane tags required for A7+ schemas

**SchemaStructure**

- **fields:** `entities`, `relations`, `constraints`  
- **constraints:** entities and relations must be resolvable in Ontology/Taxonomy

---

## 4 — Minimal metaschema instance (canonical form)

```json
{
  "schema_identity": {
    "name": "NDH-Solver-Stack-Schema",
    "version": "1.0.0",
    "namespace": "shared-horizon.architecture",
    "altitude": "A7",
    "lane": "architecture"
  },
  "schema_provenance": {
    "author": "Borealis S. Hedling",
    "repository": "shared-horizon",
    "file_path": "shared-horizon/architecture/schema/NDH-Solver-Stack-Schema-v1.0.md",
    "created_at": "2026-09-05T00:00:00Z",
    "updated_at": "2026-09-05T00:00:00Z"
  },
  "schema_visual_binding": {
    "altitude_glyph_id": "A7",
    "lane_shape_id": "architecture"
  },
  "schema_governance": {
    "sovereignty_tag": "solver",
    "membrane_tag": "neutral",
    "governance_scope": "NDH-Solver-Stack-Core"
  },
  "schema_structure": {
    "entities": [],
    "relations": [],
    "constraints": []
  }
}
```

This is the **canonical metaschema envelope** every NDH schema must satisfy.

---

## 5 — Metaschema rules (high‑level)

- **Rule 1:** Every NDH schema MUST have a `schema_identity` block.  
- **Rule 2:** Every NDH schema MUST bind to NDH Visual Grammar via `schema_visual_binding`.  
- **Rule 3:** Every A7+ schema MUST declare `sovereignty_tag` and `membrane_tag`.  
- **Rule 4:** Every schema MUST be locatable via `schema_provenance.file_path`.  
- **Rule 5:** Every schema’s `entities` and `relations` MUST be consistent with Ontology and Taxonomy.  

---

## 6 — Provenance footer

```text
────────────────────────────────────────────────────────────
Artifact-Class: Metastructural Specification (Markdown)
Artifact-Name: NDH Solver Stack Metaschema v1.0
Surface: Shared-Horizon / Architecture / Metastructural
Version: v1.0
Altitude: A7–A8 (Metaschema)
Membrane: Neutral • Non-Activating • Sovereignty-Preserving

Author: Borealis S. Hedling
Repository: shared-horizon
File: architecture/metastructural/NDH-Solver-Stack-Metaschema-v1.0.md

Commit-Lineage:
    - Added NDH Solver Stack Metaschema v1.0.
    - Defined canonical metaschema envelope for all NDH schemas.
    - Bound metaschema to NDH Visual Grammar machine-readable primitives.
    - Established governance, provenance, and identity requirements for schemas.

Provenance:
    This artifact is formal-only. It does not activate NDH solvers, Serenity
    spectral engines, ANIMA ingestion surfaces, or phenomenology layers. It
    governs how schemas describe and version themselves.

Last-Updated: 05 September 2026 — Dublin, Ireland
────────────────────────────────────────────────────────────
```

