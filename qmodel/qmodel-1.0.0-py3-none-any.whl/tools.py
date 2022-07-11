import cv2
import numpy as np
import os
# import matplotlib.pyplot as plt
from PIL import Image

class Tools:

    def __init__(self) -> None:
        pass

     #to show images
    def showImage(self, title, img):
        cv2.imshow(title, img)
        key = cv2.waitKey(0)

    #Crop every digit images of a folder.  
    def crop_display_folder(self, directory_path):
        list = []
        for filename in os.listdir(directory_path):
            if(not os.path.isdir(directory_path+filename)):
                img = cv2.imread(directory_path+filename)
                #self.showImage("not crop" , img)
                cropped = self.crop_image(img,230)
                list.append(cropped)
        return list

    #this function crop a display image to delete every useless edges of the display 
    #image to ensure that the cropping of the digits will be correctly done
    def crop_image(self, timage, threshold):
        image = self.otsu(timage) #apply the otsu filter on the image
        height, width  = image.shape
        #get the vertical coordinates to crop edges on the both side of the display 
        vertical_projection = self.getVerticalProjectionProfile(image, width ) 
        cord_vertical = self.get_coordinate_digit_line(vertical_projection , threshold)
        verticaly_cropped = self.crop_edges(cord_vertical , image)
        #get the horizontal coordinates to crop edges on the top and bot side of the display
        horizontal_projection = self.getHorizontalProjectionProfile(verticaly_cropped , height)
        horizontal_coordinate = self.get_coordinate_digit_line(horizontal_projection , threshold)
        horizontal_cropped = self.crop_top_bot(horizontal_coordinate, verticaly_cropped)
        return horizontal_cropped


    #return an image after otsu filter has been used
    def otsu(self, image):
        #convert the image in gray scale
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #convert the image in binary image using OTSU threshold provided by opencv
        ret, thresh1 = cv2.threshold(img_gray, 120, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) 
        return thresh1 


    #get average of pixel value of any column  of the image
    def getVerticalProjectionProfile(self, image , width):
        vertical_avg = np.array([0]*width , dtype= 'object')
        i = 0
        imageT = np.transpose(image, (1, 0) )
        for columns in  imageT:
            avg = np.average(columns)     
            vertical_avg[i] = avg
            i+=1
        return vertical_avg

    
    # get the coordinates of the top and bot side of every digits image 
    # where we are go to crop the image to get a nice and clean image

    def get_coordinate_digit_line(self, horizontal_avg, threshold):
        coordinate = []
        first_wb =False  #first transtion white to black, which means you find the top of the digit
        last_wb = False  #last transtion white to black, which means you find the top of the digit
        digit_begin = 0
        digit_end = len(horizontal_avg)-1
        if (horizontal_avg[0] < threshold and horizontal_avg[1] < threshold ):
            digit_begin = 0
            first_wb =True
        for i in range (1 , len(horizontal_avg)):
            if (horizontal_avg[i] <threshold and horizontal_avg[i-1] >= threshold and first_wb == False):               
                digit_begin = i
                first_wb == True
                break
        if (digit_begin != len(horizontal_avg)-1):
            coordinate.append(digit_begin)
        else:
            coordinate.append(0)
        if (horizontal_avg[len(horizontal_avg)-1] < threshold and horizontal_avg[len(horizontal_avg)-2] < threshold ):
            digit_end = len(horizontal_avg)-1
            last_wb =True
        for j in range (digit_end,-1,-1):
            if (horizontal_avg[j] >=threshold and horizontal_avg[j-1] < threshold and last_wb == False ):              
                digit_end = j
                last_wb =True               
                break
        if (digit_end != 0):
            coordinate.append(digit_end)
        else:
            coordinate.append(len(horizontal_avg)-1)
        return coordinate


    #crop the original image in sections for every digits 
    def crop_edges(self, coordinate, img):
        digit = np.transpose(img, (1, 0) )
        digit = digit[coordinate[0]:coordinate[1]]
        digit = np.transpose(digit, (1,0))
        return digit

    #get average of pixel value of any line of the image
    def getHorizontalProjectionProfile(self, image ,height ):
        horizontal_avg = np.array([0]*height , dtype= 'object')
        i = 0
        for columns in  image:
            avg = np.average(columns)     
            horizontal_avg[i] = avg
            i+=1
        return horizontal_avg

    #Horizontaly cut of every image 
    def crop_top_bot(self, coordinate, img):
        return img[coordinate[0]:coordinate[1]]
    
    #get the coordinates of every vertical digit's edges
    def get_coordinate_digit(self, vertcal_avg, threshold):
        first_wb =False  #first transtion white to black, which means you find the top of the digit
        last_wb = False
        coordinate = [0] #list of coordinates where we are go to vertically cut the image to get separated digits
        for i in range (1 , len(vertcal_avg)):
            if ( vertcal_avg[i-1] >= threshold  and vertcal_avg[i] <threshold ):
                coordinate.append(i)    
            elif (vertcal_avg[i-1] < threshold and vertcal_avg[i] >=threshold):
                coordinate.append(i)
        coordinate.append(len(vertcal_avg)-1)
        return coordinate

    #crop the original image in sections for every digits 
    def cut_digit(self, coordinate, img):
        digit1 =( img.T[coordinate[0]:coordinate[1]+1]).T
        digit2 = (img.T[coordinate[2]:coordinate[3]+1]).T
        digit3 = (img.T[coordinate[4]:coordinate[5]+1]).T
        digit4 = (img.T[coordinate[6]:coordinate[7]+1]).T
        digit5 = (img.T[coordinate[8]:coordinate[9]+1]).T
        digit6 = (img.T[coordinate[10]:coordinate[11]+1]).T
        return digit1, digit2 , digit3 , digit4 , digit5 ,digit6

    #resize every images of a folder
    def resize(self, src_path, dst_path):
        # Here src_path is the location where images are saved.
        for filename in os.listdir(src_path):
            try:
                img=Image.open(src_path+filename)
                new_img = img.resize((45,45))
                if not os.path.exists(dst_path):
                    os.makedirs(dst_path)
                new_img.save(dst_path+filename)
                # print('Resized and saved {} successfully.'.format(filename))
            except:
                continue