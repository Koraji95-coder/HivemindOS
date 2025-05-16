"""
cortexa_router.py 🧬
────────────────────────────────────────
Handles POST requests to Cortexa agent.

Route: /api/cortexa
Accepts: { "prompt": str }
Returns: { "response": str }
"""

from fastapi import APIRouter
from backend.models.prompt_model import PromptRequest
from shared.agents.cortexa_agent import CortexaAgent

router = APIRouter()
agent = CortexaAgent()

@router.post("")
async def ask_cortexa(request: PromptRequest):
    return { "response": agent.ask(request.prompt) }
