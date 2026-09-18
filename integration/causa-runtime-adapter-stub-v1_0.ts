// File: src/integration/causa-runtime-adapter.ts

import { runOperator } from "../runtime/runtime-kernel";
import { AdjacencyGuard } from "../manifold/adjacency-guard";
import {
  CausaSnapshot,
  computeExpressionCongruence,
  computeDirectionalOwnership,
  computePermutationBaseline,
  computeDriftTracking,
} from "../causa/causa-core"; // hypothetical CAUSA module

// Δ / Φ / Λ / Σ annotation surface
export interface InvariantAnnotations {
  delta: number;   // coherence (sanitize + clamp ↔ congruence)
  phi: number;     // trajectory (spectral continuity ↔ ownership)
  lambda: number;  // effect vs noise (fallback ↔ baseline)
  sigma: number;   // stability over time (adjacency ↔ drift)
}

// Runtime → CAUSA adapter input
export interface RuntimeOperatorContext<TInput, TOutput> {
  input: TInput;
  operator: (x: TInput) => TOutput;
  causaSnapshotBefore: CausaSnapshot;
  causaSnapshotAfter?: CausaSnapshot;
}

// Non‑activating adapter: observes, annotates, does not modify runtime
export function annotateOperatorWithCausa<TInput, TOutput>(
  ctx: RuntimeOperatorContext<TInput, TOutput>,
  adjacencyGuard: AdjacencyGuard
): { result: TOutput; annotations: InvariantAnnotations } {
  // 1. Run operator through governed runtime
  const result = runOperator(ctx.operator, ctx.input);

  // 2. Capture CAUSA snapshot after (caller provides or derives)
  const after = ctx.causaSnapshotAfter ?? ctx.causaSnapshotBefore;

  // 3. Compute CAUSA metrics (flat‑space, Euclidean)
  const congruence = computeExpressionCongruence(ctx.causaSnapshotBefore, after);
  const ownership = computeDirectionalOwnership(ctx.causaSnapshotBefore, after);
  const baseline = computePermutationBaseline(ctx.causaSnapshotBefore, after);
  const drift = computeDriftTracking(ctx.causaSnapshotBefore, after);

  // 4. Map CAUSA metrics → Δ / Φ / Λ / Σ (per integration spec)
  const annotations: InvariantAnnotations = {
    delta: congruence,
    phi: ownership,
    lambda: baseline,
    sigma: drift,
  };

  // 5. Optional: consult adjacency guard for sigma sanity (read‑only)
  adjacencyGuard.observeDrift(drift);

  // 6. Return runtime result + invariant annotations (read‑only)
  return { result, annotations };
}
```

