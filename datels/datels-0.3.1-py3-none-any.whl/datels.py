from datetime import datetime, timedelta

import numpy as np


def list_dates(start, end, inclusive="both", freq="D", format=None, sep=None):
    if freq != "D":
        raise NotImplementedError("datels only support date-based frequency.")

    if start > end:
        raise ValueError("start date > end date")

    start = datetime.strptime(start, "%Y-%m-%d")
    end = datetime.strptime(end, "%Y-%m-%d")

    if inclusive == "both" or start == end:
        end = end + timedelta(days=1)
    elif inclusive == "left":
        pass
    elif inclusive == "right":
        start = start + timedelta(days=1)
        end = end + timedelta(days=1)

    if format is None:
        if sep is None:
            sep = "/"
        format = sep.join(("%Y", "%m", "%d"))

    arr = np.arange(start, end, timedelta(days=1)).astype(datetime)
    return np.vectorize(lambda d: d.strftime(format))(arr).tolist()
