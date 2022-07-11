# -*- coding: utf-8 -*-
from halmoney import pcell
import pyautogui

excel = pcell.pcell()

#위치찾기 : 현재 마우스의 위치를 돌려준다


position = pyautogui.position()
output_text = "x좌표 : " + str(position.x) + ", y좌표 : " + str(position.y)

excel.show_messagebox_value(output_text)