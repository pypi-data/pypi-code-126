# Copyright 2021 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""
The CustomBlockModel configures the model for training and inference.
The respective model is compiled from the provided configuration file and net class.
Input data classes are parsed via the AnnotationClassMapper.
Data flow is regulated via Generators.
"""

import logging
import typing
from typing import Dict, Optional

import numpy as np
from mlcvzoo_base.configuration.utils import (
    create_configuration as create_basis_configuration,
)

from mlcvzoo_tf_classification.base_model import BaseModel
from mlcvzoo_tf_classification.custom_block.configuration import CustomBlockConfig
from mlcvzoo_tf_classification.custom_block.net import CustomBlockNet

logger = logging.getLogger(__name__)


class CustomBlockModel(
    BaseModel[CustomBlockConfig, CustomBlockNet],
):
    """
    The model is compiled from the respective net class and configuration file.
    Input details are parsed using the AnnotationClassMapper.
    """

    def __init__(
        self,
        from_yaml: str,
        configuration: Optional[CustomBlockConfig] = None,
        string_replacement_map: Optional[Dict[str, str]] = None,
    ):
        BaseModel.__init__(
            self,
            net_type=CustomBlockNet,
            from_yaml=from_yaml,
            configuration=configuration,
            string_replacement_map=string_replacement_map,
        )

    @staticmethod
    def create_configuration(
        from_yaml: Optional[str] = None,
        configuration: Optional[CustomBlockConfig] = None,
        string_replacement_map: Optional[Dict[str, str]] = None,
    ) -> CustomBlockConfig:
        return typing.cast(
            CustomBlockConfig,
            create_basis_configuration(
                configuration_class=CustomBlockConfig,
                from_yaml=from_yaml,
                input_configuration=configuration,
                string_replacement_map=string_replacement_map,
            ),
        )

    @staticmethod
    def preprocess_data(input_data: np.ndarray) -> np.ndarray:
        return input_data
