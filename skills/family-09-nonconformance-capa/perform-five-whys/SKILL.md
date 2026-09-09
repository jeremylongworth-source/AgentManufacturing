---
name: perform-five-whys
description: Construct and challenge a five-whys causal chain for a bounded problem without treating the chain as proof.
license: MIT
---

# Perform Five Whys

**Taxonomy metadata:** family `09` Nonconformance, RCA & CAPA; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Structure a causal questioning chain and expose unsupported links.

## Triggers
- A bounded problem and an initial why chain are supplied.

## Non-Triggers
- Treating five steps as mandatory proof, blaming an operator, or approving CAPA.

## Required Inputs
- Problem statement, observed evidence, and each proposed why answer.

## Optional Inputs
- Process standard, event history, and independent challenge.

## Assumptions
- A chain may stop before five levels when evidence stops.

## Core Workflow
1. Write each cause-effect link plainly.
2. Challenge each link with evidence and alternatives.
3. Return supported links and open questions.

## Calculations
No calculation; chain depth is not a confidence score.

## Validation
- Check that each why answers the prior statement and has evidence.

## Exception Handling
- Missing observation returns `NEEDS_INPUT`.
- Corrective-action approval returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/five-whys-checklist.md`.

## Output Contract
Return `status`, problem, chain, evidence per link, gaps, alternatives, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not assign blame or authorize action.

## References
- `references/five-whys-checklist.md`

## Examples
Stopping at "operator error" without checking the system condition leaves the chain unsupported.

## Testing
Cover correct invocation, unsupported link, missing evidence, expected output structure, and action refusal. Expected routing is not observed behavior.
