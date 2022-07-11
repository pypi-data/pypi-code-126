# Standard library imports.
import datetime
import sys

# Local package imports.
from tsofa.views._base_dy import MixInDy
from tsofa.views.snums._base import View as Base


class View(MixInDy, Base):

    # View to query for series data element numeric values.
    view = '/_design/snums_dy/_view/snums_dy/'

    # Define the minimum interval between reports in the database.
    delta = datetime.timedelta(days = 1)

    # Define the allowed intervals used to create a summary lister.
    intervals = ('days',)


for k in View._export().items():
    setattr(sys.modules[globals()['__name__']], k[0], k[1])
