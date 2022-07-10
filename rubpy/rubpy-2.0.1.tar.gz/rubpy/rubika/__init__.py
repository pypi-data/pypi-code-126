from time import sleep , time
from .encryption import Encryption
from . import connections
from json import dumps , loads
from time import time
from random import randint , choice

__version__ : str = '2.0.0'
__author__ : str = 'Shayan Heidari'
__copyright__ : str = 'CopyRight 2022'

class createMethod(object):
		def __init__(self:str , auth:str) -> int:
			self.auth : str = auth
			self.enc : str = Encryption(auth)
			self.web : str = { "app_name"    : "Main", "app_version" : "4.0.7", "platform"    : "Web", "package"     : "web.rubika.ir", "lang_code"   : "fa" } #   rubika web client
	
		async def createMethod(self , Type:int , Method:str , data:dict):
			if Type == 4:
				...
			else:
				if Type == 5:
					return dumps(
					{"api_version" : "5",
					"auth" : self.auth,
					"data_enc" : self.enc.encrypt(
					dumps({
					"method" : Method,
					"input" : data,
					"client" : self.web
					}))}).encode()
	
	
class Rubika:
		def __init__(self : str , auth : str , displayWelcome : bool = True) -> int:
			if displayWelcome: 
				text : str = f'This library was created by {__author__}, with versions {__version__} and {__copyright__}.\nLibrary activated ...\n\n'
				for char in text:
					print(char , flush = True , end = '')
					sleep(.01)
			self.auth : str = auth # account auth for connect to rubika server
			self.post : str = connections.post
			self.enc : str = Encryption(self.auth)
			self.Method : int = createMethod(self.auth)
			self.url : str = choice([
			'https://messengerg2c26.iranlms.ir' ,
			'https://messengerg2c46.iranlms.ir' ,
			'https://messengerg2c39.iranlms.ir'
			])
	
		async def getChatsUpdate(self:int) -> dict:
			data : str = await self.Method.createMethod(
			5 
			, 'getChatsUpdates', 
			{"state" : str(round(time() - 200))}
			)
			return loads(self.enc.decrypt(loads(await self.post(self.url , data)).get('data_enc'))).get('data').get('chats')
	
		async def sendMessage(self : str , chat_id : str , text : str , message_id : bool = None) -> dict:
			data : dict = await self.Method.createMethod(
			5 
			, 'sendMessage', 
			{
				"object_guid":chat_id,
				"rnd":f"{randint(100000,999999999)}",
				"text":text,
				"reply_to_message_id":message_id
					})
			return loads(self.enc.decrypt(loads(await self.post(self.url , data)).get('data_enc')))
	
		async def banGroupMember(self : str , group_guid : str , user_guid : str ,) -> dict:
			data : str = await self.Method.createMethod(
			5 
			, 'banGroupMember', 
			{
				'action' : 'Set',
				'group_guid' : group_guid,
				'member_guid' : user_guid
			})
			return loads(self.enc.decrypt(loads(await self.post(self.url , data)).get('data_enc')))
	
class client:
		def __init__(self : int , auth : str) -> int:
			try:
				open('answered.txt', 'r').read()
			except FileNotFoundError:
				open('answered.txt', 'w').write('created By Shtyhon :)')
	
			self.auth : str = auth
			self.bot : str = Rubika(self.auth)
	
		async def chats(self : str) -> dict:
			while 1:
				try:
					chats : str = await self.bot.getChatsUpdate()
					for chat in chats:
						if not chat['object_guid']+chat['last_message']['message_id'] in open('answered.txt', 'r').read().split('\n'):
							yield chat
							open('answered.txt','a+').write('\n'+chat['object_guid']+chat['last_message']['message_id'])
				except:pass