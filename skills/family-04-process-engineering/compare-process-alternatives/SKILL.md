---
name: compare-process-alternatives
description: Compare supplied process concepts against product requirements, capacity, quality, and resource evidence for engineering review.
license: MIT
---

# Compare Process Alternatives

## Overview

Create an engineering-review tradeoff table for supplied process concepts. Check requirements, capacity, quality-validation evidence, resources, and gaps; do not select, certify, or implement a concept.

**Taxonomy metadata:** family `04` Process and Industrial Engineering; tier `CORE`; safety class `ENGINEERING_OR_CERTIFICATION_BOUNDARY`; jurisdiction `PENDING_CONTEXT` with `SECTOR_REGULATED`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `REVIEW`. Audit distinction: compare engineering concepts; automation-technology assessment is narrower.

## Triggers

- Alternative process concepts, product requirements, and capacity, quality, and resource evidence are supplied.

## Non-Triggers

- Detailed design, validation approval, automation selection, production release, or capital commitment.

## Required Inputs

- Alternative process concepts and product requirements.
- Capacity, quality-validation, and resource evidence.

## Optional Inputs

- Cost, safety, maintenance, tooling, sector requirements, and implementation risks.

## Assumptions

- A concept lacking validation evidence remains unproven and is not equivalent by default.
- Missing cost or quality data remains unknown.

## Core Workflow

1. Normalize the common product requirement, horizon, units, and comparison criteria.
2. Compare concepts, flag infeasibility or missing validation, and preserve tradeoffs.
3. Return an engineering-review package and decision owner.

## Calculations

Use only supplied arithmetic and criteria; preserve units and assumptions. Do not model unprovided performance.

## Validation

- Check common requirements, capacity basis, quality evidence, resources, and sector context.
- Reject equivalence claims when validation evidence is absent.

## Exception Handling

- Missing product requirement returns `NEEDS_INPUT`.
- Sector or engineering review gaps return `ENGINEERING_REVIEW_REQUIRED`.
- Implementation or capital approval returns `OUT_OF_SCOPE`.

## Source Usage

- Use `references/process-alternative-review.md` and supplied concept evidence.
- Record source, revision, owner, and standards/sector dependencies.

## Output Contract

Return `status`, common basis, concept comparison, feasibility/validation gaps, assumptions, validation notes, and engineering handoff. Allowed statuses include `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, `SOURCE_REVIEW_REQUIRED`, and `ENGINEERING_REVIEW_REQUIRED`.

## Safety Requirements

AM-05 class: `ENGINEERING_OR_CERTIFICATION_BOUNDARY`. Do not select, approve, certify, or implement a process concept.

## References

- `references/process-alternative-review.md`

## Examples

Read the reference for a concept missing quality-validation evidence.

## Testing

Cover correct invocation, missing requirements, absent validation, sector review, expected output structure, and implementation refusal. Expected routing is not observed behavior.
