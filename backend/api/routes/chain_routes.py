"""
chain_router.py 🔁
────────────────────────────────────────
POST /api/chain → Execute agent sequence chain
"""

from fastapi import APIRouter
from backend.models.chain_model import AChainRequest
from backend.models.agent_chain_model import AgentChainRequest
from shared.workflows.chain_executor import execute_chain
from shared.workflows.agent_chain_executor import execute_agent_chain

router = APIRouter(prefix="/api/chain", tags=["Chain"])

@router.post("")
async def run_chain(request: AChainRequest):
    """
    Executes a plugin/agent chain.
    Expects a POST body like: { "chain": [...] }
    """
    results = execute_chain(request.chain)
    return { "results": results }

@router.post("/run")
async def run_agent_chain(request: AgentChainRequest):
    """
    Executes a named agent sequence using shared memory.
    """
    return {
        "chain": request.chain,
        "steps": execute_agent_chain(request.chain, request.input)
    }