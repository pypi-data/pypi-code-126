from os.path import exists
from os.path import expandvars
from typing import List

import numpy as np
from tqdm import tqdm

from sonusai import SonusAIError
from sonusai.mixture.augmentation import apply_augmentation
from sonusai.mixture.mixdb import MixtureDatabase
from sonusai.mixture.read_audio import read_audio
from sonusai.utils import p_tqdm_map

# NOTE: multiprocessing dictionary is required for run-time performance; using 'partial' is much slower.
MP_DICT = dict()


def build_noise_audios(mixdb: MixtureDatabase, show_progress: bool = False) -> List[List[np.ndarray]]:
    """Build a database of noise audio data."""
    noise_audios = list()
    for file_index in tqdm(range(len(mixdb.noises)), desc='Read noise audio', disable=not show_progress):
        audio_in = read_audio(name=mixdb.noises[file_index].name)
        noise_audios.append(list())
        for augmentation_index, augmentation in enumerate(mixdb.noise_augmentations):
            noise_audios[-1].append(apply_augmentation(audio_in=audio_in, augmentation=augmentation))

    return noise_audios


def build_target_audios(mixdb: MixtureDatabase, show_progress: bool = False) -> List[np.ndarray]:
    """Build a list of target audio data."""
    MP_DICT['mixdb']: MixtureDatabase = mixdb

    indices = list(range(len(mixdb.targets)))
    progress = tqdm(total=len(indices), desc='Read target audio', disable=not show_progress)
    target_audios = p_tqdm_map(_read_target_audio, indices, progress=progress)
    return target_audios


def _read_target_audio(file_index: int) -> np.ndarray:
    """Parallel target audio reader kernel."""
    mixdb: MixtureDatabase = MP_DICT['mixdb']
    return read_audio(name=mixdb.targets[file_index].name)


def check_audio_files_exist(mixdb: MixtureDatabase) -> None:
    """Walk through all the noise and target audio files in a mixture database ensuring that they exist."""
    for file_index in range(len(mixdb.noises)):
        file_name = expandvars(mixdb.noises[file_index].name)
        if not exists(file_name):
            raise SonusAIError(f'Could not find {file_name}')

    for file_index in range(len(mixdb.targets)):
        file_name = expandvars(mixdb.targets[file_index].name)
        if not exists(file_name):
            raise SonusAIError(f'Could not find {file_name}')


def read_raw_target_audio(mixdb: MixtureDatabase,
                          show_progress: bool = False) -> List[np.ndarray]:
    """Read in all audio data beforehand to avoid reading it multiple times in a loop."""
    names = [target.name for target in mixdb.targets]
    progress = tqdm(total=len(names), desc='Read target audio', disable=not show_progress)
    raw_target_audio = p_tqdm_map(read_audio, names, progress=progress)
    progress.close()

    return raw_target_audio
