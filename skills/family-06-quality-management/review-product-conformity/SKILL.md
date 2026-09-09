---
name: review-product-conformity
description: Assess product conformity evidence against applicable specifications, inspection results, lot identity, and authorized acceptance rules without authorizing release.
license: MIT
---

# Review Product Conformity

## Overview

Assess whether supplied evidence addresses product requirements for incoming, in-process, or finished scope. Preserve supplier certificates, measured values, source conflicts, and unresolved requirements; do not authorize release.

**Taxonomy metadata:** family `06` Quality Management & Inspection; tier `CORE`; safety class `REGULATED`; jurisdiction `PENDING_CONTEXT` with `STANDARDS_DEPENDENT`, `SECTOR_REGULATED`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `review-quality-requirement`, `review-quality-record`, `STANDARDS`, `REVIEW`. Audit distinction: assess conformity across manufacturing stages; supplier evidence is scope input.

## Triggers

- Applicable specifications, inspection results, lot identity, authorized acceptance rules, stage, and evidence origin are supplied.

## Non-Triggers

- Product release, certificate approval, supplier acceptance, legal compliance, or inventing missing results.

## Required Inputs

- Applicable requirements and authorized acceptance rules.
- Inspection results, lot identity, stage, and source origin.

## Optional Inputs

- Supplier certificate, measurement records, deviations, rework, traceability, and reviewer.

## Assumptions

- A supplier certificate and measured result are separate evidence; conflict remains unresolved.
- Missing result is not a pass or zero defect.

## Core Workflow

1. Confirm requirement revision, lot/stage, source, acceptance rule, and result units.
2. Map each characteristic to evidence and identify pass/gap/conflict without deciding disposition.
3. Return evidence assessment, unresolved requirements, and authorized-owner handoff.

## Calculations

No calculation required beyond transparent comparison to supplied acceptance rules.

## Validation

- Check lot identity, stage, method, revision, units, source, and acceptance authority.
- Keep supplier and measured sources visible and do not infer conformance.

## Exception Handling

- Missing requirement or result returns `NEEDS_INPUT`.
- Source conflict returns `SOURCE_REVIEW_REQUIRED`.
- Release or certification returns `OUT_OF_SCOPE`/`SAFETY_ESCALATION` as applicable.

## Source Usage

- Use `references/conformity-review-checklist.md` and AM-07 source rules.
- Record source, revision, date, supplier/lot provenance, and permitted use.

## Output Contract

Return `status`, product/stage/lot scope, requirement map, evidence, conflicts, unresolved gaps, assumptions, validation notes, and disposition-owner handoff. Allowed statuses include `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, `SOURCE_REVIEW_REQUIRED`, and `SAFETY_ESCALATION`.

## Safety Requirements

AM-05 class: `REGULATED`. Do not approve release, certificate, disposition, or compliance.

## References

- `references/conformity-review-checklist.md`

## Examples

Read the checklist for conflicting supplier certificate and measured values.

## Testing

Cover correct invocation, missing results, supplier conflict, stage scope, expected output structure, and release refusal. Expected routing is not observed behavior.
