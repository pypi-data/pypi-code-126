import cv2
# import matplotlib.pyplot as plt

from .tools import Tools

# author: Sebag Ethan
# date: 07/07/22
# version 1.0



class PredictionImages:
# This class do every part of the image processing to get the digits image from a display image which will be used to make prediction

    def __init__(self, display_path ):
        try:
            tools = Tools()
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
                for l in range(0,len(digits)):
                    tempo = cv2.resize(digits[l],(45,45))
                    digits[l] = cv2.cvtColor(tempo, cv2.COLOR_GRAY2RGB)
                self.digits_list = digits
        except:
            # print_exception()
            pass

    

    def getdigitlist(self):
        return self.digits_list

   