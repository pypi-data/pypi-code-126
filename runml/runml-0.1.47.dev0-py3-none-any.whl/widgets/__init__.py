import warnings

import runml.dashboard.widgets
from runml.dashboard.widgets import *

__path__ = runml.dashboard.widgets.__path__  # type: ignore

warnings.warn("'import runml.widgets' is deprecated, use 'import runml.dashboard.widgets'")
