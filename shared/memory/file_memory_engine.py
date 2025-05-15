"""
file_memory_engine.py 💾

Persistent memory engine that saves user-specific key-value data to JSON files.
Used for long-term storage of agent thoughts, feedback, context, etc.

Each user gets an isolated file under `data/memory/`.

Examples:
- Save prediction feedback
- Store analysis results or agent outputs
- Recall past input triggers per user
"""

import os
import json

class FileMemoryEngine:
    def __init__(self):
        """
        Initialize the base directory for memory files.
        Ensures the folder exists on disk.
        """
        self.base_dir = "data/memory/"
        os.makedirs(self.base_dir, exist_ok=True)

    def _path(self, user):
        """
        Generate a full file path for the given user.

        Args:
            user (str): The session username

        Returns:
            str: Full path to memory file
        """
        return os.path.join(self.base_dir, f"{user.lower()}_mem.json")

    def save(self, user, key, value):
        """
        Save a key-value pair to the user's memory file.

        Args:
            user (str): Username/session ID
            key (str): Key to store
            value (Any): Value to persist
        """
        path = self._path(user)
        memory = self._load(path)
        memory[key] = value
        with open(path, "w") as f:
            json.dump(memory, f, indent=2)

    def fetch(self, user, key):
        """
        Retrieve a stored value for a user + key from file.

        Args:
            user (str): Username/session ID
            key (str): Memory key

        Returns:
            Any: Retrieved value or None if missing
        """
        return self._load(self._path(user)).get(key)

    def clear(self, user):
        """
        Erase all stored memory for a given user.

        Args:
            user (str): Username/session ID
        """
        with open(self._path(user), "w") as f:
            json.dump({}, f)

    def _load(self, path):
        """
        Load memory JSON file contents.

        Args:
            path (str): Path to the memory file

        Returns:
            dict: Loaded memory dictionary
        """
        if os.path.exists(path):
            with open(path) as f:
                return json.load(f)
        return {}
