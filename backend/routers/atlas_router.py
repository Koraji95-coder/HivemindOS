"""
atlas_router.py 🛡️
────────────────────────────────────────
Handles system state summary via Atlas core logic.

Route: /api/atlas (GET)
Returns: full session + system state
"""

from fastapi import APIRouter
from shared.system.atlas_core import Atlas

router = APIRouter()
atlas = Atlas()

@router.get("")
async def get_state():
    # 🔍 Returns state from Atlas (session user, flags, mode, etc.)
    return atlas.summarize_state()
