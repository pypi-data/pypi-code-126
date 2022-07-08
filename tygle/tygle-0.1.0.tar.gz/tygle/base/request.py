from abc import ABCMeta, abstractmethod
from pathlib import Path
from typing import Generic, Type, TypeVar

from aiofiles.tempfile import AsyncBufferedIOBase, AsyncBufferedReader
from aiogoogle.models import Request as AiogoogleRequest
from pydantic import BaseModel
from tygle.client import Client

RequestT = TypeVar("RequestT")


class Request(Generic[RequestT], metaclass=ABCMeta):
    def __init__(self, client: Client, request: AiogoogleRequest):
        self.client = client
        self.request = request

    @abstractmethod
    def post_process(self, response) -> RequestT:
        raise NotImplementedError

    async def as_api_key(self):
        response = await self.client.as_api_key(self)
        return self.post_process(response)

    async def as_user(self):
        response = await self.client.as_user(self)
        return self.post_process(response)

    async def as_service_account(self):
        response = await self.client.as_service_account(self)
        return self.post_process(response)

    async def as_anon(self):
        response = await self.client.as_anon(self)
        return self.post_process(response)


DataT = TypeVar("DataT", bound=BaseModel)


class DataRequest(Request[DataT]):
    def __init__(
        self,
        client: Client,
        request: AiogoogleRequest,
        resource_type: Type[DataT],
    ):
        self.resource_type = resource_type
        super().__init__(client, request)

    def post_process(self, response) -> DataT:
        return self.resource_type.parse_obj(response)


class PathRequest(Request[Path]):
    def post_process(self, response):
        path = response.media_download
        return Path(path)


class BufferRequest(Request[AsyncBufferedReader]):
    def post_process(self, response: AiogoogleRequest) -> AsyncBufferedReader:
        buffer: AsyncBufferedIOBase = response.media_download
        return AsyncBufferedReader(buffer._file, buffer._loop, buffer._executor)
