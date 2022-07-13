from pathlib import Path

import numpy as np

from mixsim.conf_schema import SourceLoader
from mixsim.dataloaders.base_dataloader import BaseDataloader
from mixsim.rir_simulator.source import Source
from mixsim.util.audio import expand_path, load_wav


class SourceDataloader(BaseDataloader):
    def __init__(self, conf: SourceLoader) -> None:
        """Load clean or noise data from a database and return Source class.

        Args:
            conf: check the conf_schema.py for the details.
        """
        # Load clean dataset
        super().__init__()
        fpath_list = [line.rstrip("\n") for line in open(expand_path(conf.fpath_file), "r")]
        fpath_list = self._offset_and_limit(fpath_list, conf.offset, conf.limit)

        self.waveform_list = []
        if conf.parallel_load:
            fpath_list, self.waveform_list = self._preload_dataset(fpath_list, label="Clean")

        self.fpath_list = fpath_list
        self.num_sources = conf.num_sources
        self.include_vad = conf.include_vad
        self.preload = conf.parallel_load
        self.sr = conf.sample_rate
        self.max_norm = conf.max_norm
        self.source_id_fn = conf.collect_id_fn
        self.source_spk_id_fn = conf.collect_spk_id_fn
        self.conf = conf

    def __len__(self) -> int:
        return len(self.fpath_list)

    def _load_source(self, item) -> tuple[Path, np.ndarray]:
        fpath = Path(self.fpath_list[item])

        if self.preload:
            y = self.waveform_list[item]
        else:
            y = load_wav(fpath, sr=self.sr, norm=self.max_norm)

        return fpath, y

    def __getitem__(self, item) -> list[Source]:
        sources = []
        for _ in range(self.num_sources):
            fpath, y = self._load_source(item)
            source = Source(y=y, sr=self.sr)
            source.path = fpath
            source.source_id = self.source_id_fn(fpath) if self.source_id_fn else None
            source.source_spk_id = self.source_spk_id_fn(fpath) if self.source_spk_id_fn else None

            if self.include_vad:
                y_vad, vad_label = self._stepwise_vad(source.y)
                source.y_vad = y_vad
                source.vad_label = vad_label

            sources.append(source)

        return sources
