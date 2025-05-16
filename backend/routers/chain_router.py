"""
chain_router.py 🔁
────────────────────────────────────────
POST /api/chain → Execute agent sequence chain
"""

from fastapi import APIRouter
from backend.models.chain_model import ChainRequest
from shared.workflows.chain_executor import execute_chain


router = APIRouter()

@router.post("")
async def run_chain(request: ChainRequest):
    results = execute_chain(request.chain)
    return { "results": results }
