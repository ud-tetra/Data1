# Reproduction-slot request — eight-site loss receipt

**Status:** PREPARED / HOLD UNTIL RECEIPT COMPILE PASSES  
**Ask:** one reproduction slot, not a partnership.

## One question

On one eight-site neutral-atom block with one deliberately injected atom loss, does the MQM typed-loss receipt improve the yield/error tradeoff versus Sqale's published parity-reconstruction/postselection baseline **after its extra receipt cost is counted**?

## Frozen comparison

Two separate encodings on the same eight-site physical footprint:

**Baseline:** Sqale `[[8,3,2]]`, one known loss, parity reconstruction/postselection.

**Candidate:** MQM `[[8,1,3,3]]`, same injected-loss position, central syndrome receipt, typed `CORRECT/HOLD/LOGICAL_ERROR` output.

The two encodings are not overlaid.

## Declared success criterion

MQM must show either:
- higher kept-shot yield at matched-or-lower logical error; or
- lower logical error at matched-or-higher kept-shot yield.

Otherwise the Sqale-integration branch stops.

## Resource accounting

Count:
- all data atoms;
- receipt ancillas;
- physical CZ/two-qubit gates;
- atom moves and moved distance;
- terminal measurements;
- replay/rejected shots;
- classical decode.

## Current HOLD reason

The algebraic public release exists and the one-loss+one-extra-corruption micro-test passes, but the MQM central receipt has **not yet been compiled into a frozen Sqale-native circuit with all CZ/move/ancilla costs charged**.

Therefore this note is public, but it should **not yet be sent as a hardware request**.

No magic factory, heteronuclear sentinel, or broad UD claim belongs in the first approach.
