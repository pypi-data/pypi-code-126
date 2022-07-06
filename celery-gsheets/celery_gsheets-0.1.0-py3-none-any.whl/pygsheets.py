import pygsheets
from pygsheets.client import *
from pygsheets.worksheet import Worksheet


class Worksheet(Worksheet):
    @property
    def all_cells(self):
        cells = self.get_all_values(
            include_tailing_empty_rows=False,
            include_tailing_empty=False,
            returnas='cells',
        )
        for r, row in reversed(list(enumerate(cells))):
            if not len(row):
                del cells[r]
        return cells

    def append_rows(self, values, inherit=True, **kwargs):
        if isinstance(values, list) and len(values) == 0:
            return False
        return self.insert_rows(self.last_row, 1, values, inherit=inherit, **kwargs)

    def formula(self, addr):
        return self.get_value(addr, value_render=ValueRenderOption.FORMULA)

    @property
    def bottom_right(self):
        return self.all_cells[-1][-1]

    def col_values(self, col, **kwargs):
        return self.get_col(col, include_tailing_empty=False, **kwargs)

    @property
    def last_row(self):
        values = self.get_all_values(include_tailing_empty=False)
        for i, row in reversed(list(enumerate(values))):
            if len(set(filter(None, row))):
                return i + 1
        return 0

    @property
    def next_available_row(self):
        return self.last_row + 1


class Spreadsheet(Spreadsheet):
    worksheet_cls = Worksheet

    @classmethod
    def open(cls, title, gc: Client = None, **kwargs) -> 'Spreadsheet':
        gc: Client = pygsheets.authorize(**kwargs)
        Client.spreadsheet_cls = cls
        return gc.open(title)

    def worksheet(self, value, property='title') -> Worksheet:
        return super(Spreadsheet, self).worksheet(property, value)
