from sonusai import SonusAIError
from sonusai.mixture.mixdb import MixtureDatabase


def get_offsets(mixdb: MixtureDatabase, mixid: int) -> (int, int, int):
    if mixid >= len(mixdb.mixtures) or mixid < 0:
        raise SonusAIError(f'Invalid mixid: {mixid}')

    i_sample_offset = sum([sub.samples for sub in mixdb.mixtures[:mixid]])
    i_frame_offset = i_sample_offset // mixdb.frame_size
    o_frame_offset = i_sample_offset // mixdb.feature_step_samples

    return i_sample_offset, i_frame_offset, o_frame_offset
