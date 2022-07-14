from typing import Any, Dict, Optional, Type, Union, List
from types import TracebackType

from aiohttp import CookieJar
from aiohttp.web import Application, Response, json_response  # , WebSocketResponse
from aiohttp.test_utils import TestClient, AbstractCookieJar

import socket
import ssl

from aiohttp import ClientSession, TCPConnector, resolver, test_utils, web
from aiohttp.abc import AbstractResolver

HOST: str = 'api.app.com'
TOKEN: str = 'ER34gsSGGS34XCBKd7u'


# NOTE: https://github.com/aio-libs/aiohttp/pull/1055
class AppResolver(AbstractResolver):  # type: ignore
    _LOCAL_HOST = {0: '127.0.0.1', socket.AF_INET: '127.0.0.1', socket.AF_INET6: '::1'}

    def __init__(self, fakes: Dict[str, int]) -> None:
        '''fakes -- dns -> port dict'''
        self._fakes = fakes
        self._resolver = resolver.DefaultResolver()

    async def resolve(
        self,
        host: str,
        port: int = 0,
        family: Union[socket.AddressFamily, int] = socket.AF_INET,
    ) -> List[Dict[str, Any]]:
        fake_port = self._fakes.get(host)
        if fake_port is not None:
            return [
                {
                    'hostname': host,
                    'host': self._LOCAL_HOST[family],
                    'port': fake_port,
                    'family': family,
                    'proto': 0,
                    'flags': socket.AI_NUMERICHOST,
                }
            ]
        else:
            return await self._resolver.resolve(host, port, family)

    async def close(self) -> None:
        await self._resolver.close()


class SimpleApp:

    def __init__(self) -> None:
        self.app = Application()
        self.app.router.add_routes(
            [
                web.get('/v3.9/me', self.get_me),
                web.get('/v3.9/me/friends', self.get_my_friends),
            ]
        )

        self.app.router.add_route('*', '/v3.9/', self.request_root)

        self.root_str = 'Hello, world'
        self.root_bytes = self.root_str.encode('utf-8')
        self.me = {"name": "John Doe", "id": "12345678901234567"}
        self.my_friends = {
            "data": [
                {"name": "Bill Doe", "id": "233242342342"},
                {"name": "Mary Doe", "id": "2342342343222"},
                {"name": "Alex Smith", "id": "234234234344"},
            ],
            "paging": {
                "cursors": {
                    "before": "QVFIUjRtc2c5NEl0ajN",
                    "after": "QVFIUlpFQWM0TmVuaDRad0dt",
                },
                "next": (
                    f"https://{HOST}/v3.9/12345678901234567/"
                    "friends?access_token=EAACEdEose0cB"
                ),
            },
            "summary": {"total_count": 3},
        }

    async def get_me(self, request: web.Request) -> web.StreamResponse:
        return json_response(self.me)

    async def get_my_friends(self, request: web.Request) -> web.StreamResponse:
        return json_response(self.my_friends)

    async def request_root(self, request: web.Request) -> Response:
        return Response(body=self.root_bytes)


class AppClient(TestClient):  # type: ignore

    def __init__(
        self,
        *args: Any,
        connector: TCPConnector,
        cookie_jar: Optional[AbstractCookieJar] = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(*args, **kwargs)
        cookie_jar = CookieJar(unsafe=True)
        self._session = ClientSession(connector=connector, cookie_jar=cookie_jar, **kwargs)


class AppServer():

    def __init__(self, app: Application, ssl_cert: str, ssl_key: str) -> None:
        self.app = app

        self.runner = web.AppRunner(self.app)

        self.ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        self.ssl_context.load_cert_chain(ssl_cert, ssl_key)

    async def __aenter__(self) -> Any:
        await self.start()
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType]
    ) -> None:
        await self.stop()

    async def start(self) -> None:
        self.port = test_utils.unused_port()
        await self.runner.setup()
        site = web.TCPSite(self.runner, '127.0.0.1', self.port, ssl_context=self.ssl_context)
        await site.start()

    async def stop(self) -> None:
        await self.runner.cleanup()
