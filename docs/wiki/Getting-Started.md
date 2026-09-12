# Getting started

For a developer or manufacturing analyst, this walkthrough ends with a validated checkout and a resolved planning workflow. You need Git and Python. The validation environment is Python 3.14 on Linux and Windows; no third-party Python packages are required.

## Get and check the library

```powershell
git clone https://github.com/jeremylongworth-source/AgentManufacturing.git
cd AgentManufacturing
python scripts/validate-all.py
```

Run commands from the checkout root. The gate must finish successfully; failures identify the affected validator. This checks repository artifacts, not model output.

## Resolve a planning workflow

```powershell
python scripts/resolve-skillset.py production-planner horizon-plan
```

Expect `REFERENCES_RESOLVED`, `execution: NOT_EXECUTED` and `evidence_state: NOT_ASSESSED`. Open the returned SKILL.md files and their relevant references. Collect demand horizon, capacity, BOM, materials and labor evidence before applying the methods.

The finished artifact is a reference list for preparing a production plan proposal and readiness gaps. It is not an executable production plan or permission to release orders.

## Check sector coverage

```powershell
python scripts/inspect-sector-coverage.py automotive
python scripts/inspect-sector-coverage.py automotive --generic-only
```

Expect `COVERAGE_GAP` for sector requirements. The second command permits generic methods while retaining unsupported sector conclusions. Continue with [[Using a Skill|Using-a-Skill]] for a synthetic worked example.

If Python is unavailable, install a suitable interpreter through your normal development setup and reopen the terminal. If a file cannot be found, check the working directory and clone completeness. See [[FAQ and Troubleshooting|FAQ-and-Troubleshooting]].
