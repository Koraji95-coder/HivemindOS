"""
main.py 🌐
-----------
🚀 Entry point for the HivemindOS FastAPI backend.

Responsibilities:
- Launch API app
- Registers API routes for Daphne, Bart, Cortexa, and Atlas
- Enable CORS for frontend integration
- Register modular routers
- Display current app version and environment mode
- Auto-generates OpenAPI docs at /docs
"""

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from shared.meta.version import __version__
from shared.users.user_profile_service import load_user_profile_from_system
from shared.state.session_manager import session
from backend.api.routes import (
    daphne_routes, bart_routes, cortexa_routes, atlas_routes,
    chain_routes, plugin_routes, logs_routes, system_routes
)

# Profile Set (best practice: sets canonical user & device)
session.set_user_profile(load_user_profile_from_system())

# Detect runtime environment (default: development)
env = os.getenv("ENVIRONMENT", "development").upper()
print(f"🧠 HivemindOS v{__version__} booted in {env} mode")

# FastAPI app instance
app = FastAPI(
    title="HivemindOS API",
    description="Backend API for multi-agent system",
    version=__version__
)

# CORS config — in dev, allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route Registration
app.include_router(atlas_routes, prefix="/api/atlas")
app.include_router(bart_routes, prefix="/api/bart")
app.include_router(daphne_routes, prefix="/api/daphne")
app.include_router(cortexa_routes, prefix="/api/cortexa")
app.include_router(chain_routes, prefix="/api/chain")
app.include_router(plugin_routes, prefix="/api/plugin")
app.include_router(logs_routes, prefix="/api/logs")
app.include_router(system_routes, prefix="/api/system")

# Mount the built frontend at "/"
app.mount("/", StaticFiles(directory="hivemind-ui/dist", html=True), name="frontend")