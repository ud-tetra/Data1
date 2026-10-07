# External source ledger — Sqale Gate 1 v0.2

## 30-logical-qubit public result

Infleqtion, **“Demonstration of 30 Logical Qubits on Sqale”**, 24 Sep 2026  
https://infleqtion.com/demonstration-of-30-logical-qubits-on-sqale/

Public facts used:
- 80 physical atoms arranged as ten 8-atom blocks.
- Each block is prepared in distance-3 `[[8,3,3]]`, three logical qubits per block.
- Downstream experiments operate in `[[8,3,2]]`.
- The IQP circuit contains four logical CCZ gates.
- The “double-CZ” reduces an inter-block entangler from 8 physical two-qubit gates to 4.
- One missing X-basis measurement can be reconstructed from block parity.
- Loss correction increased useful shots while increasing error; it is explicitly a throughput/accuracy tradeoff.
- The post says a fuller 30L methods/resource paper is forthcoming.

## Public Sqale hardware/noise model used only for exploratory screening

Rines et al., **“Demonstration of a Logical Architecture Uniting Motion and In-Place Entanglement”**, arXiv:2509.13247v2  
https://arxiv.org/abs/2509.13247

Values used:
- state-preparation fidelity 97.9%;
- CZ postselected median fidelity ~98.7%;
- CZ single-qubit phase-error probability 0.73% in the published simulator;
- global-rotation fidelity 99.96%;
- local-RZ fidelity 99.8%;
- measurement postselected fidelity ~98.7%;
- measurement classification parameters `epsilon0=0.002`, `epsilon1=0.023`;
- move transfer success 98.0(8)%;
- typical move duration ~7 ms;
- moved-atom identity fidelity ~97.3% after SPAM correction;
- spectator identity fidelity ~98.3%;
- move phase-error probability 4.1%;
- spectator phase-error probability 2.6%.

The paper also explains the relevant failure mode: after one known loss, an additional bit flip can make loss correction infer the wrong logical state.

## [[8,3,2]] public code context

Butt et al., **“Demonstration of measurement-free universal logical quantum computation”**, Nature Communications 17, 995 (2026).  
https://www.nature.com/articles/s41467-026-68533-x

Used only for public `[[8,3,2]]` code/gate context. No claim is made that its trapped-ion physical schedule equals Sqale’s neutral-atom schedule.

## Governance

The Sept. 2026 30L result does not yet publish a complete frozen hardware noise model. Gate-1 numerical use of the older public Sqale model is therefore **exploratory**. Confirmatory comparison waits for the announced 30L paper/calibrations or an Infleqtion-supplied model.
