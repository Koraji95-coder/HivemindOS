"""
CortexaAgent 🧬
────────────────────────────
Handles structured prediction tasks, classification, and logic-driven workflows.
Specializes in:
- Document ingestion (e.g. PDF analysis)
- Sector prediction
- Confidence scoring
"""

from shared.agents.agent_base import AgentBase
from shared.ai.gpt_client import GPTClient
from shared.state.session import session


class CortexaAgent(AgentBase):
    def __init__(self):
        """
        Initializes the agent with session-level context:

        - Loads the current user's name, role, and device ID
        - Allows responses to be personalized per session
        - Enables future logic for role-based filtering, scoped memory, and user-based agent behavior

        Session values pulled from `SessionManager`:
        - self.username → User display name (fallback: guest)
        - self.role     → Role label (Owner / Admin / Guest)
        - self.device_id→ Source device ID or fallback token
        """
        super().__init__(name="Cortexa")
        self.gpt = GPTClient(agent="Cortexa")
        self.username = session.get_user_name()
        self.role = session.get_user_role()
        self.device_id = session.get_device_id()

    def ask(self, prompt: str) -> str:
        """
        Processes structured prompts for prediction or classification.

        Args:
            prompt (str): A model input or classification query

        Returns:
            str: Cortexa's response (currently stubbed)
        """
        try:
            return self.gpt.ask(prompt)
        except:
            return self.respond(prompt)

    def respond(self, input_text: str) -> str:
        """
        Handles model-related reasoning or analysis tasks.

        Args:
            input_text (str): Structured model task input

        Returns:
            str: Prediction explanation or result
        """
        # 🧬 Placeholder logic for future ML classification
        if "predict" in input_text.lower():
            return "📈 Cortexa predicts a bullish signal with 82% confidence."
        elif "vector" in input_text.lower():
            return "🔢 Input vector appears valid. Proceeding with classification..."
        else:
            return f"🧬 Cortexa cannot process '{input_text}' — model input unclear."
