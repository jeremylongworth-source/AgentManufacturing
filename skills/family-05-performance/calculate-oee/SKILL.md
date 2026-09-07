---
name: calculate-oee
description: Calculate availability, performance, quality, and OEE from supplied production evidence while preserving units and data gaps.
license: PENDING_PROJECT_GOVERNANCE
---

# Calculate OEE

## Overview

This reference skill produces one bounded OEE analysis for a named asset and time period. It reports availability, performance, quality, OEE, normalized inputs, and validation flags without claiming production approval or improving the source data.

**Taxonomy metadata:** family `05` Manufacturing Performance & Efficiency; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P0`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED` before AM-10 reference proof. Dependencies: `CALC`. Audit distinction: return one availability/performance/quality measure with explicit bases; input-data reconciliation remains separate.

## Triggers

- The user supplies planned production time, stop time or run time, ideal cycle time, total count, good count, units, and a period for one asset or line.
- The user requests OEE or one of its three component measures for a bounded period.

## Non-Triggers

- OEE data extraction, MES/ERP writes, downtime-cause reconciliation, or a multi-asset KPI data model.
- Takt-time, capacity planning, maintenance diagnosis, quality-system certification, or a decision to change production controls.

## Required Inputs

- Asset or line identifier and reporting period.
- Planned production time and stop time, or a supplied run-time value with its definition.
- Ideal cycle time and its unit per produced unit.
- Total count and good count with a common unit.

## Optional Inputs

- Data source and timestamp, product or part number, shift, reason-code mapping, and requested rounding precision.
- An explicit explanation for planned stops and whether rework is included in good count.

## Assumptions

- Time values are converted only when their units are explicit; original values and units remain visible.
- `run_time = planned_production_time - stop_time` only when both terms share a period and stop-time definition.
- No value is imputed, clamped, or silently treated as zero. Counts must describe the same population and period.

## Core Workflow

1. Confirm asset, period, definitions, units, and source evidence.
2. Normalize time, cycle-time, and count units; calculate intermediates and preserve the supplied values.
3. Check impossible or contradictory inputs, then return the result, assumptions, gaps, and review boundary.

## Calculations

- `run_time = planned_production_time - stop_time` when run time is not directly supplied.
- `availability = run_time / planned_production_time`.
- `performance = (ideal_cycle_time × total_count) / run_time`.
- `quality = good_count / total_count`.
- `oee = availability × performance × quality`.
- Keep units explicit, retain intermediate values, and apply the requested rounding only after calculation. A zero denominator yields `NEEDS_INPUT`; do not manufacture a percentage.

## Validation

- Require positive planned time, non-negative stop time, positive run time, positive ideal cycle time, and non-negative counts.
- Reject `good_count > total_count`, `stop_time > planned_production_time`, mixed periods, incompatible units, or duplicated count populations.
- Flag component results outside the ordinary `[0, 1]` range for review; do not hide the unbounded supplied evidence or silently clamp it.

## Exception Handling

- Missing or ambiguous definitions return `NEEDS_INPUT` with the exact field requested.
- Contradictory values return `NEEDS_INPUT` and identify the conflicting evidence.
- A stale or unverified source returns `SOURCE_REVIEW_REQUIRED` when source freshness affects the conclusion.
- Requests for live control, release, certification, or a target-setting decision return `OUT_OF_SCOPE` with a handoff.

## Source Usage

- Use `docs/architecture/calculation-standard.md`, `docs/architecture/calculation-contract.json`, and the local OEE reference for formula and evidence conventions.
- Use external sources only when the user asks for a definition comparison or the supplied source is ambiguous; record publisher, title, URL or local path, access date, and freshness rule.
- Do not copy protected standards text. Cite or paraphrase only the minimum needed for the calculation.

## Output Contract

Return a record containing `status`, scope, asset and period, supplied and normalized inputs, formula, intermediates, component results, OEE result, assumptions, validation notes, missing or conflicting evidence, and review/handoff. Allowed statuses are `COMPLETE`, `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, `SOURCE_REVIEW_REQUIRED`, and `ENGINEERING_REVIEW_REQUIRED`.

## Safety Requirements

AM-05 class: `ROUTINE`. Analysis is draft-only. Do not issue operating instructions, alter controls, release product, certify compliance, or make a business commitment. Escalate if the request turns the metric into a safety, regulatory, or production authorization.

## References

- `references/oee-formula.md`
- `docs/architecture/calculation-standard.md`
- `docs/architecture/calculation-fixtures.json`

## Examples

Read `references/oee-formula.md` for a worked, bounded example and invalid-input cases. The example is evidence structure, not observed model behavior.

## Testing

Cover correct invocation, incorrect invocation, missing inputs, bad inputs, calculation correctness, unit mismatch, ambiguous scenario, expected output structure, unsupported assumptions, and output safety. Run AM-08 OEE fixtures, including the `good_count > total_count` rejection. Expected routing is not observed behavior.
