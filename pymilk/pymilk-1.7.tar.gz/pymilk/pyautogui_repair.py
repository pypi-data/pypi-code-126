'''
该模块是为了解决 "pyautogui库导致Tk和win32gui采集屏幕分辨率不准确" 的问题
'''
import win32gui as _
import win32con as _
import win32api as _
from tkinter import Tk as _Tk

_x = _Tk()

screenWidth = _x.winfo_screenwidth()
screenHeight = _x.winfo_screenheight()

import pyautogui  # from pyautogui_repair import pyautogui
