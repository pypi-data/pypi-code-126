from sonusai.mixture.mixdb import MixtureDatabase
from sonusai.mixture.mixdb import MixtureID
from sonusai.mixture.mixid import convert_mixid_to_list
from sonusai.mixture.mixture import get_feature_frames_in_mixture
from sonusai.mixture.segment import Segment


def get_file_frame_segments(mixdb: MixtureDatabase, mixid: MixtureID = ':') -> dict:
    _mixid = convert_mixid_to_list(mixdb, mixid)
    file_frame_segments = dict()
    for m in _mixid:
        file_frame_segments[m] = Segment(mixdb.mixtures[m].o_frame_offset,
                                         get_feature_frames_in_mixture(mixdb, m))
    return file_frame_segments
