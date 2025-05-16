"""
plugin_router.py ⚙️
────────────────────────────────────────
POST /api/plugin/run → execute plugin by name
"""

from fastapi import APIRouter
from backend.models.plugin_model import PluginRequest
from shared.workflows.plugin_executor import execute_plugin

router = APIRouter()

@router.post("/run")
async def run_plugin(request: PluginRequest):
    result = execute_plugin(request.plugin, request.input)
    return result
