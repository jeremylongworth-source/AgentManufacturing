---
name: review-measurement-equipment
description: Review instrument suitability for a stated measurement task and environment while separating resolution from accuracy and withholding certification.
license: PENDING_PROJECT_GOVERNANCE
---

# Review Measurement Equipment

## Overview

Assess whether supplied instrument specifications and condition evidence address a measurement task. Identify suitability gaps without certifying fitness, calibration status, or production use.

**Taxonomy metadata:** family `07` Metrology & Measurement Systems; tier `CORE`; safety class `ENGINEERING_OR_CERTIFICATION_BOUNDARY`; jurisdiction `PENDING_CONTEXT` with `STANDARDS_DEPENDENT`, `SECTOR_REGULATED`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `STANDARDS`, `REVIEW`. Audit distinction: evaluate instrument-task suitability; calibration status and study statistics are separate.

## Triggers

- Instrument specifications, measurement task, environment, and condition evidence are supplied.

## Non-Triggers

- Selecting equipment, approving calibration interval, certifying fitness, or executing measurement.

## Required Inputs

- Measurement task/measurand and tolerance.
- Instrument specifications, environment, and condition evidence.

## Optional Inputs

- Calibration certificate, uncertainty, resolution, accuracy, operator, fixture, and standards basis.

## Assumptions

- Resolution does not prove accuracy or uncertainty suitability.
- Missing condition or calibration evidence remains unknown.

## Core Workflow

1. Confirm task, tolerance, instrument identity/specification, environment, and condition.
2. Compare resolution, accuracy, range, uncertainty, and environmental suitability.
3. Return gaps and qualified metrology handoff.

## Calculations

No calculation required beyond transparent comparison to supplied tolerance and specifications.

## Validation

- Check units, range, resolution, accuracy, uncertainty, calibration status, and environment.
- Keep suitability distinct from certification and calibration validity.

## Exception Handling

- Missing tolerance or instrument identity returns `NEEDS_INPUT`.
- Standards/sector gap returns `SOURCE_REVIEW_REQUIRED`.
- Production approval or certification returns `OUT_OF_SCOPE`/`ENGINEERING_REVIEW_REQUIRED`.

## Source Usage

- Use `references/instrument-suitability-checklist.md` and AM-07 source rules.
- Record manufacturer/source, revision, certificate, access date, and owner.

## Output Contract

Return `status`, task/instrument scope, specifications, suitability comparison, resolution/accuracy distinction, gaps, assumptions, validation notes, and qualified handoff. Allowed statuses include `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, `SOURCE_REVIEW_REQUIRED`, and `ENGINEERING_REVIEW_REQUIRED`.

## Safety Requirements

AM-05 class: `ENGINEERING_OR_CERTIFICATION_BOUNDARY`. Do not certify fitness, calibration, or production measurement use.

## References

- `references/instrument-suitability-checklist.md`

## Examples

Read the checklist for supplied resolution without accuracy evidence.

## Testing

Cover correct invocation, missing task/tolerance, resolution/accuracy gap, environmental conflict, expected output structure, and certification refusal. Expected routing is not observed behavior.
