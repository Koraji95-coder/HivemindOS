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

## [v0.0.4] - Router Activation + I/O Integration

### Added
- Daphne, Bart, and Cortexa agent routes
- POST-based `/ask` endpoints for each agent
- output_router with ui_output() for CLI/GUI print bridging
- First route-based test: `test_daphne_routes.py`

## [v0.0.5] - Output Router + Agent API Routes
- Added `shared.io.output_router` for CLI/GUI output redirection
- Added FastAPI route modules:
  - `daphne_routes.py`
  - `bart_routes.py`
  - `cortexa_routes.py`
- Each route provides a basic POST endpoint stubbed for future expansion
- Added route test scaffold: `test_routes/test_daphne_routes.py`
