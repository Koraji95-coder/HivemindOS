"""
logger.py 📓

Central logging utility for HivemindOS.
Adds user and device context automatically via SessionManager.
"""

import datetime
import os
from shared.state.session_manager import session

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def log(message, level="INFO"):
    """
    Writes a log entry with timestamp, level, and session context (user, device).
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user = session.get_user_name()
    device = session.get_device_id()
    log_entry = f"[{timestamp}] [{level}] ({user}@{device}) {message}\n"

    log_path = os.path.join(LOG_DIR, "hivemind.log")
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(log_entry)

    print(log_entry.strip())  # Optional: also print to console
