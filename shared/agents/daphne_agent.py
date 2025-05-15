"""
DaphneAgent 🧠
────────────────────────────
Primary UI-facing persona agent for HivemindOS.
Acts as the emotional voice and conversational bridge for the system.
Relays thoughts, moods, or fallback responses in natural language.
"""

from shared.agents.agent_base import AgentBase
from shared.ai.gpt_client import GPTClient
from shared.state.session import session


class DaphneAgent(AgentBase):
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
        super().__init__(name="Daphne")
        self.gpt = GPTClient(agent="Daphne")
        self.username = session.get_user_name()
        self.role = session.get_user_role()
        self.device_id = session.get_device_id()

    def ask(self, prompt: str) -> str:
        """
        Sends input to Daphne and returns her response.
        This is a simple passthrough to the `respond()` logic.

        Args:
            prompt (str): The user query or thought

        Returns:
            str: Daphne's output
        """
        try:
                return self.gpt.ask(prompt)
        except:
            return self.respond(prompt)

    def respond(self, input_text: str) -> str:
        """
        Responds with a conversational message from Daphne.
        Can be enhanced to use GPTClient or a local fallback model.

        Args:
            input_text (str): Input from user or system

        Returns:
            str: Friendly persona-styled response
        """
        # 🚧 Placeholder logic: dynamic NLP integration will come later
        if "hello" in input_text.lower():
            return ("👋 Hello there! I'm Daphne — your digital mindmate."
            )
        elif "status" in input_text.lower():
            return ("🧠 System is running fine. Ready when you are."
            )
        else:
            return f"🤔 Hmm... I’m not sure how to respond to '{input_text}' just yet."
