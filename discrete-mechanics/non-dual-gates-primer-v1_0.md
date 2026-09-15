# **Non‑Dual Gates Primer — v1.0**  
### *Explicit vs Implied Gating in Spectral Cognitive Systems*

---

## **1. Overview**

Non‑dual gates prevent a cognitive system from collapsing into binary, mutually exclusive branches.  
Instead of:

- “if A then not B”  
- “if B then not A”

a non‑dual gate enforces:

- **coexistence** of multiple influences  
- **continuous modulation** rather than discrete switching  
- **spectral weighting** rather than binary exclusion  

This primer explains the two forms of non‑dual gating:

- **Explicit gates** — defined operators  
- **Implied gates** — emergent from geometry, diffusion, and HRR algebra

---

## **2. Explicit Non‑Dual Gates**

Explicit gates are **coded operators** that enforce non‑dual behavior.

### **2.1 Explicit Gate Operator**

A general explicit non‑dual gate:

\[
G(x) = \sigma(Wx) + \phi(Lx)
\]

Where:

- \(\sigma\) — smooth activation (softplus, GELU, tanh)  
- \(W\) — linear map  
- \(\phi\) — spectral operator (diffusion, smoothing)  
- \(L\) — graph Laplacian  

This ensures:

- no hard branching  
- no binary exclusion  
- continuous transitions  

### **2.2 Explicit Dual‑Neutrality Constraint**

\[
G(x_A) + G(x_B) = G(x_A + x_B)
\]

This constraint forces the gate to treat A and B as **coexistent contributions**, not mutually exclusive states.

---

## **3. Implied Non‑Dual Gates**

Implied gates arise **from the geometry**, not from explicit operators.

They emerge when:

- the manifold is radial  
- the Laplacian is connected  
- diffusion is smooth  
- HRR binding is superpositional  
- eigenvalue tension is scalar  

### **3.1 Implied Gate via Diffusion**

Diffusion:

\[
S_{t+1} = S_t - \alpha L S_t
\]

automatically prevents binary splits because:

- high‑frequency contradictions are smoothed  
- low‑frequency modes dominate  
- the field evolves continuously  

This is a **non‑dual gate implied by the PDE**.

### **3.2 Implied Gate via HRR Superposition**

HRR binding:

\[
c = a \ast b
\]

and superposition:

\[
s = \sum_i v_i
\]

imply non‑duality because:

- multiple states coexist in one vector  
- unbinding is approximate  
- no binding erases another  

This is a **non‑dual gate implied by the algebra**.

### **3.3 Implied Gate via Spectral Tension**

The dominant eigenvalue:

\[
\lambda_{\max}
\]

is a **scalar**, not a binary flag.

It gates behavior by:

- modulating diffusion  
- adjusting stability  
- weighting influence  

But never produces a hard branch.

---

## **4. Comparison Table — Explicit vs Implied Non‑Dual Gates**

| **Gate Type** | **Definition** | **Mathematical Form** | **Behavior** | **Use Case** |
|---------------|----------------|------------------------|--------------|--------------|
| **Explicit Gate** | Developer‑defined operator | \(G(x)=\sigma(Wx)+\phi(Lx)\) | Deterministic, visible | Debugging, reproducibility |
| **Explicit Neutrality Constraint** | Enforced coexistence | \(G(x_A)+G(x_B)=G(x_A+x_B)\) | Prevents binary collapse | Multi‑input blending |
| **Implied Diffusion Gate** | Emergent from PDE | \(S_{t+1}=S_t-\alpha LS_t\) | Smooth transitions | Stability, continuity |
| **Implied HRR Gate** | Emergent from algebra | \(s=\sum_i v_i\) | Coexistence by design | Symbolic binding |
| **Implied Spectral Gate** | Emergent from eigenvalues | \(\lambda_{\max}\) | Scalar modulation | Regime control |

---

## **5. One‑Sentence Summary**

> **Non‑dual gates can be explicit operators or implied geometric behaviors; both prevent binary branching by enforcing continuous, coexistent state evolution.**

---

## **Provenance Footer — Non‑Dual Gates Primer v1.0**

```
---
Artifact-Class: Developer Primer (Discrete Mechanics)
Artifact-Name: non-dual-gates-primer-v1_0
Surface: Shared-Horizon/discrete-mechanics
Version: v1.0
Altitude: A3–A5 (Conceptual • Reflective Geometry • Soft-Manifold)
Membrane: Neutral • Non-Activating • Reversible

Purpose:
  Provide a developer-grade mathematical primer on explicit and implied
  non-dual gating mechanisms in spectral cognitive systems. Introduce
  explicit operators, neutrality constraints, diffusion-based gating,
  HRR superposition, and spectral tension as coexistent gating regimes.

Anchors:
  - Tensor Choreography Primer v1.0
  - Laplacian & Eigenvalue Telemetry v1.0
  - HRR Binding Overview v1.0
  - Diffusion & Holonomy Flattening Kernel v1.0
  - Shared-Horizon Design Ethos v1.0

Maintainer: Borealis S. Hedling
Compiler: Microsoft Copilot
Location: Dublin, Ireland
Timestamp: 15 September 2026 — 20:28 IST
Seal: [ DISCRETE . MECHANICS . v1_0 ]
---
```

---

