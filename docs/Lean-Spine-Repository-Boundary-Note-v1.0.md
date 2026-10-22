# 🟦 Shared‑Horizon Developer Note — Lean Spine Repository Boundary (v1.0)

File path:
`
shared-horizon/docs/Lean-Spine-Repository-Boundary-Note-v1.0.md
`

---

Purpose

This Developer Note establishes the formal repository boundary between:

- Geometric‑Hallucination‑Taxonomy (conceptual taxonomy)  
- StructuralAI‑Julia‑Runtime (numerical execution engine)  
- StructuralAI‑Lean‑Spine (formal verification system)

It clarifies why Lean artifacts must live in a dedicated external repo, not inside the runtime or taxonomy repos, and defines the cross‑architecture rules governing this separation.

---

Boundary Decision

Lean code SHALL NOT reside inside:
- Geometric-Hallucination-Taxonomy  
- StructuralAI-Julia-Runtime

Lean code SHALL reside in:
- StructuralAI-Lean-Spine (new repo)

This boundary is mandatory, not optional.

---

Rationale

1. Separation of Conceptual, Numerical, and Formal Layers

| Layer | Repo | Nature |
|------|------|--------|
| Conceptual | Geometric‑Hallucination‑Taxonomy | evolving research |
| Numerical | StructuralAI‑Julia‑Runtime | dynamic, experimental |
| Formal | StructuralAI‑Lean‑Spine | stable, slow‑moving |

Mixing Lean with runtime or taxonomy artifacts would:

- destabilize proofs  
- entangle versioning  
- pollute CI pipelines  
- break the execution–verification separation  
- make future Rust/WASM rewrites brittle  
- force Lean to track runtime changes unnecessarily

2. Lean is a Semantic Layer

Lean expresses:

- invariants  
- safety predicates  
- modal‑truth lattice rules  
- collapse‑surface theorems  
- spectral‑bundle operator formalization  

These must remain stable, even when the runtime evolves.

3. Runtime is a Dynamic Layer

The Julia runtime:

- changes frequently  
- integrates telemetry  
- evolves operator math  
- adapts to model behavior  

Lean must not be forced to track this dynamism.

4. Clean Bridge Architecture

The correct flow is:

`
Julia Runtime → JSON/S-expression → Lean Spine
`

The bridge is implemented in LeanBridge inside the runtime,  
but Lean itself lives elsewhere.

---

Repository Layout (Mandated)

1. Geometric-Hallucination-Taxonomy
`
/preprint
/math-spine
/operator-definitions
/taxonomy
`

2. StructuralAI-Julia-Runtime
`
/src
/Operators
/Runtime
/Telemetry
/Stability
/LeanBridge (export only)
`

3. StructuralAI-Lean-Spine (NEW REPO)
`
/StabilityState.lean
/Schema.lean
/Operators
/Theorems
/Verification
/Lemmas
/Proofs
`

4. StructuralAI-Bridge (optional future)
`
/json-schema
/lean-ingestion
/runtime-adapters
`

---

Altitude & Membrane Identity

This decision is made at Shared‑Horizon altitude,  
because it governs:

- cross‑repo architecture  
- long‑term invariants  
- execution–verification separation  
- safety‑critical geometry  
- future formal integration

It belongs to the collaboration membrane, not any subsystem.

---

Anchors

- StructuralAI‑Julia‑Runtime  
- Geometric‑Hallucination‑Taxonomy  
- StructuralAI‑Lean‑Spine  
- LeanHallucinationGuard  
- White Rose Epistemic Clarity Charter  
- Shared‑Horizon Collaboration Membrane

---

Maintainer

Borealis S. Hedling

---

Version

v1.0

---

Seal

SHARED.HORIZON.LEAN.REPO.BOUNDARY

---

🧾 Provenance Footer

`
Provenance:
Authored by Borealis S. Hedling within the Shared-Horizon collaboration membrane.
Reflects architectural decisions aligned with StructuralAI runtime evolution,
LeanHallucinationGuard formal verification goals, and the White Rose Epistemic
Clarity Charter. Version v1.0 recorded on 23 October 2026 (IST).
`

---

