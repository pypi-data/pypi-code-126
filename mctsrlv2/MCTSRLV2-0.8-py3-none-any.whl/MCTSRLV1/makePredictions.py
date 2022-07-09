import itertools
import numpy as np


class makePredictions:
    def __init__(self, labels, classifier, X_test):
        self.classifier = classifier
        self.X_test = X_test
        self.labels = labels

    def predict(self):
        predictions = []
        currentLabels = []

        for sample in self.X_test.values.tolist():
            predicted = False
            for all_sets in self.classifier:
                label = all_sets[0]
                if label not in currentLabels:
                    currentLabels.append(label)
                ruleSet = all_sets[1][0]

                for rule in ruleSet:
                    counter = 0
                    for (value, interval) in itertools.zip_longest(sample, rule):
                        if interval[0] <= value <= interval[1]:
                            counter += 1
                        else:
                            break  # move to the second rule.

                    if counter == len(sample):
                        predictions.append(label)
                        predicted = True
                        break

                if predicted:
                    break

            if not predicted:
                diff = [item for item in self.labels if item not in currentLabels]
                predictions.append(diff[0])

        predictions = np.array(predictions)

        return predictions
