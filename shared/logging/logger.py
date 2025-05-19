"""
logger.py 📓

Central logging utility for HivemindOS.
- Adds user and device context automatically via SessionManager.
- Supports per-agent/file rotating logs with contextual detail.
"""

import logging
from logging.handlers import TimedRotatingFileHandler
import os
from shared.state.session_manager import session

class ContextFormatter(logging.Formatter):
    """
    Formatter that adds user and device info from SessionManager to log records.
    """
    def format(self, record):
        # Add session context for every log record
        record.user = session.get_user_name()
        record.device = session.get_device_id()
        return super().format(record)

def get_logger(name: str) -> logging.Logger:
    """
    Returns a logger instance writing to its own rotating log file.
    Each logger is named by the module/agent (e.g., "daphne", "bart").
    
    Args:
        name (str): Logical name for log grouping (e.g. "daphne")
    Returns:
        logging.Logger: Pre-configured logger for use in your module/route file.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    if not logger.hasHandlers():
        os.makedirs("logs", exist_ok=True)
        # Rotates at midnight, keeps last 7 days
        handler = TimedRotatingFileHandler(
            f"logs/{name}.log", when="midnight", backupCount=7
        )
        fmt = '[%(asctime)s] [%(levelname)s] (%(user)s@%(device)s) %(message)s'
        formatter = ContextFormatter(fmt)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        # --- Console logging: ---
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
    return logger