import numpy as np
from typing import Union


def stringify_intensity(fan) -> Union[str, str]:
    """Creates a string from a fan's intensity.

    Returns a fan's intensity as string based on the fan's status and its current intensity.

    Args:
        fan (Fan): Fan instance

    Returns:
        nicely formatted fan intensity
    """
    if not fan.settings.active:
        return "-"
    elif fan.intensity == -1:
        return "starting"
    else:
        return str(np.int(fan.intensity))


def _start_html_table(style) -> str:
    if style:
        style_string = ";".join(
            map(lambda x: f"{str(x)}:{str(style[x])}", style.keys())
        )
        return f'<result class="result result-sm" style="{style_string}">\n'
    else:
        return '<result class="result result-sm">\n'


def _generate_html_buttons(fan_name, fan_active) -> str:
    """Function to generate buttons for a fan to be displayed in the fan status table

    Generate three buttons for a fan:
      1) Status button: showing either start or stop based on the fan's status
      2) Edit button: button to edit a fan's settings
      3) Delete button: button to delete a fan from the fan controller

    Args:
        fan_name (str): the fan's name
        fan_active (bool): True if the fan is turned on, else False

    Returns:
        A string containing HTML table cells with one HTML button per cell.
    """
    buttons = '<td class="centerText">'
    if fan_active:
        buttons += (
            f'<form action="/fans/'
            + fan_name
            + '/stop" method="get" style={"margin-right": "10px"}>\n'
            '<input type="hidden" name="fan_name" value="'
            + fan_name
            + f'"/><button type="submit" class="btn btn-danger" name="'
            + fan_name
            + '" " value="" data-toggle="tooltip" data-placement="top" title="Stop"><i class="fas fa-stop"></i> Stop</button>\n'
            "</form>"
        )
    else:
        buttons += (
            f'<form action="/fans/'
            + fan_name
            + '/start" method="get" style={"margin-right": "10px"}>\n'
            '<input type="hidden" name="fan_name" value="'
            + fan_name
            + f'"/><button type="submit" class="btn btn-success" name="'
            + fan_name
            + '" " value="" data-toggle="tooltip" data-placement="top" title="Start"><i class="fas fa-play"></i> Start</button>\n'
            "</form>"
        )
    buttons += "</td>\n"
    buttons += '<td class="centerText">'
    buttons += (
        f'<form action="/fans/'
        + fan_name
        + '/settings" method="get" style={"margin-right": "10px"}>\n'
        '<input type="hidden" name="fan_name" value="'
        + fan_name
        + f'"/><button type="submit" class="btn btn-primary" name="'
        + fan_name
        + '" " value="" data-toggle="tooltip" data-placement="top" title="Edit"><i class="far fa-edit"></i> Edit</button>\n'
        "</form>"
    )
    buttons += "</td>\n"
    buttons += '<td class="centerText">'
    buttons += (
        '<form action="/fans/' + fan_name + '/delete" method="get">\n'
        f'<button type="submit" class="btn btn-danger" name="delete_'
        + fan_name
        + '" " value="" data-toggle="tooltip" data-placement="top" title="Delete"><i class="far fa-times-circle"></i> Delete'
        "</button\n>"
        "</form>"
    )
    buttons += "</td>\n"
    return buttons


def _generate_html_table_header(headers, units) -> str:
    result = ""
    for index, header in enumerate(headers):
        if units[index]:
            result += f'    <th class="centerText">{header}<br>{units[index]}</th>\n'
        else:
            result += f'    <th class="centerText">{header}</th>\n'
    return result


def _generate_html_basic_data(mode: str) -> tuple[list[str], list[str], list[str]]:
    if mode == "full":
        headers = [
            "Fan Name",
            "Speed",
            "GPIO Pin",
            "Mode",
            "Minimum Threshold",
            "Maximum Threshold",
            "",
            "",
            "",
        ]
        units = ["", "%", "", "", "°C", "°C", "", "", ""]
        attributes = [
            "name",
            "current_intensity",
            "gpio_pin",
            "mode",
            "off_threshold",
            "max_threshold",
        ]
    else:
        headers = ["Fan Name", "Intensity"]
        units = ["", "%"]
        attributes = ["name", "current_intensity"]
    return headers, units, attributes


def _generate_html_table_fan_element(fan_controller, attributes, mode) -> str:
    result = ""
    # add table row data
    for fan in fan_controller.fans.values():
        result += "  <tr>\n"
        for attr in attributes:
            if attr == "current_intensity":
                val = stringify_intensity(fan)
                result += f'    <td class="centerText" id="fan_intensity_{fan.settings.name}">{val}</td>\n'
            elif attr == "max_threshold" and fan.settings.mode == "Classic":
                result += f'    <td class="centerText"></td>\n'
            else:
                val = getattr(fan.settings, attr)
                result += f'    <td class="centerText">{val}</td>\n'
        if mode == "full":
            result += _generate_html_buttons(
                fan_name=fan.settings.name, fan_active=fan.settings.active
            )
        result += "  </tr>\n"
    return result


def generate_html_table(fan_controller, mode="full", style=None) -> str:
    """Function to generate a table containing status information for fans registered at a fan controller."""
    if len(fan_controller.fans) <= 0:
        return "<p>Nothing to display, no fans have been added yet.</p>"
    headers, units, attributes = _generate_html_basic_data(mode)
    table = _start_html_table(style)
    table += _generate_html_table_header(headers, units)
    table += _generate_html_table_fan_element(fan_controller, attributes, mode)
    table += "</table>"
    return table
