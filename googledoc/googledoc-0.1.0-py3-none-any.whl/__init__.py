"""
Basic
"""
__version__ = '0.1.0'

__mkinit__ = """
mkinit /home/joncrall/code/googledoc/googledoc/__init__.py -w
"""


from googledoc import docscrape_google

from googledoc.docscrape_google import (DocBlock, parse_google_argblock,
                                        parse_google_args,
                                        parse_google_retblock,
                                        parse_google_returns,
                                        split_google_docblocks,)

__all__ = ['DocBlock', 'docscrape_google', 'parse_google_argblock',
           'parse_google_args', 'parse_google_retblock',
           'parse_google_returns', 'split_google_docblocks']
