# Copyright 2021 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""
Module for parsing information from yaml in python accessible attributes for different
configuration classes and also for the ModelRegistry class.
"""
from typing import Any, Dict

import related
from config_builder.BaseConfigClass import BaseConfigClass


@related.mutable(strict=True)
class ModelConfig(BaseConfigClass):
    class_type: str = related.StringField()
    constructor_parameters: Dict[str, Any] = related.ChildField(
        cls=dict,
    )
