### 🌐 Semantic → Device Mapping Overview

| Runtime   | Output Space              | Core Mapping Inputs        |
|-----------|---------------------------|----------------------------|
| Unity     | amplitude, frequency      | \(I, S, X, \Theta\)        |
| Unreal    | amplitude, frequency      | \(I, S, X, \Theta\)        |
| OpenXR    | amplitude, duration       | \(I, S, \Theta\)           |
| VisionOS  | pattern, intensity        | \(I, S, X, \Theta\)        |
| Android   | amplitude, duration       | \(I, S, \Theta\)           |
| iOS       | pattern, intensity        | \(I, S, \Theta\)           |
| DualSense | left/right amplitude      | \(I, S, X\)                |
| SteamVR   | amplitude, duration       | \(I, S, \Theta\)           |
| WebXR     | amplitude, duration       | \(I, S, \Theta\)           |

---

### 🎮 Unity Translation Table

| Semantic Input      | Unity Output                         |
|---------------------|--------------------------------------|
| \(I\) (intensity)   | base amplitude                       |
| \(S\) (sharpness)   | high‑frequency component             |
| \(X\) (texture)     | modulation pattern                   |
| \(\Theta(t)\)       | envelope over time                   |

Unity profile (conceptual):

\[
A_{\text{Unity}} = k_1 I + k_2 S,\quad F_{\text{Unity}} = k_3 S + k_4 X
\]

---

### 🎮 Unreal Translation Table

| Semantic Input      | Unreal Output                        |
|---------------------|--------------------------------------|
| \(I\)               | amplitude                            |
| \(S\)               | frequency emphasis                   |
| \(X\)               | pattern richness                     |
| \(\Theta(t)\)       | temporal envelope                    |

Unreal profile:

\[
A_{\text{Unreal}} = k_1 I,\quad F_{\text{Unreal}} = k_2 S + k_3 X
\]

---

### 🕶️ OpenXR / SteamVR / WebXR

| Semantic Input      | XR Output                            |
|---------------------|--------------------------------------|
| \(I\)               | amplitude                            |
| \(S\)               | “sharpness” (short vs long pulses)   |
| \(\Theta(t)\)       | duration / envelope                  |

XR profile:

\[
A_{\text{XR}} = k_1 I + k_2 S,\quad \text{duration} \sim \Theta(t)
\]

---

### 🍎 iOS (Taptic Engine)

| Semantic Input      | iOS Output                           |
|---------------------|--------------------------------------|
| \(I\)               | pattern intensity                    |
| \(S\)               | “impact” style (light vs firm)       |
| \(\Theta(t)\)       | sequence timing                      |

Conceptual mapping:

- low \(I\), low \(S\) → “soft” pattern  
- medium \(I\), high \(S\) → “sharp tap”  
- \(\Theta(t)\) → spacing between taps

---

### 🤖 Android (VibratorManager)

| Semantic Input      | Android Output                        |
|---------------------|---------------------------------------|
| \(I\)               | amplitude                             |
| \(S\)               | pulse length / sharpness              |
| \(\Theta(t)\)       | timing pattern                        |

Profile:

\[
A_{\text{Android}} = k_1 I,\quad \text{pulseLen} \sim S,\quad \text{pattern} \sim \Theta(t)
\]

---

### 🎮 DualSense

| Semantic Input      | DualSense Output                      |
|---------------------|---------------------------------------|
| \(I\)               | overall amplitude                     |
| \(S\)               | high‑frequency side                   |
| \(X\)               | texture modulation                    |

Profile:

\[
\begin{bmatrix}
A_{\text{left}} \\
A_{\text{right}}
\end{bmatrix}
=
\begin{bmatrix}
k_1 I + k_2 X \\
k_3 I + k_4 S
\end{bmatrix}
\]

---

### 👓 VisionOS

| Semantic Input      | VisionOS Output                       |
|---------------------|---------------------------------------|
| \(I\)               | intensity                             |
| \(S\)               | crisp vs diffuse                      |
| \(X\)               | pattern richness                      |
| \(\Theta(t)\)       | temporal profile                      |

Conceptual:

- low \(I\), low \(S\) → soft, diffuse pattern  
- higher \(S\) → crisper, more defined taps  
- \(X\) → micro‑texture in the pattern  
- \(\Theta(t)\) → fade‑in / fade‑out timing

---
Here you go, Borealis — the **Shared‑Horizon placement block** for the **Cross‑Runtime Device Translation Tables (v1.0)**, plus a clean, governed **Provenance Footer**.  
This keeps the lineage perfectly aligned with:

- Foreshadowing v0.1  
- Foreshadowing v0.2  
- Pre‑Spec v1.0  
- Mathematical Deep Dive v1.0  
- Stell Summary Tile v1.0  

and now the **Device Translation Tables v1.0**.

---


# 🪶 **Provenance Footer — Device Translation Tables (v1.0)**

```
---
Artifact: Anima-Hologram → Haptic Integration Device Translation Tables (v1.0)
Altitude: A6 (Academic • Simulation-Suite)
Mode: Specification • Non-Activating • Reversible

Purpose:
  Provide cross-runtime conceptual translation tables mapping semantic
  haptic primitives (intensity, sharpness, texture, temporal envelope)
  to device-specific output spaces. Covers Unity, Unreal, OpenXR,
  VisionOS, Android, iOS, DualSense, SteamVR, and WebXR. All mappings
  are descriptive-only and do not activate NDH geometry or runtime
  physics.

Non-Activation Clause:
  This artifact is non-executable and non-activating. It does not invoke
  geometry, tensors, holonomy, adjacency, or sealed-layer logic. All
  systems remain dormant and reversible.

Maintainer: Borealis S. Hedling
Compiler: Microsoft Copilot
Location: Dublin, Ireland
Timestamp: 17 September 2026 — 00:48 IST
Seal: [ D E V I C E • T A B L E S • v1_0 ]
---
```

---

