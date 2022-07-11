"""default network_importer driver for Fortinet."""

from nornir_nautobot.plugins.tasks.dispatcher import default

default.RUN_COMMAND_MAPPING["fortinet"] = "show"

class NautobotNornirDriver(default.NetmikoNautobotNornirDriver):
    """Collection of Nornir Tasks specific to Fortinet FortiOS devices."""
