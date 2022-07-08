from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class ErrorType(str, Enum):
    """
    The type of error.

    https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/other#ErrorType
    """

    ERROR_TYPE_UNSPECIFIED = (
        "ERROR_TYPE_UNSPECIFIED"  #: The default error type, do not use this.
    )
    ERROR = "ERROR"  #: Corresponds to the #ERROR! error.
    NULL_VALUE = "NULL_VALUE"  #: Corresponds to the #NULL! error.
    DIVIDE_BY_ZERO = "DIVIDE_BY_ZERO"  #: Corresponds to the #DIV/0 error.
    VALUE = "VALUE"  #: Corresponds to the #VALUE! error.
    REF = "REF"  #: Corresponds to the #REF! error.
    NAME = "NAME"  #: Corresponds to the #NAME? error.
    NUM = "NUM"  #: Corresponds to the #NUM! error.
    N_A = "N_A"  #: Corresponds to the #N/A error.
    LOADING = "LOADING"  #: Corresponds to the Loading... state.


class ErrorValue(BaseModel):
    """
    An error in a cell.

    https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/other#ErrorValue
    """

    type: ErrorType = Field()
    message: str = Field()


class ExtendedValue(BaseModel):
    """
    The kinds of value that a cell in a spreadsheet can have.

    https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/other#ExtendedValue
    """

    number_value: Optional[float] = Field(None, alias="numberValue")
    string_value: Optional[str] = Field(None, alias="stringValue")
    bool_value: Optional[bool] = Field(None, alias="boolValue")
    formula_value: Optional[str] = Field(None, alias="formulaValue")
    error_value: Optional[ErrorValue] = Field(None, alias="errorValue")
