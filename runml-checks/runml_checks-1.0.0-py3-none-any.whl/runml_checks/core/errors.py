# ----------------------------------------------------------------------------
# Copyright (C) 2021-2022 runml_checks (https://www.runml_checks.com)
#
# This file is part of runml_checks.
# runml_checks is distributed under the terms of the GNU Affero General
# Public License (version 3 or later).
# You should have received a copy of the GNU Affero General Public License
# along with runml_checks.  If not, see <http://www.gnu.org/licenses/>.
# ----------------------------------------------------------------------------
#
"""Module with all runml_checks error types."""

__all__ = ['runml_checksValueError', 'runml_checksNotSupportedError', 'runml_checksProcessError',
           'NumberOfFeaturesLimitError', 'DatasetValidationError', 'ModelValidationError',
           'runml_checksNotImplementedError', 'ValidationError', 'runml_checksBaseError', 'NotEnoughSamplesError',
           'runml_checksTimeoutError']


class runml_checksBaseError(Exception):
    """Base exception class for all 'runml_checks' error types."""

    def __init__(self, message: str, html: str = None):
        super().__init__(message)
        self.message = message
        self.html = html or message


class runml_checksValueError(runml_checksBaseError):
    """Exception class that represent a fault parameter was passed to runml_checks."""

    pass


class runml_checksNotImplementedError(runml_checksBaseError):
    """Exception class that represent a function that was not implemnted."""

    pass


class runml_checksNotSupportedError(runml_checksBaseError):
    """Exception class that represents an unsupported action in runml_checks."""

    pass


class runml_checksProcessError(runml_checksBaseError):
    """Exception class that represents an issue with a process."""

    pass


class NumberOfFeaturesLimitError(runml_checksBaseError):
    """Represents a situation when a dataset contains too many features to be used for calculation."""

    pass


class runml_checksTimeoutError(runml_checksBaseError):
    """Represents a situation when a computation takes too long and is interrupted."""

    pass


class ValidationError(runml_checksBaseError):
    """Represents more specific case of the ValueError (runml_checksValueError)."""

    pass


class DatasetValidationError(runml_checksBaseError):
    """Represents unappropriate Dataset instance.

    Should be used in a situation when a routine (like check instance, utility function, etc)
    expected and received a dataset instance that did not meet routine requirements.
    """

    pass


class ModelValidationError(runml_checksBaseError):
    """Represents unappropriate model instance.

    Should be used in a situation when a routine (like check instance, utility function, etc)
    expected and received a dataset instance that did not meet routine requirements.
    """

    pass


class NotEnoughSamplesError(runml_checksBaseError):
    """Represents a failure in calculation due to insufficient amount of samples."""

    pass
