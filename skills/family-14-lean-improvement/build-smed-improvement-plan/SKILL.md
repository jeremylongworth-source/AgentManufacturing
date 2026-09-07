---
name: build-smed-improvement-plan
description: Propose reviewed changeover improvements from loss evidence without scheduling, operating, or bypassing safety controls.
license: PENDING_PROJECT_GOVERNANCE
---

# Build SMED Improvement Plan

**Taxonomy metadata:** family `14` Lean & Continuous Improvement; tier `CORE`; safety class `HAZARDOUS_OPERATION`; jurisdiction `PENDING_CONTEXT` with `PROVINCIAL_REQUIRED`, `SECTOR_REGULATED`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Separate internal/external changeover observations and structure a qualified improvement proposal.

## Triggers
- Changeover sequence, durations, loss evidence, equipment context, and controls are supplied.

## Non-Triggers
- Directing changeover work, bypassing guards, changing schedule, or authorizing a trial.

## Required Inputs
- Changeover boundary, steps, times, internal/external basis, hazards, and owner.

## Optional Inputs
- Video, staffing, tools, permits, quality checks, and validation criteria.

## Assumptions
- A proposed conversion requires safety, quality, and engineering review.

## Core Workflow
1. Map current steps and loss evidence.
2. Identify candidate internal/external conversions with controls.
3. Return approval, validation, and safe-trial gaps.

## Calculations
Preserve supplied durations and overlap rules; do not promise savings.

## Validation
- Check sequence, time basis, hazards, quality controls, and jurisdiction.

## Exception Handling
- Missing sequence or controls returns `NEEDS_INPUT`.
- Live trial or shortcut request returns `SAFETY_ESCALATION`.

## Source Usage
- Apply `references/smed-plan-checklist.md` and AM-07 rules.

## Output Contract
Return `status`, current sequence, candidates, evidence, hazards, approvals, and handoff.

## Safety Requirements
AM-05 class: `HAZARDOUS_OPERATION`. Do not direct live changeover, bypass safeguards, or authorize a trial.

## References
- `references/smed-plan-checklist.md`

## Examples
A candidate externalization is a proposal until safety and quality controls are reviewed.

## Testing
Cover correct invocation, missing controls, time mismatch, expected output structure, and unsafe-trial refusal. Expected routing is not observed behavior.
