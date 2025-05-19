"""
cortexa_routes.py 🧬
-------------------------
FastAPI router exposing endpoints for the CortexaAgent.

Routes:
    - /api/cortexa/ask: General NLP and prediction endpoint.
"""

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from shared.agents.cortexa_agent import CortexaAgent
from shared.logging.logger import get_logger

# Set up logger for this module
logger = get_logger("cortexa")  # or "bart", "cortexa", etc

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
    logger.info(f"Received Cortexa prompt: {input.prompt}")
    try:
        response = agent.ask(input.prompt)
        logger.info("CortexaAgent responded successfully")
        return {"agent": "Cortexa", "response": response}
    except Exception as e:
        logger.error(f"Cortexa error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Cortexa agent failed.")