"""
atlas_router.py 🛡️
────────────────────────────────────────
Handles system state reporting and mode control.

Routes:
- GET /api/atlas → returns session, flags, version, mode
- POST /api/atlas/mode → sets runtime mode
"""

from fastapi import APIRouter
from fastapi import Request
from shared.system.atlas_core import Atlas
from shared.meta.version import __version__
from shared.state.session_manager import session

router = APIRouter()
atlas = Atlas()

@router.get("")
async def get_state():
    return {
        "mode": atlas.system_mode,
        "flags": session.get_context(),
        "user": session.get_user_profile(),
        "version": __version__  # ✅ Injected version here
    }

@router.post("/mode")
async def set_mode(request: Request):
    """
    Allows setting the system's runtime mode (development, maintenance, etc.)

    Input JSON:
        { "mode": "maintenance" }

    Effects:
    - Sets Atlas system mode
    - Does not affect flags or safety directly

    Returns:
        JSON: { status, mode }
    """
    data = await request.json()
    mode = data.get("mode")

    atlas.set_mode(mode)
    return { "status": "ok", "mode": atlas.system_mode }