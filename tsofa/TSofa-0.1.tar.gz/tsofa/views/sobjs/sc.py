# Standard library imports.
import sys

# Local package imports.
from tsofa.views._base import View as Base


class View(Base):

    # View to query for series special values.
    view = '/_design/sobjs_sc/_view/sobjs_sc/'


for k in View._export().items():
    setattr(sys.modules[globals()['__name__']], k[0], k[1])
