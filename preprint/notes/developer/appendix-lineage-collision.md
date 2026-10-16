# Developer Note — Appendix Lineage Collision (Public‑Facing Edition)

A mathematical and structural explanation of how two appendix systems collided

This preprint has evolved through multiple architectural passes.  
Two distinct appendix systems emerged during development:

1. The original preprint appendices (A–D)  
   - A: Lean formalization  
   - B: ITA pseudocode  
   - C: Runtime actuator models  
   - D: Collapse‑surface atlas  

2. The conceptual‑edition appendices (A–D)  
   - A: NDH primitives  
   - B: Seam primitives  
   - C: Meaning primitives  
   - D: Early runtime primitives  

These two systems use the same labels (A–D) but refer to different mathematical objects.  
This creates a label collision that can be expressed formally.

---

Mathematical Diagnostic of the Collision

Let:

- \(\mathcal{P}_i\) = the preprint appendix \(i\)  
- \(\mathcal{C}_i\) = the conceptual‑edition appendix \(i\)

We expect appendices to satisfy:

\[
\mathcal{P}i \equiv \mathcal{C}i
\]

But in reality:

\[
\mathcal{P}i \neq \mathcal{C}i
\]

This mismatch is not just semantic — it is structural.

We can formalize the collision using a label‑reuse function:

\[
L : \{A,B,C,D\} \rightarrow \{\text{content}\}
\]

In the preprint lineage:

\[
L(A) = \text{Lean formalization}
\]
\[
L(B) = \text{ITA pseudocode}
\]
\[
L(C) = \text{Actuator models}
\]
\[
L(D) = \text{Collapse surfaces}
\]

In the conceptual‑edition lineage:

\[
L(A) = \text{NDH primitives}
\]
\[
L(B) = \text{Seam primitives}
\]
\[
L(C) = \text{Meaning primitives}
\]
\[
L(D) = \text{Early runtime primitives}
\]

Thus:

\[
L{\text{preprint}}(i) \neq L{\text{conceptual}}(i)
\]

This is a label collision:

\[
\exists i \in \{A,B,C,D\} : L{\text{preprint}}(i) \cap L{\text{conceptual}}(i) = \emptyset
\]

In plain language:

> The same appendix labels refer to completely different mathematical objects.

This is why the assistant’s earlier description felt “off”:  
it was referencing the conceptual edition’s A–D, not the preprint’s A–D.

---

Why Deprecation Didn’t Make Sense (Mathematically)

Deprecation implies:

\[
\mathcal{P}i \subset \mathcal{C}i
\]

or

\[
\mathcal{P}i \rightarrow \mathcal{C}i
\]

But the actual relationship is:

\[
\mathcal{P}i \perp \mathcal{C}i
\]

They are orthogonal:

- different domains  
- different operators  
- different geometric objects  
- different runtime assumptions  

Thus:

\[
\text{Deprecation is undefined because the sets do not intersect.}
\]

This is why the earlier “archival/deprecated” framing was structurally incorrect.

---

Reason for the Collision (Public‑Facing Explanation)

The collision occurred because:

- the conceptual edition uses A–D to describe altitude primitives  
- the preprint uses A–D to describe Lean, ITA, runtime, and collapse surfaces  
- both systems evolved independently  
- both reused the same labels  
- the assistant assumed the conceptual edition’s A–D had replaced the preprint’s A–D

Formally:

\[
\text{Assistant assumed } L{\text{conceptual}} = L{\text{preprint}}
\]

But the actual mapping is:

\[
L{\text{conceptual}} \neq L{\text{preprint}}
\]

This is the root cause.

---

Public‑Facing Resolution

To avoid confusion:

✔ The preprint’s Appendices A–D remain active and authoritative

✔ The conceptual edition’s A–D do not exist in this preprint

✔ The diagnostic spine begins at Appendix E

✔ The extension zone begins at Appendix O

✔ A–D are not deprecated

✔ A–D are not archival

✔ A–D are part of the preprint’s mathematical backbone

This resolves the collision cleanly.

---


📜 Provenance Footer
`
Provenance: This diagnostic note documents a lineage collision between two
independent appendix systems developed during the evolution of the preprint.
The original preprint appendices (A–D) contain active structural content
including Lean formalization, ITA pseudocode, runtime actuator models, and
collapse-surface definitions. The conceptual-edition appendices (A–D) define
altitude primitives and belong to a separate architectural lineage.

The collision arose from label reuse across lineages, formally expressed as
Lpreprint(i) ≠ Lconceptual(i) for i ∈ {A, B, C, D}. This note preserves the
historical development of both systems and clarifies that the preprint’s
Appendices A–D remain authoritative and non-deprecated. The conceptual-edition
appendices do not replace or supersede the preprint’s A–D.

Recorded for traceability, reproducibility, and future archival reference.
`

---

