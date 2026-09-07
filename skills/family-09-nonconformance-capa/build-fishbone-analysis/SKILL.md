---
name: build-fishbone-analysis
description: Organize candidate causes by category while preserving evidence gaps and avoiding causal proof claims.
license: PENDING_PROJECT_GOVERNANCE
---

# Build Fishbone Analysis

**Taxonomy metadata:** family `09` Nonconformance, RCA & CAPA; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Build a structured candidate-cause map for later evidence review.

## Triggers
- A bounded problem and process context are supplied.

## Non-Triggers
- Declaring causes, selecting CAPA, or treating category completeness as proof.

## Required Inputs
- Problem statement, process boundary, and chosen category scheme.

## Optional Inputs
- People, method, machine, material, measurement, environment, and change history.

## Assumptions
- Categories organize inquiry; they do not validate a cause.

## Core Workflow
1. State the effect and boundary.
2. Place candidate causes with evidence questions.
3. Return gaps and priorities for investigation.

## Calculations
No calculation; candidate counts do not measure likelihood.

## Validation
- Check cause wording, scope, duplicates, and evidence prompts.

## Exception Handling
- Missing effect returns `NEEDS_INPUT`.
- CAPA selection returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/fishbone-analysis-checklist.md`.

## Output Contract
Return `status`, effect, categories, candidate causes, evidence questions, gaps, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not declare cause or authorize action.

## References
- `references/fishbone-analysis-checklist.md`

## Examples
A fishbone branch is a hypothesis until evidence supports it.

## Testing
Cover correct invocation, missing effect, category ambiguity, expected output structure, and CAPA refusal. Expected routing is not observed behavior.
