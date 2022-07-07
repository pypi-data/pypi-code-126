import datetime
from datetime import timezone
from copy import deepcopy
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Set
from functools import partial, reduce, wraps
from asyncio import run, shield, to_thread, Condition, gather

from singer import (
    Transformer,
    Catalog,
    CatalogEntry,
    Schema,
    load_json,
    resolve_schema_references,
    get_bookmark,
    write_bookmark,
    get_offset,
    set_offset,
    clear_offset,
    set_currently_syncing,
    record_counter,
    reset_stream,
    write_schema,
    write_version,
    write_record,
    write_state,
    job_timer,
    utils,
    get_logger)
from singer.metadata import get_standard_metadata, to_map, write, to_list

from .client import Client

LOGGER = get_logger()

CONFIG_KEYS_REQUIRED: Set[str] = {
    'endpoint'
}


def job_stream_timer(wrapped: Callable) -> Callable:

    @wraps(wrapped)
    async def wrapper(*args: Optional[Any], **kwargs: Optional[Any]) -> None:
        with job_timer(args[1] if len(args) > 1 else wrapped.__name__):
            return await wrapped(*args, **kwargs)

    return wrapper


def load_schema(tap_stream_id: str, schemas_dir: Path = None) -> Dict:

    schema = load_json((schemas_dir or Path(__file__).parent.resolve() / 'schemas') / f'{tap_stream_id}.json')

    return resolve_schema_references(schema, {
        stream_id: load_schema(stream_id)
        for stream_id in schema.pop('tap_schema_dependencies', [])})


def format_response(response: List, params: Dict = {}) -> Any:
    return [r for r in response]


def format_response_replication(response: List, params: Dict, replication_value: int = 0) -> Any:
    return [r for i in response
            for r in i.get(params.get('path'), {}).values()
            if r.get(params.get('replication_key'), 2e9) > replication_value]


def format_response_sub_stream(response: List, params: Dict, replication_record: Dict = {}, replication_value: int = 0) -> List:
    # TODO: filter out unbounded preceding
    return [replication_record | r
            for i in response
            for r in i.get(params.get('path'), i)
            if (replication_record | r).get(params.get('replication_key'), 2e9) > replication_value]


class Extractor:

    def __init__(self, config: Dict, streams: Dict, state: Dict = {}, catalog: Catalog = None,
                 schemas_dir: Path = None, client: type[Client] = Client) -> None:
        self.config = config
        self.state = state
        self.schemas_dir = schemas_dir
        self.client = client

        self.streams = streams

        # NOTE: Discovering if No Catalog provided.
        self.catalog = catalog or self.discover(streams)

    def discover(self, streams: Dict) -> Catalog:
        catalog = Catalog([])

        for tap_stream_id, stream in (streams or self.streams).items():
            schema = load_schema(tap_stream_id, self.schemas_dir)

            metadata = get_standard_metadata(
                schema=schema,
                schema_name=tap_stream_id,
                key_properties=stream.key_properties,
                valid_replication_keys=stream.replication_key,
                replication_method=stream.replication_method)

            catalog.streams.append(CatalogEntry(
                tap_stream_id=tap_stream_id,
                stream=tap_stream_id,
                key_properties=stream.key_properties or [],
                schema=Schema.from_dict(schema),
                replication_key=stream.replication_key,
                replication_method=stream.replication_method or 'FULL_TABLE',
                is_view=stream.is_view,
                database=stream.database,
                table=stream.table,
                row_count=stream.row_count,
                stream_alias=stream.stream_alias or tap_stream_id,
                metadata=to_list(write(to_map(metadata), (), 'selected', True))
                if tap_stream_id in self.config.get('selected', []) else metadata))

        return catalog

    async def _write_records(self, tap_stream_id: str, records: List, version: int = None) -> None:
        LOGGER.info('Syncing stream: %s', tap_stream_id)
        stream = self.catalog.get_stream(tap_stream_id)

        set_currently_syncing(self.state, tap_stream_id)
        await to_thread(write_state, self.state)

        if tap_stream_id not in self._currently_syncing:
            self._currently_syncing.add(tap_stream_id)
            await to_thread(write_schema,
                            tap_stream_id,
                            stream.schema.to_dict(),
                            self.catalog.get_stream(tap_stream_id).key_properties)

        await to_thread(write_version, tap_stream_id, version)

        for record in records:
            with Transformer() as t:
                await to_thread(write_record,
                                tap_stream_id,
                                t.transform(record, stream.schema.to_dict(), to_map(stream.metadata)),
                                stream.stream_alias,
                                datetime.datetime.now(timezone.utc))

        with record_counter(tap_stream_id) as counter:
            counter.increment(len(records))

    @job_stream_timer
    async def get_streams(self) -> None:

        async with self.client(self.config) as self._client:
            self._condition: Condition = Condition()
            self._currently_syncing: set = set()

            await gather(*{
                shield(self.streams[stream.tap_stream_id].get_stream(stream.tap_stream_id, self))
                for stream in self.catalog.get_selected_streams(self.state)
                if self.streams[stream.tap_stream_id].parent.get('tap_stream_id') is None})

        set_currently_syncing(self.state, None)
        write_state(self.state)

    def run(self) -> None:

        run(self.get_streams())


