# Gate 4 hardware-ask status — NOT YET READY TO SEND

**Status:** OPEN / RESOURCE-COMPILE BLOCKER  
**Physical promotion:** 0

The public algebraic Gate-1 package is ready.

The external **eight-site reproduction request is not yet ready to send** because the current MQM typed-loss result assumes access to a central-syndrome receipt. That receipt has not yet been compiled into a Sqale-native terminal circuit with frozen CZ/move/ancilla counts.

Do not hide that cost.

## Current break-even target

Using the public Sqale measurement-classification screen

[
p_m=(0.002+0.023)/2=0.0125,
]

the exploratory terminal model gives:
- Sqale parity-reconstruction logical-X error after one known loss: about **8.43%**.
- MQM stays below that value only while the effective syndrome-bit error is below about **2.69%**.

This is not a hardware win.

The public Sqale model also reports roughly:
- CZ postselected fidelity 98.7%;
- CZ single-qubit phase error 0.73%;
- movement success 98%;
- movement phase error 4.1%;
- moved-atom identity fidelity 97.3%.

A receipt that adds several CZs or shuttles can erase the algebraic gain.

## Reopening condition

Before requesting a reproduction slot, produce either:
1. a Sqale-native eight-data-site destructive receipt requiring no hidden ancillas; or
2. an explicit ancilla receipt circuit with every added atom, CZ, move, measurement, replay, and loss counted.

If neither beats the parity-reconstruction/postselection Pareto frontier, stop the Sqale branch.

No magic factory or heteronuclear sentinel belongs in the first ask.
