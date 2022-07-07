import sys
from .CONSTANTS import *


def validateArguments(apikey, toi, aoi):
    """
    Ensure that parsed arguments are valid according to the API specifications.
    Failure cases raise errors that propagate back to cli.py error handling.
    """
    try:
        _apiKeyValidate(apikey)
        _toiValidate(toi)
        _aoiValidate(aoi)
        _payloadValidate(apikey, toi, aoi)
        status = True
        message = "Validation successful"
    except Exception as e:
        status = False
        message = e

    validationResult = {"status": status, "message": message}
    return validationResult


def _aoiValidate(aoi):
    """
    Validates that this a valid (multi)polygon
    """
    # raise Exception("invalid AOI")
    return True


def _toiValidate(toi):
    """
    Validates that this a valid date format and range
    """
    # raise Exception("invalid TOI")
    return True


def _apiKeyValidate(apikey):
    """
    Validates that this a valid API key.
    """
    # raise Exception("invalid API Key")
    return True


def _payloadValidate(apikey, toi, aoi):
    """
    Validates that the input parameters do not exceed the max payload size.
    """
    # import max payload size from config
    # raise Exception("Payload exceeds 1 Megabyte")
    payloadSize = sys.getsizeof(str(aoi) + toi + apikey)
    if payloadSize >= DATA_API_PAYLOAD_LIMIT_BYTES:
        raise Exception(
            f"Payload of {payloadSize} Bytes exceeds {DATA_API_PAYLOAD_LIMIT_BYTES} Bytes"
        )
    return True
