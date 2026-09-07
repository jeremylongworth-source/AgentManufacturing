---
name: analyze-quality-kpis
description: Compare defined quality metrics using supplied counts, denominators, periods, targets, and population or supplier groupings.
license: PENDING_PROJECT_GOVERNANCE
---

# Analyze Quality KPIs

## Overview

Produce definition-based quality KPI comparisons with population, period, denominator, target, and supplier grouping visible. Flag unequal receipt exposure or noncomparable definitions; do not claim quality-system performance or supplier blame.

**Taxonomy metadata:** family `06` Quality Management & Inspection; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `CALC`. Audit distinction: own definition-based quality metric comparisons including supplier partitions.

## Triggers

- Defined quality metrics, counts/denominators, periods, comparable targets, and grouping dimensions are supplied.

## Non-Triggers

- Creating a metric definition, supplier corrective action, product release, or inferring quality from unequal exposure.

## Required Inputs

- Metric definition, numerator/denominator, period, target, and population/grouping basis.

## Optional Inputs

- Supplier/receipt exposure, product mix, lot, confidence interval request, and source owner.

## Assumptions

- Counts are comparable only when population, period, denominator, and definition align.
- Supplier defect totals with unequal receipts require exposure data before ranking.

## Core Workflow

1. Confirm metric definition, population, period, denominator, target, and grouping.
2. Calculate or compare supplied metrics with intermediate counts and comparability flags.
3. Return the analysis, gaps, and quality-owner handoff.

## Calculations

Apply the supplied definition, such as `defect rate = defects / exposed units`; preserve numerator, denominator, units, period, grouping, and rounding. Zero denominator returns `NEEDS_INPUT`.

## Validation

- Check denominator comparability, periods, product mix, supplier exposure, and target definition.
- Do not compare unequal receipt volumes without an exposure basis.
- Keep KPI analysis separate from cause, corrective action, and release.

## Exception Handling

- Missing definition or denominator returns `NEEDS_INPUT`.
- Noncomparable supplier exposure returns `PARTIAL`/`SOURCE_REVIEW_REQUIRED`.
- Corrective-action or release requests return `OUT_OF_SCOPE`.

## Source Usage

- Use `references/quality-kpi-checklist.md` and AM-08 calculation rules.
- Record source, period, population, definition owner, and target revision.

## Output Contract

Return `status`, metric definitions, populations, numerators/denominators, calculations, comparisons, exposure gaps, assumptions, validation notes, and handoff. Allowed statuses include `COMPLETE`, `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, and `SOURCE_REVIEW_REQUIRED`.

## Safety Requirements

AM-05 class: `ROUTINE`. Do not assign blame, approve supplier action, release product, or claim compliance.

## References

- `references/quality-kpi-checklist.md`

## Examples

Read the checklist for supplier defect totals with unequal receipt volumes.

## Testing

Cover calculation correctness, zero denominator, supplier exposure mismatch, period mismatch, expected output structure, and corrective-action/refusal boundaries. Expected routing is not observed behavior.
