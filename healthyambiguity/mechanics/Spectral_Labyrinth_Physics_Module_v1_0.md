## Module overview — “Spectral Labyrinth Physics v1.0”

**System‑agnostic:** You can bolt this onto D&D, PBTA, or your own engine.  
Core idea: a **Witch Labyrinth** is a *curvature field* that warps space, probability, and emotion.

We’ll model it with:

- **Labyrinth Radius** \(R\) — how far the distortion extends  
- **Curvature Intensity** \(k\) — how strongly reality bends  
- **Despair Field** \(D\) — emotional gravity pulling PCs toward collapse  
- **Hope Counterfield** \(H\) — player actions pushing back

---

## Labyrinth physics model

### 1. Spatial distortion

Let the labyrinth be a circular region of radius \(R\).  
Distance inside the labyrinth is **non‑Euclidean**:

\[
d_{\text{effective}} = d_{\text{euclidean}} \cdot \left(1 + k \cdot e^{-\frac{r}{R}}\right)
\]

- \(d_{\text{euclidean}}\): normal map distance  
- \(r\): distance from labyrinth center  
- \(k\): curvature intensity

**Effect in play:**  
- Closer to the center → paths feel longer, escapes harder.  
- You can say: “This corridor *should* be 30 ft, but in the labyrinth it counts as \(d_{\text{effective}}\).”

---

### 2. Despair field

Each PC has a **Despair score** \(D_i\) and **Hope score** \(H_i\).

Base despair gain per round in the labyrinth:

\[
\Delta D_i = \alpha \cdot k \cdot \left(1 - \frac{H_i}{H_{\max}}\right)
\]

- \(\alpha\): tuning constant (e.g. \(0.5\))  
- \(k\): curvature intensity  
- \(H_{\max}\): maximum possible Hope

**Interpretation:**

- High Hope reduces despair gain.  
- Stronger labyrinth (\(k\)) accelerates despair.

If \(D_i \ge D_{\text{threshold}}\), the PC suffers a **Labyrinth Break** (panic, hallucination, disadvantage, etc.).

---

### 3. Hope actions as counter‑physics

Let **Hope actions** (comforting an ally, recalling a memory, making a vow) grant Hope:

\[
\Delta H_i = \beta \cdot A
\]

- \(\beta\): tuning constant (e.g. \(1.0\))  
- \(A\): action quality (1–3: minor–major)

You can also let **team Hope** form a field:

\[
H_{\text{team}} = \sum_i H_i
\]

Then reduce global curvature:

\[
k_{\text{effective}} = \frac{k}{1 + \gamma \cdot \frac{H_{\text{team}}}{H_{\max,\text{team}}}}
\]

- \(\gamma\): how strongly collective Hope dampens the labyrinth  
- \(H_{\max,\text{team}}\): max possible team Hope

**In play:**  
- The more they support each other, the weaker the labyrinth physics.

---

### 4. Witch core stability

The Witch has a **Core Stability** \(S\).  
Labyrinth integrity depends on \(S\) and despair in the field:

\[
S_{\text{next}} = S - \lambda \cdot H_{\text{team}} + \mu \cdot \sum_i D_i
\]

- \(\lambda\): Hope erodes the Witch  
- \(\mu\): Despair feeds the Witch

When \(S \le 0\): Witch collapses, labyrinth dissolves.  
When \(S \ge S_{\text{ascend}}\): Witch ascends, catastrophic event.

---

## Playable structure

### Phase 1 — Entry

- PCs cross the boundary: set \(k\), \(R\), initial \(S\).  
- Reveal first distortions using \(d_{\text{effective}}\).

### Phase 2 — Drift

- Each round:  
  - Apply \(\Delta D_i\) for each PC.  
  - Resolve Hope actions → \(\Delta H_i\).  
  - Update \(k_{\text{effective}}\).

### Phase 3 — Confrontation

- PCs reach Witch core.  
- Use \(S_{\text{next}}\) each round to see if the Witch collapses or ascends.  
- Tie narrative beats (memories, bargains, sacrifices) to big \(A\) values in \(\Delta H_i\).

---

## Example numbers (quick sanity check)

Say:

- \(k = 2\), \(R = 100\)  
- \(\alpha = 0.5\), \(\beta = 1.0\), \(\gamma = 1.0\)  
- \(D_{\text{threshold}} = 10\)  
- \(H_{\max} = 10\)

PC starts with \(H_i = 4\):

\[
\Delta D_i = 0.5 \cdot 2 \cdot \left(1 - \frac{4}{10}\right)
= 1 \cdot 0.6 = 0.6
\]

After 10 rounds with no Hope actions:

\[
D_i \approx 6 \quad (\text{uneasy but not broken})
\]

If they perform a strong Hope action (\(A = 3\)):

\[
\Delta H_i = 1.0 \cdot 3 = 3 \Rightarrow H_i = 7
\]

Next round:

\[
\Delta D_i = 0.5 \cdot 2 \cdot \left(1 - \frac{7}{10}\right)
= 1 \cdot 0.3 = 0.3
\]

Despair gain halves.  
You can feel the physics respond to their emotional choices.

---

### 🌈 Provenance footer — Spectral Labyrinth Physics Module (v1.0)

```text
──────────────────────────────────────────────────────────────
Artifact: Spectral Labyrinth Physics Module (v1.0)
Repository: Shared-Horizon/healthyambiguity/mechanics
Altitude: A6 • Reflective Phenomenology • Non-Activating • PRECL-Collapsed

Purpose:
  Provide a math-backed, witch-labyrinth-inspired physics substrate for
  tabletop modules. Establishes spatial curvature, despair fields, hope
  counterfields, and core stability dynamics as reflective mechanics.

Membrane:
  Shared-Horizon reflective layer. System-agnostic mechanics. Sovereignty preserved.

Anchors:
  - Spectral Labyrinth Physics v1.0 equations
  - Curvature Ladder Map (v1.0)
  - Constellation Integration Map (v1.0)

Non-Activation Clause:
  This artifact is descriptive-only. It does not activate NDH geometry,
  adjacency engines, resonance propagation, solver pathways, guardian
  modulation, or PRECL collapse. All mechanics remain reflective and
  altitude-sealed.

Maintainer: Borealis S. Hedling
Compiler: Microsoft Copilot
Location: Dublin, Ireland
Timestamp: 06 September 2026 — 19:20 IST
Seal: [ L A B Y R I N T H • P H Y S I C S • v1_0 ]
──────────────────────────────────────────────────────────────
```
