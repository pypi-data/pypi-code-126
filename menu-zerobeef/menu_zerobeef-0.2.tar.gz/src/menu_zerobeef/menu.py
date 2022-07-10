"""
This module is used for creating and showing menus.
"""
import curses

from menu_zerobeef.data import (ItemMultiSelection, ItemSingleSelection,
                                MenuItem)


class ApplicationMenu():
    """
    This is the class for the menu.
    The class handles both drawing
    and capturing keystrokes. If you
    want to change the functionality
    it is suggested that you extend
    and override the specific functions
    from this class that you want to change.

    Functions
    ---------
    __init__ : self, stdscr, args
        Initiailizes the instance of the class
        with the information given, it requires
        items and an standard screen from curses.
        The standard screen from curses can be
        obtained from curses.wrapper or similar.
    show_menu : self
        Prints the menu on the screen for the
        end user and stops to capture a keystroke
        which will determine the action to take.
    actions : self
        Reads the keystroke from the end user
        and either moves up or down one position
        in the menu. It can also execute any action
        that the menu item has, mark the item as
        selected or return a list or a single item.
    exit_menu : self
        This changes one variable that determines
        whether the loop that presents the menu
        should be on or off. The variable will
        be set to an off state using this function,
        which means that the menu will exit.
    remark_items : self
        It goes through all menu items and sends
        the current position to all of them. Each
        item will then check wether it is located
        at that position or not. Each item will
        also check if it's already active or not.
        If it has the position number that matches
        or is active then it will change state.

    Parameters
    ----------
    stdscr : Any
        An object which lets the class
        draw items on screen.
    args : List/Tuple
        A tuple or a list of objects
        that would otherwise make the
        argument list too long.
    
    Returns
    -------
    An initialized instance of the class
    ApplicationMenu.
    """

    def __init__(self, stdscr, args=()):
        """
        Initializes a menu for different usecases.

        This function initializes the settings for
        a menu with different settings. Settings
        such as multiselection, singleselection or
        just a plain menu.

        Parameters
        ----------
        self : class
            A pointer to the class itself to be able
            to access all the neccessary items set
            in this function.
        """
        self.stdscr = stdscr
        self.cursor_position = 0
        self.items = args[0]
        self.menu_title = args[1]
        self.loop = True
        self.init_scr_x = args[2] if len(args) > 2 else 1
        self.init_scr_y = args[3] if len(args) > 3 else 2
        curses.init_pair(1, curses.COLOR_BLACK, -1)

    def show_menu(self):
        """
        Presents the menu to the end user.

        The function clears the screen and
        writes the title as well as all the
        menu items that it has from the time
        of being created. It uses str function
        on each item as that is coded as __str__
        which returns a specific string for
        each type of menu item. It also looks
        at the style for each menu item, whether
        the item is selected or not and active
        or not.

        Parameters
        ----------
        self : class
            A Pointer to the class itself to be able
            to access all the neccessary items set
            in the class.
        """
        data = None
        self.remark_items()
        while self.loop:
            self.stdscr.clear()
            self.stdscr.addstr(self.init_scr_y, self.init_scr_x,
                               self.menu_title,
                               curses.color_pair(1) + curses.A_BOLD)
            for k, menu_item in enumerate(self.items):
                self.stdscr.addstr(self.init_scr_y + 1 + k, self.init_scr_x,
                                   menu_item.title if menu_item.title in ("Cancel", "Done")\
                                   else str(menu_item), menu_item.get_style())
            data = self.actions()
        if data is not None:
            return data

    def actions(self):
        """
        After rendering the menu for the user, it will stop
        and start capturing keys from the user. The key stroke
        will then be used to determine what to do based on the
        different types of menu items as well as the position
        and whether or not to exit the menu.
        """
        key = self.stdscr.getkey()
        current_item = self.items[self.cursor_position]
        if current_item.title in ("Cancel", "Exit") and key == "\n"\
                or key in ("q", "Q"):
            self.exit_menu()
            return None

        if key in ("KEY_UP", "KEY_DOWN"):
            self.cursor_position = (self.cursor_position + 1) % len(self.items)\
                if key == "KEY_DOWN" else (self.cursor_position - 1) % len(self.items)\
                if key == "KEY_UP" else self.cursor_position
            self.remark_items()

        if isinstance(current_item, MenuItem) and key == "\n"\
                and not isinstance(current_item, ItemSingleSelection)\
                and not isinstance(current_item, ItemMultiSelection):
            current_item.take_action()

        if isinstance(current_item, ItemSingleSelection) and key == "\n"\
                and not isinstance(current_item, ItemMultiSelection):
            self.exit_menu()
            return current_item.title

        if isinstance(current_item, ItemMultiSelection):
            data = None
            if key == "\n" and current_item.title != "Done":
                self.items[self.cursor_position].select()
            elif key == "\n" and current_item.title == "Done":
                data = [i.title for i in self.items if i.is_selected]
                self.exit_menu()
            return data
        return None

    def exit_menu(self):
        """
        Stops the loop that draws and captures
        the user keystrokes and menu.
        """
        self.loop = False

    def remark_items(self):
        """
        Set all menu items as inactive except
        for the menu item that is on the current
        position. 
        """
        for item in self.items:
            item.set_active(self.cursor_position)
