---
name: review-human-machine-interface-risk
description: Review supplied human-machine interface modes, alarms, and error evidence for concerns without modifying a live interface.
license: PENDING_PROJECT_GOVERNANCE
---

# Review Human Machine Interface Risk

**Taxonomy metadata:** family `16` Automation & Advanced Manufacturing; tier `CORE`; safety class `ENGINEERING_OR_CERTIFICATION_BOUNDARY`; jurisdiction `PENDING_CONTEXT` with `STANDARDS_DEPENDENT`, `SECTOR_REGULATED`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Structure human-machine interaction concerns from supplied interface descriptions and task observations.

## Triggers
- Interface descriptions, task or error observations, alarm behavior, modes, and review context are supplied.

## Non-Triggers
- Changing HMI configuration, suppressing alarms, changing modes, or authorizing operation.

## Required Inputs
- Interface scope, operator task, modes, alarms, error states, feedback, and applicable standards or sector context.

## Optional Inputs
- Screenshots, event history, user observations, language/accessibility needs, and existing risk review.

## Assumptions
- A concern brief from supplied evidence is not a completed human-factors or machine-safety assessment.

## Core Workflow
1. Bound operator task, interface state, and error scenario.
2. Compare visibility, feedback, alarm, and mode evidence to supplied criteria.
3. Return concerns, evidence gaps, and qualified review handoff.

## Calculations
No safety conclusion is calculated; counts of alarms or observations preserve source scope.

## Validation
- Check mode visibility, alarm meaning, acknowledgment, error recovery, standards, and sector context.

## Exception Handling
- Missing mode or alarm evidence returns `NEEDS_INPUT`.
- A request to suppress or reconfigure a live interface returns `SAFETY_ESCALATION`.

## Source Usage
- Apply `references/hmi-risk-checklist.md` and AM-07 source controls.

## Output Contract
Return `status`, interaction scope, concern register, evidence gaps, standards questions, and handoff.

## Safety Requirements
AM-05 class: `ENGINEERING_OR_CERTIFICATION_BOUNDARY`. Do not change modes, suppress alarms, or authorize operation.

## References
- `references/hmi-risk-checklist.md`

## Examples
A mode change not visible to an operator is recorded as a concern without issuing configuration commands.

## Testing
Cover correct invocation, missing alarm evidence, standards gap, expected output structure, and live-interface refusal. Expected routing is not observed behavior.
