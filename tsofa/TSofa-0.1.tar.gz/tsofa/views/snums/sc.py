# Standard library imports.
import sys

# Local package imports.
from tsofa.views.snums._base import View as Base


class View(Base):

    # View to query for series data element numeric values.
    view = '/_design/snums_sc/_view/snums_sc/'


for k in View._export().items():
    setattr(sys.modules[globals()['__name__']], k[0], k[1])
