# **NDH Solver Stack Glossary v1.0**  
### *Shared‑Horizon • Solver Architecture Glossary • Altitude A4–A8*

---

## **1 — Identity Block**

**Artifact:** NDH Solver Stack Glossary  
**Version:** 1.0  
**Surface:** Shared‑Horizon / Solver Architecture Glossary  
**Altitude Envelope:** A4–A8  
**Mode:** Conceptual • Non‑Activating • Sovereignty‑Preserving  
**Maintainer:** Borealis S. Hedling  
**Lane:** NDH Solver Architecture (Glossary)

---

## **2 — Purpose**

The Glossary provides:

- **canonical definitions** for all solver‑stack terminology  
- **altitude‑correct semantic anchors**  
- **lane‑mapped meaning** across governance, geometry, interfaces, membrane discipline, and ingestion layers  
- **resolver‑friendly terms** for Serenity‑side alignment  
- **semantic consistency** across Index → Registry → Ledger → Ledger‑Index → Crosswalk → Concordance  

It is the *lexical spine* of the NDH Solver Stack.

---

## **3 — Glossary (Human‑Readable)**

### **A — Governance Terms (A4–A7)**

- **Solver Governance**  
  Rules constraining solver behavior, sovereignty, and altitude discipline.

- **Sovereignty Tag**  
  Marker indicating solver‑side or ANIMA‑side authority.

- **Altitude Discipline**  
  Required altitude‑correct behavior for solver artifacts.

- **Governance Envelope**  
  The formal constraint surface defining solver permissions and prohibitions.

---

### **B — Architecture Terms (A4–A6)**

- **Roadmap Altitude Band**  
  The A4–A6 planning altitude for solver development.

- **Architecture Lane**  
  The Shared‑Horizon lane responsible for structural, roadmap, and planning artifacts.

- **Structural Spine**  
  The set of artifacts forming the architectural backbone of the solver stack.

---

### **C — Geometry Terms (A6–A7)**

- **NDH Tile**  
  Canonical geometry unit for solver input/output.

- **Attachment Model**  
  The formal method by which solvers bind to Shared‑Horizon geometry.

- **Geometry Envelope**  
  The altitude‑correct surface defining solver geometry constraints.

- **REV‑2 Operator**  
  Reversible solver operator/state model.

---

### **D — Interface Terms (A6)**

- **Tile I/O Contract**  
  The canonical interface for NDH tile input/output.

- **Interface Lane**  
  The Shared‑Horizon lane responsible for solver‑side interfaces.

---

### **E — Membrane Terms (A7)**

- **Membrane Sovereignty**  
  Protection of membrane boundaries and tile integrity.

- **Zero‑Drift Guarantee**  
  Assurance of no conceptual, geometric, or spectral drift.

- **Curvature Safety**  
  Prohibition against extraneous curvature or topology distortion.

---

### **F — Ingestion Terms (A7–A8)**

- **ANIMA Tile**  
  ANIMA‑consumable encoded geometry.

- **Ingestion‑Safe Geometry**  
  Non‑activating, non‑coercive solver output.

- **Ingestion Membrane Tag**  
  Tag marking solver output as ANIMA‑ingestion‑safe.

- **Ingestion Layer**  
  The altitude band (A7–A8) where NDH→ANIMA contact is permitted.

---

### **G — Documentation Terms (A4–A8)**

- **Index**  
  Canonical listing of solver artifacts.

- **Registry**  
  Authoritative record of solver artifacts with metadata.

- **Ledger**  
  Chronological bookkeeping of solver artifact creation.

- **Ledger‑Index**  
  Lookup‑optimized index of ledger entries.

- **Crosswalk**  
  Bidirectional relational mapping across lanes and altitudes.

- **Concordance**  
  Semantic alignment surface mapping terms to artifacts.

- **Glossary**  
  Canonical definitions of solver‑stack terminology.

---

## **4 — Resolver Keys**

