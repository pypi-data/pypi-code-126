from functools import cached_property, partial
from operator import is_not
from itertools import takewhile

import numpy as np
import pandas as pd

from genesisapi.datatypes import JSON
from genesisapi.result import Result


class TableResult(Result):

    def __init__(self, client, json: JSON):
        super().__init__(json)
        self.client = client

    @cached_property
    def object(self):
        return TableObject(self.json['Object'])

    def to_dataframe(
            self,
            skip_rows=None,
            skip_footer=None,
            index_length=None,
            column_length=None
    ) -> pd.DataFrame:
        """

        :param skip_rows:
        :param skip_footer:
        :param index_length:
        :param column_length:
        :return:
        """

        begin_idx, end_idx = self.__startwith_index(';')
        skip_rows = skip_rows or begin_idx
        column_length = column_length or (end_idx - begin_idx) + 1

        footer_idx, _ = self.__startwith_index('__________')
        skip_footer = skip_footer or (len(self.__rows) - footer_idx)

        index_length = index_length or len(
            list(takewhile(lambda x: x == '', self.__data[begin_idx])))

        column_axis = self.object.content.get_column_index(
            skip_rows,
            column_length)

        row_axis = self.object.content.get_row_index(
            skip_rows + column_length,
            skip_footer, index_length)

        index_names = self.__get_index_names(index_length)
        row_axis.set_names(index_names, inplace=True)

        ncols, = column_axis.shape
        data = self.object.content.data[
               skip_rows + column_length: -skip_footer,
               index_length: index_length + ncols]

        return pd.DataFrame(
            data,
            index=row_axis,
            columns=column_axis)

    @property
    def __rows(self):
        return self.object.content.data_rows

    @property
    def __data(self):
        return self.object.content.data

    def __get_row_indies(self, start):
        idx = list(filter(partial(is_not, None), [
            idx if row.startswith(start) else None
            for idx, row in enumerate(self.__rows)
        ]))
        return min(idx), max(idx)

    def __startwith_index(self, sub_string):
        return self.__get_row_indies(start=sub_string)

    @staticmethod
    def __get_index_names(index_length):
        return [''] * index_length


class TableObject(Result):

    def __init__(self, json: JSON):
        super().__init__(json)

    @cached_property
    def content(self):
        return Content(super().json['Content'])

    @cached_property
    def structure(self):
        return Structure(super().json['Structure'])


class Content(Result):

    def __init__(self, json: JSON):
        super().__init__(json)

    @cached_property
    def data_rows(self, new_line_sep='\n'):
        return self.json.split(new_line_sep)

    @cached_property
    def data(self):
        cells = []

        for r in self.data_rows:
            cells.append(r.split(';'))

        nrows = len(self.data_rows)
        ncols = max([len(r) for r in self.data_rows])
        data = np.empty((nrows, ncols), dtype=object)

        for i, r in enumerate(cells):
            for j, cell in enumerate(r):
                data[i, j] = cell

        return data

    def get_row_index(self, skip_rows, skip_footer, index_length):
        index = []
        for i in range(index_length):
            index.append(self.data[skip_rows:-skip_footer, i])

        return pd.MultiIndex.from_arrays(index)

    def get_column_index(self, skip_rows, index_length):

        def is_valid(x):
            return x != '' and x is not None

        index = []
        for i in range(skip_rows, skip_rows + index_length):
            index.append(list(filter(is_valid, self.data[i, :])))

        return pd.MultiIndex.from_arrays(index)


class Structure(Result):

    def __init__(self, json: JSON):
        super().__init__(json)

    @cached_property
    def head(self):
        return Head(super().json['Head'])

    @cached_property
    def columns(self):
        return [Column(j) for j in super().json['Columns']]

    @cached_property
    def rows(self):
        return [Row(j) for j in super().json['Rows']]

    @cached_property
    def subtitel(self):
        return Subtitel(super().json['Subtitel'])

    @cached_property
    def structure(self):
        return [SubStructure(j) for j in super().json['Structure']]


class SubStructure(Result):

    def __init__(self, json: JSON):
        super().__init__(json)

    @cached_property
    def code(self):
        return super().json['Code']

    @cached_property
    def content(self):
        return super().json['Content']

    @cached_property
    def type(self):
        return super().json['Type']

    @cached_property
    def values(self):
        return super().json['Values']

    @cached_property
    def selected(self):
        return super().json['Selected']

    @cached_property
    def updated(self):
        return super().json['Updated']

    @cached_property
    def updated(self):
        return [SubStructure(j) for j in super().json['Structure']]


class Head(Result):

    def __init__(self, json: JSON):
        super().__init__(json)

    @cached_property
    def code(self):
        return super().json['Code']

    @cached_property
    def content(self):
        return super().json['Content']

    @cached_property
    def type(self):
        return super().json['Type']

    @cached_property
    def structure(self):
        return [SubStructure(j) for j in super().json['Structure']]


class Subtitel(Result):
    def __init__(self, json: JSON):
        super().__init__(json)

    @cached_property
    def code(self):
        return super().json['Code']

    # @cached_property
    def content(self):
        return super().json['Content']

    @cached_property
    def type(self):
        return super().json['Type']

    @cached_property
    def structure(self):
        return [SubStructure(j) for j in super().json['Structure']]


class Column(Result):

    def __init__(self, json: JSON):
        super().__init__(json)

    @cached_property
    def code(self):
        return super().json['Code']

    @cached_property
    def content(self):
        return super().json['Content']

    @cached_property
    def type(self):
        return super().json['Type']

    @cached_property
    def structure(self):
        return [SubStructure(j) for j in super().json['Structure']]


class Row(Result):

    def __init__(self, json: JSON):
        super().__init__(json)

    @cached_property
    def code(self):
        return super().json['Code']

    @cached_property
    def content(self):
        return super().json['Content']

    @cached_property
    def type(self):
        return super().json['Type']

    @cached_property
    def structure(self):
        return [SubStructure(j) for j in super().json['Structure']]
