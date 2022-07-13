# -*- coding: utf-8 -*-
# *******************************************************
#   ____                     _               _
#  / ___|___  _ __ ___   ___| |_   _ __ ___ | |
# | |   / _ \| '_ ` _ \ / _ \ __| | '_ ` _ \| |
# | |__| (_) | | | | | |  __/ |_ _| | | | | | |
#  \____\___/|_| |_| |_|\___|\__(_)_| |_| |_|_|
#
#  Sign up for free at http://www.comet.ml
#  Copyright (C) 2015-2021 Comet ML INC
#  This file can not be copied and/or distributed without
#  the express permission of Comet ML Inc.
# *******************************************************

from ._typing import Any, Dict


def sanitize_environment_variables(container_environment):
    # type: (Dict[Any]) -> Dict[Any]
    if not isinstance(container_environment, dict):
        return container_environment

    for key, value in container_environment.items():
        if key == "env":
            if isinstance(value, dict):
                container_environment[key] = {}
            elif isinstance(value, str):
                container_environment[key] = ""
            else:
                container_environment[key] = []
        elif isinstance(value, list):
            for i, item in enumerate(value):
                value[i] = sanitize_environment_variables(item)
        sanitize_environment_variables(value)
    return container_environment
