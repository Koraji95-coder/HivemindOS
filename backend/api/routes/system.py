"""
system.py 🧠
-------------
System-level API endpoints for HivemindOS.

Includes:
- /health
- /uptime
- /version
"""

import time
from fastapi import APIRouter
from shared.meta.version import __version__
from datetime import datetime

router = APIRouter(tags=["System"])
BOOT_TIME = time.time()

@router.get("/health")
def health_check():
    """Health ping for uptime monitors."""
    return {"status": "ok", "booted": datetime.utcnow().isoformat()}

@router.get("/uptime")
def get_uptime():
    """Returns how long the app has been running."""
    uptime = round(time.time() - BOOT_TIME, 2)
    return {"uptime_seconds": uptime}

@router.get("/version")
def get_version():
    """Returns the current HivemindOS version."""
    return {"version": __version__}
