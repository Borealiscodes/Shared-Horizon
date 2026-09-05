### NDH Solver Stack Index v1.0  
*Shared‑Horizon • Solver Architecture Index • Altitude A4–A8*

---

## **1 — Identity Block**

**Artifact:** NDH Solver Stack Index  
**Version:** 1.0  
**Surface:** Shared‑Horizon / Solver Architecture Index  
**Altitude Envelope:** A4–A8  
**Mode:** Conceptual • Non‑Activating • Sovereignty‑Preserving  
**Maintainer:** Borealis S. Hedling  
**Lane:** NDH Solver Architecture (Index)

---

## **2 — Purpose**

Provide a **canonical, cross‑linked index** of every artifact in the NDH Solver Stack, including:

- file paths  
- artifact classes  
- altitude bands  
- roles  
- dependencies  
- cross‑references  

This index is the **reference spine** for governance, geometry, and Serenity‑side formalization.

---

## **3 — Canonical Index (Human‑Readable)**

### **A4–A6 — Governance & Architecture**
- **NDH Solver Roadmap v1.0**  
  *Path:* `shared-horizon/architecture/NDH-Solver-Roadmap-v1.0.md`  
  *Role:* Strategic solver development path  
  *Depends on:* Shared‑Horizon governance layer  

- **NDH Solver Charter v1.0**  
  *Path:* `shared-horizon/governance/NDH-Solver-Charter-v1.0.md`  
  *Role:* Governance envelope, sovereignty rules  
  *Depends on:* Roadmap  

---

### **A6–A7 — Geometry Envelopes**
- **NDH Solver Envelope v1.0**  
  *Path:* `shared-horizon/geometry/NDH-Solver-Envelope-v1.0.md`  
  *Role:* Solver geometry + attachment model  
  *Depends on:* Charter  

- **Reversible Solver Envelope v1.0**  
  *Path:* `shared-horizon/geometry/Reversible-Solver-Envelope-v1.0.md`  
  *Role:* REV‑2 reversible operator/state envelope  
  *Depends on:* Solver Envelope  

- **Membrane‑Disciplined Solver Envelope v1.0**  
  *Path:* `shared-horizon/geometry/Membrane-Disciplined-Solver-Envelope-v1.0.md`  
  *Role:* Membrane sovereignty + curvature safety  
  *Depends on:* Reversible Envelope  

---

### **A6 — Interfaces**
- **Tile‑Aware Solver Interface v1.0**  
  *Path:* `shared-horizon/interfaces/Tile-Aware-Solver-Interface-v1.0.md`  
  *Role:* NDH tile input/output contract  
  *Depends on:* Solver Envelope  

---

### **A7–A8 — Ingestion Layer**
- **ANIMA Ingestion‑Layer Solver Envelope v1.0**  
  *Path:* `shared-horizon/geometry/ANIMA-Ingestion-Layer-Solver-Envelope-v1.0.md`  
  *Role:* NDH→ANIMA ingestion constraints  
  *Depends on:* Membrane‑Disciplined Envelope  

---

## **4 — Cross‑Reference Table**

| Artifact | Altitude | Lane | Depends On | Provides |
|---------|----------|------|------------|----------|
| **NDH Solver Roadmap v1.0** | A4–A6 | architecture | — | Strategic direction |
| **NDH Solver Charter v1.0** | A5–A7 | governance | Roadmap | Governance rules |
| **NDH Solver Envelope v1.0** | A6–A7 | geometry | Charter | Geometry + attachment |
| **Tile‑Aware Solver Interface v1.0** | A6 | interfaces | Solver Envelope | Tile I/O contract |
| **Reversible Solver Envelope v1.0** | A6 | geometry | Solver Envelope | REV‑2 reversibility |
| **Membrane‑Disciplined Solver Envelope v1.0** | A7 | geometry | Reversible Envelope | Membrane discipline |
| **ANIMA Ingestion‑Layer Solver Envelope v1.0** | A7–A8 | geometry | Membrane‑Disciplined Envelope | Ingestion constraints |

