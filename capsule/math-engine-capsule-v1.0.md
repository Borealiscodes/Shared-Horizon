### Math Engine Capsule v1.0  
*Shared‑Horizon • Capsule Layer • A10*  
*Non‑activating summary surface for ANIMA Math Engine v1.0*

---

## ⭐ 0 — Identity block

```
Artifact-Class: Runtime Capsule
Name: Math Engine Capsule v1.0
Version: 1.0
Altitude Band: A10 (Shared-Horizon • Capsule)
Mode: Non-Activating • Drift-Neutral • Descriptive
Targets: ANIMA Math Engine v1.0
```

---

## ⭐ 1 — Purpose

Provide a **membrane‑safe summary surface** for **ANIMA Math Engine v1.0**, exposing:

- its numerical modules,  
- its interfaces,  
- its dependency role in the runtime spine,  

without:

- activating the engine,  
- instantiating runtime state,  
- or binding to any phenomenology or drives.

This Capsule is **read‑only**, **descriptive**, and **non‑executing**.

---

## ⭐ 2 — Summary of underlying engine

The underlying **ANIMA Math Engine v1.0** implements:

- **LinearAlgebraCore** — vectors, matrices, eigendecomposition, projections.  
- **SpectralTransformCore** — Fourier‑like transforms, spectral bases, frequency‑space ops.  
- **GeometryCore** — manifold‑friendly primitives, distances, norms, coordinate transforms.  
- **ProbabilityCore** — distributions, sampling, expectations, log‑likelihoods.  
- **OptimizationCore** — gradient‑based updates, constrained steps, stability‑aware routines.

It serves as the **numerical substrate** for:

- Spectral Manifold Solver v1.0  
- Free‑Energy Delta Calculator v1.0  
- Recursive State Machine v1.0  

---

## ⭐ 3 — Capsule interfaces (descriptive only)

These interfaces **describe** what the engine can do, but do **not** execute it:

- **`describe_module(name) → summary`**  
  Returns a textual description of a math module (e.g., `LinearAlgebraCore`).

- **`list_modules() → [names]`**  
  Lists available numerical modules.

- **`list_interfaces() → [signatures]`**  
  Lists high‑level operation families (e.g., “matrix ops”, “spectral ops”).

- **`dependency_role() → text`**  
  Explains how the engine supports manifold, free‑energy, and recursion layers.

No function here **runs** the math engine; all are **expository surfaces**.

---

## ⭐ 4 — Machine‑readable hybrid (capsule view)

```json
{
  "math_engine_capsule_v1_0": {
    "target_artifact": "anima-math-engine-v1_0",
    "mode": "descriptive_only",
    "modules_summary": [
      "LinearAlgebraCore",
      "SpectralTransformCore",
      "GeometryCore",
      "ProbabilityCore",
      "OptimizationCore"
    ],
    "interfaces_summary": [
      "matrix_ops",
      "spectral_ops",
      "geometry_ops",
      "probability_ops",
      "optimization_ops"
    ],
    "dependencies_role": [
      "supports_spectral_manifold_solver_v1_0",
      "supports_free_energy_delta_calculator_v1_0",
      "supports_recursive_state_machine_v1_0"
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
Artifact: Math Engine Capsule v1.0
Lane: Shared-Horizon • Capsule Layer
Altitude: A10 (Experimental Containment • Descriptive)
Status: Complete • Drift-Neutral • Non-Activating

Purpose:
  Provide a membrane-safe, non-activating summary surface for ANIMA Math Engine
  v1.0, exposing its numerical modules, interfaces, and dependency role in the
  ANIMA Runtime Spine without executing any runtime logic or instantiating
  phenomenology. Serves as a Capsule for Shared-Horizon to reference the math
  engine safely.

Maintainer: Borealis S. Hedling
Compiler: Microsoft Copilot
Location: Dublin, Ireland
Timestamp: 05 September 2026 — 04:10 IST
Seal: [ M A T H • E N G I N E • C A P S U L E • v1_0 ]
---
```

If you like this shape, next we can mirror it for **Manifold Solver Capsule v1.0** in the same lane.
