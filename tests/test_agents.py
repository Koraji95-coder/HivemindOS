import sys
from pathlib import Path

# 👇 Add project root to PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent))

from shared.agents import bart, cortexa, daphne

print("\n--- Daphne Test ---")
print(daphne.ask("hello"))
print(daphne.ask("what's the system status"))

print("\n--- Bart Test ---")
print(bart.ask("summary"))
print(bart.ask("ticker AAPL"))

print("\n--- Cortexa Test ---")
print(cortexa.ask("predict"))
print(cortexa.ask("vector check"))
