import typing

T = typing.TypeVar('T')
N = typing.TypeVar('N')

class Field(typing.Generic[T]):
    parse:typing.Callable[[T], typing.Any]

    def __init__(self,
        parse:typing.Callable[[T], typing.Any]=None,
        default=None,
        required=False,
        options=None
    ):
        self.parse = parse
        self.default = default
        self.required = required
        self.options = options

class ConfigError(Exception):
    def __init__(self, key:str):
        self.key = key

class ParseError(ConfigError): ...

class OptionError(ConfigError):
    def __init__(self, key:str, value):
        super().__init__(key)
        self.value = value

class RequiredError(ConfigError): ...

FieldsDict = typing.Dict[
    str, 
    typing.Union[
        Field, 
        dict, 
        typing.Type[Field]
    ]
]

class Blueprint(Field[typing.Dict[str, typing.Any]], typing.Generic[T]):
    options = None

    def __init__(self, fields:FieldsDict):
        self._bp = dict()

        for key, value in fields.items():
            if isinstance(value, Field):
                self._bp[key] = value
            elif isinstance(value, dict):
                self._bp[key] = Blueprint(value)
            elif value is Field:
                self._bp[key] = Field()
    
    @property
    def _fields(self):
        for key, field in self._bp.items():
            if isinstance(field, Field):
                yield key, field

    def parse(self, config:typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
        result = dict()

        for key, field in self._fields:
            result[key] = self._parse_item(config, key, field)
        
        return result
    
    def _parse_item(self, config:typing.Dict[str, typing.Any], key:str, field:Field):
        try:
            provided_value = config[key]
        except KeyError:
            if field.required:
                raise RequiredError(key)
            else:
                return field.default

        if field.parse is None:
            parsed_value = provided_value
        else:
            try:
                parsed_value = field.parse(provided_value)
            except Exception as e:
                raise ParseError(key) from e
        
        options = field.options
        is_option = True
        
        if options is None:
            pass
        if isinstance(options, (list, tuple, set)):
            is_option = parsed_value in options
        elif callable(options):
            is_option = options(parsed_value)
        else:
            try:
                options_iter = iter(options)
            except TypeError:
                pass
            else:
                is_option = parsed_value in options_iter
        
        if is_option:
            return parsed_value
        else:
            raise OptionError(key, parsed_value)
    
    @property
    def required(self) -> bool:
        for _, field in self._fields:
            if field.required:
                return True
        
        return False
    
    @property
    def default(self) -> dict:
        config = dict()

        for key, field in self._fields:
            if field.required:
                return None
            else:
                config[key] = field.default

        return config