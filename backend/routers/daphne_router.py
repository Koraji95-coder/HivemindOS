"""
daphne_router.py 💬
────────────────────────────────────────
Handles POST requests to Daphne agent.

Route: /api/daphne
Accepts: { "prompt": str }
Returns: { "response": str }
"""

from fastapi import APIRouter
from backend.models.prompt_model import PromptRequest
from shared.agents.daphne_agent import DaphneAgent

router = APIRouter()
agent = DaphneAgent()

@router.post("")
async def ask_daphne(request: PromptRequest):
    # 🌐 Route handler that returns Daphne's response to prompt
    return { "response": agent.ask(request.prompt) }
