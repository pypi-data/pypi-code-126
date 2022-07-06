"""
This module implements the Request class which is used to represent HTTP
requests in Aioscrapy.

See documentation in docs/topics/request-response.rst
"""
from w3lib.url import safe_url_string

from aioscrapy.utils.curl import curl_to_request_kwargs
from aioscrapy.utils.url import escape_ajax
from aioscrapy.http.headers import Headers


class Request(object):

    def __init__(
            self,
            url,
            callback=None,
            method='GET',
            headers=None,
            body=None,
            cookies=None,
            meta=None,
            encoding='utf-8',
            priority=0,
            dont_filter=False,
            errback=None,
            flags=None,
            cb_kwargs=None,
            filter_mode=None,
    ):

        self._encoding = encoding  # this one has to be set first
        self.method = str(method).upper()
        self._set_url(url)
        self._set_body(body)
        if not isinstance(priority, int):
            raise TypeError(f"Request priority not an integer: {priority!r}")
        self.priority = priority

        self.callback = callback
        self.errback = errback

        self.cookies = cookies or {}
        self.headers = Headers(headers or {})
        self.dont_filter = dont_filter
        self.filter_mode = filter_mode or "IN_QUEUE"    # IN_QUEUE, OUT_QUEUE

        self._meta = dict(meta) if meta else None
        self._cb_kwargs = dict(cb_kwargs) if cb_kwargs else None
        self.flags = [] if flags is None else list(flags)

    @property
    def cb_kwargs(self):
        if self._cb_kwargs is None:
            self._cb_kwargs = {}
        return self._cb_kwargs

    @property
    def meta(self):
        if self._meta is None:
            self._meta = {}
        return self._meta

    def _get_url(self):
        return self._url

    def _set_url(self, url):
        if not isinstance(url, str):
            raise TypeError(f'Request url must be str or unicode, got {type(url).__name__}')

        s = safe_url_string(url, self.encoding)
        self._url = escape_ajax(s)

        if (
                '://' not in self._url
                and not self._url.startswith('about:')
                and not self._url.startswith('data:')
        ):
            raise ValueError(f'Missing scheme in request url: {self._url}')

    url = property(_get_url, _set_url)

    def _get_body(self):
        return self._body

    def _set_body(self, body):
        if body is None:
            self._body = ''
        else:
            self._body = body

    body = property(_get_body, _set_body)

    @property
    def encoding(self):
        return self._encoding

    def __str__(self):
        return f"<{self.method} {self.url}>"

    __repr__ = __str__

    def copy(self):
        """Return a copy of this Request"""
        return self.replace()

    def replace(self, *args, **kwargs):
        """Create a new Request with the same attributes except for those
        given new values.
        """
        for x in ['url', 'method', 'headers', 'body', 'cookies', 'meta', 'flags',
                  'encoding', 'priority', 'dont_filter', 'callback', 'errback', 'cb_kwargs']:
            kwargs.setdefault(x, getattr(self, x))
        cls = kwargs.pop('cls', self.__class__)
        return cls(*args, **kwargs)

    @classmethod
    def from_curl(cls, curl_command, ignore_unknown_options=True, **kwargs):
        """Create a Request object from a string containing a `cURL
        <https://curl.haxx.se/>`_ command. It populates the HTTP method, the
        URL, the headers, the cookies and the body. It accepts the same
        arguments as the :class:`Request` class, taking preference and
        overriding the values of the same arguments contained in the cURL
        command.

        Unrecognized options are ignored by default. To raise an error when
        finding unknown options call this method by passing
        ``ignore_unknown_options=False``.

        .. caution:: Using :meth:`from_curl` from :class:`~scrapy.http.Request`
                     subclasses, such as :class:`~scrapy.http.JSONRequest`, or
                     :class:`~scrapy.http.XmlRpcRequest`, as well as having
                     :ref:`downloader middlewares <topics-downloader-middleware>`
                     and
                     :ref:`spider middlewares <topics-spider-middleware>`
                     enabled, such as
                     :class:`~scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware`,
                     :class:`~scrapy.downloadermiddlewares.useragent.UserAgentMiddleware`,
                     or
                     :class:`~scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware`,
                     may modify the :class:`~scrapy.http.Request` object.

        To translate a cURL command into a aioscrapy request,
        you may use `curl2scrapy <https://michael-shub.github.io/curl2scrapy/>`_.

       """
        request_kwargs = curl_to_request_kwargs(curl_command, ignore_unknown_options)
        request_kwargs.update(kwargs)
        return cls(**request_kwargs)

    def serialize(self, callback):
        from aioscrapy.utils.reqser import request_to_dict
        return callback(request_to_dict(self))
