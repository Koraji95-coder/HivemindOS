"""
bart_router.py 📊
────────────────────────────────────────
Handles POST requests to Bart agent.

Route: /api/bart
Accepts: { "prompt": str }
Returns: { "response": str }
"""

from fastapi import APIRouter
from backend.models.prompt_model import PromptRequest
from shared.agents.bart_agent import BartAgent

router = APIRouter()
agent = BartAgent()

@router.post("")
async def ask_bart(request: PromptRequest):
    return { "response": agent.ask(request.prompt) }
