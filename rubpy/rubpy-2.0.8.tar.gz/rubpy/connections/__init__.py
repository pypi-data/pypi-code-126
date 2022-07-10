from aiohttp import ClientSession
from json import dumps , loads

"""This library was created by shayan heidari....
And This library works with the help of AIOhttp"""

async def get(url:str) -> str:
	async with ClientSession() as session:
		async with session.get(url) as _:
			return _.text()

async def post(url:str , data:dict) -> str:
	async with ClientSession() as _:
		async with _.post(url, data=data) as post:
			return await post.text()