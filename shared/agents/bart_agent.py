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


class BartAgent(AgentBase):
    def __init__(self):
        """
        Initializes Bart with an analytical tone and name.
        """
        super().__init__(name="Bart")
        self.gpt = GPTClient(agent="Bart")

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
