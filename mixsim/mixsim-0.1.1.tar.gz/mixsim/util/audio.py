import os
import random
from pathlib import Path

import librosa
import numpy as np
import soundfile

from mixsim.util.normalization import loudness_norm_max, loudness_norm_rms


def expand_path(path):
    return os.path.abspath(os.path.expanduser(path))


def extract_basename(path: str) -> tuple[str, str]:
    filename, ext = os.path.splitext(os.path.basename(path))
    return filename, ext


class RandomParameter:
    def __init__(self, parameter_range):
        assert len(parameter_range) == 2, "Min and max"
        self.min = parameter_range[0]
        self.max = parameter_range[1]

    def get_value(self):
        """Generate a random value within the range.

        Examples:
            >>> RandomParameter([[2, 3, 5] ,[4, 5, 6]]).get_value()
            [3, 5, 6]

        """
        return self.min + np.random.random(self.min.shape) * (self.max - self.min)


def compute_rms(y: np.ndarray, ref_mic: int = -1) -> float:
    """Compute the Root Mean Square (RMS) of the given signal."""
    is_audio(y, ref_mic=ref_mic)
    return np.sqrt(np.mean(y**2))


def scalar_to_desired_sxr(
    meaningful: np.ndarray,
    meaningless: np.ndarray,
    desired_ratio: float,
    ref_mic: int = -1,
    eps: float = 1e-6,
) -> float:
    """Generally calculate the gains of interference to fulfill a desired SXR (SNR or SIR) ratio.

    Args:
        meaningful: meaningful input, like target clean.
        meaningless: meaningless or unwanted input, like background noise.
        desired_ratio: SNR or SIR ratio.

    Returns:
        Gain, which can be used to adjust the RMS of the meaningless signals to satisfy the given ratio.
    """
    is_audio([meaningful, meaningless], ref_mic=ref_mic)

    meaningful_rms = compute_rms(meaningful if meaningful.ndim == 1 else meaningful[ref_mic, :])
    meaningless_rms = compute_rms(meaningless if meaningless.ndim == 1 else meaningless[ref_mic, :])

    scalar = meaningful_rms / (10 ** (desired_ratio / 20)) / (meaningless_rms + eps)

    return scalar


def sxr_mix(meaningful, meaningless, sxr, target_rms, target_rms_floating, ref_mic=-1, eps=1e-6):
    """

    Shapes:
        meaningful: [C, T] or [T,]
        meaningless: [T,]
        mix: [C, T] or [T,]
    """
    is_audio([meaningful, meaningless], ref_mic=ref_mic)

    meaningful, _ = loudness_norm_max(meaningful, ref_mic=ref_mic)
    meaningful, _ = loudness_norm_rms(meaningful, target_rms, ref_mic=ref_mic)

    meaningless, _ = loudness_norm_max(meaningless, ref_mic=ref_mic)
    meaningless, _ = loudness_norm_rms(meaningless, target_rms, ref_mic=ref_mic)

    sxr_scalar = scalar_to_desired_sxr(meaningful, meaningless, sxr, ref_mic=ref_mic)

    meaningless *= sxr_scalar
    mix = meaningful + meaningless

    mix_target_rms = np.random.randint(target_rms - target_rms_floating, target_rms + target_rms_floating)
    mix, mix_scalar = loudness_norm_rms(mix, mix_target_rms, ref_mic=ref_mic)

    # After rescale the noisy signal, there still need to rescale the clean and noise signals such that
    # the saved audio signals has a correct SNR ratio.
    # When training neural networks, you could apply loudness norm again.
    meaningful *= mix_scalar
    meaningless *= mix_scalar

    # May exceed [-1, 1].
    if is_clipped(mix):
        mix_scalar = np.max(np.abs(mix)) / (0.99 - eps)  # 相当于除以 1
        mix = mix / mix_scalar
        meaningful = meaningful / mix_scalar
        meaningless = meaningless / mix_scalar

    return mix, meaningful, meaningless


