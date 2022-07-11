from .training_set import TrainingSet

# og_10_img_path is a list of pathes where are the 10 digits images from every token you want to use to create a training dataset
# for example: og_10_img_path = ["path1", "path2", "path3"]
# set the storeImages to True if you want to save the digits images before renaming and resizing
og_10_img_path = ["path of token1", "path of token 2" , "path of token 3"]

test_all_model = TrainingSet("name of the training set" , "path where to save the training set" , og_10_img_path , False )