"""
plugin_model.py 📦
────────────────────────────────────────
Schema for POST /api/plugin/run
"""

from pydantic import BaseModel

class PluginRequest(BaseModel):
    plugin: str
    input: str
