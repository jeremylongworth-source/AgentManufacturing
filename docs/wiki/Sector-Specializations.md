# Sector specializations

The [sector registry](https://github.com/jeremylongworth-source/AgentManufacturing/blob/main/specializations/registry.json) is a planning framework. **No sector requirement packages are implemented.** Its labels and priorities are not claims of automotive, aerospace, food, medical-device or other sector compliance.

## Inspect coverage

```powershell
python scripts/inspect-sector-coverage.py automotive
python scripts/inspect-sector-coverage.py automotive --generic-only
```

A coverage gap means the repository cannot supply the requested sector requirements. Generic-only mode allows sector-neutral analysis and retains that gap; it does not waive requirements.

## What a future specialization needs

The registry requires explicit product/process and market scope, applicability evidence, requirement deltas, source records, authorized standards access, review ownership, acceptance cases and observed evaluation. Preserve missing and conflicting evidence. Reference canonical core methods rather than copying them.

Propose a bounded specialization through [[Contributing and Maintenance|Contributing-and-Maintenance]]. A planned entry must not be promoted solely because its metadata validates.
