# read version from installed package

from importlib.metadata import version
from word_text_counter.word_text_counter import count_words
from word_text_counter.datasets import get_flatland_path, get_time_machine_path

__version__ = version(__name__)
__all__ = ["count_words", "get_flatland_path", "get_time_machine_path"]