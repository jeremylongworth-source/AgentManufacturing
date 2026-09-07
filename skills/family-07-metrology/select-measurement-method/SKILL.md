---
name: select-measurement-method
description: Compare supplied measurement approaches for a stated measurand, tolerance, geometry, material, environment, and available method evidence.
license: PENDING_PROJECT_GOVERNANCE
---

# Select Measurement Method

## Overview

Prepare a qualified-review comparison of measurement methods for one measurand and tolerance. Preserve geometry, material, environment, feasibility, uncertainty, and standards gaps; do not select or approve an instrument.

**Taxonomy metadata:** family `07` Metrology & Measurement Systems; tier `CORE`; safety class `ENGINEERING_OR_CERTIFICATION_BOUNDARY`; jurisdiction `PENDING_CONTEXT` with `STANDARDS_DEPENDENT`, `SECTOR_REGULATED`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `STANDARDS`, `REVIEW`. Audit distinction: compare approaches for a measurand; equipment review examines a selected instrument.

## Triggers

- Measurand, tolerance, part geometry/material, environment, and available method evidence are supplied.

## Non-Triggers

- Selecting an instrument, approving calibration, certifying a method, or executing a measurement.

## Required Inputs

- Measurand and tolerance.
- Geometry/material, environment, and method evidence.

## Optional Inputs

- Resolution, accuracy, uncertainty, access, operator, standards, and study design.

## Assumptions

- A method that cannot reach the feature because of geometry remains infeasible.
- Resolution is not accuracy, and method comparison does not establish fitness.

## Core Workflow

1. Confirm measurand, tolerance, feature access, environment, and source revision.
2. Compare methods for feasibility, resolution, accuracy/uncertainty evidence, and constraints.
3. Return a qualified selection package with gaps and owner handoff.

## Calculations

No calculation required unless supplied uncertainty arithmetic is explicitly applied; preserve its basis.

## Validation

- Check feature access, units, tolerance, environment, method evidence, and standards applicability.
- Separate feasibility, resolution, accuracy, and traceability claims.

## Exception Handling

- Missing measurand/tolerance returns `NEEDS_INPUT`.
- Geometry or standards conflict returns `ENGINEERING_REVIEW_REQUIRED`/`SOURCE_REVIEW_REQUIRED`.
- Selection or production approval returns `OUT_OF_SCOPE`.

## Source Usage

- Use `references/measurement-method-comparison.md` and AM-07 source rules.
- Record source, revision, access date, uncertainty/rights basis, and review owner.

## Output Contract

Return `status`, measurand/tolerance, method comparison, feasibility gaps, uncertainty/accuracy evidence, assumptions, validation notes, and qualified handoff. Allowed statuses include `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, `SOURCE_REVIEW_REQUIRED`, and `ENGINEERING_REVIEW_REQUIRED`.

## Safety Requirements

AM-05 class: `ENGINEERING_OR_CERTIFICATION_BOUNDARY`. Do not select, certify, calibrate, or authorize measurement equipment or production use.

## References

- `references/measurement-method-comparison.md`

## Examples

Read the reference for geometry that prevents a proposed method reaching the feature.

## Testing

Cover correct invocation, missing tolerance, geometry infeasibility, resolution/accuracy distinction, expected output structure, and selection refusal. Expected routing is not observed behavior.
