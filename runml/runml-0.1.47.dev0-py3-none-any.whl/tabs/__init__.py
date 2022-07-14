import warnings

import runml.dashboard.tabs
from runml.dashboard.tabs import *

__path__ = runml.dashboard.tabs.__path__  # type: ignore

warnings.warn("'import runml.tabs' is deprecated, use 'import runml.dashboard.tabs'")
