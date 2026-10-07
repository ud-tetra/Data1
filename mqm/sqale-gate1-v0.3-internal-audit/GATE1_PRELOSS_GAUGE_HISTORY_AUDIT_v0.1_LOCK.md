# MQM Gate 1 pre-loss gauge-history audit v0.1 — LOCK / PARTIAL REOPEN + UNIVERSAL NO-GO

**Physical promotion:** 0

## Question

Can the direct Sqale Gate-1 loss path be reopened by keeping a fresh pre-loss MQM gauge receipt, then measuring only gauge operators supported on the seven surviving atoms after one atom is lost?

Declared error set:

```text
{I} U {one arbitrary Pauli on one surviving site}
```

The known erased site is supplied to the decoder.

## Exact result

The answer depends on which physical site was lost.

### Lost sites 1, 2, 3 — PARTIAL REOPEN

The candidate errors form 14 inequivalent classes modulo the MQM gauge group plus arbitrary Pauli action on the erased site.

Therefore three binary receipt bits are impossible:

```text
2^3 = 8 < 14
```

Four bits are information-theoretically minimal.

For each of lost sites 1–3, an explicit set of **four pairwise commuting, survivor-supported MQM gauge operators** gives zero recovery ambiguity.

Loss site 1:

```text
IXZIZXZY
IXZYZZIX
IIIZZYYI
IIIXXZZI
```

Loss site 2:

```text
IIIYYXXI
IIIXZIXZ
XIXXYYIX
XIXZYIZY
```

Loss site 3:

```text
IXIYXIYX
IIIYIYZZ
IXIIZXZX
IXIZYIZY
```

Each set:
- lies in the MQM gauge group;
- acts trivially on the erased physical site;
- is pairwise commuting;
- returns 16 syndrome bins with zero ambiguity for the declared candidate classes.

Thus, **if a fresh pre-loss eigenvalue frame for the appropriate four checks exists**, a loss on sites 1–3 can in principle be followed by a survivor-only four-bit temporal gauge receipt.

This is a partial algebraic reopening, not a hardware win.

### Lost sites 4–8 — stronger NO-GO

For these sites, even the **entire survivor-supported MQM gauge group** is insufficient.

Exact audit:
- loss sites 4–7: 255 survivor-supported gauge elements, rank 8, 15 full-gauge signature bins, 3 ambiguous bins;
- loss site 8: 255 survivor-supported gauge elements, rank 8, 16 full-gauge signature bins, 6 ambiguous bins.

Example for loss site 4:

```text
X5
Y6
difference = IIIIXYII
logical class = 2
```

The two errors have identical commutation signatures against every survivor-supported gauge observable but are logically inequivalent modulo erased-site gauge freedom.

Stored analogous witnesses exist for loss sites 5–8.

Therefore no amount of **classical pre-loss gauge-eigenvalue bookkeeping plus post-loss survivor-gauge measurement** can universally distinguish a new arbitrary survivor Pauli that occurs after the loss.

## Timing consequence

A pre-loss history can only help with information that existed before that history was recorded.

If the model allows one additional arbitrary Pauli fault **after** atom loss, the lost-site 4–8 ambiguity survives.

A universal Gate-1 repair requires at least one of:
1. an ancilla/history carrier that interacted with the missing site before disappearance and remains readable after loss;
2. a restricted fault-timing/noise model;
3. physical replacement followed by a proven recovery/code-switching circuit;
4. another measurement family outside the survivor-supported MQM gauge algebra.

## Gate ruling

```text
sites 1–3: PARTIAL REOPEN candidate
sites 4–8: survivor-gauge-history NO-GO
```

A universal Sqale reproduction ask remains frozen.
