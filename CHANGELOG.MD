# 📦 CHANGELOG

## v0.0.1 — Bootstrap & Core Setup

✅ Initial scaffolding of HivemindOS backend architecture

### ✨ Highlights
- `main.py` with FastAPI app + CORS
- `/health`, `/uptime`, `/version` system endpoints
- `.env` file loader with test/dev detection
- VS Code settings: black, isort, pytest
- Directory structure: backend/, shared/, tests/, tools/
- Logger + basic system bootstrap printing

## [v0.0.2] - Agent Core Integration
- Added `AgentBase` foundation for multi-agent architecture.
- Introduced `GPTClient` with test-mode fallback.
- Integrated `DaphneAgent`, `BartAgent`, `CortexaAgent`.
- Built basic `tests/test_agents.py` with output assertions.
- Implemented terminal output tagging for agent roles.

## [v0.0.3] - Route Layer Injection
- Added `/api/daphne/ask`, `/api/bart/ask`, `/api/cortexa/ask` endpoints
- Registered all route files in `main.py`
- Added `test_daphne_routes.py` using FastAPI's test client
- Enabled agent interaction over API

