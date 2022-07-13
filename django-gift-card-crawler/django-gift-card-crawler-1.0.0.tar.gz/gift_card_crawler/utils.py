import os
import re
from urllib.parse import urlparse

import pandas as pd
from django.core.cache import cache
from django.utils.translation import gettext_lazy as _

from gift_card_crawler.crawlers import EGiftActivationSpot, ClaimEGifterRewards


def get_crawl_provider(link):
    domain = urlparse(link).netloc
    return {
        'egift.activationspot.com': EGiftActivationSpot,
        'claim.egifterrewards.com': ClaimEGifterRewards,
    }.get(domain)


def check_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return re.match(regex, url) is not None


def extract_links(file):
    filename, ex = os.path.splitext(file.name)
    if ex not in ['.csv', '.txt', '.xls']:
        return None, _('The file format is out of range')

    links = []
    if file.content_type == 'application/vnd.ms-excel':
        contents = pd.read_excel(file)
    else:  # 'text/csv' , 'text/plain'
        contents = pd.read_csv(file)

    idx = range(contents.index.start, contents.index.stop)
    for i in idx:
        if contents.index.isin([i]).any():

            try:
                link = contents.iat[i, 0]
            except:
                link = None

            try:
                code = contents.iat[i, 1].replace('\t', '').replace('\n', '')
            except:
                code = None

            if check_url(link):
                provider = get_crawl_provider(link)
                links.append((link, code, provider))

    return links, None


def crawl_runner(links, reference_id):
    cards = []
    for link, code, provider in links:
        if not provider:
            continue

        scraper = provider(link=link, code=code)
        info, error = scraper.crawl()
        if not info:
            continue

        cards = cards + info
    cache.set(reference_id, cards, 3600)
