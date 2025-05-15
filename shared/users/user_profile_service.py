"""
user_profile_service.py 👤

Handles mock user profile loading for now.
Future versions could load from DB, SSO, or OAuth2.
"""

def load_user_profile(username: str):
    """
    Simulates profile loading given a username.
    Returns a mock profile dict with email + device_id.
    """
    return {
        "name": username,
        "device_id": "dev-013-Jakebox",
        "email": f"{username.lower()}@hivemind.local"
    }
