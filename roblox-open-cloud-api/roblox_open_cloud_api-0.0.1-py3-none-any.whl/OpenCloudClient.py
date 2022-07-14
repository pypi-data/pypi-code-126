
# Imports
import json

from warnings import warn

from roblox_open_cloud.Enums import Enum, BaseEnum
from roblox_open_cloud.Requests import RequestsClass

# Constants
MESSAGING_SERVICE_BASE_URL = "https://apis.roblox.com/messaging-service/v1/universes/{}/topics/{}"

# Class
class Client:
	__requestsInstance = None

	# Redirecting Functions 
	def setCookie(self, cookie_name : str, cookie_value : any, domain : str) -> None:
		self.__requestsInstance.setCookie(cookie_name, cookie_value, domain)

	def setHeader(self, header_name : str, header_value : any) -> None:
		self.__requestsInstance.setHeader(header_name, header_value)

	# Class Functions
	def checkKeyValidity(self) -> bool:
		#raise NotImplementedError("Check API Key Validity is not implemented!")
		return True, "Valid Key"

	# Primary Functions
	def PostOnMessagingService(self, universe_id=0, topic=None, data=None) -> BaseEnum:
		print(universe_id, topic, data)
		if type(universe_id) != int:
			return BaseEnum(12, "ArgumentError", "Invalid Argument", custom_error="Universe Id is invalid.")
		if type(data) != str:
			return BaseEnum(13, "ArgumentError", "Invalid Argument", custom_error="Data is invalid.")
		# get a JSON string of the data
		content = json.dumps({"message" : data})
		# endcode it
		content = content.encode()
		# post to the universe id under the topic
		try:
			response = self.__requestsInstance.post(MESSAGING_SERVICE_BASE_URL.format(universe_id, topic), content)
		except:
			return None, Enum.ProgramError
		# status code custom enum message
		response_enum = Enum.ProgramError
		if response.status_code == 200:
			response_enum = Enum.Success
		elif response.status_code == 401:
			response_enum = Enum.Unavailable
		elif response.status_code == 403:
			response_enum = Enum.Unauthorized
		elif response.status_code == 500:
			response_enum = Enum.InternalError
		if response_enum != Enum.Success:
			warn(response_enum, response.content)
		return response_enum

	# Init
	def __init__(self, api_key=None, cookies=None, headers=None):
		self.__requestsInstance = RequestsClass(api_key=api_key, cookies=cookies, headers=headers)
