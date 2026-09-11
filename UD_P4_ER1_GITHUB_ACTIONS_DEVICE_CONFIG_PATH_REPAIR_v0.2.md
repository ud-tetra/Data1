# UD P4-ER1 GitHub Actions Device-Config Path Repair v0.2

**Status:** `APPEND_ONLY EXECUTION REPAIR`  
**Physical promotion:** `0`

## Observed external run

The first GitHub Actions execution reached:

`Executing P4Runtime controller / collector...`

then failed with:

`CRITICAL:root:Error when setting config`

The uploaded evidence bundle contains the compiler output at:

`build/p4er1.json/p4er1_receipt_loopback.json`

but the v0.1 controller invocation passed:

`--bmv2-json /work/build/p4er1.json`

which is a **directory**, not the compiled BMv2 JSON file.

Thus the P4Runtime configuration stage was handed the wrong device-config path.

## Root cause

The invoked p4c image treated:

`-o build/p4er1.json`

as an output directory. It created:

`build/p4er1.json/p4er1_receipt_loopback.json`

and:

`build/p4er1.json/p4er1_receipt_loopback.p4i`.

The runner incorrectly assumed `-o` named a single JSON file.

## v0.2 repair

The runner now:

1. compiles into a deliberately named directory:
   `build/p4c_out`;
2. enumerates compiled build files;
3. resolves the actual `*.json` file inside that directory;
4. fails closed if no compiled JSON exists;
5. passes that exact file to `FwdPipeConfig`;
6. captures BMv2 logs from the EXIT trap even when the controller fails.

No source plan, event semantics, receipt law, hidden target rule, or physical interpretation was changed.

## Governance

### AUTO_LOCK

The uploaded external artifact proves the v0.1 path mismatch:
compiled JSON is nested under the p4c output directory while the controller was given the directory itself.

### REPAIR

Only the executable build-path/interface handling is changed.

### UNCHANGED

- 18-event frozen source plan;
- seven MP-1R event classes;
- source-only acquisition scope;
- sequence-gap HOLD;
- hash-chain protocol;
- physical promotion 0.

The failed v0.1 run is preserved as append-only operational evidence. It is not a scientific falsification of the MP-1R receipt law.
