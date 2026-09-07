---
name: review-calibration-status
description: Review calibration certificates, dates, usage, and supplied due-date rules while flagging unsupported validity claims.
license: PENDING_PROJECT_GOVERNANCE
---

# Review Calibration Status

## Overview

Assess calibration status evidence for identified instruments using supplied certificates, dates, usage, and due-date rules. Do not invent a valid-until date or certify measurement fitness.

**Taxonomy metadata:** family `07` Metrology & Measurement Systems; tier `CORE`; safety class `REGULATED`; jurisdiction `PENDING_CONTEXT` with `STANDARDS_DEPENDENT`, `SECTOR_REGULATED`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `build-calibration-register`, `STANDARDS`, `REVIEW`. Audit distinction: compare dates/use against supplied rules; exposure assessment is separate.

## Triggers

- Instrument register, certificates, supplied due-date rules, and usage dates are supplied.

## Non-Triggers

- Setting intervals, certifying calibration, approving product, or selecting an instrument.

## Required Inputs

- Instrument identity/register and certificates.
- Due-date rule and usage dates.

## Optional Inputs

- Out-of-tolerance findings, condition, standards, owner, and affected measurements.

## Assumptions

- A certificate without an interval does not support a valid-until date.
- Use after a due date is an evidence concern, not automatic product disposition.

## Core Workflow

1. Verify identity, certificate, date, interval rule, use date, and source revision.
2. Compare evidence and flag supported, unsupported, stale, or conflicting status claims.
3. Return review gaps and metrology/quality handoff.

## Calculations

No calculation required beyond date comparison using the supplied rule.

## Validation

- Check certificate identity, dates, interval authority, use history, and sector/standards basis.
- Do not infer missing due dates or calibration validity.

## Exception Handling

- Missing interval or use history returns `NEEDS_INPUT`.
- Stale/conflicting rule returns `SOURCE_REVIEW_REQUIRED`.
- Certification or release returns `OUT_OF_SCOPE`/`SAFETY_ESCALATION`.

## Source Usage

- Use `references/calibration-status-checklist.md` and AM-07 source rules.
- Record certificate source, rule revision, dates, access date, and owner.

## Output Contract

Return `status`, instrument scope, certificate/date evidence, rule basis, supported/unsupported status, gaps, assumptions, validation notes, and handoff. Allowed statuses include `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, `SOURCE_REVIEW_REQUIRED`, and `SAFETY_ESCALATION`.

## Safety Requirements

AM-05 class: `REGULATED`. Do not certify calibration, measurement fitness, product release, or legal compliance.

## References

- `references/calibration-status-checklist.md`

## Examples

Read the checklist for a certificate before use with no interval rule.

## Testing

Cover correct invocation, missing interval, stale rule, incomplete use history, expected output structure, and certification/release refusal. Expected routing is not observed behavior.
