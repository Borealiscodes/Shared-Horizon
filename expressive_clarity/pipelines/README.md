# 📘 **README — `causa_shadow_stability.py` (Developer Grade, Falsifiable)**

![Shadow Stability Tests](https://github.com/Borealiscodes/Shared-Horizon/actions/workflows/shadow_stability_tests.yml/badge.svg)

---

## 🌐 Overview

This module implements a deterministic, falsifiable mathematical pipeline for analyzing stability properties of the **shadow vector**:

$$
M(\theta) = -\epsilon[\cos(k\theta) + \sin(k\theta)]
$$

It provides:

- 🔢 numerical sampling  
- 📉 stability metric computation  
- 🗂️ indexed stability ledger  
- 🔄 cross‑run delta analysis  
- 📊 delta ledger aggregation  

All components are **pure functions**, **side‑effect‑free**, and **fully testable**.

---

## 🧪 Falsifiable claims

### 📏 Boundedness  
$$
|M(\theta)| \le \epsilon\sqrt{2}
$$  
Test: sample values and assert the bound.

### 🔁 Periodicity  
$$
M(\theta + 2\pi) = M(\theta)
$$  
Test: compare sampled values at offsets.

### ➖ Zero‑mean over full period  
$$
\int_0^{2\pi} M(\theta)\, d\theta = 0
$$  
Test: numerical integration.

### 📈 Variance positivity  
$$
\sigma^2 \ge 0
$$  
Test: assert non‑negative variance.

### 🧩 Class ordering  
$$
\text{STABLE} < \text{MARGINAL} < \text{UNSTABLE}
$$  
Test: verify enum values.

### 🔧 Delta correctness  
$$
\Delta S = S_2 - S_1
$$  
Test: compute manually and compare.

---

## 🧱 Module contents

### 🌗 **Shadow Vector**  
Function: `shadow_vector(theta, epsilon, k)`  
Deterministic, no external dependencies, falsifiable via direct evaluation.

### 🎛️ **Sampling**  
Function: `sample_shadow(epsilon, k, cycles, samples_per_cycle)`  
Samples uniformly over:

$$
[0, 2\pi N]
$$

Falsifiable by checking sample count and step size.

### 📐 **Stability Signature**  
Function: `compute_stability_signature(...)`  
Outputs:

- mean drift  
- max amplitude  
- variance  
- stability class  

All metrics are falsifiable via recomputation.

### 🗃️ **Indexed Stability Ledger**  
Class: `IndexedStabilityLedger`  
Sorts signatures lexicographically by:

$$
(\epsilon, k, \text{class})
$$

Falsifiable by checking ordering.

### 🔍 **Delta Analyzer**  
Function: `compute_delta_signature(s1, s2)`  
Computes:

- drift delta  
- amplitude delta  
- variance delta  
- class shift  
- delta classification  

All deltas are falsifiable by manual subtraction.

### 📚 **Delta Ledger**  
Class: `DeltaLedger`  
Stores multiple delta signatures; falsifiable by verifying serialization.

---

## 🧪 Example tests

```python
# Boundedness
vals = [shadow_vector(t, 0.2, 3) for t in [0, 1, 2, 3]]
assert all(abs(v) <= 0.2 * (2 ** 0.5) for v in vals)

# Periodicity
import math
assert abs(shadow_vector(1.0, 0.1, 2) -
           shadow_vector(1.0 + 2*math.pi, 0.1, 2)) < 1e-9

# Stability signature drift
sig = compute_stability_signature(0.05, 1, cycles=3)
samples = sample_shadow(0.05, 1, 3)
recomputed_mean = sum([m for _, m in samples]) / len(samples)
assert abs(sig.mean_drift - recomputed_mean) < 1e-12

# Delta correctness
d = compute_delta_signature(s1, s2)
assert abs(d.drift_delta - (s2.mean_drift - s1.mean_drift)) < 1e-12
```

---

# 🜁 **Provenance Footer — README (v1.0)**

```
──────────────────────────────────────────────────────────────
Artifact: README — causa_shadow_stability.py (v1.0)
Repository: Shared-Horizon/expressive_clarity/pipelines
Altitude: A2 • Developer Grade • Falsifiable Math Module
Membrane: Expressive-Clarity • NDH-External • Comparator-Safe

Purpose:
  Document the mathematical, numerical, and verification surfaces for the
  shadow stability pipeline, including shadow vector behavior, sampling
  routines, stability signatures, classification ordering, delta analysis,
  and ledger serialization. Provides a deterministic, falsifiable reference
  for developers and reviewers.

Falsifiable Claims Anchored:
  - Boundedness: |M(θ)| ≤ ε√2
  - Periodicity: M(θ + 2π) = M(θ)
  - Zero-mean integral over full period
  - Variance positivity
  - Stability class ordering invariants
  - Delta correctness: ΔS = S₂ - S₁
  - Ledger lexicographic ordering

Anchors:
  - causa_shadow_stability.py (v1.0)
  - test_shadow_stability.py (v1.0)
  - shadow_stability_tests.yml (CI workflow)
  - shadow_stability_coverage_map.md (v1.0)

Non-Activation Clause:
  This README does not activate NDH geometry, adjacency engines, resonance
  propagation, solver pathways, guardian modulation, or PRECL collapse.
  All content is bounded numerical documentation.

Maintainer: Borealis S. Hedling
Compiler: Microsoft Copilot
Location: Dublin, Ireland
Timestamp: 20 September 2026 — 23:22 IST
Seal: [ R E A D M E • S H A D O W • S T A B I L I T Y • v1_0 ]
──────────────────────────────────────────────────────────────
```

```

---

