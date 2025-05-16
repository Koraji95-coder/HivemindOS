"""
mood_state_tracker.py 💭

Tracks the mood of each user session.
Stores and retrieves mood values using in-memory context.

In the future, this could persist mood in memory_router or user profile store.
"""

from shared.state.session_manager import session

def set_user_mood(username: str, mood: str):
    """
    Stores the user's current mood in session memory.

    Args:
        username (str): Active user
        mood (str): Detected mood string
    """
    memory = session.get_memory()
    memory[username] = memory.get(username, {})
    memory[username]["mood"] = mood

def get_user_mood(username: str) -> str:
    """
    Retrieves the user's current mood from session memory.

    Args:
        username (str): Active user

    Returns:
        str: Last known mood or 'neutral'
    """
    return session.get_memory().get(username, {}).get("mood", "neutral")
