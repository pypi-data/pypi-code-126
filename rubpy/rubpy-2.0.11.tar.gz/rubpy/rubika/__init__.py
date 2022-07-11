from time import sleep , time
from rubpy.encryption import Encryption
import rubpy.connections
from json import dumps , loads
from time import time
from random import randint , choice
from rubpy.tools import Tools
from rubpy.createMethod import createMethod

__version__ : str = '2.0.10'
__author__ : str = 'Shayan Heidari'
__copyright__ : str = 'CopyRight 2022'


class Rubika(object):
	def __init__(self : str , auth : str , displayWelcome : bool = True) -> int:
		if displayWelcome: 
			text : str = f'This library was created by {__author__}, with versions {__version__} and {__copyright__}.\nLibrary activated ...\n\n'
			for char in text:
				print(char , flush = True , end = '')
				sleep(.01)
		self.auth : str = auth # account auth for connect to rubika server
		self.post : str = rubpy.connections.post
		self.enc : str = Encryption(self.auth)
		self.Method : int = createMethod(self.auth)
		self.url : str = choice([
			'https://messengerg2c26.iranlms.ir' ,
			'https://messengerg2c46.iranlms.ir' ,
			'https://messengerg2c39.iranlms.ir'
			])
		self.Tool = Tools()
		self.uploaderFile = rubpy.connections.upload
	
	async def getChatsUpdate(self:int) -> dict:
		'''This function is for
		receiving the latest messages
		that have been sent to your account...'''
		data : str = await self.Method.createMethod(
		5 ,
		'getChatsUpdates', 
		{"state" : str(round(time() - 200))}
		)
		return loads(self.enc.decrypt(loads(await self.post(self.url , data)).get('data_enc'))).get('data').get('chats')

	async def getGroupAdmins(self , group_guid : str) -> dict:
		'''
			you can get a group admins with guid
		'''
		data : str = await self.Method.createMethod(
		5 ,
		'getGroupAdminMembers' , 
		{
			"group_guid" : group_guid
		})
		return loads(self.enc.decrypt(loads(await self.post(self.url , data)).get('data_enc'))).get('data').get('in_chat_members')

	async def sendMessage(self : str , chat_id : str , text : str , metaData = None , message_id : bool = None) -> dict:
		'''Using this function, you can send
		a text message to the desired
		chat, in the first argument,
		you must enter the chat ID where
		the message is to be sent (GUID)
		and in the second argument,
		enter your message as a string
		in the last argument.
		That is, thirdly, if you are going
		to reply to the message,
		click on the message ID,
		the message that is going
		to be replied to (not required).'''
		Input : dict = {
			"object_guid" : chat_id,
			"rnd" : f"{randint(100000,999999999)}",
			"text" : text,
			"reply_to_message_id" : message_id
		}
		if metaData != None:
			Input['metadata'] = {'meta_data_parts' : metaData}
		mode : list = ['**' , '__' , '``']
		for check in mode:
			if check in text:
				metadata : list = self.Tool.textAnalysis(text)
				Input['metadata'] = {'meta_data_parts' : metadata[0]}
				Input['text'] = metadata[1]
		data : dict = await self.Method.createMethod(5 , 'sendMessage', Input)
		return loads(self.enc.decrypt(loads(await self.post(self.url , data)).get('data_enc')))

	async def deleteMessages(self , chat_id : str , messages_id : list) -> dict:
		'''
			This function is delete message from chat
		'''
		data : str = await self.Method.createMethod(
		5 ,
		"deleteMessages",
		{
			"object_guid" : chat_id,
			"message_ids" : messages_id,
			"type" : "Global"
		})
		return loads(self.enc.decrypt(loads(await self.post(self.url , data)).get('data_enc'))).get('data').get('chats')

	async def sendGroupVoiceChatActivity(self , group_guid : str , voice_chat_id : str) -> dict:
		'''
			This function is send Group Voice Chat
			Activity for send Voice
		'''
		data : str = await self.Method.createMethod(
		5 ,
		'sendGroupVoiceChatActivity' , 
		{
			"activity" : "Speaking",
			"chat_guid" : group_guid,
			"voice_chat_id" : voice_chat_id,
		})
		return loads(self.enc.decrypt(loads(await self.post(self.url , data)).get('data_enc')))

	async def getGroupVoiceChatUpdates(self , group_guid : str , voice_chat_id : str) -> dict:
		'''
			Get Group Voice Chat Updates with group guid and voice chat id
			you can write your group guid in the one arg
			you can write your voice chat id in the two arg
		'''
		data : str = await self.Method.createMethod(
		5 ,
		"getGroupVoiceChatUpdates" , 
		{
			"state" : randint(1000000000 , 9999999999),
			"chat_guid" : group_guid,
			"voice_chat_id" : voice_chat_id,
		})
		return loads(self.enc.decrypt(loads(await self.post(self.url , data)).get('data_enc'))).get('data')

	async def requestSendFile(self , file_name : str , size : str , mime : str):
		"""
			This method is used when
			you want to upload a file
			to the Rubika's server
		"""
		Trying : int = 0
		while Trying != 5:
			try:
				data : str = await self.Method.createMethod(
				5 ,
				"requestSendFile" , 
				{
					"file_name" : file_name,
					"size" : size,
					"mime" : mime,
				})
				return loads(self.enc.decrypt(loads(await self.post(self.url , data)).get('data_enc'))).get('data')
			except :
				Trying += 1

	async def uploadFile(self , url : str , access_hash_send : str , file_id : str , byte : bytes):		
		"""
			This method is used to upload
			any type of file in Rubika
			server, this is a main method
			for uploads.
		"""
		header : dict = {
			"access-hash-send" : access_hash_send,
			"file-id" : file_id,
			"part-number" : "1",
			"total-part" : "1",
			"chunk-size" : str(len(byte)),
			"auth" : self.auth
		}
		result = loads(await self.uploaderFile(
		url,
		byte,
		header
		))
		return result.get('data').get('access_hash_rec')

	async def sendImage(self , chat_id : str , file_id : str , mime : str , dc_id : str , access_hash_rec : str , file_name : str , size : str , thumbnail : bytes , width : str , height : str , caption : bool = None , message_id : bool = None) -> dict:
		Input : dict = {
			"object_guid" : chat_id,
			"rnd" : f"{randint(100000 , 999999)}",
			"text" : caption,
			"reply_to_message_id" : message_id,
			"file_inline" : {
				"access_hash_rec" : str(access_hash_rec),
				"dc_id" : str(dc_id),
				"file_id" : str(file_id),
				"file_name" : file_name,
				"mime" : mime,
				"size" : size,
				"width" : width,
				"height" : height,
				"thumb_inline" : thumbnail,
				"type" : "Image"
		}}
		mode : list = ['**' , '__' , '``']
		for check in mode:
			if check in caption:
				metadata : list = self.Tool.textAnalysis(caption)
				Input['metadata'] = {'meta_data_parts' : metadata[0]}
				Input['text'] = metadata[1]
		data : dict = await self.Method.createMethod(5 , 'sendMessage', Input)
		return loads(self.enc.decrypt(loads(await self.post(self.url , data)).get('data_enc')))

	async def sendFile(self , chat_id : str , access_hash_rec : str , dc_id : str , file_id : str , file_name : str , mime : str , size : str , caption : bool = None , message_id : bool = None) -> dict:
		"""
			This is the main method for
			sending files with mp3, mp4,
			zip, etc. extensions, it can be
			said that it is an
			attachment/documemt sending method!
		"""
		Input : dict = {
			"object_guid" : chat_id,
			"rnd" : f"{randint(100000 , 999999)}",
			"text" : caption,
			"reply_to_message_id" : message_id,
			"file_inline" : {
				"access_hash_rec" : str(access_hash_rec),
				"dc_id" : str(dc_id),
				"file_id" : str(file_id),
				"file_name" : file_name,
				"mime" : mime,
				"size" : size,
				"type" : "File"
		}}
		mode : list = ['**' , '__' , '``']
		for check in mode:
			if check in caption:
				metadata : list = self.Tool.textAnalysis(caption)
				Input['metadata'] = {'meta_data_parts' : metadata[0]}
				Input['text'] = metadata[1]
		data : dict = await self.Method.createMethod(5 , 'sendMessage', Input)
		return loads(self.enc.decrypt(loads(await self.post(self.url , data)).get('data_enc')))

	async def editMessage(self , chat_id : str , message_id : str , text : str , metaData = None) -> dict:
		'''This method is for editing messages and working with this method is very simple; Enter the chat ID in the first argument, the message ID in the second argument, and the new text in the third argument...'''
		Input : dict = {
			"message_id" : message_id,
			"object_guid" : chat_id,
			"text" : text,
		}
		mode : list = ['**' , '__' , '``']
		for check in mode:
			if check in text:
				metadata : list = self.Tool.textAnalysis(text)
				Input['metadata'] = {'meta_data_parts' : metadata[0]}
				Input['text'] = metadata[1]
		if metaData != None:
			Input['metadata'] = {'meta_data_parts' : metaData}
		data : dict = await self.Method.createMethod(5 , 'editMessage', Input)
		return loads(self.enc.decrypt(loads(await self.post(self.url , data)).get('data_enc')))

	async def banGroupMember(self : str , group_guid : str , user_guid : str ,) -> dict:
		'''You can remove a person
		from your group by using
		this function, just enter the
		group ID (GUID) in the first
		argument and the user ID in
		the second argument.'''
		# bot.banGroupMember('Group Guid' , 'User Guid')
		data : str = await self.Method.createMethod(
			5 ,
			'banGroupMember', 
			{
			'action' : 'Set',
			'group_guid' : group_guid,
			'member_guid' : user_guid
		})
		return loads(self.enc.decrypt(loads(await self.post(self.url , data)).get('data_enc')))

	async def searchInChannelMembers(self , channel_guid : str , search_text : str) -> dict:
		data : str = await self.Method.createMethod(
			5 ,
			'getChannelAllMembers', 
			{
			'channel_guid' : channel_guid,
			'search_text' : search_text
		})
		return loads(self.enc.decrypt(loads(await self.post(self.url , data)).get('data_enc')))

	async def checkMemberInChannel(self , channel_guid : str , search_text : str , member_id : str) -> bool:
		data : str = await self.Method.createMethod(
			5 ,
			'getChannelAllMembers', 
			{
			'channel_guid' : channel_guid,
			'search_text' : search_text
		})
		get_data : dict = loads(self.enc.decrypt(loads(await self.post(self.url , data)).get('data_enc'))).get('data').get('in_chat_members')
		for check in get_data:
			if check['username'] != '':
				if check['username'] == member_id:
					return True
			else:
				return 'No UserName!'
		return False

	async def forwardMessages(self , from_guid : str , messages_id : list , to_guid : str) -> dict:
		data : str = await self.Method.createMethod(
		5 ,
		"forwardMessages",
		{
			"from_object_guid" : from_guid,
			"message_ids": messages_id,
			"rnd": f"{randint(100000,999999999)}",
			"to_object_guid": to_guid
		})
		return loads(self.enc.decrypt(loads(await self.post(self.url , data)).get('data_enc')))

	async def getGroupInfo(self , group_guid : str) -> dict:
		data : str = await self.Method.createMethod(
			5 ,
			"getGroupInfo", 
			{
			'group_guid' : group_guid
		})
		return loads(self.enc.decrypt(loads(await self.post(self.url , data)).get('data_enc'))).get('data')

	async def getGroupLastMessageId(self , group_guid : str) -> dict:
		data : str = await self.Method.createMethod(
			5 ,
			"getGroupInfo", 
			{
			'group_guid' : group_guid
		})
		return loads(self.enc.decrypt(loads(await self.post(self.url , data)).get('data_enc'))).get('data').get('chat').get('last_message_id')

	async def getChannelInfo(self, channel_guid : str) -> dict:
		data : str = await self.Method.createMethod(
			5 ,
			"getChannelInfo", 
			{
			'channel_guid' : channel_guid,
		})
		return loads(self.enc.decrypt(loads(await self.post(self.url , data)).get('data_enc'))).get('data').get('channel')

	async def getMessages(self , chat_id : str , middle_message_id : str) -> dict:
		return loads(self.enc.decrypt(loads(await self.post(
		self.url ,
		await self.Method.createMethod(
			5 
			, 'getMessagesInterval', 
			{
			'object_guid' : chat_id,
			'middle_message_id' : middle_message_id
			})
		)).get('data_enc'))).get('data').get('messages')

	async def getGroupLink(self , group_guid : str) -> str:
		data : str = await self.Method.createMethod(
			5 ,
			"getGroupLink", 
			{
			'group_guid' : group_guid,
		})
		return loads(self.enc.decrypt(loads(await self.post(self.url , data)).get('data_enc'))).get("data").get("join_link")

class client(object):
	def __init__(self : int , auth : str) -> int:
		try:
			open('answered.txt', 'r').read()
		except FileNotFoundError:
			open('answered.txt', 'w').write('created By Shtyhon :)')
	
		self.auth : str = auth
		self.bot : str = Rubika(self.auth)
	
	async def chats(self : str) -> dict:
		'''This function in the client class , is
		a handler to receive the
		latest messages using
		the getChatsUpdate method.'''
		while 1:
			try:
				chats : str = await self.bot.getChatsUpdate()
				for chat in chats:
					if not chat['object_guid']+chat['last_message']['message_id'] in open('answered.txt', 'r').read().split('\n'):
						yield chat
						open('answered.txt','a+').write('\n'+chat['object_guid']+chat['last_message']['message_id'])
			except :
				...