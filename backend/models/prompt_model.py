"""
prompt_model.py 🧾
────────────────────────────────────────
Defines request schema for agent prompt APIs.

- Validates incoming POST data using Pydantic
"""

from pydantic import BaseModel

class PromptRequest(BaseModel):
    prompt: str  # Required prompt string