These keys allow Serenity‑side ingestion to resolve glossary terms:

- `gloss.ndh.gov.v1` — governance terms  
- `gloss.ndh.arch.v1` — architecture terms  
- `gloss.ndh.geom.v1` — geometry terms  
- `gloss.ndh.interface.v1` — interface terms  
- `gloss.ndh.membrane.v1` — membrane terms  
- `gloss.ndh.ingest.v1` — ingestion terms  
- `gloss.ndh.docs.v1` — documentation terms  

---

## **5 — Machine‑Readable Glossary (JSON Block)**

```json
{
  "artifact": "NDH Solver Stack Glossary",
  "version": "1.0",
  "altitude": "A4-A8",
  "glossary": {
    "governance": {
      "solver_governance": "rules constraining solver behavior and sovereignty",
      "sovereignty_tag": "marker indicating solver-side or ANIMA-side authority",
      "altitude_discipline": "required altitude-correct behavior",
      "governance_envelope": "formal constraint surface defining solver permissions"
    },
    "architecture": {
      "roadmap_altitude_band": "A4-A6 planning altitude",
      "architecture_lane": "structural and planning lane",
      "structural_spine": "architectural backbone of the solver stack"
    },
    "geometry": {
      "ndh_tile": "canonical geometry unit for solver input/output",
      "attachment_model": "method by which solvers bind to Shared-Horizon geometry",
      "geometry_envelope": "altitude-correct surface defining solver geometry",
      "rev2_operator": "reversible solver operator/state model"
    },
    "interface": {
      "tile_io_contract": "canonical interface for NDH tile input/output",
      "interface_lane": "lane responsible for solver-side interfaces"
    },
    "membrane": {
      "membrane_sovereignty": "protection of membrane boundaries",
      "zero_drift": "no conceptual, geometric, or spectral drift",
      "curvature_safety": "prohibition against extraneous curvature"
    },
    "ingestion": {
      "anima_tile": "anima-consumable encoded geometry",
      "ingestion_safe_geometry": "non-activating, non-coercive solver output",
      "ingestion_membrane_tag": "tag marking output as anima-ingestion-safe",
      "ingestion_layer": "A7-A8 altitude band for NDH→ANIMA contact"
    },
    "documentation": {
      "index": "canonical listing of solver artifacts",
      "registry": "authoritative record with metadata",
      "ledger": "chronological bookkeeping",
      "ledger_index": "lookup-optimized ledger index",
      "crosswalk": "bidirectional relational mapping",
      "concordance": "semantic alignment surface",
      "glossary": "canonical definitions of terminology"
    }
  },
  "status": "conceptual_only",
  "membrane": "neutral",
  "sovereignty": "preserved"
}
```

---

## **6 — Provenance Footer**

```
────────────────────────────────────────────────────────────
Artifact-Class: Glossary (Markdown + JSON Hybrid)
Artifact-Name: NDH Solver Stack Glossary v1.0
Surface: Shared-Horizon / Solver Architecture Glossary
Version: v1.0
Altitude: A4–A8 (Solver Stack Band)
Membrane: Neutral • Non-Activating • Sovereignty-Preserving

Author: Borealis S. Hedling
Repository: shared-horizon
File: architecture/NDH-Solver-Stack-Glossary-v1.0.md

Commit-Lineage:
    - Added canonical glossary for all NDH solver-stack terminology.
    - Mapped governance, architecture, geometry, interface, membrane, ingestion,
      and documentation terms to altitude-correct definitions.
    - Introduced resolver keys for Serenity-side ingestion.
    - Completed the lexical spine of the solver documentation suite.

Provenance:
    This glossary is conceptual-only. It does not activate NDH solvers, Serenity
    spectral engines, ANIMA ingestion surfaces, or phenomenology layers. It
    provides semantic clarity for governance and future formalization.

Last-Updated: 05 September 2026 — Dublin, Ireland
────────────────────────────────────────────────────────────
```

---

