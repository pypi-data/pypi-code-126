# Standard library imports.
import datetime
import sys

# Local package imports.
from tsofa.views.snums._base import View as Base


class View(Base):

    # View to query for series data element numeric values.
    view = '/_design/snums_mn/_view/snums_mn/'

    # Define a string template for creating date keys with minute
    # resolution.
    dk_tmpl = '["%Y","%m","%d","%H","%M"]'

    # Define the minimum interval between reports in the database.
    delta = datetime.timedelta(minutes = 1)

    # Define the allowed intervals used to create a summary lister.
    intervals = ('days', 'hours', 'minutes',)


for k in View._export().items():
    setattr(sys.modules[globals()['__name__']], k[0], k[1])
