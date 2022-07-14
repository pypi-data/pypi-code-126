"""fast_link_extractor
a program to quickly extract links from a url
"""
from bs4 import BeautifulSoup
from itertools import chain
import asyncio
import aiohttp
import re


def _format_base_url(base_url: str):
    """properly format url to start with protocl and end with slash

    Args
    ------
    base_url (str): the original URL supplied

    Returns
    ------
    str: url with format like `https://.../`
    """
    base_url = 'https://' + \
        base_url if not base_url.startswith(
            ('http://', 'https://')) else base_url
    base_url = base_url + '/' if not base_url.endswith('/') else base_url
    return base_url


async def _async_get_html(base_url: str, ssl: bool = None):
    """get html for a url

    Parameters
    ------
    base_url (str): the original URL supplied
    ssl (str): SSL validation mode. default is False
               if False then skip SSL certificate validation

    Returns
    ------
    str: html for base_url
    """
    if ssl is None:
        ssl = False

    # may need to add this to ClientSession() connector=aiohttp.TCPConnector(ssl=False)
    conn = aiohttp.TCPConnector(ssl=ssl)
    async with aiohttp.ClientSession(connector=conn, trust_env=True) as client:
        async with client.get(base_url) as resp:  # ssl=False
            return await resp.text() if (resp.status == 200) else ""


def _get_links(html_page: str):
    """gets all links from html

    Parameters
    ------
    html_page (str): document html

    Returns
    ------
    list: list of all the links in the html document
          (these could be files or sub-directories)
    """
    # "lxml" supposed to be faster than "html.parser
    soup = BeautifulSoup(html_page, "html.parser")
    regex = ".|(/$)"
    links = [f"{link.get('href')}"
             for link
             in soup.findAll('a', attrs={'href': re.compile(regex)})]

    return links


def _get_sub_dirs(links: list, base_url: str):
    """gets sub-directories from list of links

    Parameters
    ------
    links (list): list of links, contains files and sub-directories
    base_url (str): the original URL supplied

    Returns
    ------
    list: only the links that point to sub-directories are returned
    """
    sub_dirs = [f"{base_url}{link}" for link in links if re.search(r'/$', link)]
    return sub_dirs


def _get_files(links: list, regex: str = None):
    """gets files from list of links

    Parameters
    ------
    links (list): list of links to files and sub-directories
    regex (str): filter links based on a regular expression

    Returns
    ------
    list: only the links that point to files are returned
    """
    if regex is None:
        regex = r'[^/]$'
    file_links = [link for link in links if re.search(regex, link)]
    return file_links


def _filter_with_regex(links: list, regex: str):
    """filters files by regular expressions

    Parameters
    ------
        links (list): list of links to files and sub-directories
        regex (str): regular expression string

    Returns
    ------
        list: a list of links with regular expression applied
    """
    return [link for link in links if re.search(regex, link)]


def _prepend_with_baseurl(links: list, base_url: str):
    """prepend url to beginning of each file

    Parameters
    ------
        links (list): list of links to files and sub-directories
        base_url (str): base url

    Returns
    ------
        list: a list of links with base url pre-pended
    """
    return [base_url + link for link in links]


async def _gather_with_concurrency(n: int, *tasks):
    """Limits open files to avoid 'too many open files' error

    Parameters
    ------
        n (int): number of files to open at once
        tasks (list): list of tasks to gather output from

    Returns
    ------
        awaitable: gathered coroutines that need to awaited

    Notes
    ------
    ```
    https://stackoverflow.com/questions/48483348/
    how-to-limit-concurrency-with-python-asyncio/61478547#61478547
    ```
    """
    semaphore = asyncio.Semaphore(n)

    async def sem_task(task):
        async with semaphore:
            return await task
    return await asyncio.gather(*(sem_task(task) for task in tasks))


async def _async_link_extractor(base_url: str, search_subs: bool = None, regex: str = None, *args, **kwargs):
    """asyncronous extract links from url

    Parameters
    ------
        base_url (str): URL you want to search
        seach_subs (bool): True is want to search sub-directories
        regex (str): filter links based on a regular expression

    Returns
    ------
        list: list of files
    """
    files = []
    base_url = _format_base_url(base_url)
    html_page = await _async_get_html(base_url)
    links = _get_links(html_page=html_page)
    sub_dirs = _get_sub_dirs(links, base_url)
    filenames = _get_files(links, regex=regex)
    base_files = _prepend_with_baseurl(filenames, base_url)
    files.extend(base_files)

    # gathers files from sub-directories
    if search_subs:
        coros = [_async_link_extractor(sub) for sub in sub_dirs]
        new_files = await _gather_with_concurrency(200, *coros)
        files.extend(chain(*new_files))

    if regex is not None:
        files = _filter_with_regex(files, regex)

    return files


def link_extractor(base_url: str = None,
                   search_subs: bool = None,
                   regex: str = None,
                   ipython: bool = None,
                   no_warning: bool = None,
                   *args, **kwargs):
    """extract links from base_url

    to get output in jupyter you need to await the result first
        ```
        links = await link_extractor(*args)
        ```

    Parameters
    ------
        base_url (str): URL you want to search
        seach_subs (bool): True is want to search sub-directories 
            (default is True)
        regex (str): filter links based on a regular expression 
            (default is '.')
        ipython (bool): whether you are using ipython or not
            (default is False)
        no_warning (bool): toggles on/off the await warning message
            (default is False, only applies to ipython=True)

    Returns
    ------
        list: list of files

    Example
    ------
    ```
    url = 'https://www.ncei.noaa.gov/data/sea-surface-temperature-optimum-interpolation/v2.1/access/avhrr/'
    links = await link_extractor(url, search_subs=True, regex='.nc$', ipython=True)
    ```
    """
    # set default parameters
    search_subs = True if search_subs is None else search_subs
    ipython = False if ipython is None else ipython
    regex = '.' if regex is None else regex
    no_warning = False if no_warning is None else no_warning

    # ensure type is correct
    if not isinstance(base_url, str):
        raise TypeError('Argument for base_url must be a string')

    if not isinstance(search_subs, bool):
        raise TypeError('Argument for search_subs must be a bool')

    if not isinstance(regex, str):
        raise TypeError('Argument for regex must be a string')

    if not isinstance(ipython, bool):
        raise TypeError('Argument for ipython must be a bool')

    warning_message = """ 
    ======================================================
    This is a coroutine. Make sure to `await` the function
        
        links = await link_extractor(url, ...)
        
    no_warning=True will suppress this warning 
    ======================================================
    """

    if not ipython:
        return asyncio.run(_async_link_extractor(base_url=base_url,
                                                 search_subs=search_subs,
                                                 regex=regex))
    else:
        None if no_warning else print(f'{warning_message}')
        return _async_link_extractor(base_url=base_url,
                                     search_subs=search_subs,
                                     regex=regex)
