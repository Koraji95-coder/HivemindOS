"""
bart_routes.py 📊
---------------------
FastAPI router exposing endpoints for the BartAgent.

Routes:
    - /api/bart/ask: Accepts natural language input for market insights.
"""

from fastapi import APIRouter
from pydantic import BaseModel
from shared.agents.bart_agent import BartAgent
from shared.logging.logger import get_logger

# Set up logger for this module
logger = get_logger("bart")  # or "bart", "cortexa", etc


router = APIRouter(prefix="/api/bart", tags=["Bart"])

class PromptInput(BaseModel):
    prompt: str

agent = BartAgent()

@router.post("/ask")
def ask_bart(input: PromptInput):
    """
    📊 Ask Bart — financial quote analyzer.

    Args:
        input: PromptInput with user text

    Returns:
        dict: Bart's structured insight
    """
    logger.info(f"Request received for /ask: {input.prompt}")
    try:
        response = agent.ask(input.prompt)
        logger.info("BartAgent responded successfully")
        return {"agent": "Bart", "response": response}
    except Exception as e:
        logger.error(f"BartAgent error: {str(e)}")
        return {"agent": "Bart", "error": str(e)}, 500