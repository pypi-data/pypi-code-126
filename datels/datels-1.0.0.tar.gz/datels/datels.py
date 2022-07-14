from datetime import datetime, timedelta
from typing import List, Optional

import numpy as np


def list_dates(
    start: str,
    end: str,
    inclusive: str = "both",
    freq: str = "D",
    format: Optional[str] = None,
    sep: Optional[str] = None,
) -> List[str]:
    if freq != "D":
        raise NotImplementedError("datels only support date-based frequency.")

    if start > end:
        raise ValueError("startdate > enddate")

    startdate = datetime.strptime(start, "%Y-%m-%d")
    enddate = datetime.strptime(end, "%Y-%m-%d")

    if inclusive == "both" or start == end:
        enddate = enddate + timedelta(days=1)
    elif inclusive == "left":
        pass
    elif inclusive == "right":
        startdate = startdate + timedelta(days=1)
        enddate = enddate + timedelta(days=1)

    if format is None:
        if sep is None:
            sep = "/"
        format = sep.join(("%Y", "%m", "%d"))

    arr = np.arange(startdate, enddate, timedelta(days=1)).astype(datetime)
    return np.vectorize(lambda d: d.strftime(format))(arr).tolist()
