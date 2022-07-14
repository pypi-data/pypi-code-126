
from typing import Union

# Enums
ListOrNoneUnion = Union[list, None]

# Ignore these
class BaseEnum:
	name = None
	value = None
	custom_error_str = None
	description = None
	def __str__(self):
		end_str = self.custom_error_str == None and self.custom_error_str or self.description
		return self.name + " " + str(self.value) + " " + end_str
	def __repr__(self):
		end_str = self.custom_error_str == None and self.custom_error_str or self.description
		return self.name + " " + str(self.value) + " " + end_str
	def __init__(self, value : any, name : str, description : str, custom_error : Union[str, None] = None):
		self.value = value
		self.name = name
		self.description = description
		self.custom_error_str = custom_error

# Enums
EnumItemOrNone = Union[BaseEnum, None]

# Is an Enum itself but also holds Enums inside itself
class EnumParent(BaseEnum):
	__children = {} # dictionary of enums "{ EnumName : EnumItem }"
	__enums = [] # array of enums

	def getEnumByName(self, enumName) -> BaseEnum:
		if self.name == enumName:
			return self
		return self.__children[enumName]

	def getEnumByValue(self, enumValue) -> EnumItemOrNone:
		if self.value == enumValue:
			return self
		for child in self.__enums:
			# if child is the target value, return this item
			if child.value == enumValue:
				return child
			# skip over everything that has a smaller value than this enumItem
			# reducing total search scope
			if child.value < enumValue:
				continue
			# if this node doesn't have children, skip over them
			if hasattr(child, "__children") == None:
				continue
			# see if this parent / enum has the value within themselves
			enumItem = child.getEnumByValue(child.value)
			if enumItem == None:
				continue
			return enumItem
		# could not find the enum
		return None

	def getEnumItems(self) -> ListOrNoneUnion:
		return self.__enums

	def __addEnum(self, child_enum) -> None:
		self.__children[child_enum.name] = child_enum
		self.__enums.extend([child_enum])
		sorted(self.__enums, key=lambda x : x.value)

	def __addChildren(self, child_enums : list) -> None:
		# hashmap
		for child_enum in child_enums:
			self.__children[child_enum.name] = child_enum
		# extend array
		self.__enums.extend(child_enums)
		# sort enums in array with respect to the 'value'
		self.__enums = sorted(self.__enums, key=lambda x : x.value)

	def __init__(self, value : any, name : str, children : list):
		self.value = value
		self.name = name
		self.__addChildren(children)

	property(getEnumByName, __addEnum, None)

# Only import this class here
class Enum:
	# successful request
	Success = BaseEnum(1, "Success", "Successful Request"),
	# the api key is invalid
	Unavailable = BaseEnum(2, "Unavailable", "Unavailable - Check API key validity."),
	# cannot do this request due to no permission for ip
	Unauthorized = BaseEnum(3, "Unauthorized", "Unauthorized Access - Check API key permissions & IP registry."),
	# cannot do this because no permissions on specified universe
	NotAllowed = BaseEnum(4, "NotAllowed", "Not Allowed on specified universe - Check API key permissions."),
	# internal error
	InternalError = BaseEnum(5, "InternalError", "An internal error occured @ Roblox Server")
	# program error
	ProgramError = BaseEnum(6, "ProgramError", "An internal error in the python code has occured")
	# invalid argument
	InvalidArgument = BaseEnum(7, "ArgumentError", "An incorrect argument has been passed.")

Enum = Enum()
