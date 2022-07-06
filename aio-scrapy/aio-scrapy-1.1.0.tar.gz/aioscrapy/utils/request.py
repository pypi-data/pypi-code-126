"""
This module provides some useful functions for working with
aioscrapy.http.Request objects
"""

import hashlib
from typing import Dict, Iterable, Optional, Tuple, Union
from urllib.parse import urlunparse
from weakref import WeakKeyDictionary

from w3lib.http import basic_auth_header, headers_dict_to_raw
from w3lib.url import canonicalize_url

from aioscrapy.http import Request
from aioscrapy.utils.httpobj import urlparse_cached
from aioscrapy.utils.python import to_bytes, to_unicode


_fingerprint_cache: "WeakKeyDictionary[Request, Dict[Tuple[Optional[Tuple[bytes, ...]], bool], str]]"
_fingerprint_cache = WeakKeyDictionary()


def request_fingerprint(
    request: Request,
    include_headers: Optional[Iterable[Union[bytes, str]]] = None,
    keep_fragments: bool = False,
):
    """
    Return the request fingerprint.

    The request fingerprint is a hash that uniquely identifies the resource the
    request points to. For example, take the following two urls:

    http://www.example.com/query?id=111&cat=222
    http://www.example.com/query?cat=222&id=111

    Even though those are two different URLs both point to the same resource
    and are equivalent (i.e. they should return the same response).

    Another example are cookies used to store session ids. Suppose the
    following page is only accessible to authenticated users:

    http://www.example.com/members/offers.html

    Lot of sites use a cookie to store the session id, which adds a random
    component to the HTTP Request and thus should be ignored when calculating
    the fingerprint.

    For this reason, request headers are ignored by default when calculating
    the fingeprint. If you want to include specific headers use the
    include_headers argument, which is a list of Request headers to include.

    Also, servers usually ignore fragments in urls when handling requests,
    so they are also ignored by default when calculating the fingerprint.
    If you want to include them, set the keep_fragments argument to True
    (for instance when handling requests with a headless browser).

    """
    headers: Optional[Tuple[bytes, ...]] = None
    if include_headers:
        headers = tuple(to_bytes(h.lower()) for h in sorted(include_headers))
    cache = _fingerprint_cache.setdefault(request, {})
    cache_key = (headers, keep_fragments)
    if cache_key not in cache:
        fp = hashlib.sha1()
        fp.update(to_bytes(request.method))
        fp.update(to_bytes(canonicalize_url(request.url, keep_fragments=keep_fragments)))
        fp.update(to_bytes(request.body) or b'')
        if headers:
            for hdr in headers:
                if hdr in request.headers:
                    fp.update(hdr)
                    for v in request.headers.getlist(hdr):
                        fp.update(v)
        cache[cache_key] = fp.hexdigest()
    return cache[cache_key]


def request_authenticate(request: Request, username: str, password: str) -> None:
    """Autenticate the given request (in place) using the HTTP basic access
    authentication mechanism (RFC 2617) and the given username and password
    """
    request.headers['Authorization'] = basic_auth_header(username, password)


def request_httprepr(request: Request) -> bytes:
    """Return the raw HTTP representation (as bytes) of the given request.
    This is provided only for reference since it's not the actual stream of
    bytes that will be send when performing the request (that's controlled
    by Twisted).
    """
    parsed = urlparse_cached(request)
    path = urlunparse(('', '', parsed.path or '/', parsed.params, parsed.query, ''))
    s = to_bytes(request.method) + b" " + to_bytes(path) + b" HTTP/1.1\r\n"
    s += b"Host: " + to_bytes(parsed.hostname or b'') + b"\r\n"
    if request.headers:
        s += headers_dict_to_raw({to_bytes(k): to_bytes(v) for k, v in request.headers.items()}) + b"\r\n"
    s += b"\r\n"
    s += to_bytes(request.body)
    return s


def referer_str(request: Request) -> Optional[str]:
    """ Return Referer HTTP header suitable for logging. """
    referrer = request.headers.get('Referer')
    if referrer is None:
        return referrer
    return to_unicode(referrer, errors='replace')
