from abc import ABC, abstractmethod
from functools import wraps, partial
import inspect
import typing

import aiohttp
from aiohttp.client_exceptions import ClientResponseError

class APIRateLimitException(ClientResponseError):
    def __init__(self, resp: aiohttp.ClientResponse):
        super().__init__(
            request_info=resp.request_info,
            status=resp.status,
            history=(resp),
        )


class RatelimitDecorator(ABC):
    """Decorator that wraps a function with a call to the Ratelimit API.

    Use this decorator or a subclass of it to wrap function calls with a
    call to the Ratelimit API. Note that a ratelimit must be set up in
    advance and the decorator expects to take a single limit_id that will
    be sent to the Ratelimit API.

    If the Ratelimit API returns with a HTTP 200 status code then the
    decorator will proceed with calling the decorated function. Otherwise
    if a HTTP 429 status code is returned, then an APIRateLimitException
    is raised.

    An optional callback function can be provided and will be called in
    the event where an APIRateLimitException is raised. That callback will
    be called with the same args and kwargs as the original function.

    Example:
        def callback(foo: int):
            ...

        @RatelimitDecorator(
            "a9f9f31b-2c0b-321b-b398-f9d36kd30820",
            callback=callback
        )
        def my_api_func(foo: int):
            ...
    """

    @abstractmethod
    def record_request(limit_id: str):
        ...

    def __call__(
        self,
        limit_id: str,
        callback: typing.Optional[typing.Callable[..., typing.Any]] = None,
    ):
        def decorator(fn: typing.Callable[..., typing.Any]):
            if not callable(fn):
                raise TypeError("Decorated function must be a callable.")

            @wraps(fn)
            async def async_wrapper(*args, **kwargs):
                try:
                    await self.record_request(limit_id)
                except APIRateLimitException as e:
                    if callback:
                        return await self._call_fn(
                            func=partial(callback, exception=e), *args, **kwargs
                        )
                    raise e
                else:
                    return await self._call_fn(func=fn, *args, **kwargs)

            return async_wrapper

        return decorator

    async def _call_fn(func: typing.Callable[..., typing.Any], *args, **kwargs) -> typing.Any:
        if inspect.iscoroutinefunction(func):
            return await func(*args, **kwargs)
        else:
            return func(*args, **kwargs)
