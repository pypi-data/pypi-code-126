from typing import TYPE_CHECKING, ClassVar

from pydantic import Field
from tygle.apis.sheets.types.enums import (
    DateTimeRenderOption,
    Dimension,
    InsertDataOption,
    ValueInputOption,
    ValueRenderOption,
)
from tygle.base import Resource

if TYPE_CHECKING:
    from tygle.apis.sheets.rest.values import Values


class ValueRange(Resource):
    rest: ClassVar["Values"]
    """Data within a range of the spreadsheet.

    https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values#ValueRange
    """

    range: str = Field(title="range")
    major_dimension: Dimension = Field(alias="majorDimension", title="majorDimension")
    values: list[list] = Field(title="values")

    async def append(
        self,
        spreadsheet_id: str,
        range: str,
        /,
        *,
        value_input_option: ValueInputOption = ValueInputOption.RAW,
        insert_data_option: InsertDataOption = InsertDataOption.OVERWRITE,
        include_values_in_response: bool = False,
        response_value_render_option: ValueRenderOption = ValueRenderOption.FORMATTED_VALUE,
        response_date_time_render_option: DateTimeRenderOption = DateTimeRenderOption.SERIAL_NUMBER,
    ):
        """Chain to :meth:`.Values.append`.

        :param spreadsheet_id: The ID of the spreadsheet to update
        :type spreadsheet_id: int
        :param range: The `A1 notation <https://developers.google.com/sheets/api/guides/concepts#cell>` of a range to search for a logical table of data
        :type range: str
        :param value_input_option: How the input data should be interpreted, defaults to :attr:`.ValueInputOption.RAW`
        :type value_input_option: ValueInputOption, optional
        :param insert_data_option: How the input data should be inserted, defaults to :attr:`.InsertDataOption.OVERWRITE`
        :type insert_data_option: InsertDataOption, optional
        :param include_values_in_response: Determines if the update response should include the values of the cells that were appended, defaults to `False`
        :type include_values_in_response: bool, optional
        :param response_value_render_option: Determines how values in the response should be rendered, defaults to :attr:`.ValueRenderOption.FORMATTED_VALUE`
        :type response_value_render_option: ValueRenderOption, optional
        :param response_date_time_render_option: Determines how dates, times, and durations in the response should be rendered. This is ignored if :paramref:`.response_value_render_option` is :attr:`.ValueRenderOption.FORMATTED_VALUE`, defaults to :attr:`.DateTimeRenderOption.SERIAL_NUMBER`
        :type response_date_time_render_option: DateTimeRenderOption, optional
        """
        return self.rest.append(
            spreadsheet_id,
            range,
            self,
            value_input_option=value_input_option,
            insert_data_option=insert_data_option,
            include_values_in_response=include_values_in_response,
            response_value_render_option=response_value_render_option,
            response_date_time_render_option=response_date_time_render_option,
        )
