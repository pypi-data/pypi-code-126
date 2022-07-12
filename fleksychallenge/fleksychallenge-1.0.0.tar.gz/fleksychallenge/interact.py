import os

import spacy

from fleksychallenge.prepare import preprocess


def interact(args):
    """Function for the user to interact with a trained model.

    After loading the trained model, this function will keep asking the user
    to input some text (the tweet to analyze), and it will return the
    classification score for each sentiment.

    Args:
        args (argparse.Namespace): CLI arguments.
    """
    # Load our model
    print("Loading model...")
    sentiment_model = spacy.load(os.path.join(args.model, "model-best"))

    text = ""
    while text != "qq":
        text = input("Type a tweet followed by Enter to analyze its sentiment, or `qq` for leaving :")
        if text == "qq":
            break
        elif len(text) == 0:
            print("Coudln't detect any input... Type `qq` if you want to leave")
        else:
            out = sentiment_model(preprocess({"text": text})["text"])
            print(out.cats)

    print("Bye ~")
