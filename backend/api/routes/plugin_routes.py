"""
plugin_router.py ⚙️
────────────────────────────────────────
POST /api/plugin/run → execute plugin by name
"""

from fastapi import APIRouter
from backend.models.plugin_model import PluginRequest
from backend.models.plugin_chain_model import PluginChainRequest
from shared.workflows.plugin_chain_executor import execute_plugin_chain
from shared.workflows.plugin_executor import execute_plugin

router = APIRouter(prefix="/api/plugin", tags=["Plugin"])

@router.post("/run")
async def run_plugin(request: PluginRequest):
    result = execute_plugin(request.plugin, request.input)
    return result

@router.post("/chain")
async def run_plugin_chain(request: PluginChainRequest):
    results = execute_plugin_chain(request.chain)
    return results