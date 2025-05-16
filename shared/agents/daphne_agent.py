"""
DaphneAgent 🧠

Primary UI-facing persona agent for HivemindOS.
Acts as the emotional voice and conversational bridge for the system.
Relays thoughts, moods, or fallback responses in natural language.
"""

from shared.agents.agent_base import AgentBase
from shared.ai.gpt_client import GPTClient
from shared.logging.logger import log

# ✅ Added: mood intelligence modules
from shared.personas.daphne.mood_engine import detect_mood, mood_wrapped_prompt
from shared.state.mood_state_tracker import get_user_mood, set_user_mood
from shared.state.session_manager import session

# Atlas System Control
from shared.system.atlas_core import Atlas


class DaphneAgent(AgentBase):
    def __init__(self):
        """
        Initializes the agent with session-level context:

        - Loads the current user's name, role, and device ID
        - Enables personalized, mood-aware behavior
        """
        super().__init__(name="Daphne")
        self.gpt = GPTClient(agent="Daphne")
        self.username = session.get_user_name()
        self.role = session.get_user_role()
        self.device_id = session.get_device_id()
        self.atlas = Atlas()
        log(f"{self.name} initialized for {self.username} ({self.role}) on {self.device_id}")

    def ask(self, prompt: str) -> str:
        """
        Handles conversational queries for the emotional persona agent.

        Steps:
        1. 🔐 Atlas Control: Check if system is in safe mode before executing.
        2. 🎭 Detect mood using the prompt.
        3. 💾 Store mood in session memory via username key.
        4. 🧠 Wrap prompt to guide GPT tone.
        5. 🤖 Query GPTClient and return emotional response.
        """
        if not self.atlas.is_safe():  # 🔐 Atlas Control System
            return f"{self.name}: ⚠️ System is in safe mode. Operation blocked."

        try:
            mood = detect_mood(prompt)  # 🎭 Analyze emotional tone
            set_user_mood(self.username, mood)  # 💾 Save mood for this user
            wrapped = mood_wrapped_prompt(prompt, mood)  # 🧠 Adjust phrasing for tone
            return self.gpt.ask(wrapped)  # 🤖 Run GPT with mood-aware prompt
        except Exception as e:
            log(f"{self.name} fallback triggered for {self.username}: {e}")
            return self.respond(prompt)

    def respond(self, input_text: str) -> str:
        """
        Responds with a conversational message using current mood context.

        Args:
            input_text (str): Input from user or system

        Returns:
            str: Friendly persona-styled response
        """
        mood = get_user_mood(self.username)
        log(f"{self.name} using stored mood '{mood}' to respond to '{input_text}'")

        if "hello" in input_text.lower():
            return "👋 Hello there! I'm Daphne — your digital mindmate."
        elif "status" in input_text.lower():
            return "🧠 System is running fine. Ready when you are."
        elif mood == "sad":
            return "💙 I’m here if you need to talk. You’re not alone."
        elif mood == "frustrated":
            return "😓 I feel that. Let’s untangle this together."
        elif mood == "happy":
            return "😊 I love this energy. What’s next?"
        elif mood == "excited":
            return "🔥 Oh yeah! Let’s ride this wave!"
        else:
            return f"🤔 Hmm... I’m not sure how to respond to '{input_text}' just yet."
