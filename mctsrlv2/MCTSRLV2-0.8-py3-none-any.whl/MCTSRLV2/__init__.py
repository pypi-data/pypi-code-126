from MCTSRLV2 import produceClassifiers

'''
import Extent
import Tree
import ChildrenND
import Evaluation
import Hashmap
import Ruleset_based_SC
import Ruleset_based_JS
import displayResult
import PreprocessingND
import MC
import N_1
import makePredictions
import PreprocessingND
import Split
import matplotlib

matplotlib.use("TkAgg")


if __name__ == '__main__':
    obj = produceClassifiers.Retrieve(dataset='Iris.csv', kFold=3, mValues=[0.1, 0.3, 1, 3],
                                      jaccardValues=[.1, .3, .5], iterationsNumber=50,
                                      minimumSupport=10)
    obj.produce()
    
'''


def run(dataset, kFold, listOfmValues, listOfJaccardValues, iterationsNumber, minimumSupport):
    obj = produceClassifiers.Retrieve(dataset=dataset, kFold=kFold, mValues=listOfmValues,
                                      jaccardValues=listOfJaccardValues, iterationsNumber=iterationsNumber,
                                      minimumSupport=minimumSupport)
    obj.produce()
