"""
user_identity.py 🔐

Maps usernames to roles.
Helps control access to sensitive agent actions.
"""

class UserIdentity:
    def __init__(self):
        # This is your user-to-role map
        self.roles = {
            "dustin": "admin",
            "atlas": "system",
            "guest": "guest"
        }

    def get_role(self, username):
        """
        Return the role associated with the given username.
        Defaults to 'guest' if not found.
        """
        return self.roles.get(username.lower(), "guest")
