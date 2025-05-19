"""
system.py 🧠
--------------------------------
System routes for diagnostics.

Exposes health check, status info, and uptime monitoring.

Endpoints:
- GET /health: Confirms backend is alive.
- GET /status: Returns status metadata.
- GET /uptime: Returns lifetime since launch.
"""

import os
from datetime import datetime, timezone
from fastapi import APIRouter
from shared.meta.version import __version__
from shared.logging.logger import get_logger

# --- Logger for System diagnostics ---
logger = get_logger("system")

router = APIRouter(prefix="/api/system", tags=["System"])

# --- App start time (UTC) ---
START_TIME = datetime.now(timezone.utc)

def get_uptime_seconds() -> int:
    """
    Returns the number of seconds since the app started.
    """
    return int((datetime.now(timezone.utc) - START_TIME).total_seconds())

@router.get("/health", tags=["System"])
def health_check():
    """
    Quick check to confirm API is reachable.
    
    Returns:
        dict: Health status
    """
    logger.info("Health check requested.")
    return {"status": "healthy"}

@router.get("/uptime", tags=["System"])
def get_uptime():
    """
    Returns how long the app has been running.

    Returns:
        dict: Human-readable uptime
    """
    seconds = get_uptime_seconds()
    hours, rem = divmod(seconds, 3600)
    minutes, seconds = divmod(rem, 60)
    logger.info(f"Uptime requested: {hours}h {minutes}m {seconds}s")
    return {"uptime": f"{hours}h {minutes}m {seconds}s"}

@router.get("/status", tags=["System"])
def system_status():
    """
    Returns current app metadata and environment status.

    Returns:
        dict: App name, version, env, uptime
    """
    logger.info("Status endpoint requested.")
    return {
        "app": "HivemindOS",
        "version": __version__,
        "environment": os.getenv("ENVIRONMENT", "development"),
        "uptime_seconds": get_uptime_seconds()
    }