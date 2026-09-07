---
name: audit-quality-process
description: Assess a scoped quality process against supplied criteria and sample records while limiting findings to the evidence coverage.
license: PENDING_PROJECT_GOVERNANCE
---

# Audit Quality Process

## Overview

Create an evidence-linked gap report for one quality-process scope, criterion set, sample, and prior-finding context. State coverage limits and do not claim certification or whole-company assurance.

**Taxonomy metadata:** family `06` Quality Management & Inspection; tier `CORE`; safety class `REGULATED`; jurisdiction `PENDING_CONTEXT` with `STANDARDS_DEPENDENT`, `SECTOR_REGULATED`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `STANDARDS`, `REVIEW`. Audit distinction: assess evidence against scoped criteria; it is not certification or QMS redesign.

## Triggers

- Quality-process scope, applicable criteria, sample records, and prior findings are supplied for a review.

## Non-Triggers

- Certification audit, legal compliance determination, whole-company QMS redesign, or corrective-action approval.

## Required Inputs

- Process scope and applicable criteria/revisions.
- Sample records, period/coverage, and prior findings.

## Optional Inputs

- Interview notes, process owner, sample method, corrective actions, and sector overlay.

## Assumptions

- A sample covering one shift cannot support plant-wide assurance.
- A gap finding is tied to supplied criteria and evidence, not a generic judgment.

## Core Workflow

1. Confirm scope, criterion source/revision, sample coverage, and prior findings.
2. Map evidence to criteria and classify findings, exclusions, and coverage limits.
3. Return a gap report and qualified quality-system handoff.

## Calculations

No calculation required unless a supplied sample rule is explicitly applied; preserve its basis.

## Validation

- Check criteria applicability, sample coverage, record integrity, source freshness, and finding traceability.
- Limit conclusions to the sampled scope and period.

## Exception Handling

- Missing criteria or sample coverage returns `NEEDS_INPUT`.
- Standards conflict returns `SOURCE_REVIEW_REQUIRED`.
- Certification or legal-assurance requests return `OUT_OF_SCOPE`.

## Source Usage

- Use `references/quality-process-audit-checklist.md` and AM-07 source rules.
- Record publisher/owner, revision, effective date, sample period, and permitted use.

## Output Contract

Return `status`, audit scope, criteria, evidence sample, findings, coverage limits, prior findings, assumptions, validation notes, and qualified owner handoff. Allowed statuses include `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, `SOURCE_REVIEW_REQUIRED`, and `ENGINEERING_REVIEW_REQUIRED`.

## Safety Requirements

AM-05 class: `REGULATED`. Do not certify, issue an audit approval, or claim plant-wide compliance.

## References

- `references/quality-process-audit-checklist.md`

## Examples

Read the checklist for a one-shift sample with limited coverage.

## Testing

Cover correct invocation, missing criteria, narrow sample, stale source, expected output structure, and certification refusal. Expected routing is not observed behavior.
