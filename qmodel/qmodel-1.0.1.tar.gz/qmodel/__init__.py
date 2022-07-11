from .model_common import ModelCommon
from .model_testing import ModelTesting
from .model_training import ModelTraining
from .model_using import ModelUsing
from .prediction_images import PredictionImages
from .test_model_testing import TestModelTesting
from .test_model_training import TestModelTraining
from .testing_set import TestingSet
from .tools import Tools
from .training_set import TrainingSet
import os 
import cv2


def intro():
    print("Hello, welcome into that library for creating a Random Forest Classifier model to read 7 segment digit on an image")


def otsu_display(self, directory_path , directory_to_save):
        if not os.path.exists(directory_to_save):
                    os.makedirs(directory_to_save)
        for filename in os.listdir(directory_path):
            img = cv2.imread(directory_path+filename)
            otsued = self.otsu(img)
            #showImage(f"otsued {filename}", otsued)
            path_to_save = directory_to_save + filename
            cv2.imwrite(path_to_save, otsued)
