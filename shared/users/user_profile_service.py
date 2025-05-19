# shared/users/user_profile_service.py

import os
import platform

# Username aliases: OS username → profile-username
USERNAME_ALIASES = {
    "Dusti": "Dustin",
    # Add more as needed
}

def get_device_id() -> str:
    """
    Returns a device identifier string.
    Uses platform node/hostname.
    """
    return platform.node()

def get_canonical_username(username: str) -> str:
    """
    Maps a raw username to its canonical version using aliases.
    """
    return USERNAME_ALIASES.get(username, username)

def load_user_profile(username: str) -> dict:
    """
    Loads or synthesizes a user profile for the given username.
    Always applies aliasing and device id.
    """
    canonical_name = get_canonical_username(username)
    return {
        "name": canonical_name,
        "device_id": get_device_id(),
        "email": f"{canonical_name.lower()}@hivemind.local"
    }

def load_user_profile_from_system() -> dict:
    """
    Uses the current OS username (via os.getlogin()) to load a canonical user profile.
    """
    os_username = os.getlogin()
    return load_user_profile(os_username)