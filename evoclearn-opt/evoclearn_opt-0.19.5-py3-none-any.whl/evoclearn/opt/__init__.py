from os.path import dirname, abspath
from os.path import join as pjoin

from .version import __version__


from .cli import opt_simple


ETC_DIR = abspath(pjoin(dirname(__file__), "etc"))
SPEAKERS_DIR = pjoin(ETC_DIR, "speakers")
TEMPLATES_DIR = pjoin(ETC_DIR, "templates")

SPEAKERS = {"JD2", "boy3"}
