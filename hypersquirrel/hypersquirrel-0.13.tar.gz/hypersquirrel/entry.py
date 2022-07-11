import re
from typing import Iterator

from hypersquirrel.core import Watchlist
from hypersquirrel.scraperfactory import get_scraper

PAGED_PATTERN = re.compile("<\d+-\d+>")


def create_watchlist(url: str, max_items: int):
    match = PAGED_PATTERN.findall(url)
    if len(match) == 1:
        pages = match[0].replace("<", "").replace(">", "").split("-")
        return Watchlist(
            url=url.replace(match[0], "${page}"),
            max_items=max_items,
            page_min=int(pages[0]),
            page_max=int(pages[1])
        )
    return Watchlist(
        url=url,
        max_items=max_items
    )


def scrape(w: Watchlist) -> Iterator[dict]:
    return w.scrape(get_scraper(w))
