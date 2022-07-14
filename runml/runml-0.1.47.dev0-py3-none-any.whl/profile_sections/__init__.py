import warnings

import runml.model_profile.sections
from runml.model_profile.sections import *

__path__ = runml.model_profile.sections.__path__  # type: ignore

warnings.warn("'import runml.profile_sections' is deprecated, use 'import runml.model_profile.sections'")
