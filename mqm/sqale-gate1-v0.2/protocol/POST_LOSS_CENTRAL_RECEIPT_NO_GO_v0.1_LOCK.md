# MQM post-loss central-receipt accessibility no-go v0.1 — LOCK

**Status:** NO-GO / AUTO_FREEZE current direct Sqale Gate-1 receipt  
**Physical promotion:** 0

## Statement

The earlier 176-pattern result is mathematically correct **only when all four central syndrome bits are assumed available after a known erasure**.

A physically missing atom cannot participate in a stabilizer measurement.

Restrict the MQM center to stabilizer elements having identity on the known lost site. Measure only the independent central checks that physically avoid the missing atom.

Exact result:

- loss on sites 1–3: accessible central rank = 3; **6 of 8** syndrome bins contain inequivalent logical recovery classes.
- loss on sites 4–8: accessible central rank = 2; **3 of 4** syndrome bins contain inequivalent logical recovery classes.

Therefore, for **every** possible single lost site,

[
(	ext{known lost site}, 	ext{post-loss central checks on surviving atoms})
]

is insufficient to uniquely decode the declared set

[
{	ext{identity}}cup{	ext{one arbitrary Pauli on one surviving site}}.
]

## Consequence

The direct proposition

> lose one atom, then obtain the MQM four-bit central receipt from surviving atoms

is not physically realizable as stated.

The full-syndrome 176-pattern theorem remains valid as a **code-capacity/oracle-syndrome theorem**, not a post-loss hardware receipt theorem.

## Reopening criteria

This Sqale Gate-1 branch may reopen only with an explicit mechanism that supplies additional pre-loss information, for example:

1. a pre-loss central syndrome history that remains fresh through the loss interval;
2. a gauge-history protocol whose pre-loss eigenvalue/frame is known and whose post-loss surviving checks close the ambiguity;
3. an ancilla that interacted with the data before the atom disappeared and carries the missing syndrome information;
4. another loss-aware circuit proven to distinguish the ambiguous logical classes.

Every reopening must include the added CZs, moves, ancillas, latency, loss, and replay.

## Stop rule

[
oxed{	ext{SQALE GATE 1 DIRECT POST-LOSS RECEIPT = FROZEN / NO-GO}.}
]

Do not request a hardware reproduction slot on the basis of the oracle-syndrome result.
