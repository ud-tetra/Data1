# External source ledger — Sqale Gate 1 v0.2

## Primary 30-logical-qubit public result

Infleqtion, **“Demonstration of 30 Logical Qubits on Sqale”**, 24 Sep 2026  
https://infleqtion.com/demonstration-of-30-logical-qubits-on-sqale/

Public facts used:
- 80 physical atoms arranged as ten 8-atom blocks.
- Blocks are prepared in `[[8,3,3]]`, three logical qubits per block.
- Downstream experiments operate in `[[8,3,2]]`.
- The IQP circuit contains four logical CCZ gates.
- The AI-discovered “double-CZ” reduces an inter-block entangler from 8 physical two-qubit gates to 4.
- Loss correction reconstructs a missing X-basis measurement from parity.
- Infleqtion reports that loss correction quadrupled the number of good shots, at the cost of greater error rate.
- The post states a full 30-logical-qubit paper with experimental methods/resource counts is forthcoming.

## Public Sqale hardware/noise model used for the exploratory screen

Rines et al., **“Demonstration of a Logical Architecture Uniting Motion and In-Place Entanglement”**, arXiv:2509.13247v2  
https://arxiv.org/abs/2509.13247

Public facts used:
- Post-processing generally postselects atom loss except when loss correction is enabled.
- Their text explicitly states that one additional bit flip after a single loss can cause loss correction to miscorrect the lost qubit and infer the wrong logical state.
- CZ postselected median fidelity ~98.7%.
- CZ single-qubit phase error probability 0.73% in the published Sqalesim model.
- Measurement classification parameters: epsilon0=0.002, epsilon1=0.023.
- Mid-circuit movement: typical duration ~7 ms.
- Successful transfer to destination tweezer: 98.0(8)%.
- Moved-atom identity fidelity 97.3(20)% after SPAM correction; spectator identity fidelity 98.3(19)%.
- Movement phase error 4.1%; spectator phase error 2.6% in the published simulator.

## [[8,3,2]] public code context

Butt et al., **“Demonstration of measurement-free universal logical quantum computation”**, Nature Communications 17, 995 (2026)  
https://www.nature.com/articles/s41467-026-68533-x

Used only for public `[[8,3,2]]` code/gate context. No claim is made that its trapped-ion physical schedule equals Sqale’s neutral-atom schedule.

## Scope

The Sept. 2026 30-logical-qubit result does not yet publish a full frozen hardware noise model. Therefore the current Gate-1 hardware-noise screen is **exploratory**. Confirmatory comparison waits for the announced paper/calibrations or an Infleqtion-supplied model.
