"""
easyautomation.

A keyboard and mouse automation functions package for my own convenience.
"""

__version__ = "0.1.0"
__author__ = "David Pareja"
__credits__ = "pyautogui, OpenCV"

from .keyboard import Keyboard
from .mouse import Mouse

keyboard = Keyboard()
mouse = Mouse()

__all__ = [
    "keyboard",
    "mouse",
]
