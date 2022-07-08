# Copyright 2021 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

import argparse
import logging
import os
import sys
from collections import OrderedDict
from typing import Any, Dict, List, Optional, Type, cast

import yaml
from related import from_yaml, to_model

from config_builder.BaseConfigClass import BaseConfigClass
from config_builder.replacement_map import (
    clear_replacement_map,
    get_replacement_map_copy,
    set_replacement_map_value,
    update_replacement_map_from_os,
)
from config_builder.utils import build_config_path
from config_builder.yaml_constructors import (
    join_object,
    join_object_from_config_dir,
    join_path,
    join_string,
    join_string_with_delimiter,
)

logger = logging.getLogger(__name__)


class ConfigBuilder:
    def __init__(
        self,
        class_type: Type[BaseConfigClass],
        configuration: Optional[BaseConfigClass] = None,
        yaml_config_path: Optional[str] = None,
        argparse_module_description: str = "",
        string_replacement_map: Optional[Dict[str, str]] = None,
        mutual_attribute_map: Optional[Dict[str, List[str]]] = None,
        no_checks: bool = False,
        use_argparse_fallback: bool = False,
    ):
        """
        Build a configuration object of the given class type. There are three options:

        - Take the given configuration object
        - Build a configuration object from the given yaml path
        - Build a configuration object by utilizing the argparse
          parameter "--yaml_config_path" and --replacement-config-path

        After a configuration object is build a post-processing takes place,
        consisting of two parts:

        1. Recursively check the class tree for mutual attributes that are defined via the
           parameter "mutual_attribute_map"

            mutual_attribute_map FORMAT:
                KEY = class for which to define mutual exclusive parameters
                VALUE = list of names of the attributes as strings

                Example:

                mutual_attribute_map = {
                    "KEY": ["ATTRIBUTE_1", "ATTRIBUTE_2"]
                }

        2. Recursively check any string attribute (including strings in lists and dictionaries),
           for placeholders (keys of the string_replacement_map) and replacement them
           (values of the string_replacement_map).

        Args:
            class_type: The type of the configuration object
            configuration: (Optional) An already existing configuration object
            yaml_config_path: (Optional) A yaml filepath where to build the configuration
                              object from
            argparse_module_description: (Optional) In case the ConfigBuilder is used as utility
                                         class to setup a program entry, a module description can
                                         be passed which will be used to setup an ArgumentParser.
            string_replacement_map: (Optional) That defines any string placeholders which can
                                    be used in string attributes
            mutual_attribute_map: (Optional) Dictionary that states mutual exclusive attributes
            no_checks: Whether the configuration object should be checked for mutual exclusiveness
                       and the "check_values" method for each attribute of the supertype
                       "BaseConfigClass" should be called
            use_argparse_fallback: Whether to parse commandline parameters as fallback when no
                                   path or configuration object is given
        """

        self.class_type = class_type
        self.yaml_config_path: Optional[str] = yaml_config_path
        self.string_replacement_map = string_replacement_map
        self.mutual_attribute_map = mutual_attribute_map
        self.no_checks = no_checks

        self.args: Optional[argparse.Namespace] = None

        # The build of a configuration object should not be affected from any side effect,
        # therefore clear the global replacement map before each run
        clear_replacement_map()

        ConfigBuilder.__update_replacement_map(
            string_replacement_map=self.string_replacement_map
        )

        if configuration is None:
            if self.yaml_config_path is None and use_argparse_fallback:
                # Set up the argparse parser, so that it can be used afterwards
                self.parser = self._setup_argparse(
                    argparse_module_description=argparse_module_description,
                    add_argparse_parameters=self._add_argparse_parameters,
                )

                # neither a yaml config object nor a path to a config-file is given,
                # try to build yaml config based on the given file-path from argparse
                self.args = self.parser.parse_args()

                logger.info(f"Parsed arguments from command-line: {self.args}")

                ConfigBuilder.__update_placeholder_from_argparse(args=self.args)

                self.yaml_config_path = self.args.yaml_config_path

                ConfigBuilder.__update_replacement_map(
                    string_replacement_map=self.__parse_replacement_map(
                        replacement_config_path=self.args.replacement_config_path
                    )
                )

            if self.yaml_config_path is None:
                raise ValueError(
                    "Cannot build a config. Both, the configuration object"
                    " and yaml_config_path are None"
                )

            logger.debug("Update placeholder values from OS environment variables")
            update_replacement_map_from_os()

            self.yaml_config_path = ConfigBuilder.__prepare_yaml_path(
                yaml_config_path=self.yaml_config_path,
                string_replacement_map=self.string_replacement_map,
            )

            configuration = ConfigBuilder.__build_from_yaml(
                yaml_config_path=self.yaml_config_path,
                class_type=self.class_type,
            )

        self.configuration: BaseConfigClass = self.__postprocess_config(
            configuration=configuration
        )

    @staticmethod
    def __parse_replacement_map(
        replacement_config_path: Optional[str],
    ) -> Optional[Dict[str, str]]:

        if replacement_config_path is None:
            logger.warning(
                "The replacement_config_path is None, string replacement will not be available!"
            )
            return None

        if not os.path.isfile(replacement_config_path):
            logger.warning(
                "The given replacement_config_path does not exist: %s, "
                "string replacement will not be available!" % replacement_config_path
            )
            return None

        logger.info("Load replacement-map from: %s" % replacement_config_path)
        with open(
            file=replacement_config_path, mode="r", encoding="utf8"
        ) as config_file:
            return cast(
                Dict[str, str], yaml.load(stream=config_file, Loader=yaml.Loader)
            )

    @staticmethod
    def __update_replacement_map(
        string_replacement_map: Optional[Dict[str, str]],
    ) -> None:

        if string_replacement_map is not None:
            logger.debug("Update placeholder values from given string replacement map")
            for key, value in string_replacement_map.items():
                set_replacement_map_value(key=key, value=value)

    @staticmethod
    def __prepare_yaml_path(
        yaml_config_path: str, string_replacement_map: Optional[Dict[str, str]]
    ) -> str:
        if not os.path.isfile(yaml_config_path):
            if string_replacement_map is not None:
                logger.debug(
                    f"Given config-path does not exist: {yaml_config_path}. "
                    f"These placeholder keys will be used for trying to build a "
                    f"valid path: {string_replacement_map.keys()}"
                )

                yaml_config_path = build_config_path(
                    config_path=yaml_config_path,
                    string_replacement_map=string_replacement_map,
                )

            if not os.path.isfile(yaml_config_path):
                raise ValueError(
                    f"Given config-path does not exist: {yaml_config_path}"
                )

        return yaml_config_path

    @staticmethod
    def __build_from_yaml(
        yaml_config_path: str,
        class_type: Type[BaseConfigClass],
    ) -> BaseConfigClass:
        """
        Build a configuration object of the given type from the given yaml filepath.

        Args:
            yaml_config_path: The yaml filepath where to build the configuration object from
            class_type: The type of the configuration object

        Returns:
            The build configuration object
        """

        logger.info(
            f"Build config for class type '{class_type}' "
            f"from config path '{yaml_config_path}'"
        )

        if not os.path.isfile(yaml_config_path):
            raise ValueError(
                f"Config file path does not exist. The given path is: {yaml_config_path}"
            )

        with open(yaml_config_path, encoding="utf8") as yaml_file:
            original_yaml = yaml_file.read().strip()

        # register the tag handler
        yaml.add_constructor("!join_string", join_string)
        yaml.add_constructor("!join_string_with_delimiter", join_string_with_delimiter)
        yaml.add_constructor("!join_path", join_path)
        yaml.add_constructor("!join_object", join_object)
        yaml.add_constructor(
            "!join_object_from_config_dir", join_object_from_config_dir
        )

        yml_dict = from_yaml(
            yaml_package=yaml, stream=original_yaml, loader_cls=yaml.Loader
        )

        ConfigBuilder.__recursive_check_dict(yml_dict=yml_dict)

        configuration: BaseConfigClass = to_model(class_type, yml_dict)

        return configuration

    def __postprocess_config(self, configuration: BaseConfigClass) -> BaseConfigClass:

        # Ensure that the 'configuration' object has all attributes from BaseConfigClass
        # NOTE: Related does not instantiate any attributes besides the ones that are
        #       marked as "related" attributes
        for key, value in BaseConfigClass().__dict__.items():
            if not hasattr(configuration, key):
                setattr(configuration, key, value)

        # run recursive check and fill the update the globally defined replacement map
        configuration.recursive_check_mutuality_and_update_replacements(
            no_checks=self.no_checks,
            mutual_attribute_map=self.mutual_attribute_map
            if self.mutual_attribute_map is not None
            else {},
        )

        # Get values of OS environment variables for all values that are now part of
        # the globally defined replacement map
        update_replacement_map_from_os()

        # Replace any placeholder in strings that are part of the build config object
        configuration.recursive_string_replacement()

        # Save the replacement map that has been used to build this config object
        configuration.string_replacement_map.update(get_replacement_map_copy())

        if not self.no_checks:
            configuration.recursive_check_values()

            if not configuration.check_values():
                raise ValueError(
                    f"Check values for configuration class"
                    f"'{configuration.__class__}' failed!"
                )

        return configuration

    @staticmethod
    def _setup_argparse(
        argparse_module_description: str, add_argparse_parameters: Any
    ) -> argparse.ArgumentParser:
        """
        Init an argparse instance for the config-builder.
        Use the default or provided description for the help message.

        Returns:
             The created parser instance
        """

        if argparse_module_description == "":
            parser = argparse.ArgumentParser(
                prog=sys.argv[0], description="Load annotation in a variety of formats."
            )
        else:
            parser = argparse.ArgumentParser(
                prog=sys.argv[0], description=argparse_module_description
            )

        yaml_config_path_option = "yaml-config-path"
        replacement_config_path_option = "replacement-config-path"
        log_dir_option = "log-dir"
        log_level_option = "log-level"

        options = [
            item
            for sublist in [a.option_strings for a in parser._actions]
            for item in sublist
        ]

        if yaml_config_path_option not in options:
            parser.add_argument(
                "-c",
                f"--{yaml_config_path_option}",
                help="Load all parameters from the given yaml configuration file",
                type=str,
            )

        if replacement_config_path_option not in options:
            parser.add_argument(
                f"--{replacement_config_path_option}",
                help="Path to the string replacement map that defines "
                "placeholders for YAML configuration files",
                type=str,
            )

        if log_dir_option not in options:
            parser.add_argument(
                f"--{log_dir_option}",
                help="Directory where log-files should be written to",
                type=str,
            )

        if log_level_option not in options:
            parser.add_argument(
                f"--{log_level_option}",
                help="Define the logging level",
                type=str,
                default=logging.INFO,
                choices=logging._nameToLevel.keys(),
            )

        for key in get_replacement_map_copy().keys():
            parser.add_argument(
                f"--{key}",
                help=f"'{key}': os environment variable, "
                f"which can be used as placeholder",
                type=str,
                default=None,
            )

        add_argparse_parameters(parser)

        return parser

    @staticmethod
    def _add_argparse_parameters(
        parser: argparse.ArgumentParser,
    ) -> None:
        """
        This method should be used by subclasses to define extra
        arguments for the ArgumentParser instance

        Args:
            parser: The parser instance where to add parameters
        """
        pass

    @staticmethod
    def __update_placeholder_from_argparse(args: argparse.Namespace) -> None:

        args_dict = vars(args)

        for os_replacement_key in get_replacement_map_copy().keys():
            if (
                os_replacement_key in args_dict
                and args_dict[os_replacement_key] is not None
            ):
                set_replacement_map_value(
                    key=os_replacement_key, value=args_dict[os_replacement_key]
                )

    @staticmethod
    def __recursive_check_dict(yml_dict: OrderedDict) -> None:  # type: ignore
        """
        Check the dictionary that has been parsed by a from_yaml(stream=original_yaml),
        whether there have been failures while reading configs
        from file-paths. This indicates either a real wrong configured
        path or that some OS replacements haven't been configured.

        :param yml_dict: OrderedDict parsed from via "from_yaml(stream=original_yaml)"
        :return: None
        """

        for key, value in yml_dict.items():
            if isinstance(value, OrderedDict):
                ConfigBuilder.__recursive_check_dict(yml_dict=value)
            else:
                if "FileNotFoundError" in key:
                    raise FileNotFoundError(value)
