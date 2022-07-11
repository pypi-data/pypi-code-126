# Standard library imports.
import sys

# Local package imports.
from tsofa.views._base_dy import MixInDy
from tsofa.views.sdocs._base import View as Base


class View(MixInDy, Base):

    # View to query for series data documents.
    view = '/_design/sdocs_dy/_view/sdocs_dy/'


for k in View._export().items():
    setattr(sys.modules[globals()['__name__']], k[0], k[1])
