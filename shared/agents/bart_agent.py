"""
BartAgent 📊

Analytical agent responsible for financial insight, news breakdowns,
and ticker-specific summaries.
"""

from shared.agents.agent_base import AgentBase
from shared.ai.gpt_client import GPTClient
from shared.state.session_manager import session
from shared.logging.logger import get_logger
logger = get_logger("bart_agent")

# ✅ Mood intelligence modules
from shared.ai.mood_engine import detect_mood, mood_wrapped_prompt
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
        logger.info(f"{self.name} initialized for {self.username} ({self.role}) on {self.device_id}")

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
        logger.info(f"[ASK] {self.name} received prompt from {self.username}: {prompt!r}")

        # System: Last plugin lookup short-circuit
        if "last plugin" in prompt.lower() or "last result" in prompt.lower():
            last = session.get_memory().get("last_plugin_used")
            if last:
                logger.info(f"[ASK] {self.name} fetched last plugin from memory for {self.username}")
                return (
                    f"📊 Last plugin used: {last.get('plugin')}\n"
                    f"📥 Input: {last.get('input')}\n"
                    f"📤 Output: {last.get('output')}\n"
                )
            logger.info(f"[ASK] {self.name}: No last plugin found for {self.username}")
            return "📉 No plugin result found in memory."

        # Atlas safety check
        if not self.atlas.is_safe():
            logger.warning(f"[ASK] {self.name} blocked because Atlas is in safe mode.")
            return f"{self.name}: ⚠️ System is in safe mode. Operation blocked."

        try:
            mood = detect_mood(prompt)
            set_user_mood(self.username, mood)
            wrapped_prompt = mood_wrapped_prompt(prompt, mood)
            logger.info(f"[ASK] {self.name} detected mood='{mood}' for {self.username}. Wrapped prompt for GPT call.")
            reply = self.gpt.ask(wrapped_prompt)
            logger.info(f"[ASK] {self.name} got GPT reply for {self.username}")
            return reply
        except Exception as e:
            logger.error(f"[ASK-ERR] {self.name} fallback for {self.username}: {e}")
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
        logger.info(f"[RESPOND] {self.name} mood='{mood}' input='{input_text}' for {self.username}")
        if "summary" in input_text.lower():
            return f"📊 Today’s markets saw mixed movement. Tech tickers showed strength. (Mood: {mood})"
        elif "ticker" in input_text.lower():
            return f"🧾 Ticker analysis: AAPL is trending upward on strong earnings. (Mood: {mood})"
        else:
            return f"🤷‍♂️ Bart doesn’t have a breakdown for '{input_text}'... yet. (Mood: {mood})"