# AM-08 final handoff — calculation standard

## Wave

AM-08: Calculation standard

## Objective

Define a unit-safe, reviewable calculation contract before quantitative manufacturing skills scale. Cover variables, units, formulas, assumptions, rounding, missing inputs, edge cases, and worked fixtures.

## Verdict

**READY** for AM-08. The calculation contract and worked fixtures are defined and validated. The validator recomputes reference arithmetic with decimal precision, but no implemented skill or model behavior was evaluated.

## Completion token

```text
AGENTMANUFACTURING_AM_08_CALCULATION_STANDARD_READY
```

## Scope completed

- Defined calculation-record fields for purpose, scope, variables, source/origin, normalization, formula, assumptions, intermediate values, results, rounding, validation, and review handoff.
- Defined supported unit dimensions, canonical units, visible conversions, compound time-per-count units, and incompatible-unit handling.
- Defined ten reference formulas: takt time, gross capacity, OEE, first-pass yield, scrap rate, MTBF, MTTR, Cp, Cpk, and X-bar control limits.
- Defined assumptions and interpretation boundaries, including the separation of control limits from specification limits and raw arithmetic from operational recommendations.
- Defined missing-input, invalid-input, zero-denominator, stale-evidence, unstable-process, and rounding behavior.
- Defined precision and rounding policies, including explicit rules for countable operating quantities and separation of raw and rounded values.
- Added seventeen worked fixtures covering all reference formulas, unit conversion, missing data, invalid sigma, zero denominators, edge cases, and countable-result rounding.
- Added a deterministic validator that checks contract structure, recomputes fixture arithmetic, and preserves AM-08's implementation boundary.

## Files added

- `docs/architecture/calculation-standard.md` — authoring and output standard for quantitative manufacturing work.
- `docs/architecture/calculation-contract.json` — machine-readable calculation, units, validation, formula, and rounding contract.
- `docs/architecture/calculation-fixtures.json` — seventeen worked and failure fixtures.
- `scripts/validate-calculation-standard.py` — dependency-free validator and Decimal-based fixture checker.

## Files modified

- `README.md` — AM-08 artifacts, validation command, current status, and AM-09 next-wave pointer.
- `ROADMAP.md` — version 1.0, AM-08 READY status, artifacts, and AM-09 next target.
- `docs/architecture/domain-contract.md` — AM-08 calculation pointer and authority boundary.

## Reference inspection

The local AgentLogistics calculation and testing standards were read as architectural references. The portable ideas reused here are explicit variables and units, visible normalization, formula names, intermediate values, final rounding, missing-input behavior, and worked fixtures. No logistics procedure, threshold, private data, or source-specific operational rule was copied into AgentManufacturing.

## Validation performed

```text
python scripts/validate-calculation-standard.py
PASS: AM-08 calculation standard; 10 reference formulas; 17 worked fixtures; 9 unit dimensions; 8 rounding policies; numeric fixture values, failure states, and output invariants checked; no skill behavior evaluated.

python scripts/validate-source-standards-standard.py
PASS: AM-07 source and standards standard; 9 source classes; 5 precedence ranks; 5 jurisdiction systems; 6 example records; 8 freshness states; 22 legacy AM-04/05 source records compatible; 12 acceptance scenarios; no source fetched or legal applicability evaluated.

python scripts/validate-skill-authoring-standard.py
PASS: AM-06 authoring standard; package layout, frontmatter, 16 ordered sections, host metadata, references, output contract, 4 validation layers, 11 scenario categories, and templates verified; no skill implementation or host installation evaluated.

python scripts/validate-safety-boundary-model.py
PASS: AM-05 model; 4 classes; 9 topic gates; 14 source records; 12 acceptance scenarios; AM-03 safety counts preserved (95/28/11/25); no safety approval, engineering signoff, or skill behavior evaluated.

python scripts/validate-jurisdiction-model.py
PASS: AM-04 model; 4 flags; 5 applicability states; 8 source records; 5 initial extensions; 7 acceptance scenarios; no legal applicability or skill behavior evaluated.

python scripts/validate-taxonomy.py
PASS: 159 accepted records; 162 drafts audited across eight criteria; 166 original names traced; 76 ordered evidence-reuse edges; core isolation, reference priorities, pending classifications and all document projections verified. No skill behavior evaluated.

python scripts/validate-candidate-register.py
PASS: 162 draft candidates; 20 families; 166 original names traced; fields, metadata, provenance, dependency references/cycles, core isolation, AM-10 priorities, and review index checked.
```

## Known limitations

- Fixture arithmetic checks the contract's stated formulas, not whether a formula is appropriate for a specific plant, asset, product, or observation window.
- Unit conversion support is intentionally narrow; temperature offsets, currency, density, case packs, pallets, and other conversions need explicit implementation data.
- Cp, Cpk, OEE, MTBF, MTTR, and control-limit interpretation requires process definitions, stable evidence, and qualified review where applicable.
- AM-09 owns executable routing, scenario validation, and broader test orchestration; AM-10 remains the gate for reference skills and mass authoring.

## Explicitly not completed

AM-09 executable validation, AM-10 reference skills, family implementation, sector packages, professional skillsets, integration, and public release work remain open. Mass authoring remains gated on AM-10.

## Recommended next wave

Proceed to AM-09. Implement the executable validation framework using AM-06 scenario categories, AM-07 source/freshness cases, and AM-08 calculation fixtures. Keep expected routing separate from observed model behavior and fail unsafe approval claims, hidden assumptions, wrong calculations, and silent unit mismatches.