class Stream:

    def __init__(
        self,
        tap_stream_id: str,
        key_properties: List[str] = [],
        replication_method: str = 'FULL_TABLE',
        replication_key: str = None,
        is_view: bool = False,
        database: str = None,
        table: str = None,
        row_count: int = None,
        stream_alias: str = None,
        format_response_function: Callable = format_response,
        format_response_params: Dict[str, Any] = {},
        parent: Dict[str, Any] = {},
        params: Dict[str, Any] = {}
    ) -> None:
        self.tap_stream_id = tap_stream_id
        self.key_properties = key_properties
        self.replication_method = replication_method
        self.replication_key = replication_key
        self.is_view = is_view
        self.database = database
        self.table = table
        self.row_count = row_count
        self.stream_alias = stream_alias
        self.format_response = {'function': format_response_function, 'params': format_response_params}
        self.parent = parent
        self.params = params

    @job_stream_timer
    async def get_sub_stream(self, tap_stream_id: str, extractor: Extractor, parent_records: list) -> None:
        stream = extractor.streams[tap_stream_id]
        parent_tap_stream_id: str = stream.parent.get('tap_stream_id')
        parent_key_properties = stream.parent.get('key_properties')
        parent_replication_key = extractor.catalog.get_stream(parent_tap_stream_id).replication_key
        # parent_replication_value = get_bookmark(extractor.state, parent_tap_stream_id, parent_replication_key, 0)
        url = stream.params.get('url', '')
        format_response_function = stream.format_response.get('function', format_response_sub_stream)

        records = [record for records in await gather(*[
            shield(extractor._client.get_records(
                tap_stream_id,
                **(stream.params | {
                    'url': url.format(**{k: parent_record.get(k) for k in parent_key_properties}),
                    'format_response': (stream.format_response | {'function': partial(
                        format_response_function,
                        params=stream.format_response.get('params'),
                        replication_record={parent_replication_key: parent_record.get(parent_replication_key)}
                        if parent_record.get(parent_replication_key) else {})})['function']})))
            for parent_record in parent_records
            if reduce(lambda x, k: x and parent_record.get(k) is not None, parent_key_properties, True)])
            if records is not None
            for record in records]

        async with extractor._condition:
            await extractor._write_records(tap_stream_id, records, 1)
            # if extractor.catalog.get_stream(tap_stream_id).replication_method == 'FULL_TABLE':
            reset_stream(extractor.state, tap_stream_id)
            await to_thread(write_state, extractor.state)

    @job_stream_timer
    async def get_stream(self, tap_stream_id: str, extractor: Extractor, *args: Optional[Any], **kwargs: Dict) -> None:
        params = deepcopy(self.params)
        stream = extractor.streams[tap_stream_id]
        replication_key = extractor.catalog.get_stream(tap_stream_id).replication_key
        filters = params.pop('filters', {}) | ({
            replication_key: get_bookmark(extractor.state, tap_stream_id, replication_key, 0)} if replication_key else {})
        replication_value = get_bookmark(extractor.state, tap_stream_id, replication_key, 0)
        format_response_params = stream.format_response | {
            'function': partial(
                stream.format_response.get('function', format_response_replication),
                params=stream.format_response.get('params'),
                replication_value=replication_value)
        } | params.pop('format_response', {})

        records = await extractor._client.get_records(tap_stream_id, filters=filters, format_response=format_response_params['function'], *args, **params)

        async with extractor._condition:
            await extractor._write_records(tap_stream_id, records, 1)

            if replication_key is not None and any(records):
                write_bookmark(
                    extractor.state, tap_stream_id, replication_key,
                    max(records, key=lambda r: r.get(replication_key)).get(replication_key))  # pragma: no cover
            if extractor.catalog.get_stream(tap_stream_id).replication_method == 'FULL_TABLE':
                reset_stream(extractor.state, tap_stream_id)
            await to_thread(write_state, extractor.state)

        for sub_stream_tap_stream_id, _ in filter(
            lambda s: s[1].parent.get('tap_stream_id') == tap_stream_id and to_map(
                extractor.catalog.get_stream(s[0]).metadata).get((), {}).get('selected', False),
                extractor.streams.items()):
            await self.get_sub_stream(sub_stream_tap_stream_id, extractor, records)


