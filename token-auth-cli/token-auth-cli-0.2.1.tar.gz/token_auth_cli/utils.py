import logging
import asyncio
import copy

from typing import Any

import aiohttp
import rich

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
    for key, val in kwargs_dict.items():
        if val is None:
            continue
        filtered.update({key: val})
    return filtered


def filter_keys(kwargs_dict, keys: list):
    """Remove keys from dict."""
    filtered = copy.copy(kwargs_dict)
    for key in keys:
        if key in filtered:
            filtered.pop(key)
    return filtered


def show_if_debug(*args):
    for obj in args:
        if logger.isEnabledFor(logging.DEBUG):
            rich.inspect(obj)
