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
"""Module containing all outliers algorithms used in the library."""
from typing import Tuple

import numpy as np
import pandas as pd

from runml_checks.core.errors import runml_checksValueError, NotEnoughSamplesError


def iqr_outliers_range(data: np.ndarray,
                       iqr_range: Tuple[int, int],
                       scale: float,
                       min_samples: int = 10) -> Tuple[float, float]:
    """Calculate outliers range on the data given using IQR.

    Parameters
    ----------
    data: np.ndarray
        Data to calculate outliers range for.
    iqr_range: Tuple[int, int]
        Two percentiles which define the IQR range
    scale: float
        The scale to multiply the IQR range for the outliers detection
    min_samples : int, default: 10
        Minimum number of samples needed to calculate outliers
    Returns
    -------
    Tuple[float, float]
        Tuple of lower limit and upper limit of outliers range
    """
    if len(iqr_range) != 2 or any((x < 0 or x > 100 for x in iqr_range)) or all(x < 1 for x in iqr_range):
        raise runml_checksValueError('IQR range must contain two numbers between 0 to 100')

    data = data.squeeze()
    # Filter nulls
    data = [x for x in data if pd.notnull(x)]
    if len(data) < min_samples:
        raise NotEnoughSamplesError(f'Need at least {min_samples} non-null samples to calculate IQR outliers, but got '
                                    f'{len(data)}')

    q1, q3 = np.percentile(data, sorted(iqr_range))
    iqr = q3 - q1
    low_lim = q1 - scale * iqr
    up_lim = q3 + scale * iqr

    return low_lim, up_lim
