import json
import pickle
import joblib
from zipfile import ZipFile, ZIP_DEFLATED, BadZipFile

from insolver.wrappers import (
    InsolverTrivialWrapper,
    InsolverGBMWrapper,
    InsolverRFWrapper,
)
from .glm import InsolverGLMWrapper


wrapper_config = dict(
    glm=InsolverGLMWrapper,
    gbm=InsolverGBMWrapper,
    rf=InsolverRFWrapper,
    trivial=InsolverTrivialWrapper,
)


def load(obj, method=None, binary=True, **kwargs):
    if method == "pickle":
        if binary:
            with open(obj, "rb") as _file:
                return pickle.load(obj, **kwargs)
        else:
            return pickle.loads(obj, **kwargs)
    elif method == "joblib":
        return joblib.load(obj, **kwargs)
    else:
        raise ValueError(f'Invalid method "{method}" argument.')


def load_model(path, **kwargs):
    try:
        with ZipFile(file=path, mode="r", compression=ZIP_DEFLATED) as zip_file:
            filenames = zip_file.namelist()
            if (len(zip_file.filelist) == 2) and ("metadata.json" in filenames):
                metadata = json.loads(zip_file.read("metadata.json"))
                filenames.remove("metadata.json")
                model = zip_file.read(filenames[0])

                init_params = metadata["init_params"]
                init_params.update(init_params.pop("kwargs"))
                wrapper_ = wrapper_config[metadata["algo"]](**init_params)
                wrapper_.model = load(model, method=metadata["saving_method"], binary=False, **kwargs)
                metadata.pop("saving_method")
                wrapper_.metadata = metadata
                return wrapper_
            else:
                raise RuntimeError("Invalid file or model format.")
    except BadZipFile:
        print("Not insolver format.")
