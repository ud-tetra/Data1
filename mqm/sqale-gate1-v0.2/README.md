# MQM × Sqale Gate 1 — public eight-site block release v0.2

**Physical promotion:** 0  
**Claim:** no hardware advantage yet.

This public folder makes the repaired MQM `[[8,1,3,3]]` block independently runnable next to the public Sqale eight-site loss workflow.

## MQM block

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

The runnable release verifies:
- center rank 4;
- gauge rank 10;
- dressed distance 3;
- all 24 single-site Pauli faults correct modulo gauge;
- all 256 Pauli patterns on the K4 core `{1,2,3,8}` return to logical class zero under the frozen decoder;
- one known erasure + at most one other Pauli: 176 declared patterns, zero non-correct receipts.

## Side-by-side scope

Sqale keeps the memory-rate advantage:
- preparation: `[[8,3,3]]`, three logical qubits;
- downstream: `[[8,3,2]]`, three logical qubits.

MQM is **not** proposed because it encodes more logical qubits. It does not.

The Gate-1 hypothesis is narrower: when a known atom loss is followed by an additional corrupted X outcome / equivalent Pauli fault, an explicit MQM syndrome receipt can return a typed result rather than forcing the missing value from the same parity relation.

Exact micro-test:
- Sqale parity reconstruction: **56/56** one-loss + one-extra-X-flip cases give a wrong logical-X result in the frozen ideal-|+++> test.
- MQM clean typed-loss receipt: **0/56 bad, 0/56 HOLD**.
- K4 firewall: **0/256** failures.

This is not a hardware win because MQM pays for the receipt.

## Exploratory break-even

Using the public Sqale measurement-classification parameters `epsilon0=0.002`, `epsilon1=0.023`, averaged to `p_m=0.0125`:

- parity-reconstruction logical-X error: about **8.43%**;
- MQM's four-bit receipt must keep its effective syndrome-bit error below about **2.69%** to remain below that error.

Sqale's older public simulator also reports CZ postselected fidelity ~98.7%, CZ single-qubit phase error 0.73%, movement transfer success 98.0%, movement phase error 4.1%, and moved-atom identity fidelity ~97.3%. That makes the receipt circuit cost load-bearing.

The eight-atom reproduction request is therefore **OPEN, not sent** until the receipt is compiled with explicit ancilla/CZ/move counts.

## Run

Open:

`notebooks/MQM_SQALE_GATE1_RUNNABLE_v0.2.ipynb`

or run:

```bash
python gate1_public.py
```

## Stop rule

If a frozen Sqale-native MQM receipt does not strictly improve the parity-reconstruction/postselection yield–logical-error frontier after counting ancillas, CZs, moves, loss, replay and discarded shots:

**STOP THIS SQALE INTEGRATION BRANCH.**

See `SOURCES.md` and `protocol/GATE1_FROZEN_BENCHMARK_PROTOCOL_v0.1.md`.
