from os.path import dirname, abspath
from os.path import join as pjoin

from .version import __version__


# TODO: This data in the package needs to go away and speaker
# management needs to move to EVL-core
ETC_DIR = abspath(pjoin(dirname(__file__), "etc"))
SPEAKERS_DIR = pjoin(ETC_DIR, "speakers")
TEMPLATES_DIR = pjoin(ETC_DIR, "templates")

SPEAKERS = {"JD2", "boy3"}
