# Getting Started

This page is for contributors and reviewers who want a local, repeatable check of the repository.

## Outcome

By the end, you will have a checkout that resolves its canonical references and passes the public-readiness and structural validators.

## Prerequisites

- Git
- Python 3.11 or newer
- PowerShell, Bash, or an equivalent shell

## Install and validate

```bash
git clone https://github.com/jeremylongworth-source/AgentManufacturing.git
cd AgentManufacturing
python scripts/validate-public-readiness.py --require-ready
python scripts/validate-all.py
```

The expected full-gate result is:

```text
PASS: all 32 repository validators completed.
```

## Resolve a skill reference

```bash
python scripts/resolve-skill.py --skill takt-time-calculation
```

The resolver should report `REFERENCES_RESOLVED`. A resolved reference is a routing result, not an authorization to perform the work.

## Inspect sector coverage

```bash
python scripts/inspect-sector-coverage.py
python scripts/validate-sector-coverage.py
```

## You are finished when

- both repository commands pass;
- references resolve to canonical paths;
- source freshness and missing evidence remain visible; and
- you understand the qualified-review boundary for the work.

## If a check fails

Read the first failing validator output, inspect the referenced fixture or package metadata, and rerun the focused validator before rerunning the full gate. See [FAQ and Troubleshooting](FAQ-and-Troubleshooting) for common causes.
