from pathlib import Path

import librosa
from tqdm import tqdm


def find_wavs(wav_dirs, dist_path):
    file_path_list = []
    for dataset_dir in tqdm(wav_dirs, desc="Searching Directories"):
        dataset_dir = Path(dataset_dir).expanduser().absolute()
        file_path_list += librosa.util.find_files(dataset_dir.as_posix())  # Sorted

    print(f"Found WAV files: {len(file_path_list)}")

    # # filter
    # tmp = []
    # for i, line in enumerate(file_path_list):
    #     tmp.append(
    #         f"spk1___{i}___utt1___90___0_300	{line}\n"
    #     )
    #
    with open(dist_path.as_posix(), "w") as f:
        f.writelines("\n".join(file_path_list))


if __name__ == "__main__":
    wav_dirs = [
        # "/users/bdda/xhao/Datasets/wsj0-si/si_dt_05",
        "/users/bdda/xhao/Datasets/chime4-noise",
    ]
    dist_path = Path("/users/bdda/xhao/Datasets/chime4-noise/chime4-noise.txt").expanduser().absolute()

    find_wavs(wav_dirs, dist_path)
