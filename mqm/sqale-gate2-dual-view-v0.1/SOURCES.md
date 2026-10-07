# Gate 2 source note

## Sqale-specific public basis

Infleqtion, “Demonstration of 30 Logical Qubits on Sqale,” 24 Sep 2026  
https://infleqtion.com/demonstration-of-30-logical-qubits-on-sqale/

The public result establishes:
- eight-atom logical blocks;
- known atom-loss site information;
- software loss correction by parity reconstruction;
- a yield/error tradeoff from accepting reconstructed-loss shots.

Sqale product material also describes neutral-atom error detection, nondestructive readout, individual addressing, and reconfigurable arrays:
https://infleqtion.com/quantum-computing/

## Generic fluorescence context — not Sqale calibration

Neutral-atom literature demonstrates site-resolved fluorescence imaging, e.g.:
- Qiu et al., “Loading and Imaging Atom Arrays via Electromagnetically Induced Transparency,” arXiv:2509.12124 — 99.6(3)% readout fidelity and 98.2(3)% survival in that apparatus.
- Su et al., “Fast single atom imaging for optical lattice arrays,” arXiv:2404.09978 — 2.4 microsecond imaging and 99.4% fidelity in that lattice apparatus.

These results establish feasibility of high-fidelity fluorescence imaging in neutral-atom systems. They are **not substituted for Sqale's unpublished PSF/drift/common-mode calibration**.

Every numeric imaging parameter in Gate 2 is therefore a declared simulation assumption.
