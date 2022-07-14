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
"""Contain functions for configuring the runml_checks logger."""
import logging

__all__ = ['get_logger', 'get_verbosity', 'set_verbosity']

_logger = logging.getLogger('runml_checks')

_stream_handler = logging.StreamHandler()
_stream_handler.setLevel(logging.INFO)
_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
_stream_handler.setFormatter(_formatter)
_logger.addHandler(_stream_handler)  # for some reason kaggle needs it
_logger.setLevel(logging.INFO)


def get_logger() -> logging.Logger:
    """Retutn the runml_checks logger."""
    return _logger


def get_verbosity() -> int:
    """Return the runml_checks logger verbosity level.

    Same as doing logging.getLogger('runml_checks').getEffectiveLevel().
    """
    return _logger.getEffectiveLevel()


def set_verbosity(level: int):
    """Set the runml_checks logger verbosity level.

    Same as doing logging.getLogger('runml_checks').setLevel(level).
    Control the package wide log level and the progrees bars - progress bars are level INFO.

    Examples
    --------
    >>> import logging
    >>> import runml_checks

    >>> # will disable progress bars
    >>> runml_checks.set_verbosity(logging.WARNING)
    >>> # will disable also any warnings runml_checks print
    >>> runml_checks.set_verbosity(logging.ERROR)
    """
    _logger.setLevel(level)
