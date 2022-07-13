import json
from dataclasses import dataclass
from os.path import exists
from os.path import splitext
from typing import List
from typing import Optional
from typing import Union

import h5py

from sonusai import SonusAIError
from sonusai.mixture.dataclasses_sonusai import DataClassSonusAIMixin


@dataclass(frozen=True)
class TruthSetting(DataClassSonusAIMixin):
    index: Optional[List[int]] = None
    function: Optional[str] = None
    config: Optional[dict] = None


TruthSettings = List[TruthSetting]

OptionalNumberStr = Optional[Union[float, int, str]]
OptionalListNumberStr = Optional[List[Union[float, int, str]]]


@dataclass
class Augmentation(DataClassSonusAIMixin):
    normalize: OptionalNumberStr = None
    pitch: OptionalNumberStr = None
    tempo: OptionalNumberStr = None
    gain: OptionalNumberStr = None
    eq1: OptionalListNumberStr = None
    eq2: OptionalListNumberStr = None
    eq3: OptionalListNumberStr = None
    lpf: OptionalNumberStr = None
    count: Optional[int] = None
    mixup: Optional[int] = 1


Augmentations = List[Augmentation]


@dataclass(frozen=True)
class TargetFile(DataClassSonusAIMixin):
    name: str
    duration: float
    truth_settings: TruthSettings
    augmentations: Optional[Augmentations] = None
    class_balancing_augmentation: Optional[Augmentation] = None


TargetFiles = List[TargetFile]


@dataclass
class AugmentedTarget(DataClassSonusAIMixin):
    target_file_index: int
    target_augmentation_index: int


AugmentedTargets = List[AugmentedTarget]


@dataclass(frozen=True)
class NoiseFile(DataClassSonusAIMixin):
    name: str
    duration: float
    augmentations: Optional[Augmentations] = None


NoiseFiles = List[NoiseFile]

ClassCount = List[int]


@dataclass
class Mixture(DataClassSonusAIMixin):
    target_file_index: List[int] = None
    noise_file_index: int = None
    noise_offset: int = None
    target_augmentation_index: List[int] = None
    noise_augmentation_index: int = None
    snr: float = None
    samples: int = None
    target_gain: List[int] = None
    class_count: ClassCount = None
    target_snr_gain: float = None
    noise_snr_gain: float = None
    i_sample_offset: Optional[int] = None
    i_frame_offset: Optional[int] = None
    o_frame_offset: Optional[int] = None


Mixtures = List[Mixture]

MixtureID = Union[str, List[int]]


@dataclass
class MixtureDatabase(DataClassSonusAIMixin):
    class_balancing: Optional[bool] = False
    class_balancing_augmentation: Optional[Augmentation] = None
    class_count: ClassCount = None
    class_labels: List[str] = None
    class_weights_threshold: List[float] = None
    exhaustive_noise: Optional[bool] = True
    feature: str = None
    feature_samples: int = None
    feature_step_samples: int = None
    first_cba_index: Optional[int] = None
    frame_size: int = None
    mixtures: Mixtures = None
    noise_augmentations: Augmentations = None
    noises: NoiseFiles = None
    num_classes: int = None
    seed: Optional[int] = 0
    snrs: List[float] = None
    target_augmentations: Augmentations = None
    targets: TargetFiles = None
    truth_mutex: bool = None
    truth_reduction_function: str = None
    truth_settings: TruthSettings = None


def _read_mixdb(name: str) -> str:
    if not exists(name):
        raise SonusAIError(f'{name} does not exist')

    ext = splitext(name)[1]

    if ext == '.json':
        with open(file=name, mode='r', encoding='utf-8') as f:
            return f.read()

    if ext == '.h5':
        with h5py.File(name=name, mode='r') as f:
            return f.attrs['mixdb']

    raise SonusAIError(f'Do not know how to load mixdb from {name}')


def mixdb_from_str(data: str) -> MixtureDatabase:
    return MixtureDatabase.from_dict(json.loads(data))


def load_mixdb(name: str) -> MixtureDatabase:
    return mixdb_from_str(_read_mixdb(name))
