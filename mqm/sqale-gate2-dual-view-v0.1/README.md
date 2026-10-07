# MQM × Sqale Gate 2 — dual-view fluorescence certificate v0.1

**Status:** SIMULATION / HARDWARE CALIBRATION OPEN  
**Physical promotion:** 0

Gate 2 asks whether the exact MQM dual-view geometry can turn neutral-atom fluorescence into a more informative site certificate than a single image.

This is **not** a model of Infleqtion's private camera stack. Every image parameter below is declared explicitly.

## Exact geometric hypothesis

Use the MQM internal-frame view axes

[
v_A=(1,0,0),
qquad
v_B=(0,2,3)/sqrt{13}.
]

The exact geometry guarantees that every physical pair is separated by at least

[
d_{mathrm{rescue,min}}=rac{sqrt3}{2}a
]

in at least one view.

## Declared nominal imaging model

- Gaussian matched-filter PSF sigma: `0.25 a`
- Poisson shot noise: 100 signal-count equivalents per isolated occupied site
- background: 1 count per matched-filter channel
- correlated affine drift per view:
  - translation RMS `0.04 a`
  - shear RMS `2%`
  - scale RMS `1%`
  - rotation RMS `1°`
- shared/common camera failure: `0.2%`
- additional independent failure per view: `0.8%`
- physical states: `NO_LOSS` or exactly one true lost site
- decoder: nine Poisson-likelihood hypotheses
- likelihood gap < 9: `AMBIGUOUS / HOLD`

## Nominal class-balanced result

45,000 dual-view trials:

| Readout | Correct | Ambiguous/HOLD | Wrong |
|---|---:|---:|---:|
| View A only | 76.871% | 23.104% | 0.024% |
| View B only | 76.956% | 23.040% | 0.004% |
| Dual fused | **99.429%** | **0.569%** | **0.0022%** |

The single-view ambiguity is dominated by deterministic projection overlap. The dual view does real information work in this declared model.

## Working engineering criterion

This simulation gate uses:
- wrong fused certificate < `0.1%`;
- ambiguous/HOLD < `2%`;
- dual accepted fraction improves by at least 10 percentage points over the best single view.

The nominal dual simulation passes those **simulation-only** criteria.

## What is still open

Before wiring this into Superstaq, hardware calibration must supply:
- actual fluorescence PSF / localization error;
- shot-count distribution and background;
- camera/readout common-mode failure;
- cross-view calibration drift;
- imaging latency and whether the two views share one admission epoch;
- false loss, missed loss, and reimage/HOLD cost.

See:
- `protocol/GATE2_DECLARED_IMAGING_MODEL_v0.1.json`
- `results/GATE2_CONFUSION_DUAL_v0.1.csv`
- `protocol/MIDCIRCUIT_FLUORESCENCE_REQUIREMENT_ONE_PAGER_v0.1.md`

## Stop rule

If the hardware-calibrated certificate cannot keep wrong fused declarations below the preregistered limit without unacceptable HOLD/reimage overhead, do **not** wire it into Superstaq. Retain dual-view geometry only as an internal layout/readout constraint.
