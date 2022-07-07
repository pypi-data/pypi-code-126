"""
    This program was written on July 2nd, 2022
    by Anji Wong (anzhi0708@hufs.ac.kr, anzhi0708@gmail.com),
    **for research use only.**

    Even through I tried to access KR Assembly data by
    using its Open API service,
    some critical data was missing in the returned json / xml string.

    So I had to manually write this web crawler.
    Hopefully this will help me finishing my paper.

    Since we are trying to keep sending http requests
    to the KR Assembly website,
    we have to keep the request's frequency on a relatively low level,
    **so that we won't be end up in jail.**
    This is important, especially when you have no basic knowledge of
    the principles of http services.
    So please always write `time.sleep(n)` and keep n greater than 2.
"""

__version__ = "0.0.8"

from .request import send
from .site import page
from .congressman import Congressman, List
from .tools import analyzer

__all__ = ["analyzer", "page", "send", "Congressman", "List"]
