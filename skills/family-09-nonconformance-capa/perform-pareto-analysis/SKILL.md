---
name: perform-pareto-analysis
description: Rank categories on one declared metric and population without attributing cause or selecting corrective action.
license: PENDING_PROJECT_GOVERNANCE
---

# Perform Pareto Analysis

**Taxonomy metadata:** family `09` Nonconformance, RCA & CAPA; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Summarize concentration on a coherent metric, category scheme, and population.

## Triggers
- Categorized events, one metric, period, and population are supplied.

## Non-Triggers
- Claiming the largest category is the root cause or authorizing action.

## Required Inputs
- Category, metric, unit, population, period, and inclusion rule.

## Optional Inputs
- Cumulative share, stratification, denominator, and data-quality notes.

## Assumptions
- Categories must be mutually defined for ranking.

## Core Workflow
1. Validate metric, unit, period, and population.
2. Aggregate and rank categories with intermediates.
3. Report concentration and limits without causal claims.

## Calculations
Share = category metric / total metric; cumulative ordering preserves the declared metric basis.

## Validation
- Check denominator, units, duplicate events, and mixed populations.

## Exception Handling
- Incoherent metric returns `NEEDS_INPUT`.
- Action selection returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/pareto-analysis-checklist.md` and AM-08 calculation rules.

## Output Contract
Return `status`, metric, population, ranked categories, shares, assumptions, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not infer cause or authorize CAPA.

## References
- `references/pareto-analysis-checklist.md`

## Examples
A high-count category is a prioritization signal, not a causal conclusion.

## Testing
Cover correct invocation, mixed units, zero denominator, expected output structure, and action refusal. Expected routing is not observed behavior.
