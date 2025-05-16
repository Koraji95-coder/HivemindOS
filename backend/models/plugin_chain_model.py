"""
plugin_chain_model.py 📦
────────────────────────────────────────
Defines schema for chained plugin requests.
"""

from pydantic import BaseModel
from typing import List

class PluginStep(BaseModel):
    plugin: str
    input: str

class PluginChainRequest(BaseModel):
    chain: List[PluginStep]
