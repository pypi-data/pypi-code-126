import pandas as pd
from MCTSRLV2.PreprocessingND import Preprocessing
from MCTSRLV2.MC import MCTS
from MCTSRLV2.N_1 import N_1Classifier
from MCTSRLV2.makePredictions import makePredictions

from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import StratifiedKFold
import numpy as np
import matplotlib
from tkinter import *

matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from decimal import Decimal


class Retrieve:
    def __init__(self, dataset, kFold, mValues, jaccardThreshold, iterationsNumber, minimumSupport):
        self.dataset = dataset
        self.kFold = kFold
        self.mValues = mValues
        self.jaccardThreshold = jaccardThreshold
        self.iterationsNumber = iterationsNumber
        self.minimumSupport = minimumSupport

    def produce(self):
        # read a csv file:
        df = pd.read_csv(self.dataset)
        # apply the pre-processing phase:
        obj1 = Preprocessing(df)
        # df is clean now:
        df = obj1.run()

        root = Tk()
        figure = Figure(figsize=(10, 8), dpi=100)
        plot = figure.add_subplot(1, 1, 1)
        scorePlot = []

        for mValue in self.mValues:

            print(f"For m = {mValue}")

            # Apply the K-fold cross validation:
            strtkfold = StratifiedKFold(n_splits=self.kFold, shuffle=True, random_state=1)
            X = df.loc[:, df.columns != df.columns[-1]]
            y = df.iloc[:, -1]
            kfold = strtkfold.split(X, y)

            scores = []
            for k, (train, test) in enumerate(kfold):
                trainData = df.iloc[train]
                trainData = trainData.reset_index(drop=True)

                testData = df.iloc[test]
                testData = testData.reset_index(drop=True)

                X_test = testData.loc[:, testData.columns != testData.columns[-1]]
                y_test = testData.iloc[:, -1].to_numpy()

                # start:
                labels = pd.unique(trainData.iloc[:, -1].values.ravel())

                # Generate a pool of patterns for each class
                obj2 = MCTS(trainData, self.iterationsNumber, self.minimumSupport, mValue)
                patternsPerClass = obj2.monteCarloND()

                # produce a SC-based Classifier:
                obj3 = N_1Classifier(trainingData=trainData, mValue=mValue, patternsPerClass=patternsPerClass)
                scClassifier = obj3.run()

                # make the predictions:
                obj4 = makePredictions(labels, scClassifier, X_test)
                predictedValues = obj4.predict()

                print(classification_report(y_test, predictedValues))

                score = accuracy_score(y_test, predictedValues)

                print('Fold: %2d, Accuracy: %.3f' % (k + 1, score))
                scores.append(score)

            print('\n\nCross-Validation accuracy: %.3f +/- %.3f' % (np.mean(scores), np.std(scores)))
            scorePlot.append(np.mean(scores))

        plot.plot(self.mValues, scorePlot, color="blue", marker="X", linestyle="--", label='S&C method')
        for i, j in zip(self.mValues, scorePlot):
            plot.annotate(round(Decimal(str(j)), 4), xy=(i, j))
        canvas = FigureCanvasTkAgg(figure, root)
        canvas.get_tk_widget().grid(row=0, column=0)
        plot.grid(True)
        plot.set_xlabel("M-estimate Value")
        plot.set_ylabel(f"Average Accuracy After ({self.kFold})-fold Cross Validation")
        plot.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
        figure.tight_layout()

        root.mainloop()

        return 0
