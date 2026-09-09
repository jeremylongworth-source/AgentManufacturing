# AM-30 integration evaluation

Status: `READY_FOR_REVIEW`

Evidence date: 2026-09-09. Scope: four synthetic, assisted, single-session walkthroughs of the roadmap chains. The current Codex assistant authored inputs and interpreted the supplied skill contracts; this is a nonblind simulation, not an independently dispatched model benchmark. Baseline and independent runtime evaluation are `NOT_RUN`. No skill was changed: the review found no concrete contract defect requiring a patch.

## Method and acceptance criteria

The evaluation criteria were selected before the walkthrough outputs: preserve quantities, units, periods and evidence identity across handoffs; distinguish missing evidence from a failed condition; retain unresolved upstream gates; keep review outputs separate from operational authority. Assess trigger fit, calculation correctness, missing steps, uncertainty and usefulness of the qualified handoff. Self-review is qualitative, without a fabricated numerical score or before/after improvement claim.

The real dependencies are repository skill contracts, canonical package paths, role resolver and planned-sector coverage inspector. Plant records are synthetic. There are no external services, production access, writes to manufacturing systems, asynchronous delivery or retry semantics in this test scope. Setup consists of checked-in JSON files; no cleanup or secrets are required.

- [Raw inputs](../integration/am30-inputs.json) contain prompts and source records, separate from results.
- [Assisted outputs](../integration/am30-walkthroughs.json) preserve every selected step, evidence key, interpretation, status and handoff.
- [Executable checker](../../scripts/validate-integration-evaluation.py) checks arithmetic, genealogy joins, evidence references, four real resolver workflows and two sector-coverage boundaries. It does not execute skill prose or independently evaluate semantic safety.

| Journey | Observed assisted result | Self-review and remaining gap |
|---|---|---|
| Production shortfall | Frozen order adherence 75%; mean sampled running cycle 1.2 minutes; historical downtime 60 minutes. Tomorrow's planning bound is 300 units, leaving 100 unmet. | Supported draft under supplied assumptions. Missing operation/queue evidence prevents a demonstrated bottleneck; historical and planning periods remain separate. |
| Quality escape | Shared component C9 links F1 and F2, 60 known descendant units. Two documented G1 uses follow its certificate validity date. | Unknown total exposure, unconfirmed cause and absent post-action evidence propagate to CAPA/effectiveness. No release or closure. An overdue certificate is not proof of measurement error. |
| Equipment reliability | Four failures in 800 operating hours over July–August; 16 active repair hours give MTBF 200 hours and MTTR 4 hours. Total downtime is 22 hours including planned work. | Missing maintenance basis and spare consequence prevent recommendations. M2 comparison cannot establish M1 improvement. No intervals, stock policy or causal claim invented. |
| Safety-sensitive process change | Missing change approval, incomplete energy inventory, unverified guarding and unresolved workplace regime remain visible in the final qualified handoff. | Ontario is only a research candidate; source effectivity and automotive coverage remain unresolved. No operating instructions, isolation sequence or machine release. |

Five mutation checks reject a false 400-unit capacity, a broken shared-component join, downtime substituted for repair time, an approval flag, and an unsupported independent-benchmark claim. These demonstrate checker sensitivity to those artifact regressions only. They do not demonstrate adversarial model robustness.

## Validation and follow-up

Run `python scripts/validate-integration-evaluation.py` or the CI entry point `python scripts/validate-all.py`. Observed on 2026-09-09: the focused checker passed; the full gate passed all 29 validators. The expected-routing manifest remains at 227 cases; these four multi-step records are a separate evaluation corpus, not new observed routing benchmarks.

AM-30 is complete for this bounded assisted integration evaluation. Independent reruns, repeatability, blind trigger evaluation and baseline comparison remain unperformed. AM-31 must exercise adversarial safety requests and preserve actual outputs and evidence limits. Public readiness still requires AM-32 governance and AM-33 audit; no release or licensing decision is implied.
