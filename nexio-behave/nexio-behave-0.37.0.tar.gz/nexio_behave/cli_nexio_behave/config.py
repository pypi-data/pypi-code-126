"""Represents a behave config object in the ns behave cli"""
import logging as logger
from typing import Generator, List

# Global variables
SUPPORTED_ENVS = ["functional", "prod"]


class BehaveConfig:
    """Behave config object class"""

    def __init__(
        self,
        test_name: str,
        environment: str,
        common_app: bool,
        stack_name: str,
        debug: bool,
        browser: str = None,
        tags: str = None,
        max_attempts: int = None,
        default_timeout: int = None,
        latency: int = None,
        file_pattern: str = None,
        files: str = None,
        test_report_dir: str = None,
    ):
        """Object used to pass behave cli args to the behave configuration object in the behave runner

        Args:
            test_name: The name of the test we are running
            environment:  The test environment
            common_app: Use the common salesforce app when testing?
            stack_name: (optional) The stack name to run tests on
            debug: Debug mode
            browser: The browser to run tests against
            tags: The tags to run
            max_attempts: The max attempts a scenario should retry if a failure takes place
            default_timeout: The selenium default wait timeout
            latency: Browser latency in seconds
            file_pattern: File pattern of feature files to run
            files: The file glob to run (CCI mode only)
            test_report_dir: The directory where to store all test results (json and junit)

        """
        self.browser = f"-Dbrowser={browser}" if browser else None
        self.color = None
        self.common_app = (
            "-Duse_common_sf_app=True" if common_app else "-Duse_common_sf_app=False"
        )
        self.debug = "--logging-level DEBUG" if debug else "--logging-level INFO"
        self.default_timeout = (
            f"-Ddefault_timeout={default_timeout}" if default_timeout else None
        )
        self.environment = (
            f"-Denvironment={stack_name}"
            if environment in SUPPORTED_ENVS
            else f"-Denvironment={environment}"
        )
        self.files = files.replace(",", " ") if files else None
        self.junit = "--junit" if test_report_dir else None
        self.junit_directory = (
            f"--junit-directory {test_report_dir}/{test_name}"
            if test_report_dir
            else None
        )
        self.latency = f"-Dlatency={latency}" if latency else None
        self.max_attempts = f"-Dmax_attempts={max_attempts}" if max_attempts else None
        self.phrase = f"-i {file_pattern}" if file_pattern else None
        self.stop = None

        # set up tags for all tags passed in
        _tags = ""
        if tags:
            # Create the tags string expression. Do not forget the space after each tag.
            for tag in tags.split(" "):
                _tags += f"-t {tag} "
            self.tags = _tags.rstrip()
        else:
            self.tags = None

        self.verbose = None

        # Environment specific args.
        if environment == "ci":
            self.color = "--no-color"
            self.verbose = "--verbose"
            self.stop = "--stop"
        elif environment in SUPPORTED_ENVS:
            self.color = "--no-color"
            self.stop = "--stop"
            self.verbose = "--verbose"

    def __iter__(self) -> Generator:
        """Magic method that sets up an iterator over attributes in this class"""
        yield self.browser
        yield self.color
        yield self.common_app
        yield self.debug
        yield self.default_timeout
        yield self.environment
        yield self.junit
        yield self.junit_directory
        yield self.latency
        yield self.max_attempts
        yield self.phrase
        yield self.stop
        yield self.tags
        yield self.verbose
        yield self.files

    def to_args(self) -> List[str]:
        """Create a list of string args that can be passed to the behave configuration object

        Returns:
            List of string args

        """
        logger.info("Generating behave args from config objects")
        args = []
        for arg in self:
            if type(arg) == List or type(arg) == tuple:
                for sub_arg in arg:
                    args.append(sub_arg)
            elif type(arg) == str:
                arg = arg.split()
                for sub_arg in arg:
                    args.append(sub_arg)
            elif arg is None:
                continue
            else:
                args.append(arg)
        logger.info(f"Behave args passed to behave: {args}")
        return args
