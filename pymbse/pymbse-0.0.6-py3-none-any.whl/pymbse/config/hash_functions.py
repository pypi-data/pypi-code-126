import hashlib
import json
from pathlib import Path
from typing import Union

import numpy as np


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


def hash_dict(dict_to_hash: dict) -> str:
    """ Function hashing a dictionary with md5 algorithm

    :param dict_to_hash: a dictionary with content to be hashed
    :return: an md5 hash of a dictionary
    """
    return hashlib.md5(json.dumps(dict_to_hash, sort_keys=True, cls=NpEncoder).encode('utf-8')).hexdigest()


def hash_file(abs_path: Union[Path, str]) -> str:
    """Function hashing a file based on its content with md5 hash algorithm
    :param abs_path: an absolute path to a file
    :return: a string with md5 hash
    """
    with open(abs_path, 'rb') as file:
        return hashlib.md5(file.read()).hexdigest()
