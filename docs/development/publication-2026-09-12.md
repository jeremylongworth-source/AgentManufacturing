# Public development library publication

Date: 2026-09-12
Status: PARTIALLY_READY — Wiki publication awaits browser sign-in.

## Authorized scope and outcomes

The owner explicitly requested matching FUNDING.yml, a complete GitHub Wiki, public visibility and a public-facing README review. This authorization is separate from the historical AM-33 audit. No stable v1 release is claimed; V1_PARTIALLY_READY and F01–F04 remain in effect.

- FUNDING.yml contains exactly `github: jeremylongworth-source`, matching AgentSkills (rechecked today) and the previously inspected AgentLogistics, AgentCannabis and ChefSkills.
- README now includes clone instructions, Wiki navigation, sponsorship and development scope; private-checkout wording was removed. CONTRIBUTING describes public pull requests without support or merge promises.
- Thirteen Wiki pages plus sidebar and footer are complete in docs/wiki. The catalogue lists all 159 canonical skills; the role reference lists 18 roles and 38 workflows.
- Commit `8b89e205a351a226e08ffca0bb73d23c7acb6ba3` was pushed to main.
- GitHub CLI changed visibility to PUBLIC and enabled the Wiki. The signed-out browser displayed the public README and Sponsor button.
- The Wiki Git clone returned Repository not found because no initial Wiki page exists. The available browser is signed out; sign-in was requested so the initial page can be created.

## Acceptance evidence

| Criterion | Result |
|---|---|
| Funding matches existing projects | PASS |
| README reviewed, public content rendered | PASS |
| Repository public | PASS — gh repo view and signed-out browser |
| Wiki source complete | PASS — 15 files including navigation |
| Actual GitHub Wiki published | PENDING — initial page requires signed-in browser |

All 32 validators passed with `python scripts/validate-all.py`. Strict AM-32 readiness passed. The documented production-planner resolver and both automotive coverage commands produced the described states. A local link check verified 268 targets across Wiki, README and CONTRIBUTING with no missing paths. `git diff --check` and the staged whitespace check passed.

[CI run 34694595831](https://github.com/jeremylongworth-source/AgentManufacturing/actions/runs/34694595831) passed on Linux and Windows for commit 8b89e20. This is repository validation, not independent model evaluation.

## Handoff and maintenance

After the owner signs in to GitHub in the Codex browser, create Home in the Wiki, clone AgentManufacturing.wiki.git under .git/wiki-publish, synchronize docs/wiki, commit and push. Verify all published pages and navigation, then update this record to READY. Main-repository source files alone do not complete Wiki publication.

Jeremy Longworth remains the reporting recipient under SECURITY.md and CODE_OF_CONDUCT.md. No delivery test or support SLA is implied. Documentation corrections can be reverted through normal Git changes; public history may already have been copied, so reverting visibility cannot recall copies. No external announcements or tagged release were made.
