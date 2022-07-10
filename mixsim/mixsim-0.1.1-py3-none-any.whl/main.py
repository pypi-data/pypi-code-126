import argparse
from pathlib import Path

import toml

from mixsim.conf_schema import ConfigSchema
from mixsim.dataloaders.source_dataloader import SourceDataloader
from mixsim.util.utils import set_random_seed


def main(conf: ConfigSchema) -> None:
    set_random_seed(conf.seed)
    print(f"Seed: {conf.seed}")

    speech_dataloader = SourceDataloader(conf.clean)  # may map
    noise_dataloader = SourceDataloader(conf.noise)  # map iter

    for clean_sources in speech_dataloader:
        noise_source = next(iter(noise_dataloader))


print(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MixSim")
    parser.add_argument("-C", "--configuration", required=True, type=str, help="Configuration (*.toml).")
    parser.add_argument("-S", "--seed", default=1, type=int, help="Random seed for numpy, random, etc.")
    args = parser.parse_args()

    config_path = Path(args.configuration).expanduser().absolute()
    config_dict = toml.load(config_path.as_posix())
    config = ConfigSchema(**config_dict)
    main(config)
