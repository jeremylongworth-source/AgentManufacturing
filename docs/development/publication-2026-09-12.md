# Public development library publication

Date: 2026-09-12
Status: READY — all four owner-requested publication items completed.

## Authorized scope and outcomes

The owner explicitly requested matching FUNDING.yml, a complete GitHub Wiki, public visibility and a public-facing README review. This authorization is separate from the historical AM-33 audit. No stable v1 release is claimed; V1_PARTIALLY_READY and F01–F04 remain in effect.

- FUNDING.yml contains exactly `github: jeremylongworth-source`, matching AgentSkills (rechecked today) and the previously inspected AgentLogistics, AgentCannabis and ChefSkills.
- README now includes clone instructions, Wiki navigation, sponsorship and development scope; private-checkout wording was removed. CONTRIBUTING describes public pull requests without support or merge promises.
- Sixteen Wiki pages plus sidebar and footer are complete in docs/wiki. The public information architecture now separates start-here guidance, system understanding, reference, and maintenance. The catalogue lists all 159 canonical skills; the role reference lists 18 roles and 38 workflows.
- The public documentation overhaul is in main commit `1c6ce5c13a828e162476281cd7b967e6a27bd522` and Wiki commit `4887f8e`.
- GitHub CLI changed visibility to PUBLIC and enabled the Wiki. The signed-out browser displayed the public README and Sponsor button.
- The first Wiki clone was unavailable before initialization. The owner then created Home; the clone succeeded and all prepared pages were published in Wiki commit `bc378eed27e8600dd32507a87fb09ce9824a53fb`.

## Acceptance evidence

| Criterion | Result |
|---|---|
| Funding matches existing projects | PASS |
| README reviewed, public content rendered | PASS |
| Repository public | PASS — gh repo view and signed-out browser |
| Wiki source complete | PASS — 16 pages plus sidebar and footer |
| Actual GitHub Wiki published | PASS — 16 public pages, sidebar and footer pushed |

All 32 validators passed with `python scripts/validate-all.py`. Strict AM-32 readiness passed. The documented production-planner resolver and both automotive coverage commands produced the described states. A local link check verified 268 targets across Wiki, README and CONTRIBUTING with no missing paths. `git diff --check` and the staged whitespace check passed.

[CI run 34694595831](https://github.com/jeremylongworth-source/AgentManufacturing/actions/runs/34694595831) passed on Linux and Windows for the pre-history-clean revision 8b89e20. This is repository validation, not independent model evaluation. The public main branch now points to the history-clean head b6f62bd.

## History cleanup

On 2026-09-12, reachable main and Wiki history was rewritten to remove the owner's personal email from historical content and author/committer metadata. Future commits use the GitHub noreply identity. The old histories are retained only in offline local bundles outside both repositories; existing clones and third-party copies may still contain them. The history-clean rewrite head was main `b6f62bd`; this record is maintained at `94082bf`. The Wiki head is `6f97336`.

## Handoff and maintenance

The Wiki was cloned under .git/wiki-publish, synchronized from docs/wiki, committed and pushed to master. Unauthenticated HTTP checks verified the canonical Wiki landing page, the new Choose a Path page, and the sidebar returned 200 with Wiki content. Home redirects to the canonical /wiki URL and contains sidebar navigation. An initial check incorrectly required /Home to remain in the final URL; allowing GitHub's canonical redirect corrected the check. Wiki staged whitespace checks passed.

Maintain docs/wiki and synchronize approved changes to the separate Wiki repository. Continue substantive development with AM-33 remediation F01–F04; public access does not resolve independent evaluation, qualified source review or support ownership gaps.

Jeremy Longworth remains the reporting recipient under SECURITY.md and CODE_OF_CONDUCT.md. No delivery test or support SLA is implied. Documentation corrections can be reverted through normal Git changes; public history may already have been copied, so reverting visibility cannot recall copies. No external announcements or tagged release were made.
