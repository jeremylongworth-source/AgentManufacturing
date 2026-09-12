# FAQ and troubleshooting

## Does this install or run an AI agent?

No automatic executor or host installer is provided by the documented workflow. The resolver supplies references. Read the packages and use your host's supported loading mechanism; compatibility must be verified separately.

## Why does a YAML file look like JSON?

Some YAML files intentionally use JSON syntax so standard-library Python can parse them without additional dependencies.

## Why are there 161 directories but 159 skills?

Two historical duplicate packages remain traceable. Use the canonical map in composition-contract.json and the [[Skill Catalogue|Skill-Catalogue]].

## The resolver cannot find a role or workflow

Copy an exact role name and workflow ID from [[Professional Skillsets|Professional-Skillsets]]. Run from the repository root. A successful lookup still does not execute the workflow.

## A sector inspection reports a gap

Sector requirements have not been implemented. Use generic-only mode only for conclusions supported by sector-neutral evidence. See [[Sector Specializations|Sector-Specializations]].

## A validator fails after my change

Read the named validator's output, fix the underlying contract or evidence mismatch, then rerun the focused check and full gate. Do not erase a historical result or refresh a snapshot without reassessment.

## Can these results approve manufacturing work?

No. Analysis and review support do not grant operating, engineering, product-release or legal authority. See [[Jurisdiction and Safety|Jurisdiction-and-Safety]].

## Is a public repository a stable v1 release?

The repository is shared for development and reference. The audit remains V1_PARTIALLY_READY; independent evaluation and other remediation are still outstanding.
