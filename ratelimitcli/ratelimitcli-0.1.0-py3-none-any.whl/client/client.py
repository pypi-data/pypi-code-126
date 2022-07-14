import asyncio
from functools import wraps, partial
import inspect
import typing
from uuid import uuid4

import aiohttp
from ratelimitcli.client.decorator import APIRateLimitException, RatelimitDecorator

from ratelimitcli.limits.read_write import ThriftReadWrite, Base64ReadWrite
from ratelimitcli.limits import cli_thrift as T
from ratelimitcli.conf import settings


class RatelimitClient(RatelimitDecorator):
    """Http client for the Ratelimit API.

    Record requests against pre-existing rate limits directly or by using this
    class as a decorator.
    """
    def __init__(
        self, host=None, port=None, path=None, client_id=None, api_key=None, loop=None
    ):
        if host is None:
            host = settings["HOST"]
        if port is None:
            port = settings["PORT"]
        if path is None:
            base_path = settings["BASE_PATH"]
        self._base_url = f"{host}:{port}{base_path}"

        if not client_id:
            raise ValueError("Client ID must be specified.")
        if not api_key:
            raise ValueError("Auth must be specified.")

        self._headers = {
            "X-CLIENT-ID": client_id,
            "Authorization": api_key,
            "Content-Type": "application/text",
        }
        self._client_id = client_id
        self.b64rw = Base64ReadWrite()

        self._MAX_CONNECTIONS = int(settings["MAX_CONNECTIONS"])
        self._MAX_CONNECTIONS_PER_HOST = int(settings["MAX_CONNECTIONS_PER_HOST"])
        self._session = None
        self._loop = loop

    @property
    def loop(self):
        if self._loop:
            return self._loop
        try:
            self._loop = asyncio.get_running_loop()
        except:
            self._loop = asyncio.new_event_loop()
        return self._loop

    def __del__(self):
        """Close underlying session."""
        if self._session:
            self.loop.run_until_complete(self._session.close())

    def __call__(
        self,
        limit_id: str,
        callback: typing.Optional[typing.Callable[..., typing.Any]] = None,
    ):
        async def call_fn(
            func: typing.Callable[..., typing.Any], *args, **kwargs
        ) -> typing.Any:
            if inspect.iscoroutinefunction(func):
                return await func(*args, **kwargs)
            else:
                return func(*args, **kwargs)

        def decorator(fn: typing.Callable[..., typing.Any]):
            if not callable(fn):
                raise TypeError("Decorated function must be a callable.")

            @wraps(fn)
            async def async_wrapper(*args, **kwargs):
                try:
                    await self.record_request(limit_id)
                except APIRateLimitException as e:
                    if callback:
                        return await call_fn(
                            func=partial(callback, exception=e), *args, **kwargs
                        )
                    raise e
                else:
                    return await call_fn(func=fn, *args, **kwargs)

            return async_wrapper

        return decorator

    async def _create_session(self):
        """Create a ClientSession in an async method."""
        self._session = aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(
                limit=self._MAX_CONNECTIONS,
                limit_per_host=self._MAX_CONNECTIONS,
            ),
            headers=self._headers,
        )

    async def _send(
        self, url: str, request_bytes: bytes
    ) -> typing.Optional[typing.Union[bytes, typing.NoReturn]]:
        """Send the request to the API endpoint and return the response."""
        if not self._session:
            await self._create_session()

        data = self.b64rw.to_base64(request_bytes)
        async with self._session.post(url, data=data) as resp:
            if resp.status == 429:
                raise APIRateLimitException(resp)
            response = await resp.read()
            return response if response else None

    def sync_record_request(
        self, limit_id: str
    ) -> typing.Optional[typing.Union[bytes, typing.NoReturn]]:
        """Synchronously send request to the API."""
        return self.loop.run_until_complete(self.record_request(limit_id))

    async def record_request(
        self, limit_id: str
    ) -> typing.Optional[typing.Union[bytes, typing.NoReturn]]:
        url = f"{self._base_url}{settings['BUCKET_PATH']}"
        rw = _SERDE["BUCKET"]
        thrift = T.GetRemainingCapacityRequest(
            meta=T.Metadata(
                client_id=self._client_id,
                purpose="upsert_limit",
                tracking_id=str(uuid4()),
            ),
            limit_id=limit_id,
        )
        return await self._send(url, rw.to_bytes(thrift))


_SERDE = {
    "BUCKET": ThriftReadWrite(T.GetRemainingCapacityRequest),
    "CONFIG": ThriftReadWrite(T.SetLimitRequest),
}
