import os

import preprocessor as p
import spacy
from datasets import load_dataset
from spacy.tokens import DocBin


p.set_options(p.OPT.URL, p.OPT.EMOJI, p.OPT.SMILEY)


def preprocess(tweet):
    """Function for preprocessing a tweet sample.

    Args:
        tweet (dict): Annotated (or not) tweet. Should contains at least the
            key "text", which is the tweet to preprocess.

    Returns:
        dict: Preprocess tweet.
    """
    tweet["text"] = p.clean(tweet["text"])
    return tweet


def prepare(args):
    """Function used to prepare the dataset for sentiment analysis. This
    function does several things :
     * Download the dataset "TweetEval" and cache it for future use
     * Preprocess the dataset using `tweet-preprocessor`
     * Save this dataset for later use
     * And also save the dataset as Spacy data files, for easier usage with Spacy

    Args:
        args (argparse.Namespace): CLI arguments.
    """
    # Load the Tweet Eval dataset (sentiment analysis part) from HuggingFace Hub
    print("Loading Tweet Eval dataset from HuggingFace hub...")
    dataset = load_dataset("tweet_eval", "sentiment")

    # Apply preprocessing
    print("Preprocessing the data...")
    dataset = dataset.map(preprocess)

    # Save the preprocessed dataset
    print("Saving dataset...")
    dataset.save_to_disk(args.dataset)

    # Then, save the dataset in Spacy format
    print("Saving dataset in Spacy format...")
    nlp = spacy.blank("en")
    for subset in ["train", "validation"]:
        db = DocBin()
        for tweet in dataset[subset]:
            doc = nlp(tweet["text"])

            # Multilabel classification : we have 3 labels (0, 1, 2) corresponding
            # to negative, neutral, positive (see https://huggingface.co/datasets/tweet_eval)
            if tweet["label"] == 0:
                doc.cats["positive"] = 0
                doc.cats["neutral"] = 0
                doc.cats["negative"] = 1
            elif tweet["label"] == 1:
                doc.cats["positive"] = 0
                doc.cats["neutral"] = 1
                doc.cats["negative"] = 0
            else:
                doc.cats["positive"] = 1
                doc.cats["neutral"] = 0
                doc.cats["negative"] = 0
            db.add(doc)
        db.to_disk(os.path.join(args.dataset, f"{subset}.spacy"))

    print("All done !")
