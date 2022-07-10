#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses

from icecream import ic

from menu_zerobeef.example import (multi_selection, normal_menu,
                                   single_selection)

menus = {1: normal_menu, 2: single_selection, 3: multi_selection}

if __name__ == "__main__":
    print("1. Menu with submenus")
    print("2. Single selection menu")
    print("3. Multiple choice Menu")
    a = input("Which example do you want to run?")
    b = curses.wrapper(menus[int(a)])
    ic(b)
