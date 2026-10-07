# What mid-circuit fluorescence must resolve for the MQM dual-view certificate

**Status:** SIMULATION-DERIVED REQUIREMENT NOTE  
**Physical promotion:** 0  
**Target integration:** Sqale/Superstaq-style loss-aware execution

## Hypothesis

Use native MQM 3D site identity plus two orthogonal fluorescence receipts:

[
v_A=(1,0,0),
qquad
v_B=(0,2,3)/sqrt{13}.
]

The exact geometry guarantees at least

[
rac{sqrt3}{2}a
]

pair separation in one of the two views for every physical qubit pair.

## Declared model

This note is **not fitted to Sqale's private camera**.

Nominal assumptions:
- Gaussian PSF sigma `0.25a`;
- 100 detected-count equivalents per isolated atom;
- affine image drift: `0.04a` translation RMS, 2% shear RMS, 1% scale RMS, 1° rotation RMS;
- 0.2% shared camera/common-control failure;
- 0.8% additional independent failure per view;
- true class = no loss or exactly one lost site;
- `AMBIGUOUS` instead of forcing identity.

## Nominal result

45,000 class-balanced dual-view trials:
- correct certificate: **99.429%**
- ambiguous / HOLD: **0.569%**
- wrong declaration: **0.0022%**

Single-view correct fraction is only about **77%**, because one projection can make distinct sites geometrically indistinguishable.

## Working requirements before Superstaq integration

A hardware calibration should demonstrate simultaneously:

1. **Spot resolution:** effective matched-filter PSF around or below `0.4a` sigma in this model; the `0.45a` screen approaches the declared ambiguity/wrong-certificate boundary.
2. **Localization/drift:** combined affine drift around or below the nominal envelope. Roughly 2× that envelope begins to generate `10^-3`-scale wrong certificates in the exploratory screen.
3. **Shot statistics:** at least a few tens of detected-count equivalents per occupied site in the current model.
4. **Camera health:** blank/saturated/invalid frames become `HOLD`, never `ABSENT`.
5. **Cross-view common mode:** directly measure shared failure. Two views are not independent merely because they use two projection axes.
6. **Loss semantics:** deterministic overlap maps to `AMBIGUOUS/OVERLAP`, never directly to physical loss.
7. **Freshness:** both views must refer to the same admission epoch or carry a motion model; motion between exposures can mimic loss or duplication.

## Proposed Superstaq-facing record

```text
SITE_CERTIFICATE {
  block_id,
  epoch,
  site_id_3d,
  view_A_health,
  view_B_health,
  view_A_likelihood,
  view_B_likelihood,
  fused_state = PRESENT | ABSENT | AMBIGUOUS,
  drift_fit,
  confidence_gap,
  action = PASS | HOLD | REIMAGE | LOSS_PATH
}
```

## Stop rule

If hardware-calibrated fluorescence cannot keep wrong fused certificates below the preregistered limit without unacceptable HOLD/reimage overhead, **do not wire the certificate into Superstaq**.
