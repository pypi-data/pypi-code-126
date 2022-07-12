# read version from installed package

from importlib.metadata import version
from .word_text_counter import count_words

__version__ = version("word_text_counter")
__all__ = ["count_words"]