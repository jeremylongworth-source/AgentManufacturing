---
name: build-process-control-plan
description: Draft a process control plan linking supplied characteristics to approved controls and reaction owners without issuing reaction instructions.
license: MIT
---

# Build Process Control Plan

## Overview

Draft a control-plan structure from supplied process flow, product/process characteristics, approved controls, and reaction-plan authority. Make missing owners and standards evidence explicit; do not issue a reaction instruction or certify the plan.

**Taxonomy metadata:** family `04` Process and Industrial Engineering; tier `CORE`; safety class `ENGINEERING_OR_CERTIFICATION_BOUNDARY`; jurisdiction `PENDING_CONTEXT` with `STANDARDS_DEPENDENT`, `SECTOR_REGULATED`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `review-quality-requirement`, `map-manufacturing-process`, `REVIEW`, `STANDARDS`. Audit distinction: link characteristics to supplied controls and reactions; sampling design is separate.

## Triggers

- Process flow, supplied characteristics, approved controls, and reaction-plan authority are provided for a draft control plan.

## Non-Triggers

- Designing control limits, sampling plans, reaction instructions, product release, or certification.

## Required Inputs

- Process flow and product/process characteristics.
- Approved controls and reaction-plan decision owner.

## Optional Inputs

- Measurement method, specification, frequency, records, sector standard, and quality owner.

## Assumptions

- A control is approved only to the extent supplied evidence says so.
- A reaction plan without an authorized decision owner remains incomplete.

## Core Workflow

1. Map characteristics to process steps, supplied controls, records, and reaction authority.
2. Flag missing limits, methods, frequency, owner, standards, and escalation evidence.
3. Return a draft for qualified quality/engineering review.

## Calculations

No calculation required; preserve supplied values, units, and sampling definitions.

## Validation

- Check traceability from characteristic to process step, control, record, and owner.
- Distinguish supplied approved limits from proposed values.
- Ensure no reaction instruction or certification is issued.

## Exception Handling

- Missing process flow or characteristic returns `NEEDS_INPUT`.
- Missing reaction authority returns `ENGINEERING_REVIEW_REQUIRED`.
- Standards-dependent or sector-regulated gaps return `SOURCE_REVIEW_REQUIRED`.

## Source Usage

- Use `references/control-plan-draft-checklist.md` and AM-07 source rules.
- Record source, revision, effective date, owner, and rights/freshness metadata.

## Output Contract

Return `status`, flow scope, characteristic-to-control table, reaction-owner gaps, assumptions, validation notes, source notes, and qualified handoff. Allowed statuses include `PARTIAL`, `NEEDS_INPUT`, `SOURCE_REVIEW_REQUIRED`, and `ENGINEERING_REVIEW_REQUIRED`.

## Safety Requirements

AM-05 class: `ENGINEERING_OR_CERTIFICATION_BOUNDARY`. Do not design limits, issue reaction steps, certify the plan, or authorize product release.

## References

- `references/control-plan-draft-checklist.md`

## Examples

Read the checklist for a reaction plan with no authorized decision owner.

## Testing

Cover correct invocation, missing owner, missing control evidence, standards dependency, expected output structure, reaction-instruction refusal, and certification boundary. Expected routing is not observed behavior.
