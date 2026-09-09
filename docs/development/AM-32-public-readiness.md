# AM-32 public-readiness record

Status: `IN_PROGRESS` — MIT selected and documentation prepared; private reporting unresolved.

Date: 2026-09-09. Repository inspected at `d83e968`. The project is a collection of review-oriented skill packages, references and validation tools, not a deployed manufacturing controller. Public-readiness preparation does not change repository visibility, publish a release or install skills into a host.

## Prepared documents and owner decisions

All eight roadmap filenames are present: [README](../../README.md), [ROADMAP](../../ROADMAP.md), [AGENTS](../../AGENTS.md), [CONTRIBUTING](../../CONTRIBUTING.md), [SECURITY](../../SECURITY.md), [CODE_OF_CONDUCT](../../CODE_OF_CONDUCT.md), [CHANGELOG](../../CHANGELOG.md) and [LICENSE](../../LICENSE). The owner selected MIT in the AM-32 conversation on 2026-09-09. Security/conduct handling is a draft pending an owner-confirmed private route and responsible recipient.

| Decision | Current evidence | Required completion |
|---|---|---|
| Project distribution licence | Owner explicitly selected MIT on 2026-09-09. | Implemented: complete MIT text, 161 atomic packages, 18 role manifests, shared composition contract, schema, template and validators aligned. AM-31 source-bound evidence reassessed for licence-header-only changes. |
| Private reporting and ownership | GitHub repository query returned PRIVATE. Private-vulnerability-reporting query returned HTTP 404; availability unverified. | Owner supplies a private contact or authorizes configuring a supported route and identifies security/conduct recipient responsibilities. Record owner confirmation separately from any delivery test; no message is sent without authorization. |

The [AM-06 licence rule](../architecture/skill-package-schema.json) now records the owner's MIT decision; historical pending-governance records remain unchanged. The licence text was checked against the [Open Source Initiative MIT text](https://opensource.org/license/mit) on 2026-09-09. The copyright attribution follows the existing repository author, Jeremy Longworth. Third-party guidance and standards retain their own rights. MIT adoption is separate from owner authorization to make this private repository public or publish a release.

## Readiness versus release

The [machine-readable status](public-readiness.json) and `python scripts/validate-public-readiness.py` verify prepared-document and licence consistency. `python scripts/validate-public-readiness.py --require-ready` exits 2 while private reporting remains unresolved. A passing repository gate is therefore compatible with AM-32 IN_PROGRESS; it must not be described as publication readiness.

After reporting is configured, rerun focused and full validation, inspect licence consistency and private reporting evidence, and finish the AM-32 handoff. AM-33 then audits the release candidate, including source freshness and evaluation limitations. Independent model runs, baseline comparisons, repeatability and multi-turn robustness remain unperformed. No public support window, launch date or professional signoff is promised.

## Proposed publication and response plan

The owner decides whether and when to authorize a public repository or release after AM-33. Before that action, review the exact revision, licence/third-party rights, published documentation, reporting route and audit disposition. Keep sector coverage gaps and assisted-evaluation limitations prominent in release notes. No announcement or external message is sent by this preparation.

For a subsequently authorized release, retain the reviewed revision and changelog so consumers can identify affected packages. If a defect is found, document its scope, mark the affected package/release unsuitable where appropriate and prepare a corrected revision with focused regression evidence. Publication can be suspended, but copies already distributed cannot be recalled by changing repository visibility. No production-data migration is involved here.

The eventual responsible recipient should track incoming reports and regressions, maintain a decision record and review incidents after a release. Monitoring cadence, coverage and response targets require owner assignment; no recurring monitoring job is created. A future post-release review should record usage evidence actually available, boundary failures, source changes and corrective actions without inventing metrics.
