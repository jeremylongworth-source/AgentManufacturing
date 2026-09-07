# AM-00: Repository baseline audit

Date: 2026-09-06

Verdict: **READY**

Completion token: `AGENTMANUFACTURING_AM_00_BASELINE_READY`

AM-00 establishes the actual starting state and the architectural patterns to carry forward. It does not establish manufacturing, regulatory, engineering, or release readiness. AM-01 is the next wave.

## Objective and scope

The intended product is a portable library of atomic decision-support skills for commercial manufacturing in Canada, composed into professional skillsets with jurisdiction and sector overlays. Contributors need an evidence-backed baseline before freezing the domain or authoring skills.

**IN SCOPE:** inspect all starter documents; inspect AgentSkills and AgentLogistics as architectural references; record gaps, validation limits, and future owners; establish local Git against the user-supplied empty remote; update execution status; produce this audit and a final handoff.

**OUT OF SCOPE:** AM-01 domain freeze; AM-02 enumeration; AM-03 taxonomy freeze; jurisdiction or engineering determinations; standards research; skill implementation; validator implementation; bulk directory scaffolding; publication or release. The AM-10 mass-authoring gate remains unchanged.

## Starting workspace truth

The initial recursive file inventory contained exactly four files, with no hidden project files:

| File | Bytes at entry | Observed role |
|---|---:|---|
| `README.md` | 1,957 | Starter orientation and AM-00 entry instruction |
| `ROADMAP.md` | 13,170 | AM-00 through AM-33 and bounded execution protocol |
| `docs/architecture/domain-framework.md` | 9,835 | Proposed scope, boundaries, overlays, roles, and structure |
| `docs/architecture/master-taxonomy-v0.1.md` | 14,614 | Twenty families with representative candidate names |

`git status --short` initially returned “not a git repository.” No `AGENTS.md`, licence, skills, skillsets, tests, scripts, CI, dependency manifest, prior handoff, or completed wave existed. The user supplied AgentSkills routing instructions in the session; this is distinct from a project-local `AGENTS.md`.

Available tools were PowerShell 7.6.5, Git 2.53.0.windows.1, and Python 3.14.3. Their presence is an environment observation, not a project runtime requirement.

### Remote and local Git

The user identified `https://github.com/jeremylongworth-source/AgentManufacturing` as this project's remote. Authenticated `gh repo view` returned:

```json
{"defaultBranchRef":{"name":""},"isEmpty":true,"isPrivate":true,"nameWithOwner":"jeremylongworth-source/AgentManufacturing","url":"https://github.com/jeremylongworth-source/AgentManufacturing"}
```

An unauthenticated web request returned 404, and default Git HTTPS authentication failed. Neither result establishes absence of the repository. A command-scoped GitHub CLI credential helper successfully ran `git ls-remote --symref` with exit 0 and no refs, consistent with the authenticated empty-repository metadata.

Initialized local Git on `main` and set `origin` to `https://github.com/jeremylongworth-source/AgentManufacturing.git`. No global credential settings were changed. No files were staged, committed, or pushed. The local branch has no commits; the remote has no default branch yet. The original four files were retained, with status edits only to README and ROADMAP.

## Architectural reference evidence

References were inspected locally on 2026-09-06. These are observations of accessible checkouts, not certifications of upstream releases. Neither reference repository was modified or installed by this wave.

| Reference | Checkout identity | Working-tree qualification |
|---|---|---|
| AgentSkills, `D:\CodexProject\AgentSkills` | `07d67eea523f6d00381e1604b59ed1dd4d4e4708` | Modified and untracked files existed, including README and routing fixtures. Observations include working-tree content, not only this commit. |
| AgentLogistics, `D:\AgentLogistics` | `093b59771010bb8cf65d58ab644960f8659918a6` | `git status --short` was empty at inspection. |

### AgentSkills