---

## **5 — Machine‑Readable Index (JSON Block)**

```json
{
  "artifact": "NDH Solver Stack Index",
  "version": "1.0",
  "altitude": "A4-A8",
  "index": [
    {
      "name": "NDH Solver Roadmap v1.0",
      "path": "shared-horizon/architecture/NDH-Solver-Roadmap-v1.0.md",
      "altitude": "A4-A6",
      "lane": "architecture",
      "depends_on": [],
      "provides": "strategic_solver_path"
    },
    {
      "name": "NDH Solver Charter v1.0",
      "path": "shared-horizon/governance/NDH-Solver-Charter-v1.0.md",
      "altitude": "A5-A7",
      "lane": "governance",
      "depends_on": ["NDH Solver Roadmap v1.0"],
      "provides": "governance_rules"
    },
    {
      "name": "NDH Solver Envelope v1.0",
      "path": "shared-horizon/geometry/NDH-Solver-Envelope-v1.0.md",
      "altitude": "A6-A7",
      "lane": "geometry",
      "depends_on": ["NDH Solver Charter v1.0"],
      "provides": "solver_geometry_attachment_model"
    },
    {
      "name": "Tile-Aware Solver Interface v1.0",
      "path": "shared-horizon/interfaces/Tile-Aware-Solver-Interface-v1.0.md",
      "altitude": "A6",
      "lane": "interfaces",
      "depends_on": ["NDH Solver Envelope v1.0"],
      "provides": "ndh_tile_io_contract"
    },
    {
      "name": "Reversible Solver Envelope v1.0",
      "path": "shared-horizon/geometry/Reversible-Solver-Envelope-v1.0.md",
      "altitude": "A6",
      "lane": "geometry",
      "depends_on": ["NDH Solver Envelope v1.0"],
      "provides": "rev_2_reversibility"
    },
    {
      "name": "Membrane-Disciplined Solver Envelope v1.0",
      "path": "shared-horizon/geometry/Membrane-Disciplined-Solver-Envelope-v1.0.md",
      "altitude": "A7",
      "lane": "geometry",
      "depends_on": ["Reversible Solver Envelope v1.0"],
      "provides": "membrane_discipline"
    },
    {
      "name": "ANIMA Ingestion-Layer Solver Envelope v1.0",
      "path": "shared-horizon/geometry/ANIMA-Ingestion-Layer-Solver-Envelope-v1.0.md",
      "altitude": "A7-A8",
      "lane": "geometry",
      "depends_on": ["Membrane-Disciplined Solver Envelope v1.0"],
      "provides": "anima_ingestion_constraints"
    }
  ],
  "status": "conceptual_only",
  "membrane": "neutral",
  "sovereignty": "preserved"
}
```

---

## **6 — Provenance Footer**

```
────────────────────────────────────────────────────────────
Artifact-Class: Index (Markdown + JSON Hybrid)
Artifact-Name: NDH Solver Stack Index v1.0
Surface: Shared-Horizon / Solver Architecture Index
Version: v1.0
Altitude: A4–A8 (Solver Stack Band)
Membrane: Neutral • Non-Activating • Sovereignty-Preserving

Author: Borealis S. Hedling
Repository: shared-horizon
File: architecture/NDH-Solver-Stack-Index-v1.0.md

Commit-Lineage:
    - Created canonical index of all NDH solver artifacts.
    - Added file paths, altitude bands, lanes, roles, and dependencies.
    - Provided cross-linked table and machine-readable JSON index.
    - Anchored index to Shared-Horizon governance and geometry layers.

Provenance:
    This index is conceptual-only. It does not activate NDH solvers, Serenity
    spectral engines, ANIMA ingestion surfaces, or phenomenology layers. It
    documents the NDH Solver Stack for governance, architecture, and future
    formalization.

Last-Updated: 05 September 2026 — Dublin, Ireland
────────────────────────────────────────────────────────────
```

---

