import asyncio
import typing
import logging

import aiohttp

from donation_alerts_handler.types.user_profile import UserProfile
from donation_alerts_handler.types.donations import Donations


class ResponseError(Exception):
    pass


class Client:
    API_URL = "https://www.donationalerts.com/api/v1/"

    def __init__(self, token: str):
        self.token = token
        self.handlers: dict[typing.Callable, tuple] = {}
        self.connected = False
        self.check_timout = 1  # 1 All API requests are subject to rate limits. We limit requests to our HTTP API methods for each application by 60 requests per minute, making it 1 request per second
        self.__latest_requests: list[int] = []

    async def invoke(self, path: str, params: str = None, method: str = "GET", headers: dict = None):
        if headers is None:
            headers = dict()
        headers.update({"Authorization": f"Bearer {self.token}"})
        async with aiohttp.ClientSession(headers=headers) as session:
            if method == "GET":
                r = await session.get(Client.API_URL + path, params=params)
            elif method == "POST":
                r = await session.post(Client.API_URL + path, params=params)
            else:
                raise Exception("MethodNotAllowed")
            raw_object = await r.json()
            if raw_object.get("data", None) is None:
                raise ResponseError(raw_object.get("message"))
            return raw_object

    async def get_user(self):
        raw = await self.invoke("user/oauth")
        return UserProfile(**raw.get("data"))

    async def donations(self):
        raw = await self.invoke("alerts/donations")
        return [Donations(**raw_object) for raw_object in raw.get("data")]

    def on_donate(self, *filters):
        """set currency to '*', if you aren't needed to check currency"""

        def wrap(func: typing.Callable):
            self.handlers.update({func: filters})

        return wrap

    async def handle_donate(self, donate: Donations):
        async def filters_handle():
            for filter_ in filters:
                if await filter_(donate) is False:
                    return False
            return True

        for handler in self.handlers:
            filters = self.handlers[handler]
            if await filters_handle():
                try:
                    await handler(donate)
                except Exception as e:
                    logging.error(f"error while processing handler: {e}")

    async def connect(self):
        self.connected = True
        self.__latest_requests = [donation.id for donation in await self.donations()]
        logging.info("Initialized")
        while self.connected:
            await asyncio.sleep(self.check_timout)
            try:
                donations = await self.donations()
            except aiohttp.ClientConnectorError:
                logging.error("Error while connecting to the server. Check your connection! Trying again....")
                await asyncio.sleep(5)
                continue
            except Exception as e:
                logging.error(e)
                await asyncio.sleep(5)
                continue
            donations = donations[:10]
            for donation in donations:
                if donation.id in self.__latest_requests:
                    break
                self.__latest_requests.insert(0, donation.id)
                self.__latest_requests = self.__latest_requests[:10]
                await self.handle_donate(donation)

    def run(self, loop=asyncio.new_event_loop()):
        loop.run_until_complete(self.connect())

    def stop(self):
        if self.connected is False:
            raise Exception("Polling was not started")
        self.connected = False

    async def test_donate(self):
        donates = await self.donations()
        await self.handle_donate(donates[0])
