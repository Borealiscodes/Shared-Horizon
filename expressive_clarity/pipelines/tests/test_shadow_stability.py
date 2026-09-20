import math
import pytest

from causa_shadow_stability import (
    shadow_vector,
    sample_shadow,
    compute_stability_signature,
    compute_delta_signature,
    StabilityClass,
    IndexedStabilityLedger,
    DeltaLedger,
)


# ---------------------------------------------------------------------------
# 1. Shadow Vector Tests
# ---------------------------------------------------------------------------

def test_shadow_vector_boundedness():
    epsilon = 0.2
    k = 3
    thetas = [0, 1, 2, 3, math.pi/4, math.pi/2]

    bound = epsilon * math.sqrt(2)
    for t in thetas:
        assert abs(shadow_vector(t, epsilon, k)) <= bound


def test_shadow_vector_periodicity():
    epsilon = 0.1
    k = 2
    theta = 1.0

    v1 = shadow_vector(theta, epsilon, k)
    v2 = shadow_vector(theta + 2 * math.pi, epsilon, k)

    assert abs(v1 - v2) < 1e-9


# ---------------------------------------------------------------------------
# 2. Sampling Tests
# ---------------------------------------------------------------------------

def test_sample_shadow_length_and_range():
    samples = sample_shadow(0.1, 2, cycles=3, samples_per_cycle=100)
    assert len(samples) == 3 * 100 + 1

    # Check theta range
    assert samples[0][0] == pytest.approx(0.0)
    assert samples[-1][0] == pytest.approx(2 * math.pi * 3)


# ---------------------------------------------------------------------------
# 3. Stability Signature Tests
# ---------------------------------------------------------------------------

def test_stability_signature_mean_drift_recomputes():
    sig = compute_stability_signature(0.05, 1, cycles=2)
    samples = sample_shadow(0.05, 1, 2)

    recomputed_mean = sum([m for _, m in samples]) / len(samples)
    assert abs(sig.mean_drift - recomputed_mean) < 1e-12


def test_stability_signature_classification():
    # Very small drift → STABLE
    sig_stable = compute_stability_signature(0.01, 1, cycles=1)
    assert sig_stable.stability_class == StabilityClass.STABLE

    # Larger drift → UNSTABLE
    sig_unstable = compute_stability_signature(0.5, 1, cycles=1)
    assert sig_unstable.stability_class == StabilityClass.UNSTABLE


# ---------------------------------------------------------------------------
# 4. Indexed Stability Ledger Tests
# ---------------------------------------------------------------------------

def test_indexed_stability_ledger_sorting():
    s1 = compute_stability_signature(0.05, 1)
    s2 = compute_stability_signature(0.10, 1)
    s3 = compute_stability_signature(0.05, 2)

    ledger = IndexedStabilityLedger.from_signatures([s3, s2, s1])

    # Sorted lexicographically by (epsilon, k, class)
    idxs = [entry.idx for entry in ledger.entries]
    assert idxs == sorted(idxs, key=lambda x: (x[0], x[1], x[2].value))


# ---------------------------------------------------------------------------
# 5. Delta Analyzer Tests
# ---------------------------------------------------------------------------

def test_delta_correctness():
    s1 = compute_stability_signature(0.05, 1)
    s2 = compute_stability_signature(0.20, 1)

    d = compute_delta_signature(s1, s2)

    assert d.drift_delta == pytest.approx(s2.mean_drift - s1.mean_drift)
    assert d.amplitude_delta == pytest.approx(s2.max_amplitude - s1.max_amplitude)
    assert d.variance_delta == pytest.approx(s2.variance - s1.variance)


def test_delta_class_shift():
    s1 = compute_stability_signature(0.01, 1)  # likely STABLE
    s2 = compute_stability_signature(0.5, 1)   # likely UNSTABLE

    d = compute_delta_signature(s1, s2)
    assert d.class_shift == s2.stability_class.value - s1.stability_class.value


# ---------------------------------------------------------------------------
# 6. Delta Ledger Tests
# ---------------------------------------------------------------------------

def test_delta_ledger_serialization():
    s1 = compute_stability_signature(0.05, 1)
    s2 = compute_stability_signature(0.10, 1)

    d = compute_delta_signature(s1, s2)

    ledger = DeltaLedger(entries=[d])
    serialized = ledger.to_dict()

    assert "entries" in serialized
    assert len(serialized["entries"]) == 1
    assert serialized["entries"][0]["delta_id"] == d.delta_id
