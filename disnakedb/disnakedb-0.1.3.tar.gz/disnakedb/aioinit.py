import json
from typing import Any
import aiofiles
from .init import Init
default = "db"


class Aioinit(Init):
    def __init__(self, name=default):
        """
        Create database
        """
        super().__init__(name)

    async def get(self, name: str) -> Any:
        """
        Get data
        :param name: name of variable
        :return: Any
        """
        try:
            return self.cache[name]
        except KeyError:
            pass

        async with aiofiles.open(f"{self.name}.json", "r", encoding="utf-8") as reader:
            doc = json.loads(await reader.read())
        try:
            return doc[name]
        except KeyError:
            return None

    async def set(self, name: str, value: Any) -> None:
        """
        Set data
        :param name: name of variable
        :param value: value for variable
        :return: None
        """
        self.cache[name] = value
        async with aiofiles.open(f"{self.name}.json", "r", encoding="utf-8") as reader:
            doc = json.loads(await reader.read())

        doc[name] = value

        async with aiofiles.open(f"{self.name}.json", "w", encoding="utf-8") as writer:
            await writer.write(json.dumps(doc, indent=4))

    async def remove(self, name: str) -> None:
        """
        Remove data
        :param name: name of variable
        :return: None
        """
        try:
            del self.cache[name]
        except KeyError:
            pass

        async with aiofiles.open(f"{self.name}.json", "r", encoding="utf-8") as reader:
            doc = json.loads(await reader.read())

        del doc[name]

        async with aiofiles.open(f"{self.name}.json", "w", encoding="utf-8") as writer:
            await writer.write(json.dumps(doc, indent=4))

    async def sync(self) -> None:
        """
        Sync cache
        :return: None
        """
        async with aiofiles.open(f"{self.name}.json", "r", encoding="utf-8") as reader:
            doc: dict = json.loads(await reader.read())
        for key in doc.keys():
            self.cache[key] = doc[key]

    async def clear(self) -> None:
        """
        Clear cache
        :return: None
        """
        for key in self.cache.keys():
            del self.cache[key]
