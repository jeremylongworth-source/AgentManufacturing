---
name: build-inspection-plan
description: Draft an incoming, in-process, or final inspection plan from supplied characteristics, limits, sampling basis, measurement methods, and lot context.
license: PENDING_PROJECT_GOVERNANCE
---

# Build Inspection Plan

## Overview

Draft a stage-scoped inspection plan while preserving supplier/lot context, acceptance evidence, sampling authority, and measurement-method gaps. Do not invent a sample size or approve product.

**Taxonomy metadata:** family `06` Quality Management & Inspection; tier `CORE`; safety class `REGULATED`; jurisdiction `PENDING_CONTEXT` with `STANDARDS_DEPENDENT`, `SECTOR_REGULATED`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `review-quality-requirement`, `select-measurement-method`, `STANDARDS`, `REVIEW`, `LOGISTICS`. Audit distinction: own inspection-plan generation for incoming, in-process, and finished product.

## Triggers

- Characteristics, acceptance limits, lot/process scope, approved sampling basis, measurement methods, inspection stage, and supplier provenance are supplied.

## Non-Triggers

- Inventing sampling, accepting a supplier lot, product release, measurement-method selection, or inspection execution.

## Required Inputs

- Characteristics and acceptance limits.
- Lot/process scope, stage, approved sampling basis, and measurement methods.
- Supplier/receipt provenance when incoming.

## Optional Inputs

- Inspection records, calibration, operator qualification, reaction owner, and requirement revision.

## Assumptions

- Missing sample basis remains missing; no standard sample size is inferred.
- Stage and supplier context remain visible and are not silently substituted.

## Core Workflow

1. Confirm stage, lot, characteristic, limit, method, sampling authority, and provenance.
2. Structure the plan and flag missing limits, methods, sampling, records, and reaction ownership.
3. Return a draft for quality/logistics review without execution or release.

## Calculations

No calculation required unless a supplied sampling rule is applied; preserve its source, units, and revision.

## Validation

- Check stage, lot, supplier, revision, method, sample basis, and acceptance limits.
- Ensure no sample size, limit, or reaction instruction is invented.

## Exception Handling

- Missing sampling basis returns `NEEDS_INPUT`.
- Standards/sector gaps return `SOURCE_REVIEW_REQUIRED`.
- Release or inspection-execution requests return `OUT_OF_SCOPE`.

## Source Usage

- Use `references/inspection-plan-checklist.md` and AM-07 source rules.
- Record source, revision, effective date, owner, and incoming supplier provenance.

## Output Contract

Return `status`, inspection stage, lot/supplier scope, characteristic table, limits, methods, sampling basis, gaps, assumptions, validation notes, and owner handoff. Allowed statuses include `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, `SOURCE_REVIEW_REQUIRED`, and `ENGINEERING_REVIEW_REQUIRED`.

## Safety Requirements

AM-05 class: `REGULATED`. Do not approve sampling, accept/release product, certify inspection, or issue reaction instructions.

## References

- `references/inspection-plan-checklist.md`

## Examples

Read the checklist for an incoming lot with no approved sampling basis.

## Testing

Cover correct invocation, missing sample basis, supplier provenance, stage conflict, expected output structure, and execution/release refusal. Expected routing is not observed behavior.
