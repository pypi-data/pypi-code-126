import numpy as np
import joblib
from .model_common import ModelCommon

# author: Sebag Ethan
# date: 07/07/22
# version 1.0

class ModelUsing:
    #this class is call when you want to use a trained RFC model to read the value of a digit image

    def __init__(self, model_path_to_use):
        self.model_path_to_use = model_path_to_use
        self.model_common = ModelCommon()

    #load the model to use for the extraction of the otp 
    def get_model(self):
        return joblib.load(self.model_path_to_use)


    #transform a list of images into a numpy array of images
    def transform_list_into_array(self, list_of_images):
        return np.array(list_of_images)
    
    #to use for 
    def otp_prediction(self, list_of_images):
        #get the numpy array of images
        
        image_array = self.transform_list_into_array(list_of_images)

        #get the model to use to extract the otp from the token
        rfc_model = self.get_model()


        #transform images from (0,255) to (0,1)
        normalized_image = self.model_common.normalize_img(image_array)

        #get the vector of images to use 
        images_to_test = self.model_common.flatt(normalized_image)

        #make the prediction
        result = rfc_model.predict(images_to_test)

        return result
