# Gate 4 hardware-ask status — WITHDRAWN / HOLD

**Status:** FROZEN BY GATE-1 RECEIPT NO-GO  
**Physical promotion:** 0

Do **not** request the eight-site hardware reproduction slot yet.

The exact MQM one-erasure + one-extra-Pauli result assumes access to the full four-bit central syndrome after loss. For a physically missing atom, the central checks that avoid the lost site are insufficient: every loss location retains logical ambiguity.

See:
`POST_LOSS_CENTRAL_RECEIPT_NO_GO_v0.1_LOCK.md`

## Reopening condition

The hardware ask may be restored only after an explicit physical mechanism closes the missing information, such as:
- fresh pre-loss syndrome history;
- validated gauge-history receipt;
- an ancilla carrying information acquired before the atom disappeared;
- another loss-aware circuit proven to distinguish the ambiguous classes.

All added atoms, CZs, moves, latency, loss, measurements, and replay must be charged.

Until then, Gate 1 is stopped as requested.

**External-facing lead moves to Gate 2: dual-view fluorescence certification under a declared imaging-noise model.**
