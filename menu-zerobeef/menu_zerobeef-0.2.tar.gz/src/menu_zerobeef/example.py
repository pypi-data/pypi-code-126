"""
TODO: Write a docstring
"""
import curses

from icecream import ic

from menu_zerobeef.data import (ItemMultiSelection, ItemSingleSelection,
                                MenuItem)
from menu_zerobeef.menu import ApplicationMenu


def multi_selection(stdscr):
    """
    This function creates and presents the user
    with an example menu where you can select
    multiple items. If the user selects "Cancel",
    nothing is returned. However, if the user
    selects "Done", then it returns whatever is
    selected, if nothing is selected then [] is
    returned. 
    """
    curses.start_color()
    curses.use_default_colors()
    items = [
        "system", "os", "windows", "linux", "mac", "apple", "pear", "dog",
        "Cancel", "Done"
    ]
    multi_select_items = [
        ItemMultiSelection(t, p) for p, t in enumerate(items)
    ]
    menu_title = "Multiple choice menu example. Which of these are an os or contains os?"
    menu = ApplicationMenu(stdscr, (multi_select_items, menu_title))
    return menu.show_menu()


def single_selection(stdscr):
    """
    This function creates and presents the user
    with an example menu where you can select
    one item out of a list of items. If the user
    selects "Cancel", then nothing will be returned.
    However, if the user selects anything else the
    title for that item will be returned and not
    the menu item instance.
    """
    curses.start_color()
    curses.use_default_colors()
    items = [
        "system", "os", "windows", "linux", "mac", "apple", "pear", "dog",
        "Cancel"
    ]
    single_select_items = [
        ItemSingleSelection(t, p) for p, t in enumerate(items)
    ]
    menu_title = "Single selection menu example. Which one is related to apple?"

    menu = ApplicationMenu(stdscr, (single_select_items, menu_title))
    return menu.show_menu()


def normal_menu(stdscr):
    """
    This function creates a menu and presents
    the user with a normal menu that has sub-
    menus. Whenever the user goes to a specific
    item that does not contain a submenu, the
    action for that item is executed. If the
    item contains a pointer to a submenu, that
    submenu will then be drawn on screen and 
    the main menu will wait in the background.
    """
    curses.start_color()
    curses.use_default_colors()
    sub_menu = [(print, "SubFirst"), (print, "SubSecond"), (None, "Exit")]
    me = [MenuItem(*t, p, None) for p, t in enumerate(sub_menu)]
    sub_title = "Submenu"
    sub_app_menu = ApplicationMenu(stdscr, (me, sub_title))
    items = [(ic, "First"), (ic, "Second"), (ic, "Third"),
             (sub_app_menu.show_menu, "SubMenu"), (None, "Exit")]
    menu = [MenuItem(*t, k, None) for k, t in enumerate(items)]
    menu_title = "Main menu"
    menu = ApplicationMenu(stdscr, (menu, menu_title))
    return menu.show_menu()
