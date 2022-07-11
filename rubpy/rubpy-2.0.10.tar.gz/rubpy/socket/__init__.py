from websocket import create_connection
from json import dumps , loads
from random import choice
from rubpy.encryption import Encryption

''' This library was created
with the efforts of Shython,
you can get the tutorials and
documentation of the
rubpy library on the
Telegram channel @rubika_library,
if you want to support us, go to
the SYTHON GitHub, i.e. mine, and
the repository star of this library, Rubpy
Hit and fork,
thanks for you
Shayan Heydari ! '''

class connect(object):
	def __init__(self , auth : str , displayWelcome : bool = True):
		if displayWelcome:
			...
		self.auth : str = auth
		self.wss : str = choice([
		'wss://jsocket2.iranlms.ir:80' ,
		'wss://msocket1.iranlms.ir:80' ,
		'wss://jsocket3.iranlms.ir:80'
		 ])

	async def connection(self) :
		ws = create_connection(self.wss)
		data : str = dumps({
			"api_version" : "4",
			"auth" : self.auth,
			"data_enc" : "",
			"method" : "handShake"
		})
		ws.send(data)
		while 1:
			try:
				yield loads(ws.recv())
			except : ...

class Client(object) :
	def __init__(self , auth : str) :
		self.auth : str = auth
		self.connect = connect(self.auth)
		self.enc = Encryption(self.auth)

	async def handler(self) :
		while 1:
			try:
				async for data in self.connect.connection():
					if data.get('type') == 'messenger':
						updates : dict = loads(self.enc.decrypt(data.get('data_enc'))).get('chat_updates')
						if not updates == None:
							yield updates
			except:
				...