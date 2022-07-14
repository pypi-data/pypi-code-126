from pathlib import Path
from typing import Any, Callable, Dict, Iterable, Optional, Set
from functools import wraps
from asyncio import run, shield, Condition, gather

from singer import (
    Catalog,
    set_currently_syncing,
    write_state,
    job_timer,
    utils,
    get_logger)

from .client import Client

LOGGER = get_logger()

CONFIG_KEYS_REQUIRED: Set[str] = {
    'url'
}


def job_stream_timer(wrapped: Callable) -> Callable:

    @wraps(wrapped)
    async def wrapper(*args: Optional[Any], **kwargs: Optional[Any]) -> None:
        with job_timer(getattr(args[0], 'tap_stream_id', None) if len(args) > 1 else wrapped.__name__):
            return await wrapped(*args, **kwargs)

    return wrapper


def discover(streams: Iterable) -> Catalog:
    catalog: Catalog = Catalog([])

    for stream in streams:
        catalog.streams.append(stream.catalog_entry)

    return catalog


class Extractor:

    def __init__(self,
                 config: Dict = {},
                 streams: Iterable = [],
                 state: Dict = {},
                 catalog: Catalog = None,
                 client: type[Client] = Client) -> None:
        self.config: Dict[str, Any] = config
        self.state: Dict[str, Any] = state
        self.client: type[Client] = client

        # NOTE: Discovering if No Catalog provided.
        self.catalog: Catalog = catalog or discover(streams)

        # NOTE: inherit `selected` from the catalog
        selected: set = {s.tap_stream_id for s in self.catalog.get_selected_streams(self.state)}

        self.streams: Dict[str, Any] = {
            stream.catalog_entry.tap_stream_id: stream
            for stream in streams
            if stream.catalog_entry.tap_stream_id in selected}

        # self.streams = streams
        # self.streams: dict = {}
        # children: set = set()
        # for stream in streams:
        #     if stream.catalog_entry.tap_stream_id in selected:
        #         if stream.parent.get('tap_stream_id') is None:
        #             self.streams[stream.catalog_entry.tap_stream_id] = stream
        #         else:
        #             children.add(stream)

        # for stream in children:
        #     if stream.parent.get('tap_stream_id') in self.streams \
        #         and stream.catalog_entry.tap_stream_id not in self.streams[stream.parent.get('tap_stream_id')].children:
        #         self.streams[stream.parent.get('tap_stream_id')].children.add(stream)

    @job_stream_timer
    async def get_streams(self) -> None:

        async with self.client(self.config) as self._client:
            self._condition: Condition = Condition()
            self._currently_syncing: set = set()

            await gather(*{
                shield(stream.get_stream(self))
                for stream in self.streams.values()
                if stream.parent.get('tap_stream_id') is None})

        set_currently_syncing(self.state, None)
        write_state(self.state)

    def run(self) -> None:

        run(self.get_streams())


def set_streams(config: Dict = {}, schemas_dir: Path = None) -> Iterable:

    return []


async def sync(schemas_dir: Path = None, set_streams: Callable = set_streams, config_keys_required: Set[str] = CONFIG_KEYS_REQUIRED) -> None:
    try:
        args = utils.parse_args(config_keys_required)

        if args.discover:
            Extractor(args.config, set_streams(config=args.config, schemas_dir=schemas_dir)).catalog.dump()
        else:
            await Extractor(args.config, set_streams(config=args.config, schemas_dir=schemas_dir), args.state, args.catalog).get_streams()
    except Exception as e:
        LOGGER.critical(e)
        raise e


def main(schemas_dir: Path = None, set_streams: Callable = set_streams, config_keys_required: Set[str] = CONFIG_KEYS_REQUIRED) -> None:
    run(sync(schemas_dir, set_streams, config_keys_required))


# def cli(*,
#         config: str = 'config.json',
#         discover: str = None,
#         catalog: str = 'catalog.json',
#         state: str = 'state.json'
#         schemas_dir: str = None
#     ) -> Extractor:

#     LOGGER.setLevel(LEVELS_MAPPING.get(log_level))
#     with open(config) as config_io, open(catalog) as catalog_io, open(state) as state_io:
#         config_json = json.load(config_io)
#         catalog_json = json.load(catalog_io)
#         state_json = json.load(state_io)

#     streams: Dict = set_streams(config_json)

#     return Extractor(
#         config=config_json,
#         streams=streams,
#         state=state_json,
#         catalog=catalog_json,
#         schemas_dir=schemas_dir
#     )
