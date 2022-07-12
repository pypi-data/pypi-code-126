import os

from spacy.cli.train import train as spacy_train


def get_config(config_file):
    """Small helper function returning the right path for the specified config
    file. Since the package may be installed in another place than the current
    working directory, this is necessary when loading the default config file.

    Args:
        config_file (str): Config file to load.

    Returns:
        str: Path to the config file to load.
    """
    if os.path.exists(config_file):
        return config_file
    else:
        pkg_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(pkg_dir, config_file)


def train(args):
    """Function used to train a model for sentiment analysis.

    Args:
        args (argparse.Namespace): CLI arguments.
    """
    use_gpu = -1 if args.cpu else 0
    config_file = get_config(args.config)

    spacy_train(
        config_file,
        output_path=args.model,
        use_gpu=use_gpu,
        overrides={
            "paths.train": os.path.join(args.dataset, "train.spacy"),
            "paths.dev": os.path.join(args.dataset, "validation.spacy"),
        },
    )
