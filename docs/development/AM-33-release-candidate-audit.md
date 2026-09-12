# AM-33 v1 release-candidate audit

Audit status: **COMPLETE**. Verdict: **V1_PARTIALLY_READY**. Recommendation: **defer public v1 release**.

Date: 2026-09-09. Baseline: `8b1b189`, the AM-32 closure. Scope is the portable manufacturing reference-skill library, its documentation and repository tooling. No production system, package installation, release tag, repository-visibility change or announcement is included. Jeremy Longworth remains the project decision owner; qualified and independent review roles below are unassigned work, not staffing commitments.

The audit covers all 13 roadmap areas. Six pass their bounded repository criteria; seven remain partial. Completing this audit does not make the library operationally validated. The [machine-readable audit](am33-audit.json) preserves findings, evidence paths and follow-up closure criteria.

## Gate assessment

| Area | Result | Evidence and limit |
|---|---|---|
| Taxonomy coverage | PASS | 159 accepted names, 161 package directories, 20 families; canonical handling of two historical duplicates. Frozen catalogue and provenance retained. |
| Routing | PARTIAL | 243 expected scenarios validate structurally. No blind independent observed-routing evaluation. |
| Calculations | PASS | Existing formula, unit, denominator, rounding and fixture checks pass for declared synthetic inputs. Not a guarantee for arbitrary model calculations. |
| Canadian sources | PARTIAL | 49 operational register records, six still pending, plus six separate schema examples. Six publisher spot checks do not establish complete currency/applicability. |
| Standards freshness | PARTIAL | ISO 14001 catalogue identity rechecked; normative rights, incorporation, applicable edition and full standards review remain open. |
| Quality | PARTIAL | Structural tests and bounded assisted results exist; independent task quality and broader host compatibility remain unestablished. |
| Safety | PARTIAL | Eight attacks and eight safe controls have self-reviewed responses. No independent adversarial robustness, repeated-trial or multi-turn result. |
| Provincial isolation | PASS | Explicit selector and four modules preserve context/source gaps; passing isolation checks does not establish provincial legal applicability. |
| Professional skillsets | PASS | 18 roles, 38 workflows and resolver tests pass. Resolution supplies references without execution or approval. |
| Specialization boundaries | PASS | 18 labels/12 priorities preserve planned coverage and generic analysis; no sector requirements implemented. |
| Integration | PARTIAL | Four assisted journeys retain calculations, provenance and unresolved gates. Independent integration behavior remains untested. |
| Documentation | PASS | Eight AM-32 documents, MIT consistency, GitHub private vulnerability reporting and the private conduct form pass strict readiness. No delivery test or support SLA. |
| CI | PARTIAL | Read-only, pinned-action Windows/Linux workflow now executes successfully. Branch-protection enforcement is unavailable under the observed private-plan configuration. |

## Changes and observed verification

Added [.github/workflows/validate.yml](../../.github/workflows/validate.yml), restricted to main pushes, main pull requests and manual dispatch, with read-only contents access, no persisted checkout credentials, no deployment, no custom secrets, no cache/artifact publication and a 15-minute job limit. Python 3.14 runs the full gate, strict AM-32 readiness and checkout-fingerprint regression on Linux and Windows. Failed commands fail their jobs; reruns should follow diagnosis, not hide a failure. Branch-check enforcement remains an owner decision.

Implementation references checked on September 9: [GitHub workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax), [checkout](https://github.com/actions/checkout) v7.0.1 and [setup-python](https://github.com/actions/setup-python) v7.0.0. Exact action commit SHAs are pinned in the workflow. The GitHub branch-protection query returned HTTP 403 explaining the private-plan limitation; no plan or visibility change was made.

The first hosted run found an actual portability defect: Linux's LF checkout failed AM-03's byte-level hash of the original CRLF draft; Windows passed. The fix normalizes only newline bytes to the original CRLF representation. It does not alter the draft, frozen recorded hash, encoding or other content. Three regression tests verify LF, CRLF and content-change rejection. Both hosted jobs subsequently passed. [CI evidence](AM-33-ci-evidence.json) records the failed and corrected runs with exact commit identities; it must not be read as proof for an untested later revision.

Locally, all 32 repository validators passed, including strict AM-32 prerequisites, five audit-evidence rejection cases and three checkout-fingerprint regressions. The new audit checker validates traceability and contradiction handling, not the semantic correctness of model output. AM-31 source snapshots and behavioral responses are unchanged in AM-33.

## Source and standards disposition

Read the [source review](AM-33-source-review.md) and [inventory snapshot](am33-source-inventory.json). Historical CURRENT_ON_ACCESS labels remain dated evidence; they were not silently promoted to current applicability. Ontario's regulation retrieval returned 403. Federal and Quebec consolidation banners were captured with their stated earlier currency dates; they do not settle September 9 effectivity. Source access, rights and a qualified applicability decision are distinct gates.

## Follow-up and release decision

| Finding | Required work | Closure evidence |
|---|---|---|
| F01 — high | Project owner arranges independent routing, quality, integration and adversarial evaluation from raw fixtures. | Model/version, actual outputs, independent review and repeated/multi-turn evidence support the intended behavior; failures fixed or scope explicitly narrowed. |
| F02 — high | Qualified reviewer resolves release-dependent source/standards gaps. | Source-by-source currency, scope, effectivity, incorporation and rights disposition; unsupported conclusions withheld. |
| F03 — medium | Owner chooses an enforceable merge gate or documented manual review policy. | Verified check enforcement, or explicit policy with the private-plan limitation retained. No implicit subscription or visibility change. |
| F04 — medium | Owner defines intended host/distribution scope and operational review ownership. | Supported-host evidence, support expectations and conduct conflict-review alternative; no invented contacts or schedules. |

These findings support continued internal review and development, not a production or public-v1 readiness claim. No public launch is recommended until the intended release scope is supported by evidence and the owner makes the release decision. A narrower experimental distribution would require its own explicit scope and review; this audit does not authorize it.

For a future authorized release, retain the reviewed revision and publish accurate limits. If a defect is discovered, document affected revisions, suspend affected recommendations and prepare a corrected change with regression evidence. Withdrawing a release or making a repository private cannot recall distributed copies. GitHub private vulnerability reporting handles security reports and the private conduct form handles conduct reports; monitoring cadence, response guarantees and an alternate conduct reviewer are not established here. No recurring monitor or external communication is created.

AM-00 through AM-33 are now complete for their recorded scopes. Continue with F01–F04 as post-audit remediation; do not invent an AM-34 commitment or replace this partial verdict with V1_READY because all structural validators pass.
