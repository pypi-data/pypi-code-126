from typing import Optional

from pydantic import create_model
from tygle.apis.sheets.types.enums import (
    DateTimeRenderOption,
    Dimension,
    InsertDataOption,
    ValueInputOption,
    ValueRenderOption,
)
from tygle.apis.sheets.types.resources.values import ValueRange
from tygle.apis.sheets.types.responses.values import AppendValuesResponse
from tygle.base import REST, DataRequest


class Values(REST):
    @property
    def ValueRange(self):
        return create_model("ValueRange", rest=self, __base__=ValueRange)

    def get(
        self,
        spreadsheet_id: str,
        range: str,
        /,
        *,
        major_dimension: Optional[Dimension] = None,
        value_render_option: Optional[ValueRenderOption] = None,
        date_time_render_option: Optional[DateTimeRenderOption] = None,
    ) -> DataRequest["ValueRange"]:
        """Returns a range of values from a spreadsheet. The caller must specify the spreadsheet ID and a range.

        https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/get
        """
        return DataRequest(
            self.client,
            self.parent.spreadsheets.values.get(
                spreadsheetId=spreadsheet_id,
                range=range,
                majorDimension=major_dimension.value,
                valueRenderOption=value_render_option,
                dateTimeRenderOption=date_time_render_option,
            ),
            self.ValueRange,
        )

    def append(
        self,
        spreadsheet_id: str,
        range: str,
        /,
        value_range: "ValueRange",
        *,
        value_input_option: Optional[ValueInputOption] = None,
        insert_data_option: Optional[InsertDataOption] = None,
        include_values_in_response: Optional[bool] = None,
        response_value_render_option: Optional[ValueRenderOption] = None,
        response_date_time_render_option: Optional[DateTimeRenderOption] = None,
    ) -> DataRequest[AppendValuesResponse]:
        """Appends values to a spreadsheet.

        https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/append
        """
        return DataRequest(
            self.client,
            self.parent.spreadsheets.values.append(
                spreadsheetId=spreadsheet_id,
                range=range,
                json=value_range.dict(),
                valueInputOption=value_input_option.value,
                insertDataOption=insert_data_option.value,
                includeValuesInResponse=include_values_in_response,
                responseValueRenderOption=response_value_render_option.value,
                responseDateTimeRenderOption=response_date_time_render_option.value,
            ),
            AppendValuesResponse,
        )
