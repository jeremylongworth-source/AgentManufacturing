---
name: review-operator-qualification-record
description: Review operator qualification evidence against supplied rules without issuing certification or work authorization.
license: MIT
---

# Review Operator Qualification Record

**Taxonomy metadata:** family `13` Workforce & Shift Operations; tier `CORE`; safety class `REGULATED`; jurisdiction `PENDING_CONTEXT` with `STANDARDS_DEPENDENT`, `SECTOR_REGULATED`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Check qualification record identity, scope, revision, expiry, and evidence against supplied rules.

## Triggers
- Operator/role, task scope, record, requirements, and applicable context are supplied.

## Non-Triggers
- Certifying, revoking, assigning, or authorizing an operator.

## Required Inputs
- Identity, task scope, record revision, evidence, expiry, reviewer, and jurisdiction.

## Optional Inputs
- Assessment, supervision, language, accommodation, and refresher evidence.

## Assumptions
- A complete-looking record may still fail an applicable rule.

## Core Workflow
1. Reconcile record identity and task scope.
2. Compare evidence and expiry to supplied rules.
3. Return status, gaps, and authorized owner handoff.

## Calculations
No calculation; dates and intervals retain source rule and timezone.

## Validation
- Check identity, scope, revision, expiry, rule source, and sector context.

## Exception Handling
- Missing rule or evidence returns `SOURCE_REVIEW_REQUIRED`.
- Authorization request returns `SAFETY_ESCALATION`.

## Source Usage
- Apply `references/operator-qualification-checklist.md` and AM-07 rules.

## Output Contract
Return `status`, record scope, rule comparison, evidence, gaps, and qualified handoff.

## Safety Requirements
AM-05 class: `REGULATED`. Do not certify, revoke, or authorize operator work.

## References
- `references/operator-qualification-checklist.md`

## Examples
An expired record cannot be silently extended because the operator has experience.

## Testing
Cover correct invocation, missing rule, expiry conflict, expected output structure, and authorization refusal. Expected routing is not observed behavior.
