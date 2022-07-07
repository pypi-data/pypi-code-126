from flit_core import buildapi # Make Flit's build backend available as "flit_scm:buildapi"
from setuptools_scm import get_version

try:
    import tomllib
except ImportError:
    import tomli as tomllib


try:
    with open('pyproject.toml', 'rb') as f:
        pyproject = tomllib.load(f)
except OSError:
    pass # Do nothing if unable to access `pyproject.toml`
else:
    try:
        setuptools_scm_config = pyproject['tool']['setuptools_scm']
    except KeyError:
        pass # Do nothing if `setuptools_scm` is not configured in `pyproject.toml`
    else:
        get_version(**setuptools_scm_config)


# Import the version after writing the version file, to allow for bootstrapping
from ._version import version as __version__
