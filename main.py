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
