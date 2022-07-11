# Copyright 2021 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""
Central module for handling the download and upload
of zip files to CVAT via their commandline interface
"""

import argparse
import logging
import typing
from typing import Dict, List, Optional

from config_builder.ConfigBuilder import ConfigBuilder

from mlcvzoo_base.configuration.utils import handle_value_error_for_tool_configuration
from mlcvzoo_base.data_preparation.cvat_annotation_handler.configuration import (
    CVATAnnotationHandlerConfig,
)
from mlcvzoo_base.data_preparation.cvat_annotation_handler.cvat_dumper import CVATDumper
from mlcvzoo_base.data_preparation.cvat_annotation_handler.cvat_uploader import (
    PascalVOCUploader,
)

logger = logging.getLogger(__name__)


class CVATAnnotationHandler(ConfigBuilder):
    """
    Central class for handling the download and upload
    of zip files to CVAT via their commandline interface
    """

    argparse_description: str = "Download and upload annotation files from/to CVAT"

    def __init__(
        self,
        yaml_config_path: Optional[str] = None,
        configuration: Optional[CVATAnnotationHandlerConfig] = None,
        string_replacement_map: Optional[Dict[str, str]] = None,
        mutual_attribute_map: Optional[Dict[str, List[str]]] = None,
        no_checks: bool = False,
    ):
        """
        Instantiates a CVATAnnotationHandler object
        Args:
            yaml_config_path: (Optional) A yaml filepath where to build the configuration
                               object from
            configuration: (Optional) An already existing configuration object
            string_replacement_map: A dictionary that defines placeholders which can be used
                                    while parsing the file. They can be understood as variables
                                    that can be used to define configs that are valid across
                                    multiple devices.
            mutual_attribute_map: (DEPRECATED)
            no_checks: Whether the configuration object should be checked for mutual exclusiveness
                       and the "check_values" method for each attribute of the supertype
                       "BaseConfigClass" should be called
        """

        try:
            ConfigBuilder.__init__(
                self,
                class_type=CVATAnnotationHandlerConfig,
                configuration=configuration,
                yaml_config_path=yaml_config_path,
                argparse_module_description=CVATAnnotationHandler.argparse_description,
                string_replacement_map=string_replacement_map,
                no_checks=no_checks,
                use_argparse_fallback=True,
            )

            self.configuration: CVATAnnotationHandlerConfig = typing.cast(  # type: ignore
                CVATAnnotationHandlerConfig,
                self.configuration,
            )
        except ValueError as value_error:
            handle_value_error_for_tool_configuration(
                value_error=value_error, config_builder_instance=self
            )
            raise value_error

    @staticmethod
    def setup_argparse() -> argparse.ArgumentParser:
        return ConfigBuilder._setup_argparse(
            argparse_module_description=CVATAnnotationHandler.argparse_description,
            add_argparse_parameters=CVATAnnotationHandler._add_argparse_parameters,
        )

    def download_all_tasks(self) -> None:
        """
        Execute all downloads that are specified in the configuration object
        of this class

        Returns:
            None
        """

        for dump_task_config in self.configuration.dump_task_configs:
            CVATDumper.dump_task_data(
                dump_task_config=dump_task_config,
                cvat_cli_config=self.configuration.cvat_cli_config,
                disable_ssl_verify=self.configuration.cvat_cli_config.disable_ssl_verify,
            )
            logger.info("==========  DUMP TASK FINISHED  ==========\n")

    def upload_all_tasks(self) -> None:
        """
        Execute all uploads that are specified in the configuration object
        of this class

        Returns:
            None
        """

        for upload_task_config in self.configuration.upload_task_configs:
            PascalVOCUploader.upload_task_data(
                upload_task_config=upload_task_config,
                cvat_cli_config=self.configuration.cvat_cli_config,
                disable_ssl_verify=self.configuration.cvat_cli_config.disable_ssl_verify,
            )
            logger.info("==========  UPLOAD TASK FINISHED  ==========\n")

    def run(self) -> None:
        """
        Execute all downloads and uploads that are specified in the configuration object
        of this class

        Returns:
            None
        """

        logger.info("Start to download and upload tasks")

        self.download_all_tasks()
        self.upload_all_tasks()

        logger.info("Finished to download and upload tasks")
