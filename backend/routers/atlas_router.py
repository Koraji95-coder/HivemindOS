"""
atlas_router.py 🛡️
────────────────────────────────────────
Handles system state summary via Atlas core logic.

Route: /api/atlas (GET)
Returns: full session + system state
"""

from fastapi import APIRouter
from fastapi import Request
from shared.system.atlas_core import Atlas

router = APIRouter()
atlas = Atlas()

@router.get("")
async def get_state():
    # 🔍 Returns state from Atlas (session user, flags, mode, etc.)
    return atlas.summarize_state()

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