import numpy as np


def is_audio(y_s: list[np.ndarray] | np.ndarray, ref_mic=-1):
    if not isinstance(y_s, list):
        y_s = [y_s]

    for y in y_s:
        assert y.ndim in (1, 2), "Only support signals with the shape of [C, T] or [T]."

        if y.ndim == 2:
            assert ref_mic >= 0, "The input is multi-channel. Assign an explicit reference mic for computation."


def compute_rms(y: np.ndarray, ref_mic: int = -1) -> float:
    """Compute the Root Mean Square (RMS) of the given signal."""
    is_audio(y, ref_mic=ref_mic)
    return np.sqrt(np.mean(y**2))


def loudness_norm_max(
    y: np.ndarray,
    scalar: float | None = None,
    ref_mic: int = -1,
    eps: float = 1e-6,
) -> tuple[np.ndarray, float]:
    """Maximum loudness normalization to signals."""
    is_audio(y, ref_mic=ref_mic)

    if not scalar:
        scalar = np.max(np.abs(y)) + eps if y.ndim == 1 else np.max(np.abs(y[ref_mic, :])) + eps

    assert scalar is not None
    return y / scalar, scalar


def loudness_norm_rms(
    y: np.ndarray,
    scalar: float | None = None,
    target_level: float = -25,
    ref_mic: int = -1,
    eps: float = 1e-6,
) -> tuple[np.ndarray, float]:
    """Loudness normalize a signal based on the Root Mean Square (RMS).

    Normalize the RMS of signals to a given RMS based on Decibels Relative to Full Scale (dBFS).

    Args:
        y: [C, T] or [T,].
        scalar: scalar to normalize the RMS, default to None.
        target_rms: target RMS in dBFS.
        ref_mic: reference mic for multi-channel signals.

    Returns:
        Loudness normalized signal and scalar.

    Note:
        A small amount of signal samples would be clipped after normalization, but it does not matter.
    """
    is_audio(y, ref_mic=ref_mic)

    if not scalar:
        current_level = compute_rms(y) if y.ndim == 1 else compute_rms(y[ref_mic, :])
        scalar = 10 ** (target_level / 20) / (current_level + eps)

    return y * scalar, scalar
