---
name: identify-special-cause-variation
description: Compare chart signals with dated process events to identify candidate special causes without asserting causation.
license: PENDING_PROJECT_GOVERNANCE
---

# Identify Special-Cause Variation

**Taxonomy metadata:** family `08` SPC & Capability; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Screen dated events against a statistical signal and preserve causal uncertainty.

## Triggers
- A signal, ordered data, and dated process-event history are supplied.

## Non-Triggers
- Closing an investigation, assigning blame, or changing the process.

## Required Inputs
- Signal timing, chart basis, and event chronology.

## Optional Inputs
- Tooling, material, operator, maintenance, and environmental records.

## Assumptions
- An event after a signal cannot explain the earlier signal.

## Core Workflow
1. Anchor the signal time and rule.
2. Filter events by timing and scope.
3. Return candidates, contradictions, and evidence requests.

## Calculations
Use time alignment and declared signal rules; no causal probability is invented.

## Validation
- Check timestamps, timezone, data order, and event scope.

## Exception Handling
- Missing timing returns `NEEDS_INPUT`.
- Causal certainty request returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/special-cause-review-checklist.md`.

## Output Contract
Return `status`, signal, candidate events, timing tests, contradictions, gaps, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not direct corrective action.

## References
- `references/special-cause-review-checklist.md`

## Examples
A tooling change recorded after the signal is not an explanation of that earlier signal.

## Testing
Cover correct invocation, post-signal event, missing timestamps, expected output structure, and causal-certainty refusal. Expected routing is not observed behavior.
