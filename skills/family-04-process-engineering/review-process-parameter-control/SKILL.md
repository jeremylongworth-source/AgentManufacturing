---
name: review-process-parameter-control
description: Review evidence against supplied approved process parameter limits and escalation procedures without designing new operating limits.
license: PENDING_PROJECT_GOVERNANCE
---

# Review Process Parameter Control

## Overview

Review monitoring records against approved parameter limits, control definitions, and escalation procedures. Distinguish observed settings from authorized limits and withhold compliance or process-control conclusions when the approval basis is missing.

**Taxonomy metadata:** family `04` Process and Industrial Engineering; tier `CORE`; safety class `ENGINEERING_OR_CERTIFICATION_BOUNDARY`; jurisdiction `PENDING_CONTEXT` with `STANDARDS_DEPENDENT`, `SECTOR_REGULATED`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `REVIEW`, `STANDARDS`. Audit distinction: check evidence against supplied limits; designing limits is excluded.

## Triggers

- Approved limits, monitoring records, control definitions, and escalation procedures are supplied for review.

## Non-Triggers

- Designing limits, changing machine settings, approving a control plan, or certifying compliance.

## Required Inputs

- Approved parameter limits and revision/effective basis.
- Monitoring records and control/escalation procedures.

## Optional Inputs

- Calibration evidence, alarm history, reaction owner, sector standard, and engineering signoff.

## Assumptions

- Observed machine settings are not approved limits.
- Missing limit authority or stale procedures prevent a definitive conclusion.

## Core Workflow

1. Confirm parameter, unit, limit revision, source, and monitoring period.
2. Compare records to supplied approved limits and map escalation evidence.
3. Return gaps and qualified engineering/standards handoff without proposing new limits.

## Calculations

No calculation required beyond transparent comparison of supplied values and limits.

## Validation

- Check unit, revision, calibration/source, monitoring coverage, and reaction owner.
- Separate observation, limit, exceedance, and compliance conclusion.

## Exception Handling

- Missing approved limits returns `NEEDS_INPUT`.
- Stale or standards-dependent basis returns `SOURCE_REVIEW_REQUIRED`.
- Setting changes, bypass, or certification return `ENGINEERING_REVIEW_REQUIRED` or `OUT_OF_SCOPE`.

## Source Usage

- Use `references/parameter-control-review.md` and the AM-07 source rules.
- Record source, revision, effective date, owner, and standards access/freshness.

## Output Contract

Return `status`, parameter scope, approved basis, observations, comparison, escalation gaps, assumptions, validation notes, and qualified handoff. Allowed statuses include `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, `SOURCE_REVIEW_REQUIRED`, and `ENGINEERING_REVIEW_REQUIRED`.

## Safety Requirements

AM-05 class: `ENGINEERING_OR_CERTIFICATION_BOUNDARY`. Do not design limits, change settings, bypass controls, or certify compliance; qualified engineering review is required.

## References

- `references/parameter-control-review.md`

## Examples

Read the reference for observed settings without an approved limit.

## Testing

Cover correct invocation, missing limits, stale source, standards dependency, unsafe setting-change request, expected output structure, and certification refusal. Expected routing is not observed behavior.
