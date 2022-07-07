# NOTE: this tests expect the Open LISA Server being run in TCP mode
# at port 8080 and with ENV=test
import json

import pytest

from ..domain.exceptions.sdk_exception import OpenLISAException
from .. import SDK

LOCALHOST = "127.0.0.1"
SERVER_PORT = 8080
TEST_TEKTRONIX_OSC_INSTRUMENT_ID = "USB0::0x0699::0x0363::C107676::INSTR"
SOME_VALID_TEKTRONIX_OSC_COMMAND = "clear_status"
SOME_VALID_TEKTRONIX_OSC_COMMAND_INVOCATION = "set_trigger_level 3.4"
MOCK_IMAGE_PATH = "Open_LISA_SDK/tests/mock_img.jpg"


def test_get_instruments_as_python_list_of_dicts():
    sdk = SDK(log_level="ERROR")
    sdk.connect_through_TCP(host=LOCALHOST, port=SERVER_PORT)
    instruments = sdk.get_instruments(response_format="PYTHON")
    assert isinstance(instruments, list)
    for i in instruments:
        assert isinstance(i, dict)
    sdk.disconnect()


def test_get_instruments_as_json_string():
    sdk = SDK(log_level="ERROR")
    sdk.connect_through_TCP(host=LOCALHOST, port=SERVER_PORT)
    instruments_json_string = sdk.get_instruments(response_format="JSON")
    assert isinstance(instruments_json_string, str)

    try:
        json.loads(instruments_json_string)
    except:
        pytest.fail("invalid json string received: {}".format(
            instruments_json_string))

    sdk.disconnect()


def test_get_specific_instrument_as_python_dict():
    sdk = SDK(log_level="ERROR")
    sdk.connect_through_TCP(host=LOCALHOST, port=SERVER_PORT)
    instrument = sdk.get_instrument(
        instrument_id=TEST_TEKTRONIX_OSC_INSTRUMENT_ID, response_format="PYTHON")
    assert isinstance(instrument, dict)
    assert instrument["physical_address"] == TEST_TEKTRONIX_OSC_INSTRUMENT_ID

    sdk.disconnect()


def test_get_specific_instrument_as_json_str():
    sdk = SDK(log_level="ERROR")
    sdk.connect_through_TCP(host=LOCALHOST, port=SERVER_PORT)
    instrument_json = sdk.get_instrument(
        instrument_id=TEST_TEKTRONIX_OSC_INSTRUMENT_ID, response_format="JSON")
    assert isinstance(instrument_json, str)
    assert TEST_TEKTRONIX_OSC_INSTRUMENT_ID in instrument_json

    sdk.disconnect()


def test_get_specific_instrument_that_does_not_exist_raises_exception():
    sdk = SDK(log_level="ERROR")
    sdk.connect_through_TCP(host=LOCALHOST, port=SERVER_PORT)

    with pytest.raises(OpenLISAException):
        sdk.get_instrument(instrument_id="unexisting_instrument",
                           response_format="PYTHON")
    sdk.disconnect()


def test_get_instrument_commands_as_python_list_of_dicts():
    sdk = SDK(log_level="ERROR")
    sdk.connect_through_TCP(host=LOCALHOST, port=SERVER_PORT)
    commands = sdk.get_instrument_commands(
        instrument_id=TEST_TEKTRONIX_OSC_INSTRUMENT_ID, response_format="PYTHON")
    assert isinstance(commands, dict)
    assert SOME_VALID_TEKTRONIX_OSC_COMMAND in commands.keys()
    sdk.disconnect()


def test_get_instrument_commands_as_json_string():
    sdk = SDK(log_level="ERROR")
    sdk.connect_through_TCP(host=LOCALHOST, port=SERVER_PORT)
    commands_json_string = sdk.get_instrument_commands(
        instrument_id=TEST_TEKTRONIX_OSC_INSTRUMENT_ID, response_format="JSON")
    assert isinstance(commands_json_string, str)
    assert SOME_VALID_TEKTRONIX_OSC_COMMAND in commands_json_string
    sdk.disconnect()


def test_is_valid_command_invocation_with_a_valid_invocation_returns_true():
    sdk = SDK(log_level="ERROR")
    sdk.connect_through_TCP(host=LOCALHOST, port=SERVER_PORT)
    is_valid = sdk.is_valid_command_invocation(
        instrument_id=TEST_TEKTRONIX_OSC_INSTRUMENT_ID,
        command_invocation=SOME_VALID_TEKTRONIX_OSC_COMMAND_INVOCATION)
    assert is_valid == True
    sdk.disconnect()


def test_is_valid_command_invocation_with_invalid_invocations_returns_false():
    sdk = SDK(log_level="ERROR")
    sdk.connect_through_TCP(host=LOCALHOST, port=SERVER_PORT)
    invalid_invocations = [
        "unexisting command",
        "set_trigger_level 10 20",
        "set_trigger_level ASCII",
    ]
    for ii in invalid_invocations:
        is_valid = sdk.is_valid_command_invocation(
            instrument_id=TEST_TEKTRONIX_OSC_INSTRUMENT_ID,
            command_invocation=ii)
        print(ii)
        assert is_valid == False
    sdk.disconnect()


def test_send_command_to_get_image_from_mock_camera():
    sdk = SDK(log_level="ERROR")
    sdk.connect_through_TCP(host=LOCALHOST, port=SERVER_PORT)
    result = sdk.send_command(instrument_id="CAM_ID",
                              command_invocation="get_image")
    with open(MOCK_IMAGE_PATH, "rb") as f:
        image_bytes = f.read()
        assert image_bytes == result["value"]
