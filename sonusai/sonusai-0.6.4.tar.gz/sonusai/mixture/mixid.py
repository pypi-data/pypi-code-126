import json
from os.path import exists
from typing import List

from sonusai import SonusAIError
from sonusai.mixture.mixdb import MixtureDatabase
from sonusai.mixture.mixdb import MixtureID
from sonusai.mixture.mixdb import Mixtures


def load_mixid(mixdb: MixtureDatabase, name: str = None) -> List[int]:
    if name is None:
        mixid = list(range(len(mixdb.mixtures)))
    else:
        if not exists(name):
            raise SonusAIError(f'{name} does not exist')

        with open(file=name, mode='r', encoding='utf-8') as f:
            mixid = json.load(f)
            if not isinstance(mixid, dict) or 'mixid' not in mixid:
                raise SonusAIError(f'Could not find ''mixid'' in {name}')
            mixid = mixid['mixid']

    return mixid


def convert_mixid_to_list(mixdb: MixtureDatabase, mixid: MixtureID = None) -> List[int]:
    mixid_out = mixid

    if mixid_out is None:
        return list(range(len(mixdb.mixtures)))

    if isinstance(mixid_out, str):
        try:
            mixid_out = eval(f'{list(range(len(mixdb.mixtures)))}[{mixid_out}]')
        except NameError:
            return []

    if not all(isinstance(x, int) and x < len(mixdb.mixtures) for x in mixid_out):
        return []

    return mixid_out


def get_mixtures_from_mixid(mixdb: MixtureDatabase, mixid: MixtureID = None) -> Mixtures:
    return [mixdb.mixtures[i] for i in convert_mixid_to_list(mixdb, mixid)]
