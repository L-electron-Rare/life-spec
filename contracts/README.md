# Contracts Index

`life-spec` does not duplicate machine-readable contracts.

The canonical shared service contracts live in [finefab-shared](../../finefab-shared), under:

- `finefab-shared/schemas/` for JSON Schema sources
- `finefab-shared/python/` for generated Pydantic models
- `finefab-shared/typescript/` for generated TypeScript types

Use this directory as an index for contract governance, mapping, and review notes only.

## Contract Governance Rules

- Add or change shared payload contracts in `finefab-shared/schemas/`.
- Regenerate derived types with `python scripts/generate_types.py` in `finefab-shared`.
- Reference the relevant schema path from specs and gates in `life-spec`.
- Do not create a second source of truth for schemas in `life-spec/contracts/`.
