# UD P4-ER1 — GitHub Actions External Runner

This repository is a frozen operational harness for producing an externally instantiated MP-1R identity/provenance receipt corpus using:

`P4Runtime PacketOut → BMv2 simple_switch_grpc → P4Runtime PacketIn`

Start with:

**`RUN_ON_GITHUB_ACTIONS_CLICK_BY_CLICK.md`**

No Docker installation is required on the user's Windows machine.

## Frozen source scope

- six seam transactions;
- three A/B/C addresses per seam;
- 18 ordered source-only records;
- all seven MP-1R event classes represented;
- no hidden Theta endpoint in the source plan.

## PASS conditions

The cloud run must return:

- 18 receipts;
- event sequence exactly `1..18`;
- exact source-field preservation through BMv2;
- zero sequence gaps;
- valid append-only SHA-256 hash chain.

The workflow uploads the evidence as:

`UD_P4_ER1_EXTERNAL_RECEIPT_BUNDLE`

## Governance

This is an operational provenance-carrier test. It does not identify Ethernet packets, BMv2 state, or controller metadata with a physical UD carrier.

Physical promotion: **0**.
