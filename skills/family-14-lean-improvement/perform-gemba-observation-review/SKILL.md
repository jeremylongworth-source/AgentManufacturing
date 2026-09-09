---
name: perform-gemba-observation-review
description: Synthesize supplied on-site observations into facts, questions, and evidence gaps without claiming a virtual inspection.
license: MIT
---

# Perform Gemba Observation Review

**Taxonomy metadata:** family `14` Lean & Continuous Improvement; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Review observation notes and separate facts, interpretations, and follow-up questions.

## Triggers
- Dated observation notes, process area, observer, and evidence are supplied.

## Non-Triggers
- Claiming on-site presence, conducting a safety audit, or authorizing change.

## Required Inputs
- Area, observation date, notes, source, and process boundary.

## Optional Inputs
- Photos, interviews, measures, standards, and owner responses.

## Assumptions
- Supplied notes are evidence to review, not direct observation by the skill.

## Core Workflow
1. Extract factual observations.
2. Separate hypotheses and missing evidence.
3. Return questions and owner handoff.

## Calculations
No calculation; supplied measures retain units and source.

## Validation
- Check date, area, observer, evidence, and safety context.

## Exception Handling
- Missing observation source returns `NEEDS_INPUT`.
- Safety audit or intervention request returns `SAFETY_ESCALATION`.

## Source Usage
- Apply `references/gemba-review-checklist.md`.

## Output Contract
Return `status`, facts, interpretations, questions, evidence, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not claim an on-site inspection or safety clearance.

## References
- `references/gemba-review-checklist.md`

## Examples
A note saying "operator waits" is retained as an observation until timing evidence exists.

## Testing
Cover correct invocation, missing source, safety boundary, expected output structure, and inspection claim refusal. Expected routing is not observed behavior.
