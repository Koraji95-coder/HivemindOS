"""
fastapi_main.py 🚀
────────────────────────────────────────
Entry point for HivemindOS FastAPI web server.

- Registers API routes for Daphne, Bart, Cortexa, and Atlas
- Enables CORS for frontend integration
- Auto-generates OpenAPI docs at /docs
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routers import daphne_router, bart_router, cortexa_router, atlas_router
from backend.routers import chain_router
from backend.routers import plugin_router

app = FastAPI(title="HivemindOS API 🧠", version="0.1.0")

# 🔓 Allow frontend/dev clients to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔌 Route Registration
app.include_router(daphne_router.router, prefix="/api/daphne")
app.include_router(bart_router.router, prefix="/api/bart")
app.include_router(cortexa_router.router, prefix="/api/cortexa")
app.include_router(atlas_router.router, prefix="/api/atlas")
app.include_router(chain_router.router, prefix="/api/chain")
app.include_router(plugin_router.router, prefix="/api/plugin")
