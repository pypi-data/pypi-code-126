import random
from pathlib import Path

import numpy as np
import soundfile


class FileWriter:
    def __init__(self, dist_dir, num_files=None, max_num_files_per_dir=None):
        """File writer to save files into one or multiple directories.

        Args:
            dist_dir: The path to dist dir.
            num_files: The number of all files that were written.
            max_num_files_per_dir: Allowable maximum number of files in dist directory.
        """
        # Create root directory
        dist_dir = Path(dist_dir).expanduser().absolute()
        dist_dir.mkdir(exist_ok=True, parents=True)

        self.dirs = []
        if max_num_files_per_dir and max_num_files_per_dir < num_files:
            self.dirs = self.create_sub_dirs(dist_dir, num_files // max_num_files_per_dir + 1)
        else:
            # Directly use root directory without creating subdirectories.
            self.dirs = [
                dist_dir,
            ]

        self.dir_idx = 0
        self.num_files_in_dir = 0
        self.max_num_files_per_dir = max_num_files_per_dir

    @staticmethod
    def create_sub_dirs(dist_dir, num_sub_dirs):
        print(f"Creating sub directories in {dist_dir.as_posix()}")

        dirs = []  # ["/abc/abc/001", "/abc/abc/001", ...]
        for idx in range(num_sub_dirs):
            sub_dir = dist_dir / str(idx + 1).zfill(3)  # 1 => "001"
            dirs.append(sub_dir)
            sub_dir.mkdir(exist_ok=True, parents=False)  # The parent directory must exist

        return dirs

    def update_dir_status(self):
        """Determine whether the file writer need to switch to next sub dir."""
        if self.max_num_files_per_dir and self.num_files_in_dir >= self.max_num_files_per_dir:
            self.dir_idx += 1  # Turn to next sub dir
            self.num_files_in_dir = 0  # Reset counter
        else:
            self.num_files_in_dir += 1

    def write_audio(self, category, filename, audio):
        """Save audio with shape of [C, T] or [T]"""
        (self.dirs[self.dir_idx] / category).mkdir(exist_ok=True, parents=False)
        path = self.dirs[self.dir_idx] / category / filename
        soundfile.write(path.as_posix(), audio.T, samplerate=16000)

    def write_npy(self, category, filename, data):
        (self.dirs[self.dir_idx] / category).mkdir(exist_ok=True, parents=False)
        path = self.dirs[self.dir_idx] / category / filename
        np.save(path.as_posix(), data)

    def write_file(self, file):
        optional_field = (
            ("Direct Path Response", "dpr"),
            ("Room Impulse Response", "rir"),
            ("Transcription", "trans"),
            ("Dry Clean", "dry_clean"),
            ("Reverberated Clean", "rvb_clean"),
            ("Mixture", "mix_clean"),
        )


def set_random_seed(seed, print_info=True):
    if print_info:
        print(f"Set random seed to {seed}")
    random.seed(seed)
    np.random.seed(seed)
