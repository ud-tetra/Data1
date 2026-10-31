# UD P4-ER1 — GitHub Actions External Runner v0.2

This release repairs the BMv2 device-config path exposed by the first external run.

The uploaded run proved that p4c created:

`build/p4er1.json/p4er1_receipt_loopback.json`

while v0.1 passed:

`/work/build/p4er1.json`

to the P4Runtime configuration stage.

v0.2 compiles into `build/p4c_out`, resolves the actual compiled JSON file, and passes that exact file to the controller.

No source-plan or scientific-predictor rule changed.

Run instructions:

`RUN_ON_GITHUB_ACTIONS_CLICK_BY_CLICK.md`

Physical promotion: 0.


## Unified Dynamics predictive discovery policy - 2026-10-31

The program-wide [Predictive Discovery Protocol v1.0](https://github.com/ud-tetra/UD/blob/ff89221626d3258dc458f01408f1fac80a072530/docs/UD_PREDICTIVE_DISCOVERY_PROTOCOL_v1.0.md) is staged for review; local boot guidance is in [BOOTLOADER.md](BOOTLOADER.md) and [governance adoption](governance/UD_PREDICTIVE_DISCOVERY_ADOPTION_v1.0.md). Explicitly labeled exploratory modeling, calibration and FIT are permitted. Physical identification requires a specified source/observable/unit map, non-constructor review, frozen tests and replication. **No runner config, P4 program, device path, baseline data, or scientific predictor rule has changed. Physical promotion 0.**


## UD proof-first research tracking (2026-10-31)

Read governance/UD_PROOF_FIRST_ADOPTION_v1.0.md. A mathematical theorem or scoped no-go with complete proof is a scientific milestone; CI, P4 replay and build success are only supporting experimental/computational receipts. Capture theorem statements and formal dependency/status independently of implementation. Physical promotion 0.
