import random

from main.quotes import quotes


def get_quote() -> dict:
    """Get a random quote"""

    return random.choice(quotes)
