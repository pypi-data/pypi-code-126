"""Functions as the behave runner for the NS Behave CLI"""
import logging as logger
import os
from pathlib import Path
import sys
from typing import List
import warnings

from behave.__main__ import main as behave_main
from behave.runner import ContextMaskWarning

from .constants import PACKAGE_ROOT


class BehaveRunner:
    """Overrides the behave runner and gives an entry-point to the CLI"""

    @staticmethod
    def run_behave(test_package: str, args: List[str]) -> None:
        """Run a behave test based on a list of args that are passed into the behave configuration

        Args:
            test_package: The test package that contains feature files
            args: a list of behave configuration arguments

        """
        # Change our running directory to the repo root plus the type of test
        feature_location = Path.joinpath(PACKAGE_ROOT, test_package)
        logger.info(
            f"Feature files are located in: {feature_location}. Changing DIR and starting the runner."
        )
        os.chdir(feature_location)
        # Do the deed, but ignore `ContextMaskWarning` from behave
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=ContextMaskWarning)
            exit_code = behave_main(args)
            sys.exit(exit_code)
