"""
BartAgent 📊

Analytical agent responsible for financial insight, news breakdowns,
and ticker-specific summaries.
"""

from shared.agents.agent_base import AgentBase
from shared.ai.gpt_client import GPTClient
from shared.state.session_manager import session
from shared.logging.logger import log

# ✅ Mood intelligence modules
from shared.personas.daphne.mood_engine import detect_mood, mood_wrapped_prompt
from shared.state.mood_state_tracker import set_user_mood, get_user_mood

# Atlas System Control
from shared.system.atlas_core import Atlas


class BartAgent(AgentBase):
    def __init__(self):
        super().__init__(name="Bart")
        self.gpt = GPTClient(agent="Bart")
        self.username = session.get_user_name()
        self.role = session.get_user_role()
        self.device_id = session.get_device_id()
        self.atlas = Atlas()
        log(f"{self.name} initialized for {self.username} ({self.role}) on {self.device_id}")

    def ask(self, prompt: str) -> str:
        """
        Processes financial or headline summary requests with mood-based tone.

        Steps:
        1. 🔐 Atlas Check: Enforce system safeguard.
        2. 🎭 Detect user's mood from text.
        3. 💾 Store that mood for session recall.
        4. 🧠 Wrap the GPT prompt accordingly.
        5. 🤖 Query GPTClient for structured financial insight.
        """
        if "last plugin" in prompt.lower() or "last result" in prompt.lower():
            last = session.get_memory().get("last_plugin_used")
            if last:
                return (
                    f"📊 Last plugin used: {last.get('plugin')}\n"
                    f"📥 Input: {last.get('input')}\n"
                    f"📥Output: {last.get('output')}\n"
                )
            return "📉 No plugin result found in memory."
        
        if not self.atlas.is_safe():  # 🔐 Atlas Control System
            return f"{self.name}: ⚠️ System is in safe mode. Operation blocked."
        try:
            mood = detect_mood(prompt)  # 🎭 Identify emotional state
            set_user_mood(self.username, mood)  # 💾 Save user mood
            wrapped_prompt = mood_wrapped_prompt(prompt, mood)  # 🧠 Adjust prompt tone
            return self.gpt.ask(wrapped_prompt)  # 🤖 Run GPT call
        except Exception as e:
            log(f"{self.name} fallback triggered for {self.username}: {e}")
            return self.respond(prompt)

        

    def respond(self, input_text: str) -> str:
        """
        Handles fallback summaries with tone adjusted to current mood.

        Args:
            input_text (str): Financial data or inquiry

        Returns:
            str: Response text
        """
        mood = get_user_mood(self.username)
        if "summary" in input_text.lower():
            return f"📊 Today’s markets saw mixed movement. Tech tickers showed strength. (Mood: {mood})"
        elif "ticker" in input_text.lower():
            return f"🧾 Ticker analysis: AAPL is trending upward on strong earnings. (Mood: {mood})"
        else:
            return f"🤷‍♂️ Bart doesn’t have a breakdown for '{input_text}'... yet. (Mood: {mood})"
