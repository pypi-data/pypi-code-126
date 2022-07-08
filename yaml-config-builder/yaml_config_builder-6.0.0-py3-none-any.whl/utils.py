# Copyright 2021 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""
Definition of utility methods that are used across the config-builder
"""

from __future__ import absolute_import, division, print_function

import logging
import os
from typing import Any, Dict, List

logger = logging.getLogger(__name__)


def build_config_path(config_path: str, string_replacement_map: Dict[str, str]) -> str:
    """
    Take a config-path and an os-string-replacement-map and try to build a
    valid config-path by using the values of the os-string-replacement-map

    Args:
        config_path: input config-path
        string_replacement_map: dictionary that defines keys and values which
                                are used for string-replacement
    Returns:
        the adapted config-path
    """

    for (
        key,
        value,
    ) in string_replacement_map.items():

        if value != "" and key in config_path:
            logger.debug(
                f"Replace '{key}' "
                f"in config-path '{config_path}' "
                f"with '{value}' "
            )

            config_path = config_path.replace(key, value)

    return config_path


def replace_directory_in_path(
    file_path: str, replacement_key: str, replacement_value: str
) -> str:
    """
    Replaces directory in the given path.

    Args:
        file_path: String, a path to a file
        replacement_key: String, defining what is about to be replaced
        replacement_value: String, defining what the replacement looks like

    Returns: String, the updated file path

    """

    path_list = os.path.normpath(file_path).split(os.sep)

    path_list = list(
        map(
            lambda x: x if x != replacement_key else replacement_value,
            path_list,
        )
    )

    new_path = os.sep.join(path_list)

    return new_path


def check_list_type(obj: List[Any], obj_type: Any) -> bool:
    """
    Check if the given list-object only contains objects of type 'obj_type'

    Args:
        obj: list that is to be checked
        obj_type: type that every object should match

    Returns:
        true if all items of the list are of type 'obj_type', false otherwise
    """
    return bool(obj) and all(isinstance(elem, obj_type) for elem in obj)
