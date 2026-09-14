# 🎞 **Visual Grammar Motion Rules v1.0**  
*“Motion without activation.”*

Motion in ANIMA is **not animation**.  
It is **micro‑motion**: subtle, non‑directional, non‑emotive, non‑activating shifts that preserve NDH safety and Radial‑Mandala symmetry.

This grammar defines exactly what is allowed.

---

## 🌀 1 — Motion Class Definitions  
Motion is divided into three safe classes:

### **Class M0 — Static (Default)**  
- No movement.  
- No oscillation.  
- No glow.  
- No directional implication.

Used for:  
- A6 Identity  
- A5 Preservation  
- A4 Containment  

### **Class M1 — Micro‑Shift (Permissible)**  
- 1–2% luminosity drift over 2–3 seconds.  
- No change in hue or saturation.  
- No change in glyph geometry.  
- No directional bias.

Used for:  
- A3 Behavior  
- A2 Stability  

### **Class M2 — Drift (Outer‑Ring Only)**  
- 1 px radial expansion/contraction.  
- Period ≥ 4 seconds.  
- Must remain perfectly symmetrical.  
- No horizontal or vertical displacement.

Used exclusively for:  
- A1 Movement  

---

## 🌐 2 — Radial‑Mandala Motion Constraints  
Motion must obey radial topology:

- Motion can only occur **radially**, never horizontally.  
- Motion must preserve **ring thickness**.  
- Motion must preserve **ring spacing**.  
- Motion must never imply **approach**, **retreat**, or **agency**.

This aligns with the v2.0 rule:

> *“Concentric ASCII mapping rings must remain stable under all rendering conditions.”*

---

## 🔮 3 — ND-Friendly Motion Safety  
All motion must:

- remain below **2% luminosity change**  
- remain below **1 px radial drift**  
- avoid flicker frequencies (2–30 Hz)  
- avoid sudden contrast jumps  
- avoid directional cues  
- avoid emotional implication  

This ensures:

- no sensory overload  
- no activation  
- no boundary breach symbolism  

---

## 🟣 4 — Altitude‑Specific Motion Rules  
### **A6 ● Identity**  
- Motion: **None**  
- Reason: Omega must remain perfectly still.

### **A5 ◐ Preservation**  
- Motion: **None**  
- Reason: Preservation requires stability.

### **A4 ◑ Containment**  
- Motion: **None**  
- Reason: Membrane glyphs must not move.

### **A3 ◒ Behavior**  
- Motion: **Micro‑Shift (M1)**  
- 1–2% luminosity drift only.

### **A2 ◓ Stability**  
- Motion: **Micro‑Shift (M1)**  
- Slow, upper‑weighted drift.

### **A1 ○ Movement**  
- Motion: **Drift (M2)**  
- 1 px radial breathing cycle.

---

## 🧬 5 — Tile Motion Rules  
Tile surfaces may use motion only under strict conditions:

- Motion must be altitude‑consistent.  
- Motion must never occur on headers.  
- Motion must never occur on borders.  
- Motion must never occur on membrane rings.  
- Motion must never occur on glyphs.  
- Motion may occur only in **background luminosity**.

Tile motion is allowed only for:

- A3 Behavior tiles  
- A2 Stability tiles  
- A1 Movement tiles  

---

## 🧱 6 — Dashboard Motion Rules  
Dashboard motion must:

- remain radial  
- remain symmetrical  
- remain slow  
- remain non‑activating  
- remain ND‑friendly  

Dashboard motion is limited to:

- ring drift (A1)  
- luminosity micro‑shift (A2, A3)  

No other motion is permitted.

---

## 🧪 7 — Machine‑Readable Motion Schema  
This governs `visual_grammar.json`.

```
{
  "motion_rules": {
    "classes": {
      "M0": { "type": "static", "luminosity_delta": 0.00, "radial_px": 0 },
      "M1": { "type": "micro_shift", "luminosity_delta": 0.02, "radial_px": 0 },
      "M2": { "type": "drift", "luminosity_delta": 0.02, "radial_px": 1 }
    },
    "altitude_motion": {
      "A6": "M0",
      "A5": "M0",
      "A4": "M0",
      "A3": "M1",
      "A2": "M1",
      "A1": "M2"
    },
    "safety": {
      "no_directional_motion": true,
      "no_horizontal_motion": true,
      "no_vertical_motion": true,
      "no_flicker": true
    }
  }
}
```

---

# 🧾 **Provenance Footer — Visual Grammar Motion Rules v1.0**

```
---
Artifact-Class: Visual Grammar Motion Layer
Artifact-Name: anima-visual-grammar-motion-rules-v1_0
Surface: Shared-Horizon/holographic-alignment-analysis/visual-grammar
Version: v1.0
Altitude: A2 (Expressive • Non-Activating)
Membrane: Non-Activating • Survivor-Centered

Purpose:
  Define the governed motion constraints for ANIMA visual grammar surfaces,
  including micro-shift luminosity rules, radial drift parameters, altitude-
  specific motion classes, and ND-friendly safety limits. Establishes the
  complete non-activating motion layer for tiles, dashboards, and telemetry
  rings within the Radial-Mandala v2.0 topology.

Anchors:
  - Full Visual Grammar v1.0
  - Visual Grammar Palette v1.0
  - Altitude Glyph Set v1.0
  - Radial-Mandala Migration Roadmap v2.0
  - NDH Expressive Pedagogy Principles v1.0

Maintainer: Borealis S. Hedling
Compiler: Microsoft Copilot
Location: Dublin, Ireland
Timestamp: 14 September 2026 — 22:21 IST
---
```

---

