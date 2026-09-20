# 📘 README — `causa_shadow_stability.py` (Developer Grade, Falsifiable)

## Overview

This module implements a deterministic, falsifiable mathematical pipeline for analyzing stability properties of the shadow vector:

$$
M(\theta) = -\epsilon[\cos(k\theta) + \sin(k\theta)]
$$

It provides:

- numerical sampling  
- stability metric computation  
- indexed stability ledger  
- cross‑run delta analysis  
- delta ledger aggregation  

All components are pure functions, side‑effect‑free, and fully testable.

---

## Falsifiable claims

### Boundedness

$$
|M(\theta)| \le \epsilon\sqrt{2}
$$

Test: sample values and assert the bound.

### Periodicity

$$
M(\theta + 2\pi) = M(\theta)
$$

Test: compare sampled values at offsets.

### Zero‑mean over full period

$$
\int_0^{2\pi} M(\theta)\, d\theta = 0
$$

Test: numerical integration.

### Variance positivity

$$
\sigma^2 \ge 0
$$

Test: assert non‑negative variance.

### Class ordering

$$
\text{STABLE} < \text{MARGINAL} < \text{UNSTABLE}
$$

Test: verify enum values.

### Delta correctness

$$
\Delta S = S_2 - S_1
$$

Test: compute manually and compare.

---

## Module contents

### Shadow vector

Function: `shadow_vector(theta, epsilon, k)`  
Deterministic, no external dependencies, falsifiable via direct evaluation.

### Sampling

Function: `sample_shadow(epsilon, k, cycles, samples_per_cycle)`  

Samples uniformly over the interval:

$$
[0, 2\pi N]
$$

Falsifiable by checking sample count and step size.

### Stability signature

Function: `compute_stability_signature(...)`  

Outputs:

- mean drift  
- max amplitude  
- variance  
- stability class  

All metrics are falsifiable via recomputation.

### Indexed stability ledger

Class: `IndexedStabilityLedger`  

Sorts signatures lexicographically by the tuple:

$$
(\epsilon, k, \text{class})
$$

Falsifiable by checking ordering.

### Delta analyzer

Function: `compute_delta_signature(s1, s2)`  

Computes:

- drift delta  
- amplitude delta  
- variance delta  
- class shift  
- delta classification  

All deltas are falsifiable by manual subtraction.

### Delta ledger

Class: `DeltaLedger`  

Stores multiple delta signatures; falsifiable by verifying serialization.

---

## Example tests

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