Inspected `README.md`, `docs/authoring-guide.md`, `docs/skill-quality-bar.md`, `skillsets/engineering-delivery.yaml`, `scripts/validate-scenarios.py`, `tests/scenarios/agentops-skill-benchmark.md`, and `.github/workflows/validation.yml`.

- Portable procedures live in `SKILL.md` and references; `agents/openai.yaml` supplies host metadata.
- Focused triggers, useful workflows, explicit deliverables, reference checklists, and freshness rules form the quality bar.
- Skillsets select existing atomic skills and routing templates rather than embedding duplicate procedures.
- The inspected scenario validator compares scenario-declared routes with `tests/expected-routing.yaml` and checks that referenced skill files exist. It does **not** execute prompts against a model or measure actual routing behavior.
- CI invokes a repository release-check wrapper across multiple operating systems. This establishes a useful architecture pattern; no reference CI execution or pass count was independently verified here.

The checkout has no root `AGENTS.md`; routing templates live under `agents/`. Its frontmatter standard uses MIT, which is a reference-project choice and does not select AgentManufacturing's licence.

### AgentLogistics

Inspected `AGENTS.md`, `README.md`, `docs/standards/skill-authoring-standard.md`, `docs/standards/testing-standard.md`, `docs/standards/research-and-evidence-standard.md`, `skills/inventory-control/calculate-reorder-point/SKILL.md`, its `agents/openai.yaml`, `skillsets/warehouse-supervisor/skillset.yaml`, `tests/fixtures/calculate-reorder-point-cases.json`, `scripts/validate-all.ps1`, portions of `scripts/validate-tests.py`, `.github/workflows/validate.yml`, and `docs/development/handoffs/AL-25-final-handoff.md`.

- Bounded waves separate readiness verdicts from completion tokens and record explicit exclusions in handoffs.
- Grouped atomic packages distinguish triggers, non-triggers, inputs, assumptions, procedure, validation, exceptions, evidence, outputs, and authority boundaries.
- Calculation examples preserve units, intermediate results, missing-data behavior, rounding, and output invariants. Fixtures include positive, invalid-input, missing-input, and wrong-scope cases.
- Role manifests reference existing skills, scenarios, and fixtures. Jurisdiction and sector work remain source-bounded.
- The validation wrapper separates documentation, taxonomy, skills, specializations, tests, shared resources, and skillsets. Manufacturing should adapt this separation in its own later waves.
- The AL-25 handoff explicitly reports `V1_PARTIALLY_READY` and identifies live model evaluation and expanded calculation coverage as unfinished. Reference completion markers must not be mistaken for evidence that every behavior has been tested.

The attempted `AL-00-final-handoff.md` path does not exist; the available AL-25 handoff was inspected instead. No logistics procedures, thresholds, safety requirements, or licence terms were copied into manufacturing skills.

## Roadmap findings and assigned follow-ups

These are baseline findings, not later-wave decisions. No candidate has been accepted, renamed, merged, or rejected during AM-00.

