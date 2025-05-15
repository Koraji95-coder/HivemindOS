"""
Agent Registry 🎛️
────────────────────────────
Globally accessible singleton registry for all AI agents.
Used to fetch Daphne, Bart, Cortexa at runtime.
"""

from shared.agents.bart_agent import BartAgent
from shared.agents.cortexa_agent import CortexaAgent
from shared.agents.daphne_agent import DaphneAgent

# 🧠 Preloaded agents
daphne = DaphneAgent()
bart = BartAgent()
cortexa = CortexaAgent()

__all__ = ["daphne", "bart", "cortexa"]
