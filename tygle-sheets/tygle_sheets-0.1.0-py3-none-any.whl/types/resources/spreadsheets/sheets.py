from typing import Optional

from pydantic import BaseModel, Field

from .cells import CellData


class SheetProperties(BaseModel):
    """
    Properties of a sheet.

    https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/sheets#SheetProperties
    """

    sheet_id: int = Field(alias="sheetId")
    title: str = Field()


class GridRange(BaseModel):
    """
    A range on a sheet. All indexes are zero-based.
    Indexes are half open, i.e. the start index is inclusive and the end index is exclusive -- [startIndex, endIndex).
    Missing indexes indicate the range is unbounded on that side.

    https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/other#GridRange
    """

    sheet_id: Optional[int] = Field(None, alias="sheetId")
    start_row_index: int = Field(alias="startRowIndex")
    end_row_index: int = Field(alias="endRowIndex")
    start_column_index: int = Field(alias="startColumnIndex")
    end_column_index: int = Field(alias="endColumnIndex")


class RowData(BaseModel):
    """
    Data about each cell in a row.

    https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/sheets#RowData
    """

    values: list[CellData] = Field([])


class GridData(BaseModel):
    """
    Data in the grid, as well as metadata about the dimensions.

    https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/sheets#GridData
    """

    start_row: Optional[int] = Field(None, alias="startRow")
    start_column: Optional[int] = Field(None, alias="startColumn")
    row_data: list[RowData] = Field(alias="rowData")


class Sheet(BaseModel):
    """
    A sheet in a spreadsheet.

    https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/sheets#Sheet
    """

    properties: SheetProperties = Field()
    data: list[GridData] = Field()
    merges: list[GridRange] = Field()
