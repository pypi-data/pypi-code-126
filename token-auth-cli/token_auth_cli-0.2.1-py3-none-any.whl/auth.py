import logging
import asyncio

from typing import AsyncGenerator, Optional

from pydantic import BaseModel

import rich

from aiohttp.client_exceptions import ClientConnectionError

logger = logging.getLogger(__name__)


class User(BaseModel):
    username: str
    password: str
    token: Optional[str] = None

    def login_data(self) -> dict:
        return {"username": self.username,
                "password": self.password}


async def get_token(context, user: User) -> AsyncGenerator:
    """Try to get token for user."""
    settings = context.obj.settings
    repeat = settings.repeat
    app = context.obj
    request_data = user.login_data()

    async def _try_to_get_token(app, request_data):
        try:
            async with app.session.post(
                    app.settings.api_get_token, json=request_data) as req:
                if req.status != 200:
                    rich.print(f"[red]{req.status}[/red]")
                    return None
                rich.print(f"[green]{req.status}[/green]")
                return await req.json()
        except ClientConnectionError as err:
            rich.print(f"[red]{err}[/red]")

    while True:
        yield await _try_to_get_token(app, request_data)
        if repeat:
            await asyncio.sleep(settings.repeat_interval)
        else:
            break
