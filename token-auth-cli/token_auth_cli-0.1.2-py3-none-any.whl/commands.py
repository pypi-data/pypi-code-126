import logging
import asyncio

import aiohttp
import click
import rich

logger = logging.getLogger(__name__)


async def get_token(context, *args, **kwargs):
    config = context.obj.settings
    session = context.obj.session
    request_data = kwargs
    if len(request_data) > 2:
        raise ValueError
    async with session.post(config.api_get_token, json=request_data) as req:
        if req.status != 200:
            rich.print(f"[red]{req.status}[/red]")
            raise click.Abort
        else:
            rich.print(f"[green]OK[/green]")
