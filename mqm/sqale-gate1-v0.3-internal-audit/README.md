# MQM × Sqale Gate 1 v0.3 — internal algebra audit

**Status:** INTERNAL ALGEBRA AUDIT / PARTIAL REOPEN + UNIVERSAL NO-GO  
**Physical promotion:** 0  
**Hardware result:** NO

This release is **not** a Sqale hardware correction claim.

It records one narrow algebra question:

> after one known atom loss, can a fresh pre-loss MQM gauge frame plus survivor-supported gauge measurements distinguish the declared set `{I} ∪ {one arbitrary Pauli on one surviving site}`?

## Ruling

### Lost sites 1–3 — partial algebraic reopen

The declared candidate set has **14 inequivalent classes** modulo MQM gauge freedom plus arbitrary Pauli action on the erased site.

Therefore three binary receipt bits cannot suffice:

```text
2^3 = 8 < 14
```

Four bits are information-theoretically minimal.

For each of lost sites 1–3, an explicit set of **four pairwise commuting MQM gauge operators**, all identity on the lost site, gives 16 syndrome bins with zero ambiguity.

This reopens only an internal temporal-receipt hypothesis:

- a fresh pre-loss eigenvalue frame must actually exist;
- the post-loss fault model must remain the declared one;
- the physical cost of acquiring/maintaining that frame is not yet compiled.

### Lost sites 4–8 — survivor-gauge-history NO-GO

Even the **entire survivor-supported MQM gauge algebra** is insufficient.

The exact audit records:
- sites 4–7: 255 survivor-supported gauge elements, rank 8, 3 ambiguous bins;
- site 8: 255 survivor-supported gauge elements, rank 8, 6 ambiguous bins.

Site-4 witness:

```text
X5
Y6
difference = IIIIXYII
logical class = 2
```

Analogous stored witnesses exist for sites 5–8.

## Timing consequence

A pre-loss eigenvalue cannot distinguish a Pauli that occurs after the loss.

Therefore a purely classical survivor-gauge history is **not** a universal Gate-1 reopening mechanism for sites 4–8.

A universal reopening now requires information that physically crosses the loss event, such as:
- a pre-loss ancilla/history carrier that remains readable after the data atom disappears;
- a restricted fault-timing model;
- replacement/code-switching with a proof;
- another measurement family outside the survivor-supported MQM gauge algebra.

## Governance

This is an algebra result only.

Do **not** present it as:
- a Sqale hardware win;
- a reproduction-slot result;
- a completed loss-correction scheme.

The previous full-four-bit 176-pattern theorem remains valid as an oracle/full-syndrome code-capacity theorem.

See:
- `GATE1_PRELOSS_GAUGE_HISTORY_AUDIT_v0.1_LOCK.md`
- `GATE1_SURVIVOR_GAUGE_AUDIT_v0.1.csv`
- `GATE1_AMBIGUITY_WITNESSES_v0.1.json`
