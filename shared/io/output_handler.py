"""
output_handler.py 📤
---------------------
Unified output function for all system-facing messages.

Supports:
- CLI output (default)
- Future override for GUI/terminal routing
- Role-based prefixes, emojis, and color formatting
"""

from colorama import Fore, Style, init

# ✅ Initialize colorama on Windows
init(autoreset=True)

# 🧠 Default role emoji map
ROLE_EMOJIS = {
    "system": "🧠",
    "daphne": "💬",
    "bart": "📊",
    "cortexa": "🧬",
    "user": "👤",
    "info": "ℹ️",
    "warn": "⚠️",
    "error": "❌",
}


def ui_output(message: str, role: str = "system", color: str = "cyan"):
    """
    ui_output() — Global output handler for all agent/system messages.

    Args:
        message (str): The content to print.
        role (str): Optional role identifier to prefix (e.g. "daphne", "user").
        color (str): Optional color name (e.g. "cyan", "green", "yellow").
    """
    emoji = ROLE_EMOJIS.get(role.lower(), "")
    color_map = {
        "cyan": Fore.CYAN,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "red": Fore.RED,
        "magenta": Fore.MAGENTA,
        "blue": Fore.BLUE,
        "white": Fore.WHITE,
    }
    color_prefix = color_map.get(color.lower(), Fore.CYAN)
    formatted = f"{color_prefix}{emoji} {message}"
    print(formatted)
