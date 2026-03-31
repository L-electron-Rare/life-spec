# Architecture Système — FineFab Life

## Vue d'ensemble

FineFab Life est une plateforme de fabrication assistée par IA. Elle comprend :

### Services principaux (déployés sur Tower)

| Service | Technologie | Port | Rôle |
| ------- | ----------- | ---- | ---- |
| life-core | FastAPI / Python 3.12 | 8000 | Backend LLM router, RAG, cache |
| life-reborn | Hono / TypeScript | 3210 | API Gateway, auth, rate-limiting |
| life-web | React 19 / Vite | 80 | Cockpit opérationnel (6 sections) |
| Redis | Redis 7 | 6379 | Cache multi-tier |
| Qdrant | Qdrant | 6333 | Vector store RAG (184 vecteurs) |
| Forgejo | Gitea | 3000 | Miroir GitHub (6 repos) |
| Langfuse | Langfuse v2 | 3000 | Observabilité LLM |
| Jaeger | Jaeger | 16686 | Traces distribuées |
| OTEL Collector | OpenTelemetry | 4317 | Pipeline de traces |
| Traefik | Traefik 3 | 80/443 | Reverse proxy TLS |

### Machines

| Machine | IP | Rôle |
| ------- | -- | ---- |
| Tower | 192.168.0.120 | Serveur principal (11 containers) |
| KXKM-AI | 100.87.54.119 | GPU RTX 4090, Ollama (33 modèles) |
| Photon | 192.168.0.119 | VPS observabilité |

### Providers LLM

| Provider | Statut | Modèles |
| -------- | ------ | ------- |
| Ollama (Tower) | Actif | qwen3:4b, nomic-embed-text |
| Ollama GPU (KXKM-AI) | Down (Tailscale) | 33 modèles |
| Claude (Anthropic) | Clé invalide | claude-3.5-* |
| OpenAI | Quota épuisé | gpt-4o, gpt-3.5 |
| Mistral | Clé invalide | mistral-large, mistral-small |

### Domaines

| Domaine | URL |
| ------- | --- |
| API Gateway | api.saillant.cc |
| Cockpit | life.saillant.cc |
| Git miroir | git.saillant.cc |
| Langfuse | langfuse.saillant.cc |
| Jaeger | jaeger.saillant.cc |
