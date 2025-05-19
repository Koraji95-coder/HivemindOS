"""
calculator.py ➗
────────────────────────────────────────
Evaluates basic math expressions safely.
Used by plugin executor or Cortexa.
"""

def run(input_text: str) -> str:
    try:
        result = eval(input_text, {"__builtins__": {}})
        return str(result)
    except Exception as e:
        return f"❌ Calc error: {str(e)}"
