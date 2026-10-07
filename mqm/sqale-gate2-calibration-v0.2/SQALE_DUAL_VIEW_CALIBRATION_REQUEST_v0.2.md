# Sqale Gate 2 — minimal fluorescence calibration request v0.2

**Ask type:** calibration data / one analysis pass  
**Not:** partnership, new camera, correction claim, or API integration request  
**Physical promotion:** 0

## First question — go/no-go

Does the current Sqale hardware already expose either:

1. a second genuinely independent optical view of the same block; or
2. an existing observation with equivalent depth/site-disambiguation information?

If **no**, stop. No new camera is proposed.

If **yes**, the minimum requested calibration package is:

### A. Photon statistics
- occupied-site photon-count histogram;
- empty/background histogram.

### B. Localization
- effective PSF or per-site localization covariance.

### C. Correlated drift
- translation/shear/scale/rotation covariance;
- temporal correlation across adjacent receipts.

### D. Camera health
- blank/saturated/invalid-frame frequency and signatures;
- any shared failure mode between the two views.

### E. View geometry
- relative view axes / calibration covariance.

### F. Timing
- exposure time;
- processing latency;
- time between views;
- maximum expected atom displacement between receipts.

### G. Labeled images
- no-loss examples;
- one missing atom at each of the eight sites;
- repeated/drifted examples if available.

### H. Admission semantics
- how a bad/uncertain image is currently represented in the control stack.

## Frozen evaluation

Replace the declared simulator assumptions with these calibrated values.

Report:
- wrong loss/no-loss/site certificate rate;
- ambiguous/HOLD fraction;
- false loss;
- missed loss;
- false merge/duplication;
- total image/decision latency.

Only after that calibrated result beats the existing loss-decision workflow is an integration object worth specifying.
