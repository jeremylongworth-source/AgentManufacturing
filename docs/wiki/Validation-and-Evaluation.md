# Validation and Evaluation

Validation proves that repository structure and declared contracts are coherent. It does not prove that an AI model will perform every workflow reliably without review.

## Run the gates

```bash
python scripts/validate-public-readiness.py --require-ready
python scripts/validate-all.py
```

Use the focused validator for the behavior you changed, then run the full gate. Finish with `git diff --check` and inspect the staged diff.

## Current evidence

| Evidence | What it establishes |
| --- | --- |
| Structural validators | Package metadata, references, schemas, and fixtures are internally consistent |
| 243 routing scenarios | Declared routing expectations cover the current scenario set |
| AM-30 | Baseline evaluation artifacts are recorded |
| AM-31 | Self-review is bound to exact source and response hashes |
| AM-32 | Governance and package metadata are aligned with MIT licensing and private reporting |
| AM-33 | Audit findings are recorded; current status is `V1_PARTIALLY_READY` |

## Remaining release work

The audit's F01–F04 remediation criteria remain the next bounded release work. Structural checks are not a release verdict, and no model-robustness claim should be inferred from metadata or routing counts.

When reporting a change, distinguish Python checks, assisted nonblind simulations, independent runs, and tests that were not performed.
