# life-spec

Source de verite spec-first pour FineFab (specs, gates, compliance, evidence).

## Role
- Centraliser specs fonctionnelles et techniques.
- Porter les gates BMAD et controles de conformite.
- Orchestrer les evidence packs inter-repos.

## Stack
- Markdown
- JSON

## Structure cible
- `specs/`: documents spec-first
- `contracts/`: contrats et schemas
- `gates/`: definition des gates S0-S4

## Demarrage rapide
```bash
# Validation documentaire/contrats selon scripts du repo
ls -la specs contracts
```

## Roadmap immediate
- Completer S2/S3/S4.
- Connecter les gates aux pipelines CI.
- Standardiser generation d'- Standardiser generation d'- Standardiser generation d'- Standardiser generation d'- Standardiser generation d'- Standardiser generation d'- Standardiser generation d'- Standardiser generation d'- Standardiser generation d'- Standardiser generation d'- Standardiser generation d'- Standardiser generation d'- Standardiser generation d'- Standardiser generatg (datasets, evaluation, registry)

## Structure cible
- `src/`: orchestration et logique entrainement
- `datasets/`: donnees d'entrainement
- `scripts/`: runs, evaluation, publication

## Demarrage rapide
```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .
```

## Roadmap immediate
- Migrer pipeline fine-tuning depuis mascarade.
- Mettre en place model registry + hot-swap contract.
- Integrer controle qualite datasets.
