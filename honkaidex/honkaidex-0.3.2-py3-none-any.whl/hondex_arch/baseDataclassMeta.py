from dataclasses import dataclass
import dataclasses
import typing

class baseDataclassMeta(type):
    _instances = {}
    _nicknames_refs = {}
    _dataclass_fields = {}
    _inited = []

    def _init(cls):
        if cls in cls._inited:
            return

        if cls not in cls._instances:
            cls._instances[cls] = {}
        if cls not in cls._dataclass_fields:
            cls._dataclass_fields[cls] = [x.name for x in dataclasses.fields(cls)]

        cls._inited.append(cls)

    def _append_nickname(cls, nickname : str, name : str): 
        cls._init()

        if nickname in cls._instances[cls]:
            raise ValueError("nickname cannot be the same as an existing name")
        
        if nickname not in cls._nicknames_refs:
            cls._nicknames_refs[nickname] = set()

        for item in cls._nicknames_refs[nickname]:
            if item[0] == cls:
                raise ValueError("duplicate nickname with same class type")
        
        data : set = cls._nicknames_refs[nickname]
        data.add((cls, name))
    
    def get_by_name(cls, name : str):
        cls._init()

        if name not in cls._instances[cls]:
            return None

        return cls._instances[cls][name]

    def get_by_nickname(cls, nickname : str, limit_to_type : bool = False) -> typing.List[typing.Tuple[type, object]]:
        cls._init()

        if nickname not in cls._nicknames_refs and not limit_to_type:
            return []
        elif nickname not in cls._nicknames_refs and limit_to_type:
            return None

        nickname_refs = []

        for item in cls._nicknames_refs[nickname]:
            if limit_to_type and item[0] == cls:
                return item[1]
            name = item[1]
            clstype = item[0]
            if name not in cls._instances[clstype]:
                continue
            nickname_refs.append((clstype, cls._instances[clstype][name]))
        
        return nickname_refs

    def get_fields(cls):
        """
        get all field names of the dataclass

        Returns:
            list: list of field names
        """
        cls._init()
        return cls._dataclass_fields[cls]
    
    def _del(cls, obj):
        cls._init()

        if obj.name in cls._instances[cls]:
            del cls._instances[cls][obj.name]

        for nick in obj.nicknames:
            if nick in cls._nicknames_refs:
                set_data : set = cls._nicknames_refs[nick]
                set_data.pop({cls, obj.name})

        del obj

    def __call__(cls, *args, **kwargs):
        cls._init()

        name : str = kwargs.pop("name", None)

        if name is None:
            raise ValueError("name is required")

        key_name = name.lower().strip()

        # check instance
        if key_name in cls._instances[cls]:
            raise ValueError("name cannot be the same as an existing name")

        # extract list and convert into tuple
        for key, val in kwargs.items():
            if isinstance(val, typing.Iterable) and not isinstance(val, tuple) and not isinstance(val, str):
                kwargs[key] = tuple(val)

        if "nicknames" not in kwargs:
            kwargs["nicknames"] = tuple()

        instance = super().__call__(*args, **kwargs, name=key_name)

        # append instance
        cls._instances[cls][key_name] = instance

        # parse nicknames
        nicknames : typing.List[str] = kwargs.pop("nicknames", [])
        for nick in nicknames:
            nick = nick.lower().strip()
            cls._append_nickname(nick, key_name)
        return instance

