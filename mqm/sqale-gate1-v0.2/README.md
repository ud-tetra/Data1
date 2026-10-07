# HISTORICAL RELEASE — see v0.3 internal algebra audit

This v0.2 runnable block release is retained for provenance.

**Current Gate-1 ruling:** internal algebra audit only. The universal direct Sqale post-loss receipt is not a hardware result.

Current record:
`mqm/sqale-gate1-v0.3-internal-audit/`

Gate 2 is maintained separately as a calibration-data request:
`mqm/sqale-gate2-calibration-v0.2/`

Do not package Gate 1 and Gate 2 as one hardware result.

---

# IMPORTANT v0.3 SCOPE REPAIR

**Gate 1 direct post-loss receipt is now FROZEN / NO-GO.**

The 176-pattern typed-loss result assumes all four central syndrome bits remain available after the atom is lost. When the syndrome is restricted to central checks that physically avoid the missing atom, every loss location has logical ambiguity.

See:
`protocol/POST_LOSS_CENTRAL_RECEIPT_NO_GO_v0.1_LOCK.md`

The exact MQM algebra, K4 firewall, and full-syndrome code-capacity theorem remain valid. The external hardware ask is withdrawn until a pre-loss history or other physical receipt mechanism closes the information gap.

---

# MQM × Sqale Gate 1 — public eight-site block release v0.2

**Status:** public runnable algebra + frozen kill-test protocol  
**Physical promotion:** 0  
**Hardware advantage:** not claimed

This release makes the repaired MQM `[[8,1,3,3]]` subsystem block public next to the Sqale eight-site baseline.

## Public MQM block

Center / stabilizer generators:

```text
IIIXXZZI
IIIYIYZZ
IIIXZIXZ
XXXXYYIX
```

Additional noncentral gauge generators:

```text
XIIIIIII
ZIIIIIIZ
IXIIIIII
IZIIIIIZ
IIXIIIII
IIZIIIIZ
```

Logical representatives:

```text
X_L = IIIYZIZI
Z_L = IIIXIZIZ
```

K4 vertices: `{1,2,3,8}`

Six K4 edge parities:

```text
Z1Z2  Z1Z3  Z1Z8  Z2Z3  Z2Z8  Z3Z8
```

The runnable module/notebook verifies:
- center rank 4;
- gauge rank 10;
- dressed distance 3;
- all 24 single-site Pauli faults correct modulo gauge;
- all 256 Pauli patterns supported on `{1,2,3,8}` return to logical class zero;
- one known erasure + at most one other Pauli: 176 declared code-capacity patterns, zero ambiguity.

## Sqale side-by-side

The public 30-logical-qubit result reports:
- eight physical atoms per block;
- `[[8,3,3]]` for block preparation;
- `[[8,3,2]]` downstream;
- parity reconstruction of one missing X-basis outcome;
- four logical CCZ gates in the 30L IQP circuit;
- a “double-CZ” logical entangler using four physical two-qubit gates instead of eight.

This release keeps Sqale’s encoding as the **memory baseline**. MQM is compared in separate encoding runs on the same eight-site footprint. No compatibility between MQM gauge checks and a live `[[8,3,2]]` state is assumed.

## Gate-1 hypothesis

This is **not** a “more logical qubits” claim.

The narrow hypothesis is:

> after one known atom loss, an explicit MQM syndrome receipt can identify/correct an additional corruption that can make parity reconstruction infer the wrong logical X outcome.

Exact micro-test:
- Sqale parity reconstruction, one loss + one other X-outcome flip: **56/56 wrong logical-X cases** for the ideal `|+++>` block readout.
- MQM typed-loss code-capacity receipt, one erasure + one equivalent survivor Z fault: **0/56 bad, 0/56 HOLD**.
- K4 firewall: **0/256 logical failures**.

That is an algebraic information-content result, **not a hardware win**.

## Exploratory public-Sqale break-even

Using the public Sqale measurement-classification screen

[
p_m=(0.002+0.023)/2=0.0125,
]

the parity-reconstruction terminal logical-X error is approximately **8.43%**.

In the effective four-bit MQM receipt model, MQM stays below that error only while the syndrome-bit error remains below approximately **2.69%**.

This does not yet charge the actual circuit required to acquire the receipt.

## Kill rule

Gate 1 passes only if a **Sqale-native compiled receipt** beats parity reconstruction + postselection after counting:
- data and ancilla atoms;
- physical CZ/two-qubit gates;
- atom moves and moved distance;
- loss during moves;
- measurements;
- replay/discarded shots;
- classical decoding.

MQM must show either:
- higher kept-shot yield at equal-or-lower logical error; or
- lower logical error at equal-or-higher kept-shot yield.

If it cannot, **stop this Sqale integration branch**.

## Run

```bash
python mqm/sqale-gate1-v0.2/gate1_public.py
```

Notebook:

`mqm/sqale-gate1-v0.2/notebooks/MQM_SQALE_GATE1_RUNNABLE_v0.2.ipynb`

See:
- `SOURCES.md`
- `protocol/GATE1_FROZEN_BENCHMARK_PROTOCOL_v0.1.md`
- `protocol/SQALE_PUBLIC_NOISE_BASELINE_v0.1.json`
- `protocol/HARDWARE_ASK_STATUS_v0.2.md`
