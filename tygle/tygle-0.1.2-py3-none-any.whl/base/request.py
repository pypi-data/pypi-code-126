from abc import ABCMeta, abstractmethod
from io import BytesIO
from pathlib import Path
from typing import Generic, Type, TypeVar

from aiofiles.tempfile import TemporaryFile
from aiogoogle.models import MediaDownload
from aiogoogle.models import Request as AiogoogleRequest
from aiogoogle.models import Response as AiogoogleResponse
from pydantic import BaseModel
from tygle.client import Client

RequestT = TypeVar("RequestT")


class Request(Generic[RequestT], metaclass=ABCMeta):
    def __init__(self, client: Client, request: AiogoogleRequest):
        self.client = client
        self.request = request

    @abstractmethod
    async def pre_process(self, request: AiogoogleRequest):
        raise NotImplementedError

    @abstractmethod
    async def post_process(
        self, request: AiogoogleRequest, response: AiogoogleResponse
    ) -> RequestT:
        raise NotImplementedError

    async def as_api_key(self):
        await self.pre_process(self.request)
        response = await self.client.as_api_key(self)
        return await self.post_process(self.request, response)

    async def as_user(self):
        await self.pre_process(self.request)
        response = await self.client.as_user(self)
        return await self.post_process(self.request, response)

    async def as_service_account(self):
        await self.pre_process(self.request)
        response = await self.client.as_service_account(self)
        return await self.post_process(self.request, response)

    async def as_anon(self):
        await self.pre_process(self.request)
        response = await self.client.as_anon(self)
        return await self.post_process(self.request, response)


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

    async def pre_process(self, request: AiogoogleRequest):
        pass

    async def post_process(
        self, request: AiogoogleRequest, response: AiogoogleResponse
    ):
        return self.resource_type.parse_obj(response.json)


class PathRequest(Request[Path]):
    async def pre_process(self, request: AiogoogleRequest):
        pass

    async def post_process(
        self, request: AiogoogleRequest, response: AiogoogleResponse
    ):
        return Path(response.download_file)


class BufferRequest(Request[BytesIO]):
    async def pre_process(self, request: AiogoogleRequest):
        request.temporary_file = TemporaryFile("wb+")
        pipe_to = await request.temporary_file.__aenter__()
        request.media_download = MediaDownload(pipe_to=pipe_to)

    async def post_process(
        self, request: AiogoogleRequest, response: AiogoogleResponse
    ):
        await response.pipe_to.seek(0)
        contents = await response.pipe_to.read()
        buffer = BytesIO(contents)
        await request.temporary_file.__aexit__(None, None, None)
        return buffer
