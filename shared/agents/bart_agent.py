"""
BartAgent 📊
────────────────────────────
Analytical agent responsible for financial insight, news breakdowns,
and ticker-specific summaries.

Goals:
- Digest market data
- Summarize news headlines
- Provide structured insight or ratings
"""

from shared.agents.agent_base import AgentBase
from shared.ai.gpt_client import GPTClient
from shared.state.session import session


class BartAgent(AgentBase):
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
        super().__init__(name="Bart")
        self.gpt = GPTClient(agent="Bart")
        self.username = session.get_user_name()
        self.role = session.get_user_role()
        self.device_id = session.get_device_id()

    def ask(self, prompt: str) -> str:
        """
        Processes input as a summary request.

        Args:
            prompt (str): User or system input

        Returns:
            str: Structured response or quote summary
        """
        try:
            return self.gpt.ask(prompt)
        except:
            return self.respond(prompt)

    def respond(self, input_text: str) -> str:
        """
        Handles financial or summary prompts.
        Can be upgraded to extract tickers, use GPTClient, etc.

        Args:
            input_text (str): Financial data or inquiry

        Returns:
            str: Response text
        """
        # 🧠 Placeholder logic for mock analysis
        if "summary" in input_text.lower():
            return (
                "📊 Today’s markets saw mixed movement. Tech tickers showed strength."
            )
        elif "ticker" in input_text.lower():
            return ("🧾 Ticker analysis: AAPL is trending upward on strong earnings."
            )
        else:
            return f"🤷‍♂️ Bart doesn’t have a breakdown for '{input_text}'... yet."
