# FAQ and Troubleshooting

## Is this an installer or executor?

No. The repository provides methods, references, routing metadata, and validation artifacts. It does not execute manufacturing work or approve an engineering, safety, legal, or product decision.

## Why do the counts differ?

The repository can contain 161 skill directories while the catalogue lists 159 canonical skills. The difference reflects traceable historical or duplicate packages. Use canonical paths for new references.

## Why do some YAML files look like JSON?

The package contract permits JSON-compatible YAML for machine-readable metadata. Validate it with the repository scripts rather than relying on filename appearance.

## What does the resolver prove?

It proves that a declared reference maps to a canonical package. It does not prove applicability, source freshness, or qualified approval.

## What if a sector or source is missing?

Keep the gap visible. Record the missing evidence, avoid an unsupported conclusion, and route the question to a qualified reviewer.

## Where do I report a vulnerability?

Use [GitHub private vulnerability reporting](https://github.com/jeremylongworth-source/AgentManufacturing/security/advisories/new). For conduct concerns, use the [private conduct form](https://conduct.pmgate.ai/).

## Is V1 stable?

No. The current release status is `V1_PARTIALLY_READY`; see [Roadmap and Release Status](Roadmap-and-Release-Status).
