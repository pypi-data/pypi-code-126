"""
The data module defines three models for items in the menu.
One of the models is for a single menu item where there
might be a submenu or not. The second item is for single
selection only where there are no submenus and multichoice
can't be done. The third class is for multichoice, where
more than one item can be selected and there are no
submenus present.

Each class inherits the menu_item class where it holds
actions and submenus, however they will use same variables
but different content for easier understanding of how the
menu works.
"""
import curses


class MenuItem():
    """
    A basic menu item for use with a normal
    menu that can or might have submenus in
    it.

    Functions
    ---------
    __init__(self, action, title, position, fargs)
    __str__(self)
    set_active(self, position)
    get_style(self)
    take_action(self)

    Parameters
    ----------
    self : Any
        An object pointing to an instance
        of this class.
    action : Func
        A pointer to a function to execute
        once the menu item is selected by 
        the user.
    title : str
        A string which should be displayed
        in the menu when drawing it on screen
    position : int
        An integer which is used to determine
        whether the menu item is active or not.
    fargs : tuple
        A tuple with extra items that should be
        sent further to the action when the item
        is selected, works almost like a pipe
    """

    def __init__(self, action, title, position, fargs):
        self.action = action
        self.title = title
        self.position = position
        self.fargs = fargs
        self.is_active = False
        curses.init_pair(10, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(11, curses.COLOR_BLACK, -1)

    def __str__(self):
        return str(self.title)

    def set_active(self, position):
        """
        Takes two parameters and checks whether cur_pos
        is the same as the item position that got set
        from the beginning. If this is the case it sets
        self.is_active to True otherwise False

        Parameters
        ----------
        self : object
            The pointer to the class itself

        Returns
        -------
        None
        """
        if position == self.position or\
                self.is_active:
            self.is_active = not self.is_active

    def get_style(self):
        """
        Returns the style specific to the position that
        the cursor is on.

        Parameters
        ----------
        self: object
            The pointer to the class itself

        Returns
        -------
        color_pair
            A color pair used in curses that
            will show the user what item is
            selected or not.
        """
        return curses.color_pair(10) + curses.A_BOLD if self.is_active else\
            curses.color_pair(11)

    def take_action(self):
        """
        Takes no parameter as input. Checks wether the
        item that is set to the variable action in
        the self object is callable. If the item is
        a callable then we can call it as we want.
        Otherwise we would do anything else with the
        data. Probably ignore the item which is set
        at that variable for the moment being.
        """
        if callable(self.action) and self.fargs is None:
            self.action()
        elif callable(self.action) and self.fargs is not None:
            self.action(*self.fargs)


class ItemSingleSelection(MenuItem):
    """
    TODO: Write a docstring
    """

    def __init__(self, title, position):
        super().__init__(None, title, position, None)
        self.single_choice = True

    def __str__(self):
        return f"{self.title} <-" if self.is_active else f"{self.title}"

    def get_style(self):
        return super().get_style()


class ItemMultiSelection(MenuItem):
    """
    ItemMultiSelection is used when the menu is in
    a mode where multiple items can be selected.
    The menu item inherits the same properties from
    the MenuItem class and adds some extra functionality
    or changes the functions to differentiate from
    the super class.

    Parameters
    ----------
    title : str
        An items title which should be displayed in
        the menu.
    position : int
        Where in the menu is it located at
    """

    def __init__(self, title, position):
        super().__init__(None, title, position, None)
        self.is_selected = False
        curses.init_pair(12, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(13, curses.COLOR_GREEN, -1)

    def __str__(self):
        return f"[x] {self.title} <-" if self.is_selected and self.is_active else\
            f"[x] {self.title}" if self.is_selected else\
            f"[ ] {self.title} <-" if self.is_active else\
            f"[ ] {self.title}"

    def select(self):
        """
        The action can be used when the menu type
        is a multiple choice menu. The function
        works in the same wat as self.set_active
        by negating is own variable. See the
        function definition for set_active
        """
        self.is_selected = not self.is_selected

    def get_style(self):
        """
        Changes how the menu item is displayed on
        screen. If the menu item is not selected
        but active or selected but not active or
        selected and active, then different styles
        are applited to the menu item.
        """
        return super().get_style() if not self.is_selected else\
            curses.color_pair(13) if self.is_selected and not self.is_active else\
            curses.color_pair(12) + curses.A_BOLD
