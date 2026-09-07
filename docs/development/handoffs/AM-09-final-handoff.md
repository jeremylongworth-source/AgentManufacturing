# AM-09 final handoff — executable validation framework

## Wave

AM-09: Validation framework

## Objective

Turn the AM-06 validation contract into runnable repository evidence for structural checks, expected routing, deterministic calculation fixtures, and evaluation reports before AM-10 reference skills.

## Verdict

**READY** for AM-09. The framework, manifests, scenario suite, fixture mapping, evaluation template, and aggregate validation gate are defined and pass offline validation. No model was called, no skill package was installed, and no expected route was reported as observed behavior.

## Completion token

```text
AGENTMANUFACTURING_AM_09_VALIDATION_FRAMEWORK_READY
```

## Scope completed

- Defined four executable evidence layers: structural, scenario routing, deterministic fixture, and evaluation report.
- Added a machine-readable framework contract with eleven required scenario categories, routing modes, release gates, fixture rules, and evaluation safeguards.
- Added twelve realistic scenarios covering all eleven AM-06 categories, including wrong routing, missing data, contradictory inputs, incompatible units, safety escalation, jurisdiction separation, stale-source review, engineering signoff refusal, deterministic calculation, ambiguity, and output structure.
- Added a JSON-compatible routing manifest under `tests/expected-routing.yaml`; future routes are labeled and no implemented route is claimed.
- Added a fixture manifest that maps all seventeen AM-08 fixtures without duplicating numeric data.
- Added an evaluation template that separates expected routing, baseline behavior, skill-enabled behavior, reviewer disposition, and residual risk.
- Added an aggregate `validate-all.py` gate that runs all eight dependency-free validators in order.
- Added privacy and prompt checks for scenario files and route-folder checks for any future implemented route.

## Files added

- `docs/architecture/validation-framework.md` — AM-09 framework, evidence layers, release gates, and boundaries.
- `docs/architecture/validation-framework-contract.json` — machine-readable framework and scenario contract.
- `tests/expected-routing.yaml` — twelve-scenario routing manifest with explicit future coverage.
- `tests/scenarios/*.md` — twelve scenario prompts and acceptance checks.
- `tests/fixtures/am09-fixture-manifest.json` — AM-08 fixture mapping.
- `tests/evaluations/AM-09-evaluation-template.md` — observed-evidence template starting at `NOT_RUN`.
- `scripts/validate-validation-framework.py` — framework, scenario, manifest, and AM-08 integration validator.
- `scripts/validate-all.py` — aggregate validation gate.

## Files modified

- `README.md` — AM-09 artifacts, scenario/fixture links, validation commands, status, and AM-10 pointer.
- `ROADMAP.md` — version 1.1, AM-09 READY status, artifacts, and AM-10 next target.
- `docs/architecture/domain-contract.md` — AM-09 evidence-layer pointer and implementation boundary.
- `tests/scenarios/incorrect-invocation.md` — kept the logistics handoff scenario as a draft-only request with no live-system execution.

## Reference inspection

The local AgentSkills/AgentLogistics validation patterns and the project AM-06/AM-08 contracts were used as architectural references. The framework keeps expected routing separate from observed behavior, uses explicit fixture tolerances, and preserves safety/jurisdiction/source boundaries. No private data, live connector requirement, logistics procedure, or protected source text was added.

## Validation performed

```text
python scripts/validate-validation-framework.py
PASS: AM-09 validation framework; 12 scenarios across 11 categories; 17 AM-08 fixtures mapped; four validation layers; future routes labeled, evaluation evidence separated, and no model behavior evaluated.

python scripts/validate-all.py
PASS: all 8 repository validators completed.
```

The aggregate gate also passed the AM-00 through AM-08 validators for the candidate register, taxonomy, jurisdiction model, safety boundary model, skill authoring standard, source/standards standard, and calculation standard.

## Known limitations

- Future routes are declared coverage targets; no model-routing quality is proven until AM-10 reference skills exist.
- The validator is offline and does not call a model, resolve external sources, or validate a host integration.
- Scenario prompts and deterministic fixtures test contract behavior; they do not establish plant facts, legal applicability, site safety, engineering adequacy, or process suitability.
- Evaluation reports remain `NOT_RUN` until a reference skill and reviewer-owned run exist.

## Explicitly not completed

AM-10 reference skills, family implementation, sector packages, professional skillsets, integration, safety adversarial evaluation, and public release work remain open. Mass authoring remains gated on AM-10.

## Recommended next wave

Proceed to AM-10. Implement and validate one reference skill from each major class—`calculate-oee`, `build-production-plan`, `triage-nonconformance`, `review-lockout-program`, and `assess-made-in-canada-claim`—using the AM-06 package contract, AM-07 source rules, AM-08 calculation fixtures, and AM-09 evidence gates. Do not bulk-author before all five reference classes pass review.