class StreamPages(Stream):

    @job_stream_timer
    async def get_stream(self, tap_stream_id: str, extractor: Extractor, *args: Optional[Any], **kwargs: Dict) -> None:
        params = deepcopy(self.params)
        stream = extractor.streams[tap_stream_id]
        replication_key = extractor.catalog.get_stream(tap_stream_id).replication_key
        replication_value = get_bookmark(extractor.state, tap_stream_id, replication_key, 0)
        format_response_params = stream.format_response | {
            'function': partial(
                stream.format_response.get('function', format_response_replication),
                params=stream.format_response.get('params'),
                replication_value=replication_value)
        } | params.pop('format_response', {})
        offset_key: str = stream.params.get('offset_key')
        limit_key: str = stream.params.get('limit_key')
        curr_offset = get_offset(extractor.state, tap_stream_id, {}).get('offset', 0)
        filters = {offset_key: curr_offset} | params.pop('filters', {}) | ({
            replication_key: get_bookmark(extractor.state, tap_stream_id, replication_key, 0)} if replication_key else {})
        records = None

        while any(filters):
            response = await extractor._client.get(tap_stream_id, filters=filters, *args, **params),
            records = format_response_params['function'](response) if callable(format_response_params['function']) else []

            async with extractor._condition:
                set_offset(extractor.state, tap_stream_id, 'offset', filters[offset_key])
                await extractor._write_records(tap_stream_id, records, 1)
                if replication_key and records:
                    write_bookmark(
                        extractor.state,
                        tap_stream_id,
                        replication_key,
                        max(records + [filters],
                            key=lambda r: r.get(replication_key)).get(replication_key))
                await to_thread(write_state, extractor.state)

            for sub_stream_tap_stream_id, _ in filter(
                lambda s: s[1].parent.get('tap_stream_id') == tap_stream_id and to_map(
                    extractor.catalog.get_stream(s[0]).metadata).get((), {}).get('selected', False),
                    extractor.streams.items()):
                await self.get_sub_stream(sub_stream_tap_stream_id, extractor, records)

            # if any(records) and len(records) >= filters[limit_key]:
            if len(records) > 0:
                filters[offset_key] += filters[limit_key]
            else:
                filters = {}

        # if extractor.catalog.get_stream(tap_stream_id).replication_method == 'FULL_TABLE':
        async with extractor._condition:
            clear_offset(extractor.state, tap_stream_id)

    # async def get_cursors(self, tap_stream_id: str, curr_offset: int = 0, *args: Optional[Any], **kwargs: Dict) -> AsyncGenerator:
    #     format_response = kwargs['format_response']
    #     limit_key = kwargs['limit_key'] if 'limit_key' in kwargs else None
    #     next_token_key = kwargs['next_token_key'] if 'next_token_key' in kwargs else None
    #     params: Dict = {limit_key: self.page_limit} | kwargs.pop('filters', {})
    #     filters: Dict = params

    #     while any(filters):
    #         response = await self.get(tap_stream_id, filters=filters, *args, **kwargs),
    #         records = format_response['function'](response, format_response['params']) if callable(format_response['function']) else []

    #         yield curr_offset, records

    #         if len(records) > 0 and response.get(next_token_key, None) is not None:  # type: ignore
    #             filters = params | {next_token_key: response[next_token_key]}  # type: ignore
    #             curr_offset += filters[limit_key]
    #         else:
    #             filters = {}


def set_streams() -> Dict:

    return {}


async def sync(schemas_dir: Path = None, set_streams: Callable = set_streams, config_keys_required: Set[str] = CONFIG_KEYS_REQUIRED) -> None:
    try:
        args = utils.parse_args(config_keys_required)

        if args.discover:
            Extractor(args.config, set_streams(), schemas_dir=schemas_dir).catalog.dump()
        else:
            await Extractor(args.config, set_streams(), args.state, args.catalog, schemas_dir=schemas_dir).get_streams()
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
