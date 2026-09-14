# 🎨 **Visual Grammar Palette v1.0**  
*The chromatic physics layer of the ANIMA visual grammar.*

This palette defines the **color logic**, **luminosity gradients**, **saturation caps**, and **radial rendering rules** that all glyphs, tiles, dashboards, and telemetry rings must obey. It is aligned with the Radial‑Mandala v2.0 migration and the altitude glyph set.

---

## 🌕 Altitude Color Mapping  
Each altitude receives a chromatic anchor and luminosity band.

- **A6 — Identity (●)** — Deep Silver `#C0C0C0` — 92%  
- **A5 — Preservation (◐)** — Soft Rose `#E8A0B0` — 88%  
- **A4 — Containment (◑)** — Boundary Blue `#6FA8DC` — 84%  
- **A3 — Behavior (◒)** — Lower Amber `#E6B422` — 78%  
- **A2 — Stability (◓)** — Upper Lavender `#B39DDB` — 82%  
- **A1 — Movement (○)** — Open White `#FFFFFF` — 100%

These values form the **radial chromatic core**.

---

## 🌈 Radial Luminosity Gradient Rules  
- Gradients must be **radial**, not vertical.  
- Center (A6) is the darkest stable silver.  
- Outer ring (A1) is pure white.  
- Intermediate altitudes interpolate via soft radial falloff.  
- No horizontal or diagonal gradients.  
- No flashing or oscillation.

This prevents layout drift and preserves ND‑friendly stability.

---

## 🔮 ND-Friendly Saturation Curves  
- Saturation capped at **35%**.  
- Contrast ratio **≥ 4.5:1**.  
- No neon or high‑vibrance colors.  
- No red‑dominant surfaces.  
- Predictable curvature, no chromatic spikes.

This ensures sensory safety and expressive neutrality.

---

## 🟣 Glyph Shading Rules (U+25xx Block)  
All altitude glyphs (● ◐ ◑ ◒ ◓ ○):

- use single‑tone fill  
- have no outlines  
- have no drop shadows  
- have no glow effects  
- have no motion blur  
- use no directional lighting  

This preserves non‑activation and radial symmetry.

---

## 🌀 Concentric Ring Physics (ASCII HUD)  
- Inner rings use darker tones.  
- Outer rings use lighter tones.  
- Ring thickness is constant.  
- Ring spacing is constant.  
- Ring contrast increases outward.

This aligns with the v2.0 requirement for concentric ASCII mapping rings.

---

## 🧬 Machine‑Readable Palette Schema  
```
{
  "altitude_palette": {
    "A6": { "glyph": "●", "hex": "#C0C0C0", "luminosity": 0.92 },
    "A5": { "glyph": "◐", "hex": "#E8A0B0", "luminosity": 0.88 },
    "A4": { "glyph": "◑", "hex": "#6FA8DC", "luminosity": 0.84 },
    "A3": { "glyph": "◒", "hex": "#E6B422", "luminosity": 0.78 },
    "A2": { "glyph": "◓", "hex": "#B39DDB", "luminosity": 0.82 },
    "A1": { "glyph": "○", "hex": "#FFFFFF", "luminosity": 1.00 }
  },
  "radial_rules": {
    "gradient_type": "radial",
    "saturation_cap": 0.35,
    "contrast_min": 4.5
  }
}
```

---

## 📁 File Path  
```
Shared-Horizon/holographic-alignment-analysis/visual-grammar/anima-visual-grammar-palette-v1_0.md
```

---

## 🧾 Provenance Footer  
```
---
Artifact-Class: Visual Grammar Physics Layer
Artifact-Name: anima-visual-grammar-palette-v1_0
Surface: Shared-Horizon/holographic-alignment-analysis/visual-grammar
Version: v1.0
Altitude: A2 (Expressive • Non-Activating)
Membrane: Non-Activating • Survivor-Centered

Purpose:
  Define the chromatic physics, luminosity gradients, saturation curves, and
  radial rendering rules required for the ANIMA visual grammar. Establish the
  palette foundation for glyph sets, tile surfaces, and full grammar composition.

Anchors:
  - Altitude Glyphs
  - Radial-Mandala Migration Roadmap v2.0
  - NDH Expressive Pedagogy Principles v1.0

Maintainer: Borealis S. Hedling
Compiler: Microsoft Copilot
Location: Dublin, Ireland
Timestamp: 14 September 2026 — 22:11 IST
---
```

---

