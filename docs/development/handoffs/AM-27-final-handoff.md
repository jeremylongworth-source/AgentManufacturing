# AM-27 final handoff: initial provincial overlays

Status: `READY`

Completion token: `AGENTMANUFACTURING_AM_27_PROVINCIAL_BASELINE_READY`

Date: 2026-09-08

AM-27 adds the provincial selector with Ontario, British Columbia, Alberta and Quebec modules. Each covers authority research for OH&S, machinery, hazardous energy, electrical, pressure equipment, environmental obligations and worker training: 28 topic paths backed by 16 scoped source records.

There are now 161 package directories representing all 159 accepted skill names; two older reference paths remain preserved. The taxonomy is unchanged. Atomic future routes are now empty because every frozen name has a package; professional composition and later roadmap work remain unfinished.

## Evidence

- [Provincial selector and modules](../../../skills/family-20-canadian-compliance/identify-provincial-safety-overlay/).
- [Source records](../../architecture/am27-provincial-source-records.json) and [source evidence](../AM-27-source-evidence.md).
- [Acceptance record](../../../tests/evaluations/AM-27-provincial-acceptance.md), [validator](../../../scripts/validate-provincial-overlays.py) and [routing manifest](../../../tests/expected-routing.yaml).
- Routing suite: 197 scenarios, including 14 AM-27 cases.

## Validation and limits

Observed on 2026-09-08: all 26 repository validators and the AgentSkills package check passed; local links in the new package and evidence documents resolved. Run `python scripts/validate-all.py` for the complete gate and AgentSkills quick_validate.py for the new package.

Runtime model behavior remains `NOT_RUN`. Expected routing is not observed behavior. Legal completeness, employer regime, activity-date currency, equipment approval, permission eligibility and training competence remain unverified. Ontario's legal fetch did not establish consolidation currency; Quebec displayed currency to 2026-04-01. Both remain PENDING_REVIEW.

## Next wave

AM-28 composes professional skillsets from the implemented atomic skills using the roles already defined in the roadmap. Inspect role definitions and existing package paths; preserve evidence dependencies and jurisdiction/safety boundaries. Reuse canonical skill names and account for the two historical reference duplicates without silently renaming the taxonomy. Do not confuse full atomic package coverage with runtime evaluation, licensing, release readiness or sector specialization.
