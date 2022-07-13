from typing import List

import numpy as np

from sonusai import SonusAIError
from sonusai.mixture.augmentation import apply_augmentation
from sonusai.mixture.generate_truth import generate_truth
from sonusai.mixture.get_next_noise import get_next_noise
from sonusai.mixture.mixdb import Mixture
from sonusai.mixture.mixdb import MixtureDatabase


def get_target_noise_audio(mixdb: MixtureDatabase,
                           mixture: Mixture,
                           target_audios: List[np.ndarray],
                           noise_audios: List[List[np.ndarray]]) -> (List[np.ndarray], np.ndarray):
    """Apply augmentations and return augmented target and noise data."""
    target_file_index = mixture.target_file_index
    target_augmentation_index = mixture.target_augmentation_index
    if len(target_file_index) != len(target_augmentation_index):
        raise SonusAIError('target_file_index and target_augmentation_index are not the same length')

    if mixture.samples % mixdb.frame_size != 0:
        raise SonusAIError(f'Number of samples in mixture is not a multiple of {mixdb.frame_size}')

    target_audio = list()
    for idx in range(len(mixture.target_file_index)):
        target_augmentation = mixdb.target_augmentations[target_augmentation_index[idx]]

        audio_in = target_audios[target_file_index[idx]]
        audio_out = apply_augmentation(audio_in=audio_in,
                                       augmentation=target_augmentation,
                                       length_common_denominator=mixdb.feature_step_samples)

        audio_out = np.array(np.single(audio_out) * mixture.target_snr_gain, dtype=np.int16)

        pad = mixture.samples - len(audio_out)
        audio_out = np.pad(audio_out,
                           (0, pad),
                           mode='constant',
                           constant_values=0)

        target_audio.append(audio_out)

    noise_file_index = mixture.noise_file_index
    noise_augmentation_index = mixture.noise_augmentation_index
    audio_in = noise_audios[noise_file_index][noise_augmentation_index]
    noise_audio, _ = get_next_noise(offset_in=mixture.noise_offset,
                                    length=mixture.samples,
                                    audio_in=audio_in)

    noise_audio = np.array(np.single(noise_audio) * mixture.noise_snr_gain, dtype=np.int16)

    return target_audio, noise_audio


def get_audio_and_truth_t(mixdb: MixtureDatabase,
                          mixture: Mixture,
                          target_audios: List[np.ndarray],
                          noise_audios: List[List[np.ndarray]],
                          compute_truth: bool = True,
                          compute_segsnr: bool = False,
                          frame_based_segsnr: bool = False) \
        -> (np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray):
    target_audio, noise_audio = get_target_noise_audio(mixdb=mixdb,
                                                       mixture=mixture,
                                                       target_audios=target_audios,
                                                       noise_audios=noise_audios)

    truth_t = generate_truth(mixdb=mixdb,
                             mixture=mixture,
                             target_audio=target_audio,
                             compute=compute_truth)

    target_audio = sum(target_audio)

    segsnr = generate_segsnr(mixdb=mixdb,
                             mixture=mixture,
                             target_audio=target_audio,
                             noise_audio=noise_audio,
                             compute=compute_segsnr,
                             frame_based=frame_based_segsnr)

    mixture_audio = np.array(target_audio + noise_audio, dtype=np.int16)
    return mixture_audio, truth_t, target_audio, noise_audio, segsnr


def set_mixture_offsets(mixdb: MixtureDatabase,
                        initial_i_sample_offset: int = 0,
                        initial_i_frame_offset: int = 0,
                        initial_o_frame_offset: int = 0) -> None:
    i_sample_offset = initial_i_sample_offset
    i_frame_offset = initial_i_frame_offset
    o_frame_offset = initial_o_frame_offset
    for mixid in range(len(mixdb.mixtures)):
        mixdb.mixtures[mixid].i_sample_offset = i_sample_offset
        mixdb.mixtures[mixid].i_frame_offset = i_frame_offset
        mixdb.mixtures[mixid].o_frame_offset = o_frame_offset

        i_sample_offset += get_samples_in_mixture(mixdb, mixid)
        i_frame_offset += get_transform_frames_in_mixture(mixdb, mixid)
        o_frame_offset += get_feature_frames_in_mixture(mixdb, mixid)


def get_samples_in_mixture(mixdb: MixtureDatabase, mixid: int) -> int:
    return mixdb.mixtures[mixid].samples


def get_transform_frames_in_mixture(mixdb: MixtureDatabase, mixid: int) -> int:
    return mixdb.mixtures[mixid].samples // mixdb.frame_size


def get_feature_frames_in_mixture(mixdb: MixtureDatabase, mixid: int) -> int:
    return mixdb.mixtures[mixid].samples // mixdb.feature_step_samples


def get_sample_offsets_in_mixture(mixdb: MixtureDatabase, mixid: int) -> (int, int):
    i_sample_offset = sum([sub.samples for sub in mixdb.mixtures[:mixid]])
    return i_sample_offset, i_sample_offset + mixdb.mixtures[mixid].samples


def get_transform_frame_offsets_in_mixture(mixdb: MixtureDatabase, mixid: int) -> (int, int):
    start, stop = get_sample_offsets_in_mixture(mixdb, mixid)
    return start // mixdb.frame_size, stop // mixdb.frame_size


def get_feature_frame_offsets_in_mixture(mixdb: MixtureDatabase, mixid: int) -> (int, int):
    start, stop = get_sample_offsets_in_mixture(mixdb, mixid)
    return start // mixdb.feature_step_samples, stop // mixdb.feature_step_samples


def generate_segsnr(mixdb: MixtureDatabase,
                    mixture: Mixture,
                    target_audio: np.ndarray,
                    noise_audio: np.ndarray,
                    compute: bool = True,
                    frame_based: bool = False) -> np.ndarray:
    """Generate segmental SNR."""
    from pyaaware import ForwardTransform

    from sonusai.utils import int16_to_float

    if not compute:
        return np.empty(0, dtype=np.single)

    fft = ForwardTransform(N=mixdb.frame_size * 4, R=mixdb.frame_size)

    if frame_based:
        segsnr = np.empty(mixture.samples // mixdb.frame_size, dtype=np.single)
    else:
        segsnr = np.empty(mixture.samples, dtype=np.single)

    frame = 0
    for offset in range(0, mixture.samples, mixdb.frame_size):
        indices = slice(offset, offset + mixdb.frame_size)

        target_energy = fft.energy(int16_to_float(target_audio[indices]))
        noise_energy = fft.energy(int16_to_float(noise_audio[indices]))

        if noise_energy == 0:
            snr = np.single(np.inf)
        else:
            snr = np.single(target_energy / noise_energy)

        if frame_based:
            segsnr[frame] = snr
            frame += 1
        else:
            segsnr[indices] = snr

    return segsnr
