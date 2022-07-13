import argparse
import sys
import warnings
from argparse import HelpFormatter, Namespace
from collections import defaultdict
from logging import getLogger
from pathlib import Path
from typing import Dict, List, Sequence, Text, Type, Union, TypeVar, Generic, Optional

from pydantic import BaseModel

from mixsim.config import cfgparsing
from mixsim.config.help_formatter import SimpleHelpFormatter
from mixsim.config.parsers import decoding
from mixsim.config.utils import CONFIG_ARG, flatten, deflatten
from mixsim.config.wrappers.dataclass_wrapper import DataclassWrapper

logger = getLogger(__name__)

T = TypeVar('T')


class ArgumentParser(Generic[T], argparse.ArgumentParser):
    def __init__(
        self,
        config_class: Type[T],
        config_path: Optional[str] = None,
        formatter_class: Type[HelpFormatter] = SimpleHelpFormatter,
        *args,
        **kwargs,
    ):
        """ Creates an ArgumentParser instance. """
        kwargs["formatter_class"] = formatter_class
        super().__init__(*args, **kwargs)

        # Constructor arguments for the dataclass instances.
        # (a Dict[dest, [attribute, value]])
        self.constructor_arguments: Dict[str, Dict] = defaultdict(dict)

        self._wrappers: List[DataclassWrapper] = []

        self.config_path = config_path
        self.config_class = config_class

        self._assert_no_conflicts()
        self.add_argument(f'--{CONFIG_ARG}', type=str, help='Path for a config file to parse with MixSim')
        self.set_dataclass(config_class)

    def set_dataclass(
        self,
        dataclass: Union[Type[BaseModel], BaseModel],
        prefix: str = "",
        default: Union[BaseModel, Dict] = None,
        dataclass_wrapper_class: Type[DataclassWrapper] = DataclassWrapper,
    ):
        """ Adds command-line arguments for the fields of `dataclass`. """
        if not isinstance(dataclass, type):
            default = dataclass if default is None else default
            dataclass = type(dataclass)

        new_wrapper = dataclass_wrapper_class(dataclass, prefix=prefix, default=default)
        self._wrappers.append(new_wrapper)
        self._wrappers += new_wrapper.descendants

        for wrapper in self._wrappers:
            logger.debug(
                f"Adding arguments for dataclass: {wrapper.dataclass} "
                f"at destination {wrapper.dest}"
            )
            wrapper.add_arguments(parser=self)

    def _assert_no_conflicts(self):
        """ Checks for a field name that conflicts with utils.CONFIG_ARG"""
        if CONFIG_ARG in [k for k in self.config_class.__fields__]:
            raise NotImplementedError(f'{CONFIG_ARG} is a reserved word for MixSim')

    def parse_args(self, args=None, namespace=None) -> T:
        return super().parse_args(args, namespace)

    def parse_known_args(
        self,
        args: Sequence[Text] = None,
        namespace: Namespace = None,
        attempt_to_reorder: bool = False,
    ):
        # NOTE: since the usual ArgumentParser.parse_args() calls
        # parse_known_args, we therefore just need to overload the
        # parse_known_args method to support both.
        if args is None:
            # args default to the system args
            args = sys.argv[1:]
        else:
            # make sure that args are mutable
            args = list(args)

        if '--help' not in args:
            for action in self._actions:
                # TODO: Find a better way to do that?
                action.default = argparse.SUPPRESS  # To avoid setting of defaults in actual run
                action.type = str  # In practice, we want all processing to happen with yaml
        parsed_args, unparsed_args = super().parse_known_args(args, namespace)

        parsed_args = self._postprocessing(parsed_args)
        return parsed_args, unparsed_args

    def print_help(self, file=None):
        return super().print_help(file)

    def _postprocessing(self, parsed_args: Namespace) -> T:
        logger.debug("\nPOST PROCESSING\n")
        logger.debug(f"(raw) parsed args: {parsed_args}")

        parsed_arg_values = vars(parsed_args)

        for key in parsed_arg_values:
            parsed_arg_values[key] = cfgparsing.parse_string(parsed_arg_values[key])

        config_path = self.config_path  # Could be NONE

        if CONFIG_ARG in parsed_arg_values:
            new_config_path = parsed_arg_values[CONFIG_ARG]
            if config_path is not None:
                warnings.warn(
                    UserWarning(f'Overriding default {config_path} with {new_config_path}')
                )
            config_path = new_config_path
            del parsed_arg_values[CONFIG_ARG]

        if config_path is not None:
            file_args = cfgparsing.load_config(open(config_path, 'r'))
            file_args = flatten(file_args, sep='.')
            file_args.update(parsed_arg_values)
            parsed_arg_values = file_args

        deflatten_dict = deflatten(parsed_arg_values, sep='.')
        cfg = decoding.decode(self.config_class, deflatten_dict)

        return cfg


def parse(config_class: Type[T], config_path: Optional[Union[Path, str]] = None,
          args: Optional[Sequence[str]] = None) -> T:
    parser = ArgumentParser(config_class=config_class, config_path=config_path)
    return parser.parse_args(args)
