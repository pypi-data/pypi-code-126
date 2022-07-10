import argparse
from pathlib import Path

import toml
from tqdm import tqdm

from mixsim.util.audio import set_random_seed

from .simulator import Simulator


def entry(config, seed):
    set_random_seed(seed)

    simulator = Simulator(
        dataloader_conf=config["dataloader"],
        mixer_conf=config["mixers"],
    )

    for _ in tqdm(simulator):
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Single-Channel Enhancement Dataset")
    parser.add_argument("-C", "--configuration", required=True, type=str, help="Configuration (*.toml).")
    parser.add_argument("-S", "--seed", default=1, type=int, help="Random seed for numpy, random, etc.")
    args = parser.parse_args()

    config_path = Path(args.configuration).expanduser().absolute()
    configuration = toml.load(config_path.as_posix())

    entry(configuration, args.seed)
