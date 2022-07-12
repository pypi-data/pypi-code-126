# -*- coding: utf8 -*-
import math


def sec2time(seconds: int):
    """
    秒转时间

    :param seconds: 秒
    :return

    >>> sec2time(60)
        00:01:00
    >>> sec2time(60*60)
        01:00:00
    >>> sec2time(60*60*24)
        1 days, 00:00:00
    """

    seconds = 0 if seconds < 0 else math.ceil(seconds)

    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)

    if d == 0:
        return '%02d:%02d:%02d' % (h, m, s)

    return '%d days, %02d:%02d:%02d' % (d, h, m, s)
