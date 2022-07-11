# Copyright 2021 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""
Module for parsing information from yaml in python accessible attributes for the ModelSuite class.
"""
from typing import List

import related
from config_builder.BaseConfigClass import BaseConfigClass

from mlcvzoo_base.configuration.model_config import ModelConfig


@related.mutable(strict=False)
class ModelSuiteConfig(BaseConfigClass):
    """
    Class for parsing general information about the model suite and also further information
    in respective hierarchy
    """

    model_configs: List[ModelConfig] = related.SequenceField(cls=ModelConfig)
