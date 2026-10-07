# Gate 1 frozen benchmark protocol — Sqale eight-site loss test v0.1

**Status:** PRE-REGISTERED DEVELOPMENT PROTOCOL  
**Physical promotion:** 0

## Question

On the same eight physical sites, does the MQM `[[8,1,3,3]]` typed-loss receipt outperform published Sqale parity reconstruction/postselection **after counting the extra receipt circuit, Rydberg two-qubit error, moves, loss, and discarded shots**?

## Compatibility rule

Compare the two codes in **separate encoding runs**.

MQM gauge measurements are not overlaid on a live `[[8,3,2]]` memory state. That would require a separate compatibility/code-switch proof.

Sqale `[[8,3,3]] / [[8,3,2]]` remains the memory baseline.

## Frozen primary metrics

At each frozen noise point report:
1. kept-shot yield;
2. conditional logical error among kept shots;
3. total success = kept and logically correct;
4. physical two-qubit gate count;
5. move count / moved distance where available;
6. discarded/replayed shot count;
7. decoder outcomes `CORRECT / HOLD / LOGICAL_ERROR`.

## Primary decision

Plot logical error vs kept-shot yield.

MQM passes only if its Pareto curve strictly improves the Sqale baseline at at least one nontrivial operating point:
- higher kept-shot yield at equal-or-lower logical error; or
- lower logical error at equal-or-higher kept-shot yield.

## Stop rule

If MQM does not beat parity reconstruction + postselection after receipt overhead is charged under the frozen Sqale model:

**STOP THIS SQALE INTEGRATION BRANCH.**

No threshold or decoder retuning after target exposure.

## Noise-model rule

Use only published Sqale parameters or parameters supplied directly by Infleqtion.

The September 2026 30L post does not yet publish the full physical error model. Until the promised paper/calibration data are public, hardware-noise runs using the older public model remain **exploratory**.

## External reproduction ask

Do not send the hardware ask until the MQM receipt is compiled into either:
1. an eight-data-atom destructive receipt requiring no hidden ancillas; or
2. an explicit ancilla circuit with all added atoms, CZs, moves, measurements, replay, and loss counted.

The phrase “eight atoms” must not hide receipt ancillas.
