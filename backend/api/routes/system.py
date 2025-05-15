"""
System routes for diagnostics 🧠
--------------------------------
Exposes health check, status info, and uptime monitoring.

Endpoints:
- GET /health
- GET /status
- GET /uptime
"""

import os
import time
from datetime import datetime, timezone

from fastapi import APIRouter

from shared.meta.version import __version__

router = APIRouter()

# App start time (UTC)
START_TIME = datetime.now(timezone.utc)

def get_uptime_seconds() -> int:
    return int((datetime.now(timezone.utc) - START_TIME).total_seconds())

@router.get("/health", tags=["System"])
def health_check():
    """
    Quick check to confirm API is reachable.
    """
    return {"status": "healthy"}

@router.get("/uptime", tags=["System"])
def get_uptime():
    """
    Returns how long the app has been running.
    """
    seconds = get_uptime_seconds()
    hours, rem = divmod(seconds, 3600)
    minutes, seconds = divmod(rem, 60)
    return {"uptime": f"{hours}h {minutes}m {seconds}s"}

@router.get("/status", tags=["System"])
def system_status():
    """
    Returns current app metadata and environment status.
    """
    return {
        "app": "HivemindOS",
        "version": __version__,
        "environment": os.getenv("ENVIRONMENT", "development"),
        "uptime_seconds": get_uptime_seconds()
    }
