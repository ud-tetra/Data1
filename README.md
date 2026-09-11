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
