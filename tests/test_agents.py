import sys
from pathlib import Path

# 👇 Add project root to PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent))

from shared.agents.daphne_agent import DaphneAgent
from shared.agents.bart_agent import BartAgent
from shared.agents.cortexa_agent import CortexaAgent
from shared.io.output_handler import ui_output

# --- Daphne ---
print("\n--- Daphne Test ---")
agent = DaphneAgent()
resp1 = agent.ask("hello")
ui_output(resp1, role="daphne", color="yellow")

# --- Bart ---
print("\n--- Bart Test ---")
bart = BartAgent()
resp2 = bart.ask("summary")
ui_output(resp2, role="bart", color="blue")

# --- Cortexa ---
print("\n--- Cortexa Test ---")
cortexa = CortexaAgent()
resp3 = cortexa.ask("predict")
ui_output(resp3, role="cortexa", color="green")
