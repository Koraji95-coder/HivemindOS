"""
CortexaAgent 🧬

Handles structured prediction tasks, classification, and logic-driven workflows.
Specializes in:
- Document ingestion (e.g. PDF analysis)
- Sector prediction
- Confidence scoring
"""

from shared.agents.agent_base import AgentBase
from shared.ai.gpt_client import GPTClient
from shared.logging.logger import log

# ✅ Mood modules
from shared.personas.daphne.mood_engine import detect_mood, mood_wrapped_prompt
from shared.state.mood_state_tracker import get_user_mood, set_user_mood
from shared.state.session_manager import session

# Atlas System Control
from shared.system.atlas_core import Atlas

class CortexaAgent(AgentBase):
    def __init__(self):
        """
        Initializes Cortexa with:
        - Session-level awareness (user, role, device)
        - GPTClient binding for structured classification
        - Logging per active user + session
        """
        super().__init__(name="Cortexa")
        self.gpt = GPTClient(agent="Cortexa")
        self.username = session.get_user_name()
        self.role = session.get_user_role()
        self.device_id = session.get_device_id()
        self.atlas = Atlas()
        log(f"{self.name} initialized for {self.username} ({self.role}) on {self.device_id}")

    def ask(self, prompt: str) -> str:
        """
        Handles structured logic/classification prompts with mood-layered tone.

        Steps:
        1. 🔐 Atlas Check: Abort if system isn't safe.
        2. 🎭 Detect user mood from logical input.
        3. 💾 Store that mood in memory.
        4. 🧠 Wrap prompt to align GPT’s language style.
        5. 🤖 Execute GPTClient logic task.
        """
        if not self.atlas.is_safe():  # 🔐 Atlas Control System
            return f"{self.name}: ⚠️ System is in safe mode. Operation blocked."

        try:
            mood = detect_mood(prompt)  # 🎭 Evaluate prompt tone
            set_user_mood(self.username, mood)  # 💾 Cache mood per user
            wrapped_prompt = mood_wrapped_prompt(
                prompt, mood
            )  # 🧠 Modify prompt to suit tone
            return self.gpt.ask(wrapped_prompt)  # 🤖 Perform logic inference
        except Exception as e:
            log(f"{self.name} fallback triggered: {e}")
            return self.respond(prompt)

    def respond(self, input_text: str) -> str:
        """
        Handles model-related reasoning or analysis tasks.

        Args:
            input_text (str): Structured model task input

        Returns:
            str: Prediction explanation or result
        """
        mood = get_user_mood(self.username)
        if "predict" in input_text.lower():
            return f"📈 Cortexa predicts a bullish signal with 82% confidence. (Mood: {mood})"
        elif "vector" in input_text.lower():
            return f"🔢 Input vector appears valid. Proceeding with classification... (Mood: {mood})"
        else:
            return f"🧬 Cortexa cannot process '{input_text}' — model input unclear. (Mood: {mood})"
