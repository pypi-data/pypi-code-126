import cv2
import os
from .tools import Tools

class TestingSet:
# This class can be used to create a dataset for testing a trained model
# To do it, the "display_path" need to include every display images that you wanna use for your testing dataset
# You will get at the destination_path, a folder with all the images of every digits on your display images
# To test a RFC model you will have to sort them by their value and put them into a specified folder
# like, every images of a 1 go into a folder named 1 etc.

    def __init__(self , display_path, destination_path):
        try:
            tools = Tools()
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)
            self.dest = destination_path
            #list of cropped and otsued image
            cropped_image = tools.crop_display_folder(display_path)
            #for each image we extract digit images
            for i in range (0, len(cropped_image)):
                height, width = cropped_image[i].shape
                vertical_avg = tools.getVerticalProjectionProfile(cropped_image[i],  width) #get vertical profile of the token image to separate every digit
                # x = np.arange(0,len(vertical_avg))
                # plt.plot(x,vertical_avg)
                # plt.show()
                coordinate = tools.get_coordinate_digit(vertical_avg , 240) #get coorfinates of every digit on the token image
                #cut every digit 
                digit1, digit2 , digit3 , digit4 , digit5 ,digit6 = tools.cut_digit(coordinate, cropped_image[i]) 
                digits = [digit1, digit2 , digit3 , digit4 , digit5 ,digit6]
                for j in range(0, len(digits)):
                #    self.showImage("digit" ,digits[j])
                    path_to_save = destination_path +f"digits_{i}_{j}.jpg"
                    cv2.imwrite(path_to_save, digits[j])
        except:
            # print_exception()
            pass

    def get_dest_path(self):
        return self.dest