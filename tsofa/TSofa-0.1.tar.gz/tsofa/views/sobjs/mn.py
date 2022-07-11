# Standard library imports.
import sys

# Local package imports.
from tsofa.views._base import View as Base


class View(Base):

    # View to query for series special values.
    view = '/_design/sobjs_mn/_view/sobjs_mn/'

    # Define a string template for creating date keys with minute
    # resolution.
    dk_tmpl = '["%Y","%m","%d","%H","%M"]'


for k in View._export().items():
    setattr(sys.modules[globals()['__name__']], k[0], k[1])
