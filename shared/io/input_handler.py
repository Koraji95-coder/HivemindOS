"""
input_handler.py 👤
---------------------
Unified input() function for user prompts, future GUI overrides.
"""

def get_input(prompt="> "):
    """
    get_input() — Global input prompt handler.

    Args:
        prompt (str): The prompt message.

    Returns:
        str: User-entered text.
    """
    try:
        return input(prompt)
    except EOFError:
        return ""
    except KeyboardInterrupt:
        print("\n[Interrupted]")
        return ""
