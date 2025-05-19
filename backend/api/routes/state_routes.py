"""
state_router.py 📊
────────────────────────────────────────
Provides runtime visibility into session state:
- Mood
- Flags
- Temporary memory
"""

from fastapi import APIRouter
from shared.state.session_manager import session
from shared.state.mood_state_tracker import get_user_mood

router = APIRouter(prefix="/api/state", tags=["State"])

@router.get("/mood")
def get_current_mood():
    """
    Returns the current mood for the active session user.

    Source:
    - `session.get_user_name()` for ID
    - `get_user_mood()` for tracked mood (from mood_state_tracker)

    Returns:
        JSON: { user, mood }
    """
    user = session.get_user_name()
    mood = get_user_mood(user)
    return { "user": user, "mood": mood }

@router.get("/memory")
def get_memory_dump():
    """
    Returns the full memory + runtime flags of the session.

    Includes:
    - Current user
    - Context flags (`set_flag()`)
    - Memory dict (`set_memory()` / mood / agent chains etc.)

    Returns:
        JSON: { user, flags, memory }
    """
    return {
        "user": session.get_user_name(),
        "flags": session.get_context(),
        "memory": session.get_memory()
    }