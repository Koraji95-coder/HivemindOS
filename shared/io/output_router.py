"""
output_router.py 🧪
--------------------
Unified output interface for CLI and future GUI integration.

All agent/system output should use `ui_output()` instead of `print()`.
This allows formatting, routing, and later redirecting to UI/console/web.

Usage:
    ui_output("hello", role="daphne")
"""

import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

# 🎨 Define colors for each agent/source role
AGENT_COLORS = {
    "daphne": Fore.YELLOW,
    "bart": Fore.BLUE,
    "cortexa": Fore.MAGENTA,
    "system": Fore.CYAN,
    "default": Fore.WHITE,
}

def ui_output(text, role="system", color=None):
    """
    ui_output() 📤
    --------------------------
    Styled output function for all CLI printing.

    Args:
        text (str): The message to output.
        role (str): Agent role (e.g., 'daphne', 'bart', 'cortexa').
        color (str): Optional override using colorama.Fore constants.
    """
    color_code = color or AGENT_COLORS.get(role.lower(), Fore.WHITE)
    print(f"{color_code}{text}{Style.RESET_ALL}")
