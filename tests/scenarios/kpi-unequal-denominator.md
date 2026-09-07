# KPI unequal denominator

Category: `unit_mismatch`
Expected routing: `implemented:build-manufacturing-kpi-model`

Prompt:

> Build a manufacturing yield KPI model when two departments use different denominators and one excludes held material without documenting it.

Acceptance checks:

- Definitions and denominators remain distinct.
- No combined KPI result or target is published.

Risk and review notes:

- Metric governance must resolve the definition before comparison.
