import os
import cv2
import numpy as np
import glob
import joblib
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn import metrics
from .model_common import ModelCommon

# author: Sebag Ethan
# date: 07/07/22
# version 1.0

class ModelTesting:
    #this class is to test a trained model to see if it is accurate or not

    def __init__(self, testing_set_path, path_of_model_to_test) :
        self.testing_set_path = testing_set_path
        self.path_of_model_to_test = path_of_model_to_test
        self.model_common = ModelCommon()

    
    #get a testing dataset to test 
    def get_test_set(self):
        # get the testing images for the RFC
        test_images = []
        test_labels = [] 
        for directory_path in glob.glob(self.testing_set_path):
            fruit_label = directory_path.split("\\")[-1]
            for img_path in glob.glob(os.path.join(directory_path, "*.jpg")):
                img = cv2.imread(img_path)
                print(fruit_label +"," +img_path)
                test_images.append(img)
                test_labels.append(fruit_label)
        #transform the list of images and the list of label into a numpy array of each        
        test_images = np.array(test_images)
        test_labels = np.array(test_labels)
        return test_images ,test_labels



    #Realize a prediction on an image dataset to see the accuracy of the model  
    def rfc_predict(self, x_test, model , RF_model , le):
        #Send test data through same feature extractor process
        X_test_feature = model.predict(x_test)
        #Now predict using the trained RF model. 
        prediction_RF = RF_model.predict(X_test_feature)
        #Inverse le transform to get original label back. 
        prediction_RF = le.inverse_transform(prediction_RF)
        return prediction_RF
    

    #show the heat map of the prediction made before to see clearly how did the model learn.
    def showmetrics (self ,prediction_RF ,test_labels):
        print ("Accuracy = ", metrics.accuracy_score(test_labels, prediction_RF))
        #Confusion Matrix - verify accuracy of each class
        cm = confusion_matrix(test_labels, prediction_RF)
        
        sns.heatmap(cm, annot=True)
        

    #Test the Model
    def prediction(self):
        
        test_image , test_label = self.get_test_set()

        y_test_encoded , le = self.model_common.encode_labels(test_label)

        x_test = self.model_common.normalize_img(test_image)

        X = self.model_common.flatt(x_test)
        rfc = joblib.load(self.path_of_model_to_test)

        result = rfc.predict(X)

        inverted_resulted = le.inverse_transform(result)
        self.showmetrics(inverted_resulted, test_label)
        accuracy = metrics.accuracy_score(test_label, inverted_resulted)
        
        return inverted_resulted , accuracy