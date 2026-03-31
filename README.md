# life-spec — Spécifications Fonctionnelles FineFab

Dépôt des spécifications fonctionnelles, contrats techniques et gates BMAD pour l'écosystème Factory 4 Life.

## Structure

```text
specs/          # Spécifications fonctionnelles par domaine
contracts/      # Contrats techniques inter-services
gates/          # Définitions des gates BMAD (S0-S4)
```

## Gates BMAD

| Gate | Nom | Description |
| ---- | --- | ----------- |
| S0 | Cadrage | Périmètre système, acteurs, contraintes |
| S1 | Architecture | Composants, interfaces, flux de données |
| S2 | Implémentation | Code, tests, couverture, CI |
| S3 | Intégration | Tests E2E, déploiement, monitoring |
| S4 | Production | Go-live, observabilité, gouvernance |

## Projets couverts

- `life-core` — Backend LLM router, RAG, cache
- `life-reborn` — API Gateway
- `life-web` — Cockpit opérationnel
- `makelife-cad` — Plateforme CAO/EDA
- `makelife-firmware` — Firmware ESP32
- `makelife-hard` — Conception électronique
- `finefab-shared` — Contrats partagés (24 schemas JSON)

## Convention

- Documentation en français
- Un fichier par spec, nommé `DOMAINE_SUJET.md`
- Chaque spec référence le gate BMAD correspondant
