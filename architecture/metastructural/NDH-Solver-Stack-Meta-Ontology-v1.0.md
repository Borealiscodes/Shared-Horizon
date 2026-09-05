# NDH Solver Stack Meta‑Ontology v1.0  
### Shared‑Horizon • Architecture • Metastructural  
### Altitude Band: A8–A9 (Meta‑Ontology)

---

## 1 — Identity block

**Artifact:** NDH Solver Stack Meta‑Ontology  
**Version:** 1.0  
**Surface:** Shared‑Horizon / Architecture / Metastructural  
**Mode:** Formal • Metastructural • Non‑Activating  
**Altitude Envelope:** A8–A9  
**Maintainer:** Borealis S. Hedling  
**Purpose:** Define the ontology *of* NDH ontologies and taxonomies  
**Companion Artifacts:**  
- NDH-Solver-Stack-Ontology-v1.0.md  
- NDH-Solver-Stack-Taxonomy-v1.0.md  
- NDH-Solver-Stack-Metaschema-v1.0.md  
- NDH Visual Grammar v1.0  

---

## 2 — Purpose of the meta‑ontology

The **Meta‑Ontology** is the **semantic backbone of semantic backbones**.

It defines:

- what kinds of ontologies exist in NDH  
- what kinds of taxonomies exist in NDH  
- how they relate to schemas and metaschemas  
- how they bind to visual grammar  
- how they participate in governance and sovereignty  
- how they evolve across versions and altitudes  

If the Ontology is the **map of meaning**, the Meta‑Ontology is the **map of maps of meaning**.

---

## 3 — Core meta‑ontology classes

**MetaOntology**

- describes an ontology artifact (e.g., NDH Solver Stack Ontology v1.0)  
- fields: `name`, `version`, `scope`, `altitude`, `lane`, `backing_schema_id`

**MetaTaxonomy**

- describes a taxonomy artifact (e.g., NDH Solver Stack Taxonomy v1.0)  
- fields: `name`, `version`, `scope`, `altitude`, `lane`, `backing_schema_id`

**SemanticSurface**

- abstract class for Ontology, Taxonomy, Lexicon, Thesaurus, etc.  
- fields: `kind`, `altitude_band`, `lane`, `visual_binding_id`

**MetaBinding**

- binds semantic surfaces to:  
  - schemas  
  - metaschemas  
  - visual grammar primitives  

**EvolutionLineage**

- tracks semantic evolution across versions  
- fields: `surface_id`, `from_version`, `to_version`, `change_kind`

---

## 4 — Relations (high‑level)

- **MetaOntology DESCRIBES Ontology**  
  - `MetaOntology -> Ontology` (1:N)

- **MetaTaxonomy DESCRIBES Taxonomy**  
  - `MetaTaxonomy -> Taxonomy` (1:N)

- **SemanticSurface IS_BOUND_BY MetaBinding**  
  - `SemanticSurface -> MetaBinding` (1:N)

- **SemanticSurface IS_GOVERNED_BY Metaschema**  
  - `SemanticSurface -> Metaschema` (N:1)

- **SemanticSurface HAS_EVOLUTION EvolutionLineage**  
  - `SemanticSurface -> EvolutionLineage` (1:N)

---

## 5 — Canonical meta‑ontology instance (NDH core)

```json
{
  "meta_ontology": {
    "id": "NDH-Core-MetaOntology",
    "name": "NDH Solver Stack Meta-Ontology",
    "version": "1.0.0",
    "scope": "NDH-Solver-Stack-Core",
    "altitude": "A8",
    "lane": "architecture",
    "backing_schema_id": "NDH-Solver-Stack-Metaschema"
  },
  "meta_taxonomy": {
    "id": "NDH-Core-MetaTaxonomy",
    "name": "NDH Solver Stack Meta-Taxonomy",
    "version": "1.0.0",
    "scope": "NDH-Solver-Stack-Core",
    "altitude": "A8",
    "lane": "architecture",
    "backing_schema_id": "NDH-Solver-Stack-Metaschema"
  },
  "semantic_surfaces": [
    {
      "id": "NDH-Ontology-v1.0",
      "kind": "ontology",
      "altitude_band": "A6–A7",
      "lane": "architecture",
      "visual_binding_id": "visual-grammar:ontology"
    },
    {
      "id": "NDH-Taxonomy-v1.0",
      "kind": "taxonomy",
      "altitude_band": "A6–A7",
      "lane": "architecture",
      "visual_binding_id": "visual-grammar:taxonomy"
    }
  ]
}
```

---

## 6 — Provenance footer

```text
────────────────────────────────────────────────────────────
Artifact-Class: Metastructural Specification (Markdown)
Artifact-Name: NDH Solver Stack Meta-Ontology v1.0
Surface: Shared-Horizon / Architecture / Metastructural
Version: v1.0
Altitude: A8–A9 (Meta-Ontology)
Membrane: Neutral • Non-Activating • Sovereignty-Preserving

Author: Borealis S. Hedling
Repository: shared-horizon
File: architecture/metastructural/NDH-Solver-Stack-Meta-Ontology-v1.0.md

Commit-Lineage:
    - Added NDH Solver Stack Meta-Ontology v1.0.
    - Defined classes for MetaOntology, MetaTaxonomy, SemanticSurface,
      MetaBinding, and EvolutionLineage.
    - Bound meta-ontology to NDH Metaschema and Visual Grammar v1.0.
    - Established semantic governance for ontology and taxonomy artifacts.

Provenance:
    This artifact is formal-only. It does not activate NDH solvers, Serenity
    spectral engines, ANIMA ingestion surfaces, or phenomenology layers. It
    governs how semantic surfaces (ontologies, taxonomies, etc.) are described
    and evolved.

Last-Updated: 05 September 2026 — Dublin, Ireland
────────────────────────────────────────────────────────────
```