def sir_snr_mix(tgt, ref, noise, sir, snr, target_rms, target_rms_floating, ref_mic=-1, eps=1e-6):
    """
    Shapes:
        meaningful: [C, T] or [T,]
        meaningless: [T,]
        mix: [C, T] or [T,]
    """
    is_audio([tgt, ref], ref_mic=ref_mic)

    tgt, _ = loudness_norm_max(tgt, ref_mic=ref_mic)
    tgt, _ = loudness_norm_rms(tgt, target_rms, ref_mic=ref_mic)

    ref, _ = loudness_norm_max(ref, ref_mic=ref_mic)
    ref, _ = loudness_norm_rms(ref, target_rms, ref_mic=ref_mic)

    noise, _ = loudness_norm_max(noise, ref_mic=ref_mic)
    noise, _ = loudness_norm_rms(noise, target_rms, ref_mic=ref_mic)

    sir_scalar = scalar_to_desired_sxr(tgt, ref, sir, ref_mic=ref_mic)
    snr_scalar = scalar_to_desired_sxr(tgt, noise, snr, ref_mic=ref_mic)

    ref *= sir_scalar
    noise *= snr_scalar

    mix = tgt + ref + noise

    mix_target_rms = np.random.randint(target_rms - target_rms_floating, target_rms + target_rms_floating)
    mix, mix_scalar = loudness_norm_rms(mix, mix_target_rms, ref_mic=ref_mic)

    # After rescale the noisy signal, there still need to rescale the clean and noise signals such that
    # the saved audio signals has a correct SNR ratio.
    # When training neural networks, you could apply loudness norm again.
    tgt *= mix_scalar
    ref *= mix_scalar
    noise *= mix_scalar

    # May exceed [-1, 1].
    if is_clipped(mix):
        mix_scalar = np.max(np.abs(mix)) / (0.99 - eps)  # 相当于除以 1
        mix = mix / mix_scalar
        tgt = tgt / mix_scalar
        ref = ref / mix_scalar
        noise = noise / mix_scalar

    return mix, tgt, ref, noise


def compute_sxr(meaningful, meaningless, ref_mic=-1):
    """Compute SNR or SIR with the given signals.

    Refer to the function scalar_to_desired_sxr.

    """
    is_audio([meaningful, meaningless], ref_mic=ref_mic)

    assert meaningful.ndim in (
        1,
        2,
    ), "Only support signals with the shape of [C, T] or [T]."

    if meaningful.ndim == 2:
        assert ref_mic >= 0, "The input is multi-channel. Assign an explicit reference mic for computation."

    meaningful_rms = compute_rms(meaningful, ref_mic=ref_mic)
    meaningless_rms = compute_rms(meaningless, ref_mic=ref_mic)

    return 20 * np.log10(meaningful_rms / meaningless_rms)


def is_audio(y_s: list[np.ndarray] | np.ndarray, ref_mic=-1):
    if not isinstance(y_s, list):
        y_s = [y_s]

    for y in y_s:
        assert y.ndim in (1, 2), "Only support signals with the shape of [C, T] or [T]."

        if y.ndim == 2:
            assert ref_mic >= 0, "The input is multi-channel. Assign an explicit reference mic for computation."


def is_clipped(y, clipping_threshold=0.999):
    return (np.abs(y) > clipping_threshold).any()


def load_wav(path: Path, sr=16000, norm=False) -> np.ndarray:
    # [C, T] or [T]
    y = librosa.load(path.expanduser().absolute().as_posix(), mono=False, sr=sr)[0]

    if norm:
        y, _ = loudness_norm_max(y)

    return y


def shuffle_lists_with_same_order(lists):
    """
    Examples:
        a = [1, 2, 3, 4]
        b = ["a", "b", "c", "d"]
        c, d = _shuffle_list_with_same_order((a, b))
        c = (2, 3, 1, 4)
        d = ('b', 'c', 'a', 'd')
    """
    tmp = list(zip(*lists))
    random.shuffle(tmp)
    return zip(*tmp)


def ndarray_info(arr):
    return (
        f"shape: {arr.shape}, "
        f"max: {arr.max():.3f}, "
        f"min: {arr.min():.3f}, "
        f"mean: {arr.mean():.3f}, "
        f"std: {arr.std():.3f}, "
        f"rms: {compute_rms(arr):.3f}"
    )


def write_audio(audio, path):
    soundfile.write(path.as_posix(), audio.T, samplerate=16000)


def write_npy(data, path):
    np.save(path.as_posix(), data)
