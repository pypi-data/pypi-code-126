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
"""Utils module with methods for fast calculations."""
import numpy as np


def fast_sum_by_row(matrix: np.ndarray) -> np.array:
    """Faster alternative to np.sum(matrix, axis=1)."""
    return np.matmul(matrix, np.ones(matrix.shape[1]))
