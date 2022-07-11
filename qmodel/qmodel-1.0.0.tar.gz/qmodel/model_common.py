from sklearn import preprocessing

# author: Sebag Ethan
# date: 07/07/22
# version 1.0

class ModelCommon:
    
    #Here is reunited every methods that are used for training, training and testing an Random Forest Classifier Model

    def __init__(self) -> None:
        pass

    #encode the label of the images to be used by the Random Forest Classifier 
    def encode_labels(self, set_label ):
        #Encode labels from text to integers.
        le = preprocessing.LabelEncoder()
        le.fit(set_label)
        labels_encoded = le.transform(set_label)
        return labels_encoded , le


    #normalize an image or an image set which need to be a np.array of images
    def normalize_img(self, image):
        image = image / 255.0
        return image   


    #To flat a numpy array of images like a train set or a test set (from 4dimension to 2)
    def flatt(self, np_array):
        return np_array.reshape(np_array.shape[0], (np_array.shape[1]*np_array.shape[2]*np_array.shape[3]))


    




