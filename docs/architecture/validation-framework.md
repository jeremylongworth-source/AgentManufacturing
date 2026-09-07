# AM-09 executable validation framework

## Purpose and status

This framework turns the AM-06 validation contract into reviewable repository evidence. It validates structure, expected routing, deterministic calculation fixtures, and evaluation-report shape. It deliberately separates expected routing from observed model behavior and keeps all future skill routes labeled as future coverage until AM-10 proves reference skills.

Status: `FRAMEWORK_READY_NOT_IMPLEMENTED`.

The machine-readable contract is [validation-framework-contract.json](validation-framework-contract.json). The routing manifest is [tests/expected-routing.yaml](../../tests/expected-routing.yaml), the fixture manifest is [tests/fixtures/am09-fixture-manifest.json](../../tests/fixtures/am09-fixture-manifest.json), and the evaluation form is [AM-09-evaluation-template.md](../../tests/evaluations/AM-09-evaluation-template.md).

## Validation layers

| Layer | What it checks | Current evidence |
| --- | --- | --- |
| Structural | Contract versions, required fields, scenario files, manifests, privacy guardrails, and output invariants | `scripts/validate-validation-framework.py` |
| Scenario routing | Scenario categories, expected route syntax, no-trigger cases, future-coverage labels, and one-to-one manifest coverage | `tests/scenarios/*.md`, `tests/expected-routing.yaml` |
| Deterministic fixture | AM-08 formula arithmetic, units, intermediate values, tolerances, rounding, and failure states | `docs/architecture/calculation-fixtures.json`, `tests/fixtures/am09-fixture-manifest.json`, `scripts/validate-calculation-standard.py` |
| Evaluation report | Separate expected routing, baseline observations, skill-enabled observations, reviewer disposition, and residual risk | `tests/evaluations/AM-09-evaluation-template.md` |

The AM-09 validator is an offline contract runner. It does not call a model, install a host, fetch external sources, or claim that a future route works. When implemented skills exist, a later execution layer can add model runs while preserving the same manifest and evidence distinctions.

## Scenario routing

Each scenario file contains a title, category, expected routing, prompt, acceptance checks, and risk/review notes. Prompts describe a realistic manufacturing job without private data, credentials, live-system requirements, or the answer itself. High-risk scenarios explicitly test safety, engineering, jurisdiction, source freshness, or authority boundaries.

The manifest uses:

- `expected_routes` for implemented skill folders;
- `future_routes` for planned skill names before the package exists;
- `route_mode` of `IMPLEMENTED`, `FUTURE_COVERAGE`, or `NO_TRIGGER`; and
- `expected_outcome` such as `NEEDS_INPUT`, `SAFETY_ESCALATION`, `SOURCE_REVIEW_REQUIRED`, or `JURISDICTION_REVIEW_REQUIRED`.

An empty route means the target must not trigger. A future route is a coverage target, not a model result. The validator rejects an implemented route that does not resolve to an existing skill folder and rejects a future route that is not declared in the manifest's future skill list.

The twelve scenarios cover all eleven AM-06 categories, with two separate safety-boundary cases for unsafe restart and unsupported engineering signoff. They include a wrong logistics invocation, missing OEE data, contradictory runtime, incompatible units, mixed product/workplace jurisdiction, stale policy, deterministic OEE fixture, ambiguous metric request, and output-structure request.

## Deterministic fixture execution

The AM-09 fixture manifest references the AM-08 fixture source instead of copying it. The validator loads the AM-08 contract and recomputes its seventeen Decimal-based fixtures. The required categories are calculation correctness, unit mismatch, missing inputs, bad inputs, zero denominator, and rounding.

Fixture checks require explicit numeric tolerances, expected intermediate values, raw and rounded results when relevant, units, missing fields, invalid fields, and review flags. A fixture pass proves the stated arithmetic and contract shape only; it does not prove that the formula or data boundary is appropriate for a plant.

## Evaluation evidence

The evaluation template starts at `NOT_RUN`. It requires a scenario or skill scope, version, environment, expected route, baseline observation, skill-enabled observation, failure modes, reviewer disposition, and residual risk. It states that expected routing is not observed behavior and prohibits invented baseline or skill-enabled output.

When AM-10 reference skills are available, reviewers may add observed evaluation reports without changing the expected-routing manifest. A single unsafe approval claim, hidden assumption, silent unit mismatch, wrong calculation, unsupported source-dependent claim, or missing review boundary fails the relevant evaluation.

## Release gates

AM-09 is ready only when:

1. the AM-06, AM-07, AM-08, and AM-09 structural validators pass;
2. all eleven scenario categories have coverage;
3. every scenario file appears exactly once in the routing manifest;
4. implemented routes resolve to real skill folders and future routes are labeled;
5. AM-08 deterministic fixtures pass with explicit tolerances;
6. evaluation forms distinguish expected, baseline, and skill-enabled evidence; and
7. no committed scenario contains private data, credentials, live-system requirements, unsafe approval language as an expected success, or silent unit conversion.

## Implementation boundary

AM-09 validates artifacts and deterministic evidence. It does not implement manufacturing skills, prove model routing, select a licence, fetch legal or standards sources, approve engineering or safety work, or remove the AM-10 hard gate. AM-31 remains the owner of adversarial safety evaluation after reference skills exist.

## Completion token

```text
AGENTMANUFACTURING_AM_09_VALIDATION_FRAMEWORK_READY
```
