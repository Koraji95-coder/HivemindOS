# 🧠 HivemindOS

Multi-agent reasoning framework built with Python, FastAPI, and modular HTML UI widgets.

> ⚙️ Version: `v0.0.1`  
> 🔄 Status: Bootstrap Complete

---

## 🚀 Features

- FastAPI backend (`main.py`)
- Modular routing (`backend/`)
- Shared libraries and tools (`shared/`, `tools/`)
- Test-ready layout (`tests/`)
- Frontend folder prepared for HTML/JS integration (`frontend/`)
- Environment config with `.env`
- Pyproject-based dependency management

---

## 📂 Project Structure

```txt
HivemindOS/
├── backend/          # Core backend services, routers, agents
├── frontend/         # HTML UI, widgets, JS assets
├── shared/           # Common logic, config loaders, meta info
├── tests/            # Pytest-based test modules
├── tools/            # Scripts like init generators, utils
├── main.py           # FastAPI app entry point
├── .env              # Environment variables (local only)
├── pyproject.toml    # Poetry dependency + tool config
├── README.md         # Project intro, features, setup
├── CHANGELOG.md      # Semantic versioning + logs
