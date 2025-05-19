"""
session_manager.py 🧠

Provides shared session context (user profile, memory, state, etc).
"""
import os
from shared.users.user_identity import UserIdentity

class SessionManager:
    def __init__(self):
        self._context = {}
        self._profile = {}  # Holds user profile dict set once at app/user login
        self._memory = {}
        self.user_identity = UserIdentity()

    def set_user_profile(self, profile: dict):
        """
        Sets user profile object. No hardcoding of usernames or device!
        """
        self._profile = profile
        self._context["username"] = profile.get("name", "unknown")

    def get_user_profile(self):
        return self._profile

    def get_user_name(self):
        return self._profile.get("name") or os.getenv("USER") or "guest"

    def get_user_role(self):
        return self.user_identity.get_role(self.get_user_name())

    def get_flag(self, key):
        return self._context.get(key)

    def set_flag(self, key, value):
        self._context[key] = value

    def get_context(self):
        return self._context

    def get_memory(self):
        return self._memory

    def get_device_id(self):
        return self._profile.get("device_id") or "unknown-device"

# Singleton
session = SessionManager()