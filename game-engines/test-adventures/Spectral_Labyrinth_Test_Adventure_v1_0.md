# ⭐ **Spectral Labyrinth Test Adventure v1.0**  
### *A live-play, math-backed micro‑scenario for immediate testing of the Spectral Labyrinth Engine*

This adventure is designed to:

- Stress-test curvature physics  
- Stress-test despair/hope fields  
- Stress-test core stability  
- Validate turn structure  
- Validate emotional mechanics  
- Validate branching consequences  
- Be fun

And it includes **random character generation**.

---

# 🎲 **1 — Random Character Generation (Live)**  
Lead term: **random character**

### **Your Test PC: “Lira Vale”**

- **Resolve (R):** 3  
- **Empathy (E):** 4  
- **Focus (F):** 2  
- **Hope (H):** starts at 4  
- **Despair (D):** starts at 0  
- **Trait:** “Echo-Sensitive” — gains +1 Hope when hearing emotional resonance  
- **Flaw:** “Fracture Memory” — gains +1 Despair when confronted with childhood imagery  
- **Gear:**  
  - *Memory Pendant* (once per adventure: +2 Hope)  
  - *Fractured Map* (reveals true distance once per scene)

This is your test avatar.

---

# 🧊 **2 — Test Labyrinth: “The Glass Orchard”**

A small, safe, controlled labyrinth designed for engine testing.

### **Labyrinth Stats**

- **Curvature Intensity (k):** 1.8  
- **Radius (R_lab):** 120 m  
- **Base Despair Rate (α):** 0.4  
- **Hope Gain Rate (β):** 1.0  
- **Curvature Dampening (γ):** 0.8  
- **Core Stability (S):** 20  
- **Ascension Threshold (S_ascend):** 40  
- **Break Threshold (D_break):** 8  

### **Theme**

A forest of glass trees that reflect memories instead of light.

### **Core Entity**

**The Orchard Keeper** — a gentle but grieving figure whose sorrow crystallized into the labyrinth.

---

# 🧮 **3 — Scene 1: Entry Distortion**

Lira steps into the orchard.

A path that looks **20 meters** long is actually distorted.

Compute:

\[
d_{\text{eff}} = 20 \cdot \left(1 + 1.8 \cdot e^{-\frac{30}{120}}\right)
\]

\[
e^{-0.25} \approx 0.778
\]

\[
1 + 1.8 \cdot 0.778 \approx 1 + 1.400 = 2.400
\]

\[
d_{\text{eff}} \approx 48
\]

**Result:**  
The path counts as **48 meters** — more than double.

Lira must make a **Focus check** (DC 10).  
She has **F = 2**, so she rolls with +2.

If she succeeds → she stays on the path.  
If she fails → she drifts into a memory grove.

---

# 💔 **4 — Scene 2: Despair Pulse**

A glass tree shows Lira a childhood moment.

Because of her **Fracture Memory flaw**, she gains:

\[
D_i = D_i + 1
\]

Then apply despair field:

\[
\Delta D_i = 0.4 \cdot 1.8 \cdot \left(1 - \frac{H_i + R_i}{10 + 10}\right)
\]

\[
H_i + R_i = 4 + 3 = 7
\]

\[
1 - \frac{7}{20} = 0.65
\]

\[
\Delta D_i = 0.72
\]

Rounded → **+1 Despair**

**Total Despair:** 2

Still safe.

---

# 🌈 **5 — Scene 3: Hope Action**

Lira touches her **Memory Pendant**.

\[
\Delta H_i = 1.0 \cdot 2 = 2
\]

Hope becomes **6**.

This reduces future despair gain.

---

# 🌀 **6 — Scene 4: Core Confrontation**

The Orchard Keeper appears.

Compute next stability:

\[
S_{\text{next}} = 20 - \lambda \cdot H_{\text{team}} + \mu \cdot \sum D_i
\]

Assume:

- \(\lambda = 0.5\)  
- \(\mu = 0.3\)  
- Team Hope = 6  
- Team Despair = 2  

\[
S_{\text{next}} = 20 - 3 + 0.6 = 17.6
\]

The core weakens but does not collapse.

Lira can:

- **Comfort the Keeper** → Hope action  
- **Break the glass trees** → Despair action  
- **Reflect her own memory** → Grey action  

Each leads to different consequences.

---

# 🌟 **7 — Scene 5: Ending Branches**

### **Ending A — Collapse (Hope Path)**  
Lira comforts the Keeper.  
Hope rises.  
Stability drops below 0.  
The orchard dissolves peacefully.

### **Ending B — Ascension (Despair Path)**  
Lira shatters the trees.  
Despair rises.  
Stability rises above 40.  
The Keeper ascends into a dangerous crystal entity.

### **Ending C — Fracture (Grey Path)**  
Lira reflects her own memory.  
Stability oscillates.  
The orchard splits into two micro‑labyrinths.

---

# 🐋 Whale’s Summary

> “This is a real adventure.  
> You can run it right now.  
> And every choice updates the Roadmap and feeds the Meta Constructor.”

---

