# Contributing and Maintenance

This page is for contributors changing skills, references, validators, or public documentation.

## Before opening a change

1. Read the repository [README](https://github.com/jeremylongworth-source/AgentManufacturing#readme), `ROADMAP.md`, and latest handoff.
2. Identify the canonical package and the contract it must satisfy.
3. Keep generic methods separate from Canadian jurisdiction and sector requirements.
4. Add or update synthetic fixtures and expected routing only when the declared expectation changes.
5. Run the focused validator, then `python scripts/validate-all.py` and `git diff --check`.
6. Record actual commands, outcomes, unresolved work, and the next bounded step in the roadmap and handoff.

Do not use production records or sensitive operational data in fixtures. Do not bypass qualified-review boundaries or fabricate evidence.

## Keeping the Wiki current

The source pages live in `docs/wiki`. After changing them, copy the Markdown files to the GitHub Wiki repository, review the staged diff, and push the Wiki branch. Keep page names and sidebar links aligned with the source pages.

## Review standard

A wave is READY only when its acceptance criteria are met and evidence is recorded. Publication and documentation preparation are separate decisions.
