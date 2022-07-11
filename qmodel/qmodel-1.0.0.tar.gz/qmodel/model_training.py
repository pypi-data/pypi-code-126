import os
import cv2
import numpy as np
import glob
import joblib
from sklearn.ensemble import RandomForestClassifier
from .model_common import ModelCommon

# author: Sebag Ethan
# date: 07/07/22
# version 1.0

class ModelTraining:

    #this class is to create a RFC model and train it to make it usable

    def __init__(self, train_set_path, model_path):
        self.train_set_path = train_set_path
        self.model_path = model_path+"rfc.joblib"
        self.model_common = ModelCommon()

    #return the path of the trained model
    def get_model_path(self):
        return self.model_path
    #get a training dataset already created
    def get_train_set(self):
        train_images = []
        train_labels = []
        # for path in self.train_set_path:

        for directory_path in glob.glob(self.train_set_path):
            label = directory_path.split("\\")[-1]
            #print(label)
            for img_path in glob.glob(os.path.join(directory_path, "*.jpg")):
                #print(label +"," +img_path)
                img = cv2.imread(img_path)       
                #img = cv2.resize(img, (45, 45))
                #img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
                train_images.append(img)
                #print("label" ,label)
                train_labels.append(label)
        #transform the list of images and the list of labels into a numpy array of each
        train_images = np.array(train_images)
        train_labels = np.array(train_labels)
        return train_images , train_labels
        
    #train a new Random Forest Classifier Model
    def rfc_training(self, X_for_RF,y_train):
        RF_model = RandomForestClassifier(n_estimators = 100, random_state = 42)
        RF_model.fit(X_for_RF, y_train) #For sklearn no one hot encoding
        return RF_model
       
    #Train the Model
    def train(self):
        train_set, train_label = self.get_train_set()
        
        #create a ModelCommon object to use its methods which are commons
        #to model_training, modul_testing and module_using
        y_train_label_encoded, le = self.model_common.encode_labels(train_label)
        x_train = self.model_common.normalize_img(train_set)
        
        X_for_RF = self.model_common.flatt(x_train)
        RF_model = self.rfc_training(X_for_RF, y_train_label_encoded)
        #save the trained model in the self.model_path
        joblib.dump(RF_model , self.model_path )
        return RF_model


   