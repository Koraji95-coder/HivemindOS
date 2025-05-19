"""
daphne_routes.py 🤖
--------------------
FastAPI router exposing endpoints for the DaphneAgent.

Routes:
    - /api/daphne/ask: Accepts user input and returns Daphne's response.
"""

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from shared.agents.daphne_agent import DaphneAgent
from shared.logging.logger import get_logger

# Set up logger for this module
logger = get_logger("daphne")  # or "bart", "cortexa", etc

router = APIRouter(prefix="/api/daphne", tags=["Daphne"])

class PromptInput(BaseModel):
    """
    Pydantic model for input to Daphne endpoint.
    """
    prompt: str

# NOTE: If DaphneAgent is stateless, keep global singleton.
# If not, move inside the request function or use Depends().
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
    logger.info(f"Received Daphne prompt: {input.prompt}")
    try:
        response = agent.ask(input.prompt)
        logger.info("DaphneAgent responded successfully.")
        return {"agent": "Daphne", "response": response}
    except Exception as e:
        logger.error(f"Daphne error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Daphne agent failed."
        )