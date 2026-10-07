# Sqale-facing factory branch — DEMOTED / HELD

**Status:** HELD / LATER BRANCH  
**Physical promotion:** 0

The direct Reed–Muller temporary-gauge factory is **not** the lead Sqale proposition.

## Why

Sqale already has native non-Clifford/logical structure:
- the 2026 30-logical-qubit IQP circuit includes four logical CCZ gates;
- the public “double-CZ” logical entangler uses four physical two-qubit gates instead of eight;
- atom motion is a first-class hardware cost and can introduce both error and loss.

Therefore MQM does not lead with a 15-to-1 temporary-gauge factory merely because it reduces abstract CNOT composition.

## Reopening condition

Reopen only if both are true:

1. Sqale's transversal/native non-Clifford path stops scaling for the target workload; and
2. an MQM factory compiled onto the Sqale block schedule is competitive in **physical two-qubit gates + atom moves + move loss + replay**, not CNOT count alone.

Any direct RM factory comparison must include:
- temporary-gauge physical gate count;
- move count and moved distance;
- added atom-loss probability;
- Layer-A requalification after the temporary gauges;
- kept-shot yield and logical error.

A factory that saves logical CNOTs but adds shuttles can lose.

**Current lead:** Gate 1 eight-site typed-loss kill test, followed by Gate 2 dual-view readout certificate.
