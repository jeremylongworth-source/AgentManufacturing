---
name: analyze-cycle-time
description: Summarize measured cycle-time observations with explicit start/end definitions, product mix, sampling period, and observation-quality limits.
license: MIT
---

# Analyze Cycle Time

## Overview

Summarize supplied cycle observations for one operation, definition, product mix, and sampling period. Keep downtime, outliers, and observation quality visible; do not set takt or machine parameters.

**Taxonomy metadata:** family `05` Manufacturing Performance & Efficiency; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `CALC`. Audit distinction: summarize measured cycles; takt and machine operating parameters are separate.

## Triggers

- Cycle observations, start/end definition, product mix, and sampling period are supplied.

## Non-Triggers

- Takt calculation, capacity estimation, machine setting, or performance guarantee.

## Required Inputs

- Observations with units and start/end definition.
- Product mix and sampling period.

## Optional Inputs

- Downtime flags, percentile request, operator/asset, exclusions, and data-quality notes.

## Assumptions

- A downtime event included as a cycle is retained and its effect disclosed.
- One sample is not a stable process baseline.

## Core Workflow

1. Confirm observation definition, product mix, period, units, and exclusions.
2. Summarize count, central tendency/range or requested distribution, and data-quality limits.
3. Return the result and review handoff without creating a target.

## Calculations

Use supplied observations and requested summary method; preserve count, units, exclusions, and intermediate aggregation. Do not silently remove downtime or outliers.

## Validation

- Check start/end consistency, units, product mix, duplicate observations, and downtime definition.
- Flag small or biased samples and mixed products.

## Exception Handling

- Missing definition or period returns `NEEDS_INPUT`.
- Mixed cycle/downtime definitions return `SOURCE_REVIEW_REQUIRED`.
- Machine-target requests return `OUT_OF_SCOPE`.

## Source Usage

- Use `references/cycle-time-observation-checklist.md` and supplied records.
- Record observer, asset, period, source, and exclusions.

## Output Contract

Return `status`, operation/product scope, definition, sample, summary, units, exclusions, quality limits, assumptions, validation notes, and handoff. Allowed statuses include `COMPLETE`, `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, and `SOURCE_REVIEW_REQUIRED`.

## Safety Requirements

AM-05 class: `ROUTINE`. Do not set machine parameters, staffing, or production targets.

## References

- `references/cycle-time-observation-checklist.md`

## Examples

Read the checklist for a downtime event included in the cycle sample.

## Testing

Cover calculation correctness, downtime inclusion, mixed product, missing definition, expected output structure, and target-setting refusal. Expected routing is not observed behavior.
