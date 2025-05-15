from fastapi import APIRouter
from pydantic import BaseModel
from shared.agents.bart_agent import BartAgent

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
    response = agent.ask(input.prompt)
    return {"agent": "Bart", "response": response}
