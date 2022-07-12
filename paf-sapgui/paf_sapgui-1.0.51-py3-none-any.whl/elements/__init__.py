from ..session import active
import re


class Element:
    def __init__(self, element_id: str):
        self._id = element_id
        self._object = None
        self.make_element()

    def make_element(self):
        self._object = active.session.findById(self._id)

    def set_focus(self):
        self._object.setFocus()

    def element(self):
        return self._object


class Checkbox(Element):
    def __init__(self, element_id):
        super().__init__(element_id)

    def activate(self):
        self._object.selected = -1

    def deactivate(self):
        self._object.selected = 0

    def set(self, state: bool = True):
        self._object.selected = -1 if state else 0


class Button(Element):
    def __init__(self, element_id):
        super().__init__(element_id)

    def click(self):
        self._object.press()


class Label(Element):
    def __init__(self, element_id: str):
        super().__init__(element_id)


class Textarea(Element):
    def __init__(self, element_id: str):
        super().__init__(element_id)

    def value(self, new_value: str = None):
        if new_value is not None:
            self._object.text = new_value
            return self
        return self._object.text


class Textfield(Element):
    def __init__(self, element_id: str):
        super().__init__(element_id)

    def value(self, new_value: str = None):
        if new_value is not None:
            self._object.text = new_value
            return self
        return self._object.text


class Combobox(Element):
    def __init__(self, element_id: str):
        super().__init__(element_id)


class Tabstrip(Element):
    def __init__(self, element_id: str):
        super().__init__(element_id)


class Tab(Element):
    def __init__(self, element_id: str):
        super().__init__(element_id)

    def select(self):
        self._object.select()


class Table(Element):
    def __init__(self, element_id: str):
        super().__init__(element_id)

    def refresh(self):
        self.make_element()
        return self

    def click_cell(self, row_number: int, column: str, double_click: bool = False):
        try:

            if double_click:
                self._object.doubleClick(str(row_number), column)
            else:
                self._object.click(str(row_number), column)
            return self
        except Exception as ex:
            print(f"An error occurred while clicking the cell in row {row_number} and column {column} of"
                  f" the element '{self._id}' ({ex})")

    def row(self, row_number: int):
        try:

            self._object.selectedRows = str(row_number)
            return self
        except Exception as ex:
            print(f"An error occurred while setting the row {row_number} of the element '{self._id}' ({ex})")
            return self

    def activate_row(self, search_value: str | None):

        if search_value is not None:
            self.find_row(search_value=search_value)
        self._object.doubleClickCurrentCell()

    def find_row(self, search_value: str, activate: bool = False):

        self._object.selectedRows = "0"
        active.session.findById("wnd[0]").sendVKey(71)
        active.session.findById("wnd[1]/usr/txtGS_SEARCH-VALUE").text = search_value
        active.session.findById("wnd[1]/usr/txtGS_SEARCH-VALUE").caretPosition = 7
        active.session.findById("wnd[1]/tbar[0]/btn[0]").press()
        active.session.findById("wnd[1]/tbar[0]/btn[12]").press()
        if activate:
            self.activate_row(search_value=None)

    def find_row_by_list(self, search_values: list):

        found_row = None
        for row in range(self._object.rowCount):
            found = []
            for search_value in search_values:
                value_from_row = self._object.getCellValue(row, search_value["column"])
                if value_from_row == search_value["value"]:
                    found.append(True)
                else:
                    found.append(False)
            if False not in found:
                return row

        return None

    def row_count(self) -> int:
        try:

            return self._object.rowCount
        except Exception as ex:
            print(f"An error occurred while getting the row count of element '{self._id}'")

    def cell_value(self, row: int, column_name: str):
        return self._object.getCellValue(row, column_name)

    def get_values_from_columns_by_search_string(self, search_string, columns: dict):
        return_values = []

        self._object.selectedRows = "0"
        active.session.findById("wnd[0]").sendVKey(71)
        from . import search_window

        # active.session.findById("wnd[1]/usr/chkGS_SEARCH-SHOW_HITS").selected = -1
        search_window.anzahl_der_treffer_anzeigen.activate()
        # active.session.findById("wnd[1]/usr/txtGS_SEARCH-VALUE").text = search_string
        search_window.suchbegriff.value(search_string)
        # active.session.findById("wnd[1]/usr/chkGS_SEARCH-SHOW_HITS").setFocus()
        # active.session.findById("wnd[1]/tbar[0]/btn[0]").press()
        search_window.gruener_haken.click()
        from . import search_window_results
        # active.session.findById("wnd[1]/usr/txtGS_SEARCH-SEARCH_INFO").setFocus()
        search_window_results.anzahl_suchergebnisse.set_focus()

        # hits = re.sub("\D.*: 1 von ", "", active.session.findById("wnd[1]/usr/txtGS_SEARCH-SEARCH_INFO").text)
        hits = re.sub("\D.*: 1 von ", "", search_window_results.anzahl_suchergebnisse.value())

        if hits == "Keinen Treffer gefunden":
            search_window.roter_kreis.click()
            return return_values
        hits = int(hits)

        # active.session.findById("wnd[1]/tbar[0]/btn[12]").press()
        search_window.roter_kreis.click()

        row = self._object.currentCellRow

        for counter in range(hits):
            row += counter
            self._object.selectedRows = str(row)
            for key in columns:
                temp_dict = {key: self._object.getCellValue(row, columns[key])}
                return_values.append(temp_dict)
