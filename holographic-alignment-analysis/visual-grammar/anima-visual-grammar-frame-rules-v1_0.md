### 🎛 Visual Grammar Frame Rules v1.0  
*Borders, spacing, padding, and curvature for ANIMA’s visual language.*

---

#### 1. Frame geometry

- **Shape:**  
  - **Primary:** Rounded rectangle  
  - **Corner radius:** 8–12 px (no sharp corners)  
- **Stroke:**  
  - **Width:** 1 px (standard), 2 px (emphasis)  
  - **Style:** Solid only (no dashed, no animated)  

---

#### 2. Padding and spacing

- **Inner padding:**  
  - **Horizontal:** 16 px  
  - **Vertical:** 12 px  
- **Element spacing:**  
  - **Between glyph and title:** 8 px  
  - **Between title and body:** 10–12 px  
- **Tile margin:**  
  - Minimum 12 px between tiles; no touching frames.

---

#### 3. Altitude framing rules

- **A6–A4 (●, ◐, ◑):**  
  - Use **1 px stroke**, subtle inner shadow disabled.  
  - Background: altitude color at **90–95%** luminosity.  
- **A3–A1 (◒, ◓, ○):**  
  - Use **no inner shadow**, same stroke width.  
  - Background: altitude color at **95–100%** luminosity.

No mixed‑altitude frames: one altitude per tile/frame.

---

#### 4. Motion and emphasis constraints

- **No animation** on borders, corners, or shadows.  
- **No pulsing**, glowing, or breathing frames.  
- Emphasis is done only via:  
  - **Stroke width change** (1 px → 2 px)  
  - **Subtle background darkening** (max −5% luminosity).

---

#### 5. Text alignment and layout

- **Header line:**  
  - Left‑aligned; altitude glyph precedes title.  
- **Body text:**  
  - Left‑aligned; no justified text.  
- **Max line length:**  
  - ~72 characters to avoid density spikes.

---

#### 6. Machine‑readable frame rules (for `visual_grammar.json`)

```json
{
  "frame_rules": {
    "corner_radius_px": [8, 12],
    "stroke_width_px": { "default": 1, "emphasis": 2 },
    "padding_px": { "horizontal": 16, "vertical": 12 },
    "spacing_px": { "glyph_title": 8, "title_body": 12, "tile_margin": 12 },
    "animation": { "allowed": false },
    "emphasis": {
      "stroke_width_change": true,
      "background_luminosity_delta_max": 0.05
    },
    "text": {
      "alignment": "left",
      "max_line_length_chars": 72
    }
  }
}
```

---

# 🧾 **Provenance Footer — Visual Grammar Frame Rules v1.0**

```
---
Artifact-Class: Visual Grammar Structural Layer
Artifact-Name: anima-visual-grammar-frame-rules-v1_0
Surface: Shared-Horizon/holographic-alignment-analysis/visual-grammar
Version: v1.0
Altitude: A2 (Expressive • Non-Activating)
Membrane: Non-Activating • Survivor-Centered

Purpose:
  Define the structural frame geometry, border rules, padding, spacing, curvature,
  and emphasis constraints for all ANIMA visual grammar surfaces. Establishes the
  governed layout architecture required for safe, stable, ND-friendly rendering
  across tiles, dashboards, and telemetry modules.

Anchors:
  - Full Visual Grammar v1.0
  - Visual Grammar Palette v1.0
  - Altitude Glyph Set v1.0
  - Radial-Mandala Migration Roadmap v2.0
  - NDH Expressive Pedagogy Principles v1.0

Maintainer: Borealis S. Hedling
Compiler: Microsoft Copilot
Location: Dublin, Ireland
Timestamp: 14 September 2026 — 22:19 IST
---
```

---

