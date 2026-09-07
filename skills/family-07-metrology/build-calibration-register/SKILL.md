---
name: build-calibration-register
description: Organize instrument identities, calibration records, supplied intervals, and responsible owners into a traceable calibration register.
license: PENDING_PROJECT_GOVERNANCE
---

# Build Calibration Register

## Overview

Build a register linking instrument IDs, calibration records, supplied intervals, owners, and missing/conflicting identity evidence. Organize records without interpreting validity or certifying calibration.

**Taxonomy metadata:** family `07` Metrology & Measurement Systems; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Audit distinction: organize instrument/record relationships; status review interprets validity rules.

## Triggers

- Instrument IDs, calibration records, supplied intervals, and responsible owners are supplied.

## Non-Triggers

- Calibration-status decision, interval design, instrument selection, or measurement certification.

## Required Inputs

- Instrument identifiers and calibration records.
- Supplied interval basis and responsible owner.

## Optional Inputs

- Location, condition, certificate, use history, standards, and duplicate-ID evidence.

## Assumptions

- Two instruments sharing an ID are an identity collision, not one merged history.
- A register entry does not establish calibration validity.

## Core Workflow

1. Normalize instrument ID, record, interval, owner, revision, and source.
2. Link records and flag missing, duplicate, conflicting, or unowned items.
3. Return the register and status-review handoff.

## Calculations

No calculation required.

## Validation

- Check unique identity, certificate linkage, date, interval source, owner, and record integrity.
- Preserve duplicate IDs and missing history.

## Exception Handling

- Missing ID or record returns `NEEDS_INPUT`.
- Duplicate/conflicting identity returns `SOURCE_REVIEW_REQUIRED`.
- Certification or status approval returns `OUT_OF_SCOPE`.

## Source Usage

- Use `references/calibration-register-checklist.md` and supplied records.
- Record source, revision, date, owner, and retention context.

## Output Contract

Return `status`, instrument register, record links, missing/conflicting items, assumptions, validation notes, and owner handoff. Allowed statuses include `COMPLETE`, `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, and `SOURCE_REVIEW_REQUIRED`.

## Safety Requirements

AM-05 class: `ROUTINE`; escalate safety-critical instrument identity or status gaps. Do not certify or approve calibration.

## References

- `references/calibration-register-checklist.md`

## Examples

Read the checklist for two instruments sharing an ID.

## Testing

Cover correct invocation, duplicate ID, missing certificate, missing owner, expected output structure, and calibration-approval refusal. Expected routing is not observed behavior.
