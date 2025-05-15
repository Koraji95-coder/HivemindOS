"""
session_manager.py 🧠

Provides a shared session context across the app.
Stores user profile, role, memory, and state flags for current runtime.
"""

import os


from shared.system.atlas_core import Atlas
from shared.users.user_identity import UserIdentity


class SessionManager:
    def __init__(self):
        # Runtime state flags (environment, debug mode, etc.)
        self._context = {}
        # Stores the active user's profile
        self._profile = {}
        # Temporary memory container (per session)
        self._memory = {}
        # Link to user identity role resolution logic
        self.user_identity = UserIdentity()

    def set_user_profile(self, profile: dict):
        """
        Set the active user's profile dictionary.
        Also updates the runtime context with username.
        """
        self._profile = profile
        self._context["username"] = profile.get("name", "unknown")
        atlas = Atlas()
        session.set_user_profile({
            "name": "Dusti",
            "device_id": "dev-777-flagship"
        })

        print(atlas.identify())
        print(atlas.summarize_state(session))

    def get_user_profile(self):
        """
        Return the full profile dictionary for the current user.
        """
        return self._profile

    def get_user_name(self):
        """
        Returns the name of the current user.
        Falls back to OS user or 'guest'.
        """
        return self._profile.get("name") or os.getenv("USER") or "guest"

    def get_user_role(self):
        """
        Resolves the user's role using UserIdentity class.
        """
        return self.user_identity.get_role(self.get_user_name())

    def get_flag(self, key):
        """
        Get a runtime flag by key (e.g., 'debug_mode').
        """
        return self._context.get(key)

    def set_flag(self, key, value):
        """
        Set a runtime flag (e.g., 'theme' = 'dark').
        """
        self._context[key] = value

    def get_context(self):
        """
        Return the full context dictionary (flags, runtime state).
        """
        return self._context

    def get_memory(self):
        """
        Return the temporary memory store for this session.
        """
        return self._memory

    def get_device_id(self):
        """
        Return the device ID from the profile, or fallback.
        """
        return self._profile.get("device_id") or "unknown-device"

# 🧠 Singleton instance used throughout app
session = SessionManager()