| ID | Finding and consequence | Owning wave / closure evidence |
|---|---|---|
| B-01 | The domain and logistics interface are proposed, not frozen. Receiving quality, line-side shortages, and finished-goods transfer need explicit handoff ownership. | AM-01: domain contract and scope boundaries with in/out examples. |
| B-02 | The taxonomy is representative only. Candidate records lack the required tier, jurisdiction, safety class, sector dependency, inputs, outputs, dependencies, and priority. | AM-02: complete candidate records across all twenty families. |
| B-03 | Naming and possible overlap require review: `build-smED-improvement-plan`; value-stream mapping in Families 01/14; constraints and bottlenecks across 01/04/05; changeover analysis across 05/14; process/change/document review across 03/04/18; WHMIS review in 11/20. | AM-02/03: per-candidate atomicity decisions, normalized names, dependency map, and audited index. |
| B-04 | The roadmap's AM-29 sector list and domain framework's longer list differ, including combined wood/paper versus separate groups and additional pharmaceutical, process, and additive categories. | AM-01: sector model and scope rule; AM-03/29: reconciled registry and specialization priorities. |
| B-05 | Jurisdiction labels are listed but their cardinality, applicability, and missing-province behavior are undefined. Four initial provinces do not establish nationwide coverage. | AM-04: source hierarchy, label semantics, provincial extension and unsupported-jurisdiction behavior. |
| B-06 | Safety classes and excluded activities exist only as planning prose. | AM-05: review/escalation boundaries; AM-09/10 and AM-31: scenario and behavioral evidence. |
| B-07 | Starter text contains unverified, time-sensitive standards-edition and legal assertions. These remain source-proposal claims, not findings of this audit. | AM-07: official source and edition metadata; relevant regulatory/sector waves: claim-level verification before use. |
| B-08 | No manufacturing authoring, calculation, test, or fixture contract exists. Copying a reference validator would import unrelated assumptions. | AM-06/08/09: manufacturing-specific standards and validators; AM-10: five proved reference skills. |
| B-09 | Expected-route consistency alone cannot establish routing, refusal, or safe model behavior. | AM-09: distinguish structural checks, deterministic calculations, and observed agent outputs; AM-10/30/31: execute and record relevant behavioral evaluations. |
| B-10 | Licence and project governance are absent; inherited MIT examples do not authorize a licence choice. | Resolve licence choice before licensed skill distribution; AM-06 must expose this dependency, and AM-32 must complete governance. |
| B-11 | Local and remote history are empty. A local baseline is now connected, but no durable commit or remote snapshot exists. | Subsequent repository work: review and commit/push as appropriate; public release remains AM-32/33 work. |

Retain the existing sequence. In particular, prove the five reference classes at AM-10 before authoring family batches. AM-28 composes validated skills; AM-29 defines specialization architecture and priorities rather than implementing every sector. AM-33 must keep its audit-complete token separate from a `V1_READY` verdict.

## Acceptance and validation

The artifact audience is the contributor beginning AM-01. Optional broader research or reference-repository test execution is not required for this documentation-only baseline.

| Criterion | Evidence | Result |
|---|---|---|
| Inventory the actual project before editing. | Four-file inventory, sizes, initial Git failure, all four files read. | PASS |
| Inspect both reference projects and qualify evidence. | Checkout identities, working-tree status, specific files and limitations above. | PASS |
| Establish the user-supplied remote without overwriting content. | Authenticated metadata, empty refs, local `main`, verified `origin`. | PASS |
| Preserve bounded scope and the AM-10 gate. | Only audit/handoff additions and README/ROADMAP status edits; architecture hashes unchanged. | PASS |
| Make the next wave actionable without implementing it. | Findings mapped to owners and AM-01 brief in the final handoff. | PASS |
| Validate documentation integrity and status. | Relative-link check, six-file scope check excluding `.git`, all required handoff sections, contiguous AM-00–AM-33 definitions, ledger and hash checks. | PASS |
| Review the actual changes. | README/ROADMAP compared with pre-edit snapshots using `git diff --no-index`; added documents read in full. | PASS |

No manufacturing tests exist or were claimed to pass. Validation here consists of documentation integrity and repository-state checks. No model behavior, formula correctness, source freshness, legal applicability, live equipment safety, or release readiness was tested.

The architecture snapshots retained these SHA-256 hashes:

```text
domain-framework.md
7A9F73B7FF2CE631545BAA413C83C12EBBF8C1EFEA80531287FE1EC549E4A62D
master-taxonomy-v0.1.md
A4F1D40193B7D196DC8CE0BEC1710E3D678C989966003A477081BD05F9F76F34
```

## Closure

AM-00 is READY because the baseline, reference review, gaps, scope checks, and next-wave handoff are complete. All later waves remain unstarted. Continue with [AM-01 as defined in the handoff](handoffs/AM-00-final-handoff.md), using [ROADMAP.md](../../ROADMAP.md) as planning authority and current files as execution truth.
