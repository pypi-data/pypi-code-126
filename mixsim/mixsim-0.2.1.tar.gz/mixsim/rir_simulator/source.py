from pathlib import Path
from typing import Tuple

import gpuRIR
import numpy as np
from pydantic import BaseConfig


class DataSource(BaseConfig):
    y: np.ndarray
    sr: int
    path: Path
    id: str
    spk_id: str
    traj: np.ndarray
    rir: np.ndarray
    y_rir: np.ndarray
    rir_early: np.ndarray
    y_vad: np.ndarray
    vad_label: np.ndarray


class Source:
    def __init__(self, y: np.ndarray, sr: int = 16000) -> None:
        """Initialize a source object.

        Args:
            y: 1-D numpy array of audio samples.
            sr: sampling rate, default is 16000.
        """
        self.y = y
        self.sr = sr

        # Be assigned in the future
        self.path: Path | None = None
        self.source_id: str | None = None
        self.source_spk_id: str | None = None

        # [num_points, 3 or 2]
        self.traj: np.ndarray | None = None
        self.rir: np.ndarray | None = None
        self.y_vad: np.ndarray | None = None
        self.vad_label: np.ndarray | None = None
        self.y_rvb: np.ndarray | None = None
        self.rir_direct_path: np.ndarray | None = None
        self.rir_early: np.ndarray | None = None
        self.rir_late: np.ndarray | None = None
        self.y_rvb_early: np.ndarray | None = None
        self.y_rvb_late: np.ndarray | None = None
        self.y_rvb_direct_path: np.ndarray | None = None
        self.rir_peak_idx: np.ndarray | None = None
        self.transcription: str = ""
        self.loudness_gain: float = -1
        self.n_y: np.ndarray | None = None

    @property
    def traj_len(self) -> int:
        if self.traj:
            return self.traj.shape[0]
        else:
            return 0

    @property
    def is_static(self) -> bool:
        """Check if the source is static or not.

        Returns:
            True if the source is static; False if the source is dynamic.

        Raise:
            ValueError: if the trajectory of the source is not initialized.
        """
        if self.traj_len == 0:
            raise ValueError("The source has no trajectory.")
        if self.traj_len >= 1:
            return True
        else:
            return False

    def add_rvb(self, rir: np.ndarray, further_split_rir: bool = False) -> None:
        """Filter the RIR with the source audio.

        Note:
            For the function ``simulateTrajectory``, if the dim of num_sources or num_traj is 1, it will
            omit the first dim. Otherwise, it will do dynamic convolution.

        Args:
            rir: RIR with the shape of [num_sources or num_traj, num_mic, num_channels]
            further_split_rir: If True, it will further split the RIR into direct-path, early and late parts.
        """
        # filtered audio with the shape of 2D [num_samples, num_mics]
        y_rir = gpuRIR.simulateTrajectory(self.y, RIRs=rir, fs=self.sr).transpose(1, 0)
        self.rir = rir
        self.y_rvb = y_rir

        if further_split_rir:
            dp, early, late = self.split_rir(rir)
            y_rir_direct_path = gpuRIR.simulateTrajectory(self.y, RIRs=dp, fs=self.sr).transpose(1, 0)
            y_rir_early = gpuRIR.simulateTrajectory(self.y, RIRs=early, fs=self.sr).transpose(1, 0)
            y_rir_late = gpuRIR.simulateTrajectory(self.y, RIRs=late, fs=self.sr).transpose(1, 0)

            self.rir_direct_path = dp
            self.rir_early = early
            self.rir_late = late
            self.y_rvb_direct_path = y_rir_direct_path
            self.y_rvb_early = y_rir_early
            self.y_rvb_late = y_rir_late

    @staticmethod
    def _find_peak_idx(rir: np.ndarray) -> int:
        """Find the peak index of the RIR."""
        peak_idx = np.max(np.abs(rir))
        if peak_idx > 1:
            raise ValueError("The peak of the RIR is too high.")

        return peak_idx

    def split_rir(self, rir: np.ndarray, early_limit: int = 50) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """Split the RIR into direct-path, early and late parts."""
        rir_peak_idx = self._find_peak_idx(rir)
        dp = rir[..., rir_peak_idx : rir_peak_idx + 1]
        early = rir[..., rir_peak_idx:early_limit]
        late = rir[..., early_limit:]
        return dp, early, late


class Microphone:
    """Microphone class is used to store the microphone information."""

    def __init__(self, mic_position: np.ndarray) -> None:
        self.position = mic_position
        self.num_mics = self.position.shape[0]
