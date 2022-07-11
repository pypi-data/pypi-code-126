# Standard library imports.
import datetime
import sys

# Local package imports.
from tsofa.views.snums._base import View as Base


class View(Base):

    # View to query for series data element numeric values.
    view = '/_design/snums_hr/_view/snums_hr/'

    # Define a string template for creating date keys with hourly
    # resolution.
    dk_tmpl = '["%Y","%m","%d","%H"]'

    # Define the minimum interval between reports in the database.
    delta = datetime.timedelta(hours = 1)

    # Define the allowed intervals used to create a summary lister.
    intervals = ('days',)


for k in View._export().items():
    setattr(sys.modules[globals()['__name__']], k[0], k[1])
