import logging
import os
import subprocess
from pathlib import Path

import librosa.util

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler(filename="sphere2wav.log", mode="a+"), logging.StreamHandler()],
)
logger = logging.getLogger()


def get_basename(path):
    return os.path.splitext(os.path.basename(path))[0]


def entry(sphere_dir, wav_dir):
    # logging.info("Download sph2pipe_v2.5")
    # url = "https://www.openslr.org/resources/3/sph2pipe_v2.5.tar.gz"
    # sph2pipe = requests.get(url, allow_redirects=True)
    # open("sph2pipe_v2.5.tar.gz", 'wb').write(sph2pipe.content)

    # logger.info("Extract sph2pipe_v2.5")
    # tar = tarfile.open("sph2pipe_v2.5.tar.gz")
    # tar.extractall()
    # tar.close()

    # subprocess.run("gcc -o sph2pipe_v2.5/sph2pipe sph2pipe_v2.5/*.c -lm")
    sph2pipe_path = "/users/bdda/xhao/Center/Audio-ZEN/tools/sph2pipe_v2.5/sph2pipe"

    logger.info(f"Find wv1 files in {sphere_dir.as_posix()}")
    sph_path_list = librosa.util.find_files(sphere_dir.as_posix(), ext="wv1")
    logger.info(f"Found wv1 files == {len(sph_path_list)}")

    wav_dir.mkdir(exist_ok=True, parents=True)

    logger.info("Convert sphere format to wav format")
    for sph_path in sph_path_list:
        wav_path = (wav_dir / (get_basename(sph_path) + ".wav")).as_posix()
        logger.info(f"Convert {sph_path} to {wav_path}")
        subprocess.run(f"{sph2pipe_path} -f wav {sph_path} > {wav_path}", shell=True)


if __name__ == "__main__":
    sphere_dir = Path("/project_bdda3/bdda/skhu/project/LDC/LDC93S6B")
    wav_dir = Path("/project_bdda6/bdda/xhao/Datasets/tmp")
    entry(sphere_dir, wav_dir)
