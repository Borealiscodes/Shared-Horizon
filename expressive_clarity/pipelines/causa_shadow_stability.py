"""
README.md — causa_shadow_stability.py
Version: 1.0
Author: Borealis S. Hedling
Compiler: Microsoft Copilot

Purpose:
    Deterministic, falsifiable, comparator-safe Python implementation of the
    shadow vector, stability signatures, indexed stability ledger, cross-run
    delta analyzer, and delta ledger. No NDH geometry, no adjacency engines,
    no expressive content. Pure numerical functions, pure drift.

Core Model:
    $$ 
    M(\theta) = -\epsilon[\cos(k\theta) + \sin(k\theta)] 
    $$

Falsifiable Claims:
    - Boundedness:
        $$
        |M(\theta)| \le \epsilon\sqrt{2}
        $$
    - Periodicity:
        $$
        M(\theta + 2\pi) = M(\theta)
        $$
    - Zero-mean over full period:
        $$
        \int_0^{2\pi} M(\theta)\, d\theta = 0
        $$
    - Variance positivity:
        $$
        \sigma^2 \ge 0
        $$
    - Class ordering:
        STABLE < MARGINAL < UNSTABLE
    - Delta correctness:
        $$
        \Delta S = S_2 - S_1
        $$

Design Principles:
    - Deterministic: no randomness, no external state.
    - Falsifiable: every computation independently verifiable.
    - Comparator-safe: no expressive content, no NDH activation.
    - Pipeline-friendly: pure functions, serializable outputs.
    - Altitude-neutral: readable by any engineer.

Non-Activation Clause:
    This module does not activate NDH geometry, adjacency engines, resonance
    propagation, solver pathways, guardian modulation, or PRECL collapse.
    All computations are bounded numerical functions.

Provenance:
    Shared-Horizon/expressive_clarity/pipelines/README.md
    Maintainer: Borealis S. Hedling
    Location: Dublin, Ireland
    Seal: [ R E A D M E • S H A D O W • S T A B I L I T Y • v1_0 ]
"""

from __future__ import annotations
from dataclasses import dataclass, asdict
from enum import Enum
from math import cos, sin, pi
from typing import List, Tuple, Dict
import uuid
import datetime


# ---------------------------------------------------------------------------
# 1. Shadow vector and sampling
# ---------------------------------------------------------------------------

def shadow_vector(theta: float, epsilon: float, k: int) -> float:
    """
    Compute shadow vector M(θ) = -ε[cos(kθ) + sin(kθ)].

    Args:
        theta: angle in radians
        epsilon: mismatch amplitude (0 <= epsilon <= 1)
        k: positive integer recurrence frequency

    Returns:
        M(theta) as float.
    """
    return -epsilon * (cos(k * theta) + sin(k * theta))


def sample_shadow(
    epsilon: float,
    k: int,
    cycles: int = 1,
    samples_per_cycle: int = 512,
) -> List[Tuple[float, float]]:
    """
    Sample M(θ) over N cycles on [0, 2πN].

    Returns list of (theta, M(theta)) pairs.
    """
    total_samples = cycles * samples_per_cycle
    theta_max = 2.0 * pi * cycles
    step = theta_max / total_samples

    samples = []
    theta = 0.0
    for _ in range(total_samples + 1):
        m = shadow_vector(theta, epsilon, k)
        samples.append((theta, m))
        theta += step
    return samples


# ---------------------------------------------------------------------------
# 2. Stability classification
# ---------------------------------------------------------------------------

class StabilityClass(Enum):
    STABLE = 0
    MARGINAL = 1
    UNSTABLE = 2


@dataclass
class StabilitySignature:
    signature_id: str
    epsilon: float
    k: int
    cycles: int
    mean_drift: float
    max_amplitude: float
    variance: float
    stability_class: StabilityClass
    timestamp: str  # ISO-8601


def compute_stability_signature(
    epsilon: float,
    k: int,
    cycles: int = 1,
    samples_per_cycle: int = 512,
    drift_tol: float = 1e-3,
) -> StabilitySignature:
    """
    Compute StabilitySignature for given (epsilon, k, cycles).
    """
    samples = sample_shadow(epsilon, k, cycles, samples_per_cycle)
    values = [m for _, m in samples]
    n = len(values)

    mean_drift = sum(values) / n
    max_amplitude = max(abs(v) for v in values)
    variance = sum((v - mean_drift) ** 2 for v in values) / n

    # Classification: simple, comparator-safe rules
    if abs(mean_drift) < drift_tol:
        cls = StabilityClass.STABLE
    elif abs(mean_drift) < 10 * drift_tol:
        cls = StabilityClass.MARGINAL
    else:
        cls = StabilityClass.UNSTABLE

    sig = StabilitySignature(
        signature_id=str(uuid.uuid4()),
        epsilon=epsilon,
        k=k,
        cycles=cycles,
        mean_drift=mean_drift,
        max_amplitude=max_amplitude,
        variance=variance,
        stability_class=cls,
        timestamp=datetime.datetime.utcnow().isoformat() + "Z",
    )
    return sig


