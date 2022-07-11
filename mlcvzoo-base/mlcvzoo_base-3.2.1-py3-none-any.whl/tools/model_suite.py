# Copyright 2021 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""Module for working with different models at once"""
import logging
import os
import typing
from typing import Dict, List, Optional

from config_builder.ConfigBuilder import ConfigBuilder

from mlcvzoo_base.api.interfaces import Trainable
from mlcvzoo_base.api.model import ConfigurationType, DataType, Model, PredictionType
from mlcvzoo_base.configuration.model_suite_config import ModelSuiteConfig
from mlcvzoo_base.models.model_registry import ModelRegistry
from mlcvzoo_base.tools.logger import Logger
from mlcvzoo_base.utils import get_project_path_information

logger = logging.getLogger(__name__)


class ModelSuite(ConfigBuilder):
    """Class to run overall evaluation or training on different models"""

    config: ModelSuiteConfig

    models: List[Model[PredictionType, ConfigurationType, DataType]] = list()  # type: ignore

    def __init__(
        self,
        yaml_config_path: Optional[str] = None,
        configuration: Optional[ModelSuiteConfig] = None,
        string_replacement_map: Optional[Dict[str, str]] = None,
        mutual_attribute_map: Optional[Dict[str, List[str]]] = None,
        no_checks: bool = False,
    ):
        ConfigBuilder.__init__(
            self,
            class_type=ModelSuiteConfig,
            configuration=configuration,
            yaml_config_path=yaml_config_path,
            argparse_module_description="Run training for given model configurations",
            string_replacement_map=string_replacement_map,
            mutual_attribute_map=mutual_attribute_map,
            no_checks=no_checks,
        )

        self.config = typing.cast(ModelSuiteConfig, self.configuration)

        self.model_registry = ModelRegistry()

        logger.info("Initialized")

    def run_training(self) -> None:
        """Runs the training with each of the models in the models attribute"""

        for model_config in self.config.model_configs:

            model: Model[PredictionType, ConfigurationType, DataType]  # type: ignore
            model = self.model_registry.init_model(
                model_config=model_config,
                string_replacement_map=self.string_replacement_map,
            )

            if isinstance(model, Trainable):
                model.train()  # TODO: put data_stream here?


def main() -> None:

    _, project_root, _ = get_project_path_information(
        file_path=__file__, dir_depth=3, code_base="mlcvzoo_base"
    )

    Logger.init_logging_basic(
        log_dir=os.path.join(project_root, "logs"),
        log_file_postfix="ModelSuite",
        no_stdout=False,
        root_log_level=logging.DEBUG,
        file_log_level=logging.DEBUG,
        stdout_log_level=logging.INFO,
    )

    model_suite = ModelSuite()

    model_suite.run_training()


if __name__ == "__main__":
    main()
