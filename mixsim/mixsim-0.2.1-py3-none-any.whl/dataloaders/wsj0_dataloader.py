from typing import Tuple, Union

import numpy as np

from mixsim.dataloaders.base_dataloader import BaseDataloader
from mixsim.rir_simulator.source import Source
from mixsim.util.audio import expand_path, extract_basename, load_wav


class WSJDataloader(BaseDataloader):
    def __init__(self, data_conf, num_sources: int):
        super().__init__()
        self._num_yielded = 0

        # Load clean dataset
        clean_fpath_list = [line.rstrip("\n") for line in open(expand_path(data_conf["clean_fpath_list"]), "r")]
        clean_fpath_list = self._offset_and_limit(
            clean_fpath_list,
            data_conf["clean_list_offset"],
            data_conf["clean_list_limit"],
        )
        self.clean_waveform_list = []
        if data_conf["preload_clean_data"]:
            clean_fpath_list, self.clean_waveform_list = self._preload_dataset(clean_fpath_list, label="Clean")

        # Load noise dataset
        noise_fpath_list = [line.rstrip("\n") for line in open(expand_path(data_conf["noise_fpath_list"]), "r")]
        noise_fpath_list = self._offset_and_limit(
            noise_fpath_list,
            data_conf["noise_list_offset"],
            data_conf["noise_list_limit"],
        )
        self.noise_waveform_list = []
        if data_conf["preload_noise_data"]:
            noise_fpath_list, self.noise_waveform_list = self._preload_dataset(noise_fpath_list, label="Noise")

        self.clean_fpath_list = clean_fpath_list
        self.noise_fpath_list = noise_fpath_list
        self.num_sources = num_sources
        self.pre_load_clean_data = data_conf["preload_clean_data"]
        self.pre_load_noise_data = data_conf["preload_noise_data"]
        self.sr = data_conf["sample_rate"]
        self.silence_duration = data_conf["silence_duration"]

    def __len__(self):
        return len(self.clean_fpath_list)

    def __iter__(self):
        return self

    def __next__(self):
        if self._num_yielded < len(self):
            data = self[self._num_yielded]
            self._num_yielded += 1
            return data
        raise StopIteration

    def _select_clean_y(self, item_idx: int = -1) -> Tuple[str, np.ndarray]:
        """Select clean signal.

        Args:
            item_idx: Random select an item if index=-1.

        Returns:
            A two-element tuple: [file_path, y]
        """
        if item_idx < 0:
            # random index
            item_idx = np.random.randint(0, len(self.clean_fpath_list))

        clean_fpath = self.clean_fpath_list[item_idx]

        if self.pre_load_clean_data:
            clean_y = self.clean_waveform_list[item_idx]
        else:
            clean_y = load_wav(clean_fpath, sr=self.sr, norm=True)

        return clean_fpath, clean_y

    def _select_chime_noise_y(self) -> Tuple[str, np.ndarray]:
        """The noises in ChiME-4 are far longer than utterances in the WSJ dataset."""
        # random index
        item_idx = np.random.randint(0, len(self.noise_fpath_list))
        noise_fpath = self.noise_fpath_list[item_idx]

        if self.pre_load_noise_data:
            noise_y = self.noise_waveform_list[item_idx]
        else:
            noise_y = load_wav(noise_fpath, sr=self.sr, norm=True)

        return noise_fpath, noise_y

    def _select_noise_y(self, target_length: int) -> np.ndarray:
        """Select a noise segment with a given length from noise_dataset_list.

        Args:
            target_length: Target length of the noise segment.
        """
        noise_y = np.zeros(0, dtype=np.float32)
        silence_segment = np.zeros(int(self.sr * self.silence_duration), dtype=np.float32)
        remaining_length = target_length

        while remaining_length > 0:
            noise_fpath = self._random_select_from(self.noise_fpath_list)
            noise_segment = load_wav(noise_fpath, sr=self.sr, norm=True)
            noise_y = np.append(noise_y, noise_segment)
            remaining_length -= len(noise_segment)

            # if the noise length is not sufficient, add a short silence segment before concatenating
            if remaining_length > 0:
                silence_len = min(remaining_length, len(silence_segment))
                noise_y = np.append(noise_y, silence_segment[:silence_len])
                remaining_length -= silence_len

        if len(noise_y) > target_length:
            idx_start = np.random.randint(len(noise_y) - target_length)
            noise_y = noise_y[idx_start: idx_start + target_length]

        return noise_y

    @staticmethod
    def _get_wsj_speech_id(fpath):
        # 050a050e.wav => 050a050e
        basename, _ = extract_basename(fpath)
        return basename

    @staticmethod
    def _random_slice_signal_segment(y, desired_length) -> np.ndarray:
        start = np.random.randint(0, len(y) - desired_length)
        return y[start: start + desired_length]

    @staticmethod
    def _get_wsj_speaker_id(fpath):
        """Parse the speaker ID of WSJ dataset from a given file path."""
        # 050a050e.wav => 050
        basename, _ = extract_basename(fpath)
        return basename[:3]

    @staticmethod
    def _get_chime_noise_id(fpath):
        # /users/bdda/xhao/Datasets/chime4-noise/bus.wav
        noise_id, _ = extract_basename(fpath)
        return noise_id

    def _select_tgt_ref(self, item):
        tgt_fpath, tgt_y = self._select_clean_y(item)
        tgt_speaker_id = self._get_wsj_speaker_id(tgt_fpath)

        ref_fpath, ref_y = self._select_clean_y(-1)
        ref_speaker_id = self._get_wsj_speaker_id(ref_fpath)

        while tgt_speaker_id == ref_speaker_id:
            # Another clean signals
            ref_fpath, ref_y = self._select_clean_y(-1)
            ref_speaker_id = self._get_wsj_speaker_id(ref_fpath)

        return tgt_fpath, tgt_speaker_id, tgt_y, ref_fpath, ref_speaker_id, ref_y

    @staticmethod
    def _parse_snr_range(snr_range: list[Union[int, float]]):
        assert len(snr_range) == 2, f"The value of snr_range should be like [low, high] instead of {snr_range}."
        assert snr_range[0] <= snr_range[-1], f"The low bound should not larger than high bound."

        low, high = snr_range
        return [i for i in (low, high + 1)]

    def __getitem__(self, item) -> tuple[list[Source], Source]:
        # TODO Unify tgt and ref to source list
        # select target and reference signals.
        (
            tgt_fpath,
            tgt_spk_id,
            tgt_y,
            ref_fpath,
            ref_spk_id,
            ref_y,
        ) = self._select_tgt_ref(item)
        tgt_y, tgt_vad_label = self._stepwise_vad(tgt_y)  # VAD smoothly
        ref_y, ref_vad_label = self._stepwise_vad(ref_y)
        tgt_len = len(tgt_y)
        ref_len = len(ref_y)
        desired_len = tgt_len if tgt_len > ref_len else ref_len

        # Select noise segment
        noise_fpath, noise_y = self._select_chime_noise_y()
        noise_y = self._random_slice_signal_segment(noise_y, desired_len)
        noise_id = self._get_chime_noise_id(noise_fpath)

        sources = []
        sources.append(Source(y=tgt_y, id=tgt_spk_id, fpath=tgt_fpath))
        sources.append(Source(y=ref_y, id=ref_spk_id, fpath=ref_fpath))

        # TODO Introduce a variable for the slice position.
        noise = Source(y=noise_y, id=noise_id, fpath=noise_fpath)
        return sources, noise