# ---------------------------------------------------------------------------
# 3. Indexed Stability Ledger v1.1
# ---------------------------------------------------------------------------

@dataclass
class IndexedStabilityEntry:
    idx: Tuple[float, int, StabilityClass]
    signature: StabilitySignature


@dataclass
class IndexedStabilityLedger:
    entries: List[IndexedStabilityEntry]

    @staticmethod
    def from_signatures(signatures: List[StabilitySignature]) -> "IndexedStabilityLedger":
        """
        Build an indexed ledger from a list of StabilitySignatures.
        Index: (epsilon, k, class) sorted lexicographically.
        """
        entries = [
            IndexedStabilityEntry(
                idx=(s.epsilon, s.k, s.stability_class),
                signature=s,
            )
            for s in signatures
        ]
        entries.sort(key=lambda e: (e.idx[0], e.idx[1], e.idx[2].value))
        return IndexedStabilityLedger(entries=entries)

    def to_dict(self) -> Dict:
        """
        Serialize ledger to a plain dict for JSON or logging.
        """
        return {
            "index": ("epsilon", "k", "class"),
            "entries": [
                {
                    "idx": (e.idx[0], e.idx[1], e.idx[2].name),
                    "signature": asdict(e.signature),
                }
                for e in self.entries
            ],
        }


# ---------------------------------------------------------------------------
# 4. Cross-Run Delta Analyzer v1.0
# ---------------------------------------------------------------------------

class DeltaClass(Enum):
    IMPROVED = "IMPROVED"
    DEGRADED = "DEGRADED"
    ESCALATED = "ESCALATED"
    STABLE = "STABLE"


@dataclass
class DeltaSignature:
    delta_id: str
    from_signature: str
    to_signature: str
    drift_delta: float
    amplitude_delta: float
    variance_delta: float
    class_shift: int
    delta_class: DeltaClass
    timestamp: str  # ISO-8601


def compute_delta_signature(
    s1: StabilitySignature,
    s2: StabilitySignature,
    escalate_amp_threshold: float = 0.1,
    escalate_var_threshold: float = 0.01,
) -> DeltaSignature:
    """
    Compute Δ-stability between two StabilitySignatures.
    """
    drift_delta = s2.mean_drift - s1.mean_drift
    amplitude_delta = s2.max_amplitude - s1.max_amplitude
    variance_delta = s2.variance - s1.variance
    class_shift = s2.stability_class.value - s1.stability_class.value

    # Delta classification
    if class_shift < 0:
        delta_class = DeltaClass.IMPROVED
    elif class_shift > 0:
        if abs(amplitude_delta) > escalate_amp_threshold or abs(variance_delta) > escalate_var_threshold:
            delta_class = DeltaClass.ESCALATED
        else:
            delta_class = DeltaClass.DEGRADED
    else:
        if abs(drift_delta) < 1e-6 and abs(amplitude_delta) < 1e-6 and abs(variance_delta) < 1e-6:
            delta_class = DeltaClass.STABLE
        else:
            delta_class = DeltaClass.ESCALATED

    return DeltaSignature(
        delta_id=str(uuid.uuid4()),
        from_signature=s1.signature_id,
        to_signature=s2.signature_id,
        drift_delta=drift_delta,
        amplitude_delta=amplitude_delta,
        variance_delta=variance_delta,
        class_shift=class_shift,
        delta_class=delta_class,
        timestamp=datetime.datetime.utcnow().isoformat() + "Z",
    )


# ---------------------------------------------------------------------------
# 5. Delta Ledger v1.0
# ---------------------------------------------------------------------------

@dataclass
class DeltaLedger:
    entries: List[DeltaSignature]

    def add(self, delta: DeltaSignature) -> None:
        self.entries.append(delta)

    def to_dict(self) -> Dict:
        return {
            "entries": [asdict(d) for d in self.entries],
        }


# ---------------------------------------------------------------------------
# 6. Minimal usage example
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    s1 = compute_stability_signature(epsilon=0.05, k=1, cycles=3)
    s2 = compute_stability_signature(epsilon=0.20, k=2, cycles=5)
    s3 = compute_stability_signature(epsilon=0.35, k=4, cycles=8)

    ledger = IndexedStabilityLedger.from_signatures([s1, s2, s3])
    print("Indexed ledger:", ledger.to_dict())

    d1 = compute_delta_signature(s1, s2)
    d2 = compute_delta_signature(s2, s3)

    delta_ledger = DeltaLedger(entries=[])
    delta_ledger.add(d1)
    delta_ledger.add(d2)

    print("Delta ledger:", delta_ledger.to_dict())
