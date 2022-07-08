from typing import Optional

from aiogoogle import GoogleAPI
from pydantic import create_model
from tygle.apis.sheets.types.resources.spreadsheets import Spreadsheet
from tygle.base import REST, DataRequest
from tygle.client.client import Client

from .values import Values


class Spreadsheets(REST):
    def __init__(self, client: Client, parent: GoogleAPI) -> None:
        super().__init__(client, parent)
        self.values = Values(client, self.parent)  # todo move

    @property
    def Spreadsheet(self):
        return create_model("Spreadsheet", rest=self, __base__=Spreadsheet)

    async def get(
        self,
        spreadsheet_id: str,
        ranges: Optional[list[str]] = None,
        include_grid_data: bool = True,
    ) -> DataRequest["Spreadsheet"]:
        if ranges is None:
            ranges = []
        return DataRequest(
            self.client,
            self.parent.spreadsheets.get(
                spreadsheetId=spreadsheet_id,
                ranges=ranges,
                includeGridData=include_grid_data,
            ),
            Spreadsheet,
        )
