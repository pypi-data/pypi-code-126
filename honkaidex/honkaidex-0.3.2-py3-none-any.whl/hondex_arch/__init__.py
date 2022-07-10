from hondex_arch.baseDataclass import BaseDataclass
from hondex_arch.baseDataclassMeta import baseDataclassMeta
import orjson
# get package path
import os
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_dir = os.path.join(base_dir, "hondex_model")
db_dir = os.path.join(base_dir, "hondex_db")

def load_file(ty : str):
    ty = ty[0].lower() + ty[1:]
    json_file = os.path.join(db_dir, ty + ".json")

    if not os.path.exists(json_file):
        with open(json_file, "w") as f:
            f.write("{}")

    with open(json_file, "rb") as f:
        return orjson.loads(f.read())

def get_file_path(ty : str):
    ty = ty[0].lower() + ty[1:]
    json_file = os.path.join(db_dir, ty + ".json")
    return json_file

def load_model(ty : str):
    model_file = os.path.join(model_dir, ty + ".py")

    if not os.path.exists(model_file):
        raise ValueError(f"{model_file} does not exist")

    import importlib
    mod = importlib.import_module(f"hondex_model.{ty}")
    cls_ = getattr(mod, ty[0].capitalize()+ty[1:])
    # if not dataclass
    if not hasattr(cls_, "__dataclass_fields__"):
        raise ValueError(f"{model_file} is not a dataclass")

    if not hasattr(cls_, "from_json"):
        raise ValueError(f"{model_file} does not have from_json")

    return cls_