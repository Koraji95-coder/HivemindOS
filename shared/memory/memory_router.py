"""
memory_router.py 🧠

Manages temporary and persistent memory for the current session.
Delegates to in-memory or file-based engines depending on config.
"""

from shared.memory.in_memory_engine import InMemoryEngine
from shared.memory.file_memory_engine import FileMemoryEngine
from shared.state.session_manager import session

class MemoryRouter:
    def __init__(self):
        self.mode = session.get_flag("memory_mode") or "in-memory"
        self.user = session.get_user_name()

        self.in_memory = InMemoryEngine()
        self.file_memory = FileMemoryEngine()

    def save(self, key, value):
        """
        Stores memory for this session's user.
        """
        if self.mode == "file":
            return self.file_memory.save(self.user, key, value)
        else:
            return self.in_memory.save(self.user, key, value)

    def fetch(self, key):
        """
        Retrieves memory for this session's user.
        """
        if self.mode == "file":
            return self.file_memory.fetch(self.user, key)
        else:
            return self.in_memory.fetch(self.user, key)

    def clear(self):
        """
        Clears memory for this session's user.
        """
        if self.mode == "file":
            return self.file_memory.clear(self.user)
        else:
            return self.in_memory.clear(self.user)
