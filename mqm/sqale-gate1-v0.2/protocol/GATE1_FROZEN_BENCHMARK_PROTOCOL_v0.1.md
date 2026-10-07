# Gate 1 frozen benchmark protocol — Sqale eight-site loss test v0.1

**Status:** PRE-REGISTERED DEVELOPMENT PROTOCOL  
**Physical promotion:** 0

## Question

On the same eight physical sites, does the MQM `[[8,1,3,3]]` typed-loss receipt outperform the published Sqale parity-reconstruction/postselection baseline **after counting the extra receipt circuit, Rydberg two-qubit error, moves, loss, and discarded shots**?

## Compatibility rule

The two codes are compared in **separate encoding runs**.

MQM gauge measurements are **not** overlaid on a live `[[8,3,2]]` memory state. Such an overlay requires a separate compatibility/code-switching proof.

Sqale's `[[8,3,3]] / [[8,3,2]]` encoding remains the memory baseline.

## Frozen metrics

At each frozen physical-noise point report:
1. kept-shot yield;
2. conditional logical error among kept shots;
3. total success = kept and logically correct;
4. physical two-qubit gate count;
5. move count / total moved-atom distance if available;
6. discarded/replayed shot count;
7. decoder outcomes: `CORRECT`, `HOLD/REJECT`, `LOGICAL_ERROR`.

## Primary comparison

Plot logical error vs kept-shot yield.

MQM passes only if its Pareto curve strictly improves the Sqale baseline at at least one nontrivial operating point:
- higher kept-shot yield at equal-or-lower logical error; **or**
- lower logical error at equal-or-higher kept-shot yield.

## Stop rule

If MQM does not beat parity reconstruction + postselection after the hardware receipt overhead is charged under the frozen Sqale noise model:

**STOP THIS SQALE INTEGRATION BRANCH.**

Do not rescue the claim by retuning thresholds after seeing the result.

## Noise-model rule

Use only public/published Sqale parameters or parameters supplied directly by Infleqtion.

The September 2026 30-logical-qubit technical post does not yet publish the full physical error model. Until the promised paper/calibration data are available, Gate-1 numerical runs using the older Sqale model are **exploratory**, not confirmatory.

## Reproduction request gate

Minimal external run should use:
- eight data atoms, one block per encoding;
- declared logical state;
- one preregistered known atom loss;
- one additional X-readout corruption / equivalent Pauli fault;
- Sqale parity reconstruction vs MQM typed-loss receipt;
- success criteria frozen in advance.

If MQM requires extra ancillas for the receipt, those atoms and gates are counted. “Eight atoms” may not hide receipt ancillas.
