import logging
import asyncio

from typing import Any

import aiohttp

logger = logging.getLogger(__name__)


def add_session(func):
    """Add ClientSession to App object."""
    async def add_session_wrapper(context, *args, **kwargs):
        api = context.obj.settings.api
        async with aiohttp.ClientSession(api) as session:
            context.obj.session = session
            result = await func(context, *args, **kwargs)
        return result
    return add_session_wrapper


def run_async_command(func, *args, **kwargs) -> Any:
    """Run async command"""
    func = add_session(func)
    return asyncio.run(func(*args, **kwargs))


def filter_none(kwargs_dict):
    """Remove 'None' from dict."""
    filtered = {}
    for name, val in kwargs_dict.items():
        if val is None:
            continue
        filtered.update({name: val})
    return filtered
