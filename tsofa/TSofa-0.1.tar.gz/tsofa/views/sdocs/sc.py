# Standard library imports.
import sys

# Local package imports.
from tsofa.views.sdocs._base import View as Base


class View(Base):

    # View to query for series data documents.
    view = '/_design/sdocs_sc/_view/sdocs_sc/'


for k in View._export().items():
    setattr(sys.modules[globals()['__name__']], k[0], k[1])
