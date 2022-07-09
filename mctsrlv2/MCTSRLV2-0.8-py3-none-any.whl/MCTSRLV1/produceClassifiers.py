import pandas as pd
from MCTSRLV2.PreprocessingND import Preprocessing
from sklearn.model_selection import StratifiedKFold
from MCTSRLV2.MC import MCTS
from MCTSRLV2.N_1 import N_1Classifier
from MCTSRLV2.makePredictions import makePredictions
from sklearn.metrics import classification_report, accuracy_score
import numpy as np
from tkinter import *
from matplotlib.figure import Figure
from decimal import Decimal
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from statistics import mean
import os


class Retrieve:
    def __init__(self, dataset, kFold, mValues, jaccardValues, iterationsNumber, minimumSupport):
        self.dataset = dataset
        self.kFold = kFold
        self.mValues = mValues
        self.jValues = jaccardValues
        self.iterationsNumber = iterationsNumber
        self.minimumSupport = minimumSupport

    def produce(self):
        # the name of ds:
        name, extension = os.path.splitext(self.dataset)
        name = os.path.basename(name)

        # read a csv file:
        df = pd.read_csv(self.dataset)
        # apply the pre-processing phase:
        obj1 = Preprocessing(df)
        # df is clean now:
        df = obj1.run()

        # the plot settings:
        root = Tk()
        figure = Figure(figsize=(10, 8), dpi=100)
        plot = figure.add_subplot(1, 1, 1)
        # lStyles = ['-.', ':', '--', None]

        # Starting with the Jaccard classifiers:

        # max1: the JS max accuracy got:
        max1_Acc = 0
        max1_mValue = 0
        max1_Jaccard_value = 0
        max1_var = 0

        # max2: the SC max accuracy got:
        max2_acc = 0
        max2_mValue = 0
        max2_var = 0

        for jValue in self.jValues:
            print(f"For Jaccard Value = {jValue}")
            scorePlot = []
            for mValue in self.mValues:
                print(f"For m = {mValue}")  # each jValue will produce m classifiers.

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

                    # produce a Jaccard similarity-based Classifier:
                    obj3 = N_1Classifier(trainingData=trainData, mValue=mValue, patternsPerClass=patternsPerClass,
                                         jaccardValue=jValue, name=name)
                    jsClassifier = obj3.run1()

                    # make the predictions:
                    obj4 = makePredictions(labels, jsClassifier, X_test)
                    predictedValues = obj4.predict()

                    print(classification_report(y_test, predictedValues))

                    score = accuracy_score(y_test, predictedValues)

                    print('Fold: %2d, Accuracy: %.3f' % (k + 1, score))
                    print('-------------------------------------------------------------------------------------------')

                    scores.append(score)

                print('\n\nCross-Validation accuracy: %.3f +/- %.3f' % (np.mean(scores), np.std(scores)))
                print('-------------------------------------------------------------------------------------------')

                scorePlot.append(np.mean(scores))

            plot.plot(self.mValues, scorePlot, marker="X", label=f'JS with J={jValue}', linestyle=':')
            for i, j in zip(self.mValues, scorePlot):
                plot.annotate(round(Decimal(str(j)), 4), xy=(i, j))

            if max1_Acc < mean(scorePlot):
                max1_Acc = mean(scorePlot)
                max1_mValue = self.mValues[scorePlot.index(max(scorePlot))]
                max1_Jaccard_value = jValue
                max1_var = np.var(scorePlot)

        print("The best result using JS")
        print(f"Mean Accuracy = {max1_Acc}, Corresponding m-value: {max1_mValue}, Corresponding Jaccard value: "
              f"{max1_Jaccard_value}, variance = {max1_var}")

        # For the SC classifiers:
        print('----------------------------Separate and Conquer Approach----------------------------------')
        scorePlot2 = []
        for mValue in self.mValues:
            print(f"For m = {mValue}")

            # Apply the K-fold cross validation:
            strtkfold = StratifiedKFold(n_splits=self.kFold, shuffle=True, random_state=1)
            X = df.loc[:, df.columns != df.columns[-1]]
            y = df.iloc[:, -1]
            kfold = strtkfold.split(X, y)

            scores2 = []
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
                obj3 = N_1Classifier(trainingData=trainData, mValue=mValue, patternsPerClass=patternsPerClass,
                                     jaccardValue=None, name=name)
                scClassifier = obj3.run2()

                # make the predictions:
                obj4 = makePredictions(labels, scClassifier, X_test)
                predictedValues = obj4.predict()

                print(classification_report(y_test, predictedValues))

                score = accuracy_score(y_test, predictedValues)

                print('Fold: %2d, Accuracy: %.3f' % (k + 1, score))
                scores2.append(score)
                print('-------------------------------------------------------------------------------------------')

            print('\n\nCross-Validation accuracy: %.3f +/- %.3f' % (np.mean(scores), np.std(scores)))
            print('-------------------------------------------------------------------------------------------')

            scorePlot2.append(np.mean(scores2))

        plot.plot(self.mValues, scorePlot2, marker="X", label='S&C method')
        for i, j in zip(self.mValues, scorePlot2):
            plot.annotate(round(Decimal(str(j)), 4), xy=(i, j))

        max2_acc = mean(scorePlot2)
        max2_mValue = self.mValues[scorePlot2.index(max(scorePlot2))]
        max2_var = np.var(scorePlot2)

        print("The best result using SC")
        print(f"Mean Accuracy = {max2_acc}, Corresponding m-value: {max2_mValue}, Variance ={max2_var}")

        canvas = FigureCanvasTkAgg(figure, root)
        canvas.get_tk_widget().grid(row=0, column=0)
        plot.grid(True)
        plot.set_xlabel("M-estimate Value")
        plot.set_ylabel(f"Average Accuracy After ({self.kFold})-fold Cross Validation")
        plot.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
        figure.tight_layout()
        figure.savefig(f'{name}.png')

        print('------------------------------------ Final Result ------------------------------------------')

        # after selecting the best parameters, we need to use them to generate the classifier:
        def continue_u():

            if max1_Acc > max2_acc or (max1_Acc == max2_acc and max1_var < max2_var):
                print('Jaccard Similarity wins!')
                print(f"Selected M-Value: {max1_mValue}")
                print(f'Selected Jaccard values: {max1_Jaccard_value}')
                # Generate a pool of patterns but based on the whole training data and the selected mValue:
                obj = MCTS(df, self.iterationsNumber, self.minimumSupport, max1_mValue)
                patternsPerClas = obj.monteCarloND()
                # produce a Jaccard similarity-based Classifier:
                obj22 = N_1Classifier(trainingData=df, mValue=max1_mValue, patternsPerClass=patternsPerClas,
                                      jaccardValue=max1_Jaccard_value, name=name)
                obj22.run1()

            elif max2_acc > max1_Acc or (max1_Acc == max2_acc and max2_var < max1_var):
                print('Separate and Conquer Similarity wins!')
                print(f"Selected M-Value: {max2_mValue}")
                # Generate a pool of patterns but based on the whole training data and the selected mValue:
                obj = MCTS(df, self.iterationsNumber, self.minimumSupport, max2_mValue)
                patternsPerClas = obj.monteCarloND()

                # produce a SC-based Classifier:
                obj33 = N_1Classifier(trainingData=df, mValue=max2_mValue, patternsPerClass=patternsPerClas,
                                      jaccardValue=None, name=name)
                obj33.run2()

            quit()

        root.after(0, continue_u)
        root.mainloop()
