"""
in_memory_engine.py 🧠

Lightweight, session-scoped in-memory key-value store.
Used for volatile memory operations that persist only during runtime.

Memory is isolated per user and accessed via MemoryRouter.

Examples:
- Store temporary thoughts, commands, scratch data
- Used in testing, dev mode, or fallback from file memory
"""

class InMemoryEngine:
    def __init__(self):
        """
        Initialize the in-memory storage dictionary.
        Structure: { username: { key: value } }
        """
        self._store = {}

    def save(self, user, key, value):
        """
        Save a key-value pair under a specific user's memory scope.

        Args:
            user (str): The username/session identifier
            key (str): The memory key
            value (Any): The value to store
        """
        self._store.setdefault(user, {})[key] = value

    def fetch(self, user, key):
        """
        Retrieve a value for a given key from a user's memory.

        Args:
            user (str): The username/session identifier
            key (str): The memory key to retrieve

        Returns:
            Any: The stored value or None if not found
        """
        return self._store.get(user, {}).get(key)

    def clear(self, user):
        """
        Wipe all in-memory data for a given user.

        Args:
            user (str): The username/session identifier
        """
        self._store[user] = {}
