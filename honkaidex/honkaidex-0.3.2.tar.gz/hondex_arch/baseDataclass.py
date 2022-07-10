import dataclasses
import hondex_arch
from hondex_arch.baseDataclassMeta import baseDataclassMeta
import typing
from fuzzywuzzy import process

@dataclasses.dataclass(frozen=True)
class BaseDataclass(metaclass=baseDataclassMeta):
    name : str
    nicknames : typing.Tuple[str]

    @classmethod
    def create(cls, **kwargs):
        return cls(**kwargs)

    @classmethod
    def create_with_sanitize(cls, **kwargs):
        """
        create a new instance that filters out unwanted keys
        """
        dcfields = [x.name for x in dataclasses.fields(cls)]
        return cls(**{k:v for k,v in kwargs.items() if k in dcfields})

    @classmethod
    def get_all(cls):
        return cls._instances.get(cls, {})

    @classmethod
    def iterate_all(cls):
        for val in cls._instances[cls].values():
            yield val

    @classmethod
    def get_all_fields(cls, field_name : str):
        if field_name not in cls.get_fields():
            raise ValueError(f"{field_name} is not a field of {cls.__name__}")
        
        ret = []
        for val in cls.iterate_all():
            val = getattr(val, field_name, None)
            if val is not None:
                ret.append(val)

        return ret

    @classmethod
    def iterate_all_fields(cls, field_name : str, ret_object=False):
        if field_name not in cls.get_fields():
            raise ValueError(f"{field_name} is not a field of {cls.__name__}")
        
        for val in cls._instances[cls].values():
            x = getattr(val, field_name, None)
        

            if not x:
                continue
            
            if ret_object:
                yield x, val
            else:
                yield x
        
    @classmethod
    def match_all(cls,func : typing.Callable, yield_only : bool = False):
        ret = []
        for val in cls.iterate_all():
            if not func(val):
                continue
        
            if yield_only:
                yield val
                continue

            ret.append(val)

        if yield_only:
            return
        return ret
                
    @classmethod
    def match_fields(cls, func : typing.Callable, field_name : str, yield_only : bool = False):
        ret = []
        for val in cls.iterate_all_fields(field_name):
            if not func(val):
                continue
        
            if yield_only:
                yield val
                continue

            ret.append(val)

        if yield_only:
            return
        return ret

    @classmethod
    def get(cls, **kwargs):

        for val in cls.iterate_all():
            if all(getattr(val, k) == v for k,v in kwargs.items()):
                return val
        return None

    @classmethod
    def fuzzy_match_field(cls, field_name : str, query, limit : int = 1, confidence : int = 90):
        if field_name not in cls.get_fields():
            raise ValueError(f"{field_name} is not a field of {cls.__name__}")

        match_maps = {}
        for field_val, item in cls.iterate_all_fields(field_name, ret_object=True):
            if query == field_val:
                return item

            match_maps[field_val] = item

        results = process.extractBests(query, list(match_maps.keys()), limit=limit)

        ret = []
        for result in results:
            if result[1] == 100:
                return match_maps[result[0]]
            if result[1] < confidence:
                continue
            ret.append(match_maps[result[0]])

        if not results:
            return None

        return ret

    @classmethod
    def match_name(cls, query : str, confidence : int = 90):
        query = query.lower().strip()
        
        val = cls.get_by_name(query)
        if val is not None:
            return val
        
        val = cls.get_by_nickname(query, True)
        if val is not None:
            return val

        all_names = cls._instances[cls].keys()
        results = process.extractBests(query, all_names, limit=1)

        if not results:
            return None

        if results[0][1] < confidence:
            return None

        return cls.get_by_name(results[0][0])


    @classmethod
    def from_json(cls, json_data, force : bool = False):
        if not force:
            json_data = {k:v for k,v in json_data.items() if k not in cls.get_all()}

        for key, val in json_data.items():
            if "name" not in val:
                val["name"] = key

            cls.create_with_sanitize(**val)

    @classmethod
    def init(cls):
        data = hondex_arch.load_file(cls.__name__)