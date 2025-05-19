"""
backend.api.routes
------------------
Aggregates all FastAPI routers; for easy import in backend.main.
"""

from .atlas_routes import router as atlas_routes
from .bart_routes import router as bart_routes
from .chain_routes import router as chain_routes
from .cortexa_routes import router as cortexa_routes
from .daphne_routes import router as daphne_routes
from .logs_routes import router as logs_routes
from .plugin_routes import router as plugin_routes
from .system_routes import router as system_routes

__all__ = [
    "atlas_routes",
    "bart_routes",
    "chain_routes",
    "cortexa_routes",
    "daphne_routes",
    "logs_routes",
    "plugin_routes",
    "system_routes"
]