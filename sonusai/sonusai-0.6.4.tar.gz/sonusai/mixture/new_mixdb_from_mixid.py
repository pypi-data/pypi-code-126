from copy import deepcopy

from sonusai import SonusAIError
from sonusai.mixture.mixdb import MixtureDatabase
from sonusai.mixture.mixdb import MixtureID
from sonusai.mixture.mixid import get_mixtures_from_mixid
from sonusai.mixture.mixture import set_mixture_offsets


def new_mixdb_from_mixid(mixdb: MixtureDatabase, mixid: MixtureID) -> MixtureDatabase:
    mixdb_out = deepcopy(mixdb)
    mixdb_out.mixtures = get_mixtures_from_mixid(mixdb_out, mixid)
    set_mixture_offsets(mixdb_out)

    if not mixdb_out.mixtures:
        raise SonusAIError(f'Error processing mixid: {mixid}; resulted in empty list of mixtures')

    return mixdb_out
