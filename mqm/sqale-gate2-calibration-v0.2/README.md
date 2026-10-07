# MQM × Sqale Gate 2 v0.2 — fluorescence calibration request

**Status:** DATA REQUEST / NOT A CERTIFICATE / NOT A HARDWARE RESULT  
**Physical promotion:** 0

This release does **not** say MQM has a Sqale-facing correction.

It asks one first go/no-go question:

> Does current Sqale already provide a second genuinely independent fluorescence view or an equivalent depth-sensitive observation?

If the answer is **no**, stop this integration branch. Do **not** answer by proposing a new camera in the first approach.

If the answer is **yes**, request the eight calibration fields below, replace the declared simulator assumptions with the measured values, and rerun the frozen confusion model including latency.

## Publicly supported basis

The public Sqale record supports the narrow ask:
- array/tweezer spacing is 6 micrometres in the architecture paper;
- 80 atoms are grouped into ten blocks of eight in the Sept. 2026 report;
- blocks are prepared in `[[8,3,3]]` and operated downstream in `[[8,3,2]]`;
- loss correction reconstructs a missing X-basis outcome in software;
- the architecture paper explicitly states that one additional bit flip can miscorrect the inferred lost qubit.

The public sources do **not** provide:
- occupied/empty photon-count histograms;
- calibrated PSF / localization covariance;
- affine drift covariance;
- bad-frame/common-mode camera failure rate;
- second-view calibration or even confirmation that an independent second view exists;
- cross-view timing;
- the 30-logical-qubit imaging latency/calibration set.

## The eight requested fields

1. Occupied-site photon-count distribution.
2. Empty/background photon-count distribution.
3. Effective PSF or localization covariance.
4. Affine drift covariance + frame-to-frame correlation.
5. Common-mode bad-frame probability/signatures.
6. Second independent view or equivalent depth-observation availability + axis calibration.
7. Inter-view acquisition timing and total image/decision latency.
8. Small loss-labeled calibration set: no-loss + one missing atom at each of the eight sites.

## Hypothesis under test

The current internal geometry hypothesis remains:

```text
v_A = (1,0,0)
v_B = (0,2,3)/sqrt(13)
pair rescue separation = sqrt(3)/2 * a
```

That geometry is **not** the result being offered.

The result to be tested is whether a calibrated two-view presence/absence inference actually improves the operational loss decision after latency.

## Stop rule

Stop Gate 2 for Sqale if either:
- there is no second independent view/equivalent depth observation; or
- the calibrated simulator no longer improves the absence-plus-reconstruct/discard workflow at acceptable latency.

No Superstaq JSON/API proposal is authorized before both conditions pass.
