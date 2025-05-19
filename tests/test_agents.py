import sys
from pathlib import Path

# 👇 Add project root to PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent))

from shared.agents.bart_agent import BartAgent
from shared.agents.daphne_agent import DaphneAgent
from shared.agents.cortexa_agent import CortexaAgent
from shared.system.atlas_core import Atlas

# 🛡️ System guard on
atlas = Atlas()
atlas.set_mode("maintenance")  # Lock system

# Agents under test
bart = BartAgent()
daphne = DaphneAgent()
cortexa = CortexaAgent()

print("🔒 Safe Mode Test:")
print(bart.ask("How’s the stock market today?"))
print(daphne.ask("Hey, just checking in."))
print(cortexa.ask("Predict market direction based on volume."))

# 🧠 System guard off
atlas.set_mode("development")  # Unlock

print("\n🎭 Mood-Aware Test:")
print(bart.ask("Everything sucks, I’m frustrated."))   # → Mood: frustrated
print(daphne.ask("I feel so tired and alone."))        # → Mood: sad
print(cortexa.ask("Let's go! Show me the prediction now."))  # → Mood: excited
