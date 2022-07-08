from pydantic import BaseModel, Field
from tygle.apis.sheets.types.enums import Dimension
from tygle.base import Resource

from .sheets import Sheet


class SpreadsheetProperties(BaseModel):
    """
    Properties of a spreadsheet.

    https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets#spreadsheetproperties
    """

    title: str


class Spreadsheet(Resource):
    """
    Resource that represents a spreadsheet.

    https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets#resource:-spreadsheet
    """

    spreadsheet_id: str = Field(alias="spreadsheetId")
    properties: SpreadsheetProperties = Field(title="properties")
    sheets: list[Sheet] = Field(title="sheets")

    async def get_values(
        self,
        range: str,
        major_dimension: Dimension = Dimension.ROWS,
    ):
        return await self.client.sheets.spreadsheets.values.get(
            self.spreadsheet_id, range, major_dimension
        )
