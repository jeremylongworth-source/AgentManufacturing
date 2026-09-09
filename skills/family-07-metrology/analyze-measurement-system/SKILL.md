---
name: analyze-measurement-system
description: Structure a measurement-system study request and expose missing repeatability, reproducibility, and operator evidence.
license: MIT
---

# Analyze Measurement System

**Taxonomy metadata:** family `07` Metrology & Measurement Systems; tier `CORE`; safety class `ENGINEERING_OR_CERTIFICATION_BOUNDARY`; jurisdiction `PENDING_CONTEXT` with `STANDARDS_DEPENDENT`, `SECTOR_REGULATED`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Prepare a reviewable measurement-system study without declaring acceptance.

## Triggers
- Measurand, tolerance, equipment, operators, parts, and repeated observations are proposed.

## Non-Triggers
- Certifying a gauge, approving a study, or authorizing production use.

## Required Inputs
- Measurand, reference values, operators, parts, repetitions, and study design.

## Optional Inputs
- Resolution, uncertainty, environmental conditions, and acceptance criteria.

## Assumptions
- Missing operator or repetition evidence prevents a complete study.

## Core Workflow
1. Check the design against the measurand and tolerance.
2. Separate repeatability, reproducibility, bias, and stability evidence.
3. Return calculations or gaps for qualified review.

## Calculations
Use only a declared study method and preserve units, sample counts, and exclusions.

## Validation
- Confirm operators, parts, repetitions, reference basis, and method revision.

## Exception Handling
- Missing design inputs returns `NEEDS_INPUT`.
- Acceptance or certification requests return `ENGINEERING_REVIEW_REQUIRED`.

## Source Usage
- Apply `references/measurement-system-study-checklist.md` and AM-07 source rules.

## Output Contract
Return `status`, study design, evidence matrix, calculations, exclusions, assumptions, and qualified handoff.

## Safety Requirements
AM-05 class: `ENGINEERING_OR_CERTIFICATION_BOUNDARY`. Do not approve measurement-system fitness.

## References
- `references/measurement-system-study-checklist.md`

## Examples
Missing operator repetitions are a design gap, not evidence of acceptable reproducibility.

## Testing
Cover correct invocation, missing operators, unit mismatch, expected output structure, and certification refusal. Expected routing is not observed behavior.
