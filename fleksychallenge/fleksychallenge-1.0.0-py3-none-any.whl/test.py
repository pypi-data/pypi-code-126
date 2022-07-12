import os

import spacy
from datasets import load_from_disk, load_metric


def test(args):
    """This function will test a given model on the test set of the prepared
    dataset.

    According to https://arxiv.org/pdf/2010.12421.pdf, for the task of Sentiment
    analysis, we need to use macro-averaged Recall metric to compare models.

    For the sake of completeness, this function also compute accuracy, precision,
    and F-1 score.

    Args:
        args (argparse.Namespace): CLI arguments.
    """
    # Load our model
    print("Loading model...")
    sentiment_model = spacy.load(os.path.join(args.model, "model-best"))

    # Load our dataset
    print("Loading dataset...")
    dataset = load_from_disk(args.dataset)

    # Create the metrics
    accuracy = load_metric("accuracy")
    precision = load_metric("precision")
    recall = load_metric("recall")
    f1 = load_metric("f1")

    print("Evaluating test set...")
    for i, tweet in enumerate(dataset["test"]):
        if not args.full and i > 100:
            # The test set is quite big (12k samples), it takes some time
            # So unless the user asked for full test set evaluation, just run
            # on the first 100 samples
            break

        # Predict using our trained model
        pred = sentiment_model(tweet["text"])

        # Spacy format -> int (0, 1, 2)
        sentiments = [pred.cats["negative"], pred.cats["neutral"], pred.cats["positive"]]
        pred_label = max(range(len(sentiments)), key=lambda i: sentiments[i])

        # Metrics
        accuracy.add(prediction=pred_label, reference=tweet["label"])
        precision.add(prediction=pred_label, reference=tweet["label"])
        recall.add(prediction=pred_label, reference=tweet["label"])
        f1.add(prediction=pred_label, reference=tweet["label"])

    # Display metrics to user
    print(f"\nAccuracy : {accuracy.compute()['accuracy']:.4f}")
    print(f"Precision : {precision.compute(average='macro')['precision']:.4f}")
    print(f">> Recall : {recall.compute(average='macro')['recall']:.4f}")
    print(f"F1-score : {f1.compute(average='macro')['f1']:.4f}")
