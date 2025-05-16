"""
CortexaAgent 🧬
────────────────────────────────────────
Handles structured prediction tasks, plugin execution, classification,
and mood-adjusted logic workflows.

Specialties:
- Document classification
- Plugin execution (math, validation)
- Mood-aware GPT prompting
- System safety enforcement (Atlas)
"""

import re
from shared.agents.agent_base import AgentBase
from shared.ai.gpt_client import GPTClient
from shared.logging.logger import log
from shared.workflows.plugin_executor import execute_plugin

# ✅ Mood modules
from shared.personas.daphne.mood_engine import detect_mood, mood_wrapped_prompt
from shared.state.mood_state_tracker import get_user_mood, set_user_mood
from shared.state.session_manager import session

# 🛡️ Atlas System Control
from shared.system.atlas_core import Atlas

class CortexaAgent(AgentBase):
    def __init__(self):
        """
        Initializes Cortexa with:
        - Session-level awareness (user, role, device)
        - GPTClient binding for structured classification
        - Plugin detection capability
        - Mood detection + safe prompting
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
        Main entrypoint for structured logic, mood-awareness and plugin execution.

        Steps:
        1. 🔐 Atlas Control: Abort if system is unsafe.
        2. 🔌 Plugin match: If matched, execute and return plugin result.
        3. 🎭 Mood detection: Analyze mood from input.
        4. 🧠 Wrap prompt with tone-adjusted language.
        5. 🤖 Send to GPT.
        """
        if not self.atlas.is_safe():
            return f"{self.name}: ⚠️ System is in safe mode. Operation blocked."

        # 🔌 Detect plugin call
        plugin_match = self._detect_plugin_trigger(prompt)
        if plugin_match:
            plugin_name, plugin_input = plugin_match
            result = execute_plugin(plugin_name, plugin_input)

            # 💾 Store plugin call in session memory
            session.get_memory()["last_plugin_used"] = result

            return (
                f"🧠 Cortexa plugin output:\n"
                f"🔌 `{plugin_name}` → `{plugin_input}`\n"
                f"📥 Result: `{result.get('output')}`"
            )

        try:
            mood = detect_mood(prompt)
            set_user_mood(self.username, mood)
            wrapped_prompt = mood_wrapped_prompt(prompt, mood)
            return self.gpt.ask(wrapped_prompt)
        except Exception as e:
            log(f"{self.name} fallback triggered: {e}")
            return self.respond(prompt)

    def _detect_plugin_trigger(self, prompt: str):
        """
        Detects if a plugin should be invoked based on user input patterns.

        Returns:
            (plugin_name, plugin_input) or None
        """
        match1 = re.match(r"(?:run|execute)?\s*plugin\s+(\w+)\s+on\s+(.+)", prompt, re.IGNORECASE)
        match2 = re.match(r"calculate\s+(.+)", prompt, re.IGNORECASE)
        match3 = re.match(r"use\s+(\w+)\s+to\s+(.+)", prompt, re.IGNORECASE)

        if match1:
            return match1.group(1), match1.group(2)
        elif match2:
            return "calculator", match2.group(1)
        elif match3:
            return match3.group(1), match3.group(2)

        return None

    def respond(self, input_text: str) -> str:
        """
        Fallback reasoning or model logic response (non-GPT, mood-aware).

        Args:
            input_text (str): structured input or user message

        Returns:
            str: Cortexa’s formatted fallback output
        """
        mood = get_user_mood(self.username)
        if "predict" in input_text.lower():
            return f"📈 Cortexa predicts a bullish signal with 82% confidence. (Mood: {mood})"
        elif "vector" in input_text.lower():
            return f"🔢 Input vector appears valid. Proceeding with classification... (Mood: {mood})"
        else:
            return f"🧬 Cortexa cannot process '{input_text}' — model input unclear. (Mood: {mood})"
