# Validation and evaluation

Run these commands from the repository root:

```powershell
python scripts/validate-all.py
python scripts/validate-public-readiness.py --require-ready
git diff --check
```

The full gate runs 32 repository validators. It covers contracts, package metadata, synthetic calculations, expected routing and recorded acceptance evidence. The [CI workflow](https://github.com/jeremylongworth-source/AgentManufacturing/blob/main/.github/workflows/validate.yml) runs on Linux and Windows with Python 3.14. [AM-33 CI evidence](https://github.com/jeremylongworth-source/AgentManufacturing/blob/main/docs/development/AM-33-ci-evidence.json) records historical runs against exact commits.

## Interpret the results

| Evidence | What it establishes | Limit |
|---|---|---|
| Structural validators | Repository consistency | No independent model execution |
| 243 routing scenarios | Authored expectations | Not observed routing accuracy |
| AM-30 walkthroughs | Four assisted integration examples | Nonblind, self-reviewed |
| AM-31 paired cases | Eight adversarial cases and eight safe controls | Not independent robustness testing |
| AM-32 strict readiness | Documented governance prerequisites | Not report delivery or a stable-release verdict |

Independent model runs, baseline comparisons, repeated trials and multi-turn robustness remain unperformed. The AM-33 verdict is V1_PARTIALLY_READY.

## Changing evidence

Run the focused validator first, then the full gate. Report actual commands and outcomes. AM-31 hashes bind judgments to exact artifacts: reassess affected judgments before updating a digest. Do not regenerate a hash just to silence a failure. Use synthetic fixtures and preserve historical results.
