# life-spec

Spec-first pipeline for FineFab -- functional specifications, BMAD gates, and compliance evidence.

Part of the [FineFab](https://github.com/L-electron-Rare) platform.

## What it does

- Defines functional specifications for every FineFab subsystem
- Enforces a structured gate process (BMAD S0-S4) from scoping through production
- Stores compliance evidence and technical contracts between services
- Acts as the single source of truth for platform architecture decisions

## BMAD gates

| Gate | Name | Purpose |
|------|------|---------|
| S0 | Scoping | System perimeter, actors, constraints |
| S1 | Architecture | Components, interfaces, data flows |
| S2 | Implementation | Code, tests, coverage, CI |
| S3 | Integration | E2E tests, deployment, monitoring |
| S4 | Production | Go-live, observability, governance |

## Project structure

```
specs/        # Functional specifications by domain
contracts/    # Contract governance index; canonical schemas live in finefab-shared
gates/        # BMAD gate definitions (S0-S4)
```

## Related repos

| Repo | Role |
|------|------|
| [life-core](https://github.com/L-electron-Rare/life-core) | AI backend engine |
| [life-reborn](https://github.com/L-electron-Rare/life-reborn) | API gateway |
| [life-web](https://github.com/L-electron-Rare/life-web) | Operator cockpit UI |
| [finefab-shared](https://github.com/L-electron-Rare/finefab-shared) | Shared contracts and types |

## License

[MIT](LICENSE)
