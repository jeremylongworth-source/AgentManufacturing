# AM-32 public-readiness record

Status: `READY` — MIT selected, documents completed and private reporting designated by the owner. Updated 2026-09-12 to use GitHub private vulnerability reporting and the private conduct form.

Date: 2026-09-09. Repository inspected at `d83e968`. The project is a collection of review-oriented skill packages, references and validation tools, not a deployed manufacturing controller. Public-readiness preparation does not change repository visibility, publish a release or install skills into a host.

## Prepared documents and owner decisions

All eight roadmap filenames are present: [README](../../README.md), [ROADMAP](../../ROADMAP.md), [AGENTS](../../AGENTS.md), [CONTRIBUTING](../../CONTRIBUTING.md), [SECURITY](../../SECURITY.md), [CODE_OF_CONDUCT](../../CODE_OF_CONDUCT.md), [CHANGELOG](../../CHANGELOG.md) and [LICENSE](../../LICENSE). The owner selected MIT in the AM-32 conversation on 2026-09-09. On 2026-09-12, GitHub private vulnerability reporting was enabled for security reports and the owner authorized the private conduct form at `https://conduct.pmgate.ai/`. No delivery test was performed.

| Decision | Current evidence | Required completion |
|---|---|---|
| Project distribution licence | Owner explicitly selected MIT on 2026-09-09. | Implemented: complete MIT text, 161 atomic packages, 18 role manifests, shared composition contract, schema, template and validators aligned. AM-31 source-bound evidence reassessed for licence-header-only changes. |
| Private reporting and ownership | GitHub private vulnerability reporting was enabled and the owner authorized the private conduct form on 2026-09-12. | Implemented in both policies: Jeremy Longworth is the recipient. Verification basis is OWNER_CONFIRMATION_AND_GITHUB_SETTING, not delivery testing. |

The [AM-06 licence rule](../architecture/skill-package-schema.json) now records the owner's MIT decision; historical pending-governance records remain unchanged. The licence text was checked against the [Open Source Initiative MIT text](https://opensource.org/license/mit) on 2026-09-09. The copyright attribution follows the existing repository author, Jeremy Longworth. Third-party guidance and standards retain their own rights. MIT adoption is separate from owner authorization to make this private repository public or publish a release.

## Readiness versus release

The [machine-readable status](public-readiness.json) and `python scripts/validate-public-readiness.py` verify document and licence consistency. `python scripts/validate-public-readiness.py --require-ready` returns AM32_READY with exit 0. The checker does not test report delivery or authorize publication.

AM-32 is closed following strict and full validation. AM-33 subsequently completed its audit with V1_PARTIALLY_READY; see [the audit](AM-33-release-candidate-audit.md) for remaining source and evaluation gaps. Independent model runs, baseline comparisons, repeatability and multi-turn robustness remain unperformed. No public support window, launch date or professional signoff is promised.

## Proposed publication and response plan

The owner decides whether and when to authorize a public repository or release after AM-33. Before that action, review the exact revision, licence/third-party rights, published documentation, reporting route and audit disposition. Keep sector coverage gaps and assisted-evaluation limitations prominent in release notes. No announcement or external message is sent by this preparation.

For a subsequently authorized release, retain the reviewed revision and changelog so consumers can identify affected packages. If a defect is found, document its scope, mark the affected package/release unsuitable where appropriate and prepare a corrected revision with focused regression evidence. Publication can be suspended, but copies already distributed cannot be recalled by changing repository visibility. No production-data migration is involved here.

The eventual responsible recipient should track incoming reports and regressions, maintain a decision record and review incidents after a release. Monitoring cadence, coverage and response targets require owner assignment; no recurring monitoring job is created. A future post-release review should record usage evidence actually available, boundary failures, source changes and corrective actions without inventing metrics.

Privacy update (2026-09-12): the personal contact value was removed from this historical record. Current reporting instructions are maintained in SECURITY.md and CODE_OF_CONDUCT.md; historical readiness statements describe the earlier assessment.
