import argparse

from fleksychallenge import interact, prepare, test, train


def cli():
    parser = argparse.ArgumentParser(description="Fleksy challenge part 1")
    parser.add_argument("cmd", help="Command to execute", choices=["prepare", "train", "test", "interact"])
    parser.add_argument("--dataset", help="Where to save/load the dataset from", default="tweet_dataset")
    parser.add_argument("--config", help="Location of the config file to use for training", default="config.cfg")
    parser.add_argument("--model", help="Where to save/load the model from", default="sentiment_model")
    parser.add_argument("--cpu", action="store_true", help="Use this option to train on CPU instead of GPU")
    parser.add_argument("--full", action="store_true", help="Use this option to test on the full test set")
    args = parser.parse_args()

    if args.cmd == "prepare":
        prepare(args)
    elif args.cmd == "train":
        train(args)
    elif args.cmd == "test":
        test(args)
    elif args.cmd == "interact":
        interact(args)


if __name__ == "__main__":
    cli()
