"""
chain_model.py 📦
────────────────────────────────────────
Defines the chain step schema for prompt routing.
"""

from typing import List

from pydantic import BaseModel


class AChainStep(BaseModel):
    agent: str
    prompt: str

class AChainRequest(BaseModel):
    chain: List[AChainStep]
