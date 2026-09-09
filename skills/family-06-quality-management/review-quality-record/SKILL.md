---
name: review-quality-record
description: Review a quality record for completeness, revision, source integrity, and overwritten or missing values while preserving the original evidence.
license: MIT
---

# Review Quality Record

## Overview

Assess one quality record against required fields and revision evidence. Identify missing, overwritten, inconsistent, or untraceable values and preserve all available source values without judging product conformance.

**Taxonomy metadata:** family `06` Quality Management & Inspection; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `REVIEW`. Audit distinction: assess record completeness and integrity; conformance uses records to assess requirements.

## Triggers

- A quality record, required fields/revision, and source evidence are supplied for review.

## Non-Triggers

- Product conformity, record correction, release, certification, or overwriting a controlled record.

## Required Inputs

- Quality record and required fields.
- Revision/effective context and source evidence.

## Optional Inputs

- Audit trail, original instrument export, owner, signatures, and record-retention rule.

## Assumptions

- Overwritten or missing values are integrity gaps, not values to reconstruct.
- A complete form does not prove product conformance.

## Core Workflow

1. Confirm record identity, revision, required fields, source, and audit trail.
2. Classify completeness, integrity, traceability, and conflicts while preserving originals.
3. Return findings and record-owner handoff.

## Calculations

No calculation required.

## Validation

- Check field presence, revision, timestamp, source, audit trail, units, and alteration evidence.
- Separate record quality from product result.

## Exception Handling

- Missing source or required field returns `NEEDS_INPUT`.
- Overwritten value returns `SOURCE_REVIEW_REQUIRED`.
- Requests to rewrite or certify record returns `OUT_OF_SCOPE`.

## Source Usage

- Use `references/quality-record-integrity.md` and supplied records.
- Record source path, revision, date, owner, and retention context.

## Output Contract

Return `status`, record identity, completeness map, integrity findings, original values, conflicts, assumptions, validation notes, and owner handoff. Allowed statuses include `COMPLETE`, `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, and `SOURCE_REVIEW_REQUIRED`.

## Safety Requirements

AM-05 class: `ROUTINE`; escalate regulated or safety-critical record concerns. Do not rewrite, certify, or release.

## References

- `references/quality-record-integrity.md`

## Examples

Read the reference for overwritten inspection results.

## Testing

Cover correct invocation, missing fields, overwritten values, revision conflict, expected output structure, and record-rewrite refusal. Expected routing is not observed behavior.
