"""
atlas_core.py 🛡️

Atlas is the central system intelligence of HivemindOS.
All agents operate beneath its awareness. Atlas tracks runtime mode,
global state, and can override agents when needed.

Serves as the final fallback brain and strategic monitor.
"""
from shared.state import session_manager




class Atlas:
    def __init__(self):
        # Internal identity metadata
        self.name = "Atlas"
        self.version = "v0.0.9"
        self.system_mode = "development"  # could be production/test/maintenance
        self.safe_guard = True  # critical runtime control flag
        session = session_manager.session
        session.get_user_name()
        session.get_context()


    def identify(self):
        """
        Return core metadata about the Atlas system itself.
        """
        return {
            "name": self.name,
            "version": self.version,
            "mode": self.system_mode
        }

    def elevate(self):
        """
        Trigger system-level override mode.
        Used if agents are failing or unsafe state is detected.
        """
        self.safe_guard = False
        return f"⚠️ Atlas override activated. Agents may be suspended."

    def is_safe(self):
        """
        Return the current safeguard status.
        """
        return self.safe_guard

    def set_mode(self, mode):
        """
        Dynamically change system mode (e.g., to 'maintenance').
        """
        self.system_mode = mode

    def summarize_state(self, session):
        """
        Return a full runtime snapshot tied to the active session.
        """
        return {
            "user": session.get_user_name(),
            "role": session.get_user_role(),
            "device": session.get_device_id(),
            "flags": session.get_context(),
            "mode": self.system_mode,
            "safe": self.safe_guard
        }
