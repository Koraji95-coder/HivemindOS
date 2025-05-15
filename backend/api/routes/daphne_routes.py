"""
daphne_routes.py 🤖
--------------------
FastAPI router exposing endpoints for the DaphneAgent.

Routes:
    - /api/daphne/ask: Accepts user input and returns Daphne's response.
"""

from fastapi import APIRouter
from pydantic import BaseModel
from shared.agents.daphne_agent import DaphneAgent

router = APIRouter(prefix="/api/daphne", tags=["Daphne"])

class PromptInput(BaseModel):
    prompt: str

agent = DaphneAgent()

@router.post("/ask")
def ask_daphne(input: PromptInput):
    """
    🔮 Ask Daphne — the assistant persona.

    Args:
        input: PromptInput object with the user's prompt

    Returns:
        dict: Response from Daphne
    """
    response = agent.ask(input.prompt)
    return {"agent": "Daphne", "response": response}
