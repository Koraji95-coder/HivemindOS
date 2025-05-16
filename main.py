"""
main.py 🌐
-----------
🚀 Entry point for the HivemindOS FastAPI backend.

Responsibilities:
- Launch API app
- Enable CORS for frontend
- Register modular routers
- Display current app version and environment mode
"""

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.routes import system
from shared.meta.version import __version__
from shared.users.user_profile_service import load_user_profile
from shared.state.session_manager import session
# 🧩 Agent Routes
from backend.api.routes import daphne_routes, bart_routes, cortexa_routes

#Profile Set
session.set_user_profile(load_user_profile("Dusti"))
# Detect runtime environment (default: development)
env = os.getenv("ENVIRONMENT", "development").upper()
print(f"🧠 HivemindOS v{__version__} booted in {env} mode")

# FastAPI app instance
app = FastAPI(
    title="HivemindOS",
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

# Register routers
app.include_router(system.router)
# 🧩 Agent Routes
app.include_router(daphne_routes.router)
app.include_router(bart_routes.router)
app.include_router(cortexa_routes.router)
