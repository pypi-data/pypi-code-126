import random
from typing import Tuple

import numpy as np
import webrtcvad
from joblib import Parallel, delayed
from tqdm import tqdm

from mixsim.util.audio import load_wav


class BaseDataloader:
    def __init__(self) -> None:
        self.vad = webrtcvad.Vad()

    def __len__(self):
        raise NotImplementedError

    @staticmethod
    def _preload_dataset(
            fpath_list: list, label: str = "", num_workers: int = 40
    ) -> Tuple[list[str], list[np.ndarray]]:
        # Joblib keeps the correct order.
        waveform_list = Parallel(n_jobs=num_workers)(
            delayed(load_wav)(f_path, norm=True) for f_path in tqdm(fpath_list, desc=f"Loading {label}")
        )
        return fpath_list, waveform_list

    @staticmethod
    def _offset_and_limit(data_list, offset=0, limit=None):
        data_list = data_list[offset:]

        if limit:
            data_list = data_list[:limit]

        return data_list

    def _clean_silences(self, y, aggressiveness, sr=16000):
        self.vad.set_mode(aggressiveness)

        vad_out = np.zeros_like(y)
        vad_frame_len = int(10e-3 * sr)
        n_vad_frames = len(y) // vad_frame_len
        for frame_idx in range(n_vad_frames):
            frame = y[frame_idx * vad_frame_len: (frame_idx + 1) * vad_frame_len]
            frame_bytes = (frame * 32767).astype("int16").tobytes()
            vad_out[frame_idx * vad_frame_len: (frame_idx + 1) * vad_frame_len] = self.vad.is_speech(frame_bytes, sr)

        # vad_out: [1, 0, 0, 1, ...]
        # s_clean: signals after binary filtering
        s_clean = y * vad_out
        return s_clean, vad_out

    def _stepwise_vad(self, y):
        # Vad starts with the highest aggressiveness of webrtcvad,
        # but it reduces it if removes more than the 66% of the samples.
        s_clean, vad_label = self._clean_silences(y, 3)

        if np.count_nonzero(s_clean) < len(s_clean) * 0.66:
            s_clean, vad_label = self._clean_silences(y, 2)

        if np.count_nonzero(s_clean) < len(s_clean) * 0.66:
            s_clean, vad_label = self._clean_silences(y, 1)

        return s_clean, vad_label

    @staticmethod
    def _random_select_from(data_list):
        return random.choice(data_list)
