import random
from pyautogui import press
from pyautogui import hotkey
from pyautogui import typewrite
from time import sleep


class Keyboard:
    def __init__(self):
        pass

    def newTab(self):
        hotkey("ctrl", "t")
        sleep(0.8)

    def ctrlEnter(self):
        hotkey("ctrl", "enter")
        sleep(0.8)

    def maximizeWindow(self):
        hotkey("alt", "space", "x")

    def snapLeft(self):
        hotkey("win", "left", "left", "left")

    def addressBar(self):
        hotkey("ctrl", "l")
        sleep(0.8)

    def selectAll(self):
        hotkey("ctrl", "a")

    def copy(self):
        hotkey("ctrl", "c")

    def paste(self):
        hotkey("ctrl", "v")

    def write(self, string):
        for x in string:
            press(x, interval=random.uniform(0.01, 0.21))

    def instaWrite(self, string):
        typewrite(string)

    def f12(self):
        press("f12")

    def enter(self):
        press("enter")

    def backspace(self):
        press("backspace")

    def escape(self):
        press("esc")

    def space(self):
        press("space")

    def win(self):
        press("win")
        sleep(0.8)

    def left(self):
        press("left")

    def right(self):
        press("right")

    def up(self):
        press("up")

    def down(self):
        press("down")
