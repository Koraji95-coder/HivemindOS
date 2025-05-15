"""
cortexa_routes.py 🧬
-------------------------
FastAPI router exposing endpoints for the CortexaAgent.

Routes:
    - /api/cortexa/ask: General NLP and prediction endpoint.
"""

from fastapi import APIRouter
from pydantic import BaseModel
from shared.agents.cortexa_agent import CortexaAgent

router = APIRouter(prefix="/api/cortexa", tags=["Cortexa"])

class PromptInput(BaseModel):
    prompt: str

agent = CortexaAgent()

@router.post("/ask")
def ask_cortexa(input: PromptInput):
    """
    🧬 Ask Cortexa — ML logic and inference engine.

    Args:
        input: PromptInput with a statement or query

    Returns:
        dict: Cortexa's analytical output
    """
    response = agent.ask(input.prompt)
    return {"agent": "Cortexa", "response": response}
