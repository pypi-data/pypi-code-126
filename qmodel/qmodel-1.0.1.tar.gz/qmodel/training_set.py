import shutil
from skimage.util import random_noise
import os
import cv2
import numpy as np
from PIL import Image
import cv2


# author: Sebag Ethan
# date: 07/07/22
# version 1.0

class TrainingSet:

    # This class create a full set of digits images for training a RFC Model just with 10 images of every digits
    # from 0 to 9. 
    # She can also take images from more than one token, so if you want to create a training dataset from multiple 
    # token you have to give a list of path where are save the 10 digits images for every token.
    
    def __init__(self,  name,  path, original_10_img , storeImages = False):
        self.storeImages = storeImages
        name = str(name)
        transformed_path = path + f"{name}/transformation/"
        if not os.path.exists(transformed_path):
            os.makedirs(transformed_path)
        for i in range (0, len(original_10_img)):
            tpath = original_10_img[i]
            self.transformation(i,tpath,transformed_path )
        training_set_path = path + f"{name}/training_set/"
        if not os.path.exists(training_set_path):
                os.makedirs(training_set_path)
        self.process(transformed_path, training_set_path)
        #if you want to save images before they have been renamed and resized set storeImages to True
        if (not self.storeImages):
            shutil.rmtree(transformed_path , ignore_errors=False, onerror=None)
            




        

    #return the path of the model created
    def get_model_path(self):
        return self.joblibl_model_path
    
    #to show images
    def showImage(self, title, img):
        cv2.imshow(title, img)
        key = cv2.waitKey(0)
        cv2.destroyWindow(title)


    #Rotation function
    def rotation(self, img, angle):
        #get the size of the image
        height, width , third = img.shape
        #get center point of the image
        x_center = width/2
        y_center = height/2
        #invert the image to get white number on black background
        inverted = cv2.bitwise_not(img)
        #rotate the image
        M = cv2.getRotationMatrix2D((x_center, y_center), angle, 1.0)
        rotated_img = cv2.warpAffine(inverted, M, (width, height) )

        rotated_img = cv2.bitwise_not(rotated_img)
        #showImage(f"rotated image with an angle of {angle} °", rotated_img)
        return rotated_img


    #Erosion function
    def erosion(self, img, size):
        # Creating kernel
        kernel = np.ones((size, size), np.uint8)
        
        # Using cv2.erode() method 
        eroded_img = cv2.erode(img, kernel) 
        #showImage("eroded", eroded_img)
        return eroded_img
        

    #dilatation function
    def dilatation(self, img, size):
        # Creating kernel
        kernel = np.ones((size, size), np.uint8)
        
        # Using cv2.dilate() method 
        dilated_img = cv2.dilate(img, kernel) 
        #showImage("eroded", dilated_img)
        return dilated_img

    #########################################
    ####      CROPPING PART       ###########
    #########################################

    #get average of pixel value of any column  of the image
    def getVerticalProjectionProfile(self, image , width):
        vertical_avg = np.array([0]*width , dtype= 'object')
        i = 0
        imageT = np.transpose(image, (1, 0, 2) )
        for columns in  imageT:
            avg = np.average(columns)     
            #print(f"la moyenne de la colonne {i} est {avg}")
            vertical_avg[i] = avg
            i+=1
        return vertical_avg

    #get average of pixel value of any line of the image
    def getHorizontalProjectionProfile(self, image ,height ):
        horizontal_avg = np.array([0]*height , dtype= 'object')
        i = 0
        for columns in  image:
            avg = np.average(columns)     
            #print(f"la moyenne de la ligne {i} est {avg}")
            horizontal_avg[i] = avg
            i+=1
        return horizontal_avg


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
            #print(f"on a pas crop au debut")

        
        for i in range (1 , len(horizontal_avg)):
            if (horizontal_avg[i] <threshold and horizontal_avg[i-1] >= threshold and first_wb == False):
                #beginning of the digit
                #print("debut du digit")
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
            #print("on a pas crop a la fin")


        for j in range (digit_end,-1,-1):
            if (horizontal_avg[j] >=threshold and horizontal_avg[j-1] < threshold and last_wb == False ):
                #print("fin du digit")
                digit_end = j
                last_wb =True
                
                break
        if (digit_end != 0):
            coordinate.append(digit_end)
        else:
            coordinate.append(len(horizontal_avg)-1)

        return coordinate


    #Horizontaly cut of every image 
    def crop_top_bot(self, coordinate, img):
        return img[coordinate[0]:coordinate[1]]

    #crop the original image in sections for every digits 
    def crop_edges(self, coordinate, img):
        digit = np.transpose(img, (1, 0, 2) )
        digit = digit[coordinate[0]:coordinate[1]]
        digit = np.transpose(digit, (1,0,2))
        return digit

    def crop_image(self, image, threshold):
        
        height, width , third_dimension = image.shape

        #print(f"height is {height}, width is {width}")

        vertical_projection = self.getVerticalProjectionProfile(image, width )
        #print (f"vertical image {vertical_projection}")

        cord_vertical = self.get_coordinate_digit_line(vertical_projection , threshold)
        #print(f"here are vertical coordinates of the images {cord_vertical}")

        verticaly_cropped = self.crop_edges(cord_vertical , image)


        horizontal_projection = self.getHorizontalProjectionProfile(verticaly_cropped , height)

        horizontal_coordinate = self.get_coordinate_digit_line(horizontal_projection , threshold)
        #print (f"horizontall projection {horizontal_coordinate}")

        horizontal_cropped = self.crop_top_bot(horizontal_coordinate, verticaly_cropped)
        #showImage("image_crope", horizontal_cropped)
        return horizontal_cropped


    #return an image after otsu filter has been passed
    def otsu(self, image):
        #convert the image in gray scale
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #showImage("gray", img_gray)

        #convert the image in binary image using OTSU threshold provided by opencv
        ret, thresh1 = cv2.threshold(img_gray, 120, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) 
        return thresh1 


    #Noise creator function
    def noise_creator(self,img, perc):
        noised_image = random_noise(img, mode='s&p' , seed = None , clip = True, amount = perc )
        #adding some noise to the image
        noised_image = self.otsu((noised_image*255).astype(np.uint8))
        return noised_image


###############################################################
##       TO CREATE A TRAINING SET USE THIS FUNCTION          ##
###############################################################
    #create a training set by affecting rotation, erosion, dilatation to the 10 digits images
    def transformation(self,token_name, path, dpath):
        #loop over every images from the token
        for i in range (0,10):
            #look the right image
            impath = path + str(i) + ".jpg"
            dest_path = dpath + str(i)+"/"
            if not os.path.exists(dest_path):
                    os.makedirs(dest_path)
            #read the image from path
            img =  cv2.imread(impath)
            #for each image we make 11 rotation (from -5 to 5 degree) 
            for j in range (-50, 60,10):
                #call the rotation function to rotate the image of j degree
                angle = j/10
                rotated_image = self.rotation(img,angle )
                #call the erosion function to erode the image with a 3x3 mask
                eroded_image_1 = self.erosion(rotated_image, 3)
                #call the crop function to get the cropped image of the eroded one
                cropped_image_1 = self.crop_image(eroded_image_1,240)
                path_to_save = os.path.join(dest_path,f"{token_name}_" "erode3" f"angle_{angle}_.jpg"  )
                #save the cropped image in the path:
                cv2.imwrite(path_to_save  , cropped_image_1)
                #call the erosion function to erode the image with a 5x5 mask
                eroded_image_2 = self.erosion(rotated_image, 5)
                #call the crop function to get the cropped image of the eroded one
                cropped_image_2 = self.crop_image(eroded_image_2,240)
                path_to_save2 = os.path.join(dest_path ,f"{token_name}_" "erode5" f"angle_{angle}_.jpg"  )
                #save the cropped image in the path:
                cv2.imwrite(path_to_save2, cropped_image_2)
                #call the dilatation function to erode the image with a 3x3 mask
                dilated_image_1 = self.dilatation(rotated_image, 3)
                #call the crop function to get the cropped image of the eroded one
                cropped_image_3 = self.crop_image(dilated_image_1,240)
                path_to_save3 = os.path.join(dest_path ,f"{token_name}_""dilate3" f"angle_{angle}_.jpg"  )
                #save the cropped image in the path:
                cv2.imwrite(path_to_save3, cropped_image_3)
                #call the dilatation function to erode the image with a 5x5 mask
                dilated_image_2 = self.dilatation(rotated_image, 5)
                #call the crop function to get the cropped image of the eroded one
                cropped_image_5 = self.crop_image(dilated_image_2,240)
                path_to_save4 = os.path.join(dest_path,f"{token_name}_" "dilate5" f"angle_{angle}_.jpg"  )
                #save the cropped image in the path:
                cv2.imwrite(path_to_save4, cropped_image_5)


##############################################################################


    #Filter every image of a folder with an Otsu filter
    def otsu_display_transform(self, directory_path , directory_to_save):
        if not os.path.exists(directory_to_save):
                    os.makedirs(directory_to_save)
        for filename in os.listdir(directory_path):
            img = cv2.imread(directory_path+filename)
            otsued = self.otsu(img)
            path_to_save = directory_to_save + filename
            cv2.imwrite(path_to_save, otsued)


    #Crop every digit images of a folder to delete the useless edges of digits images.  
    def crop_folder(self, directory_path,directory_to_save):
        if not os.path.exists(directory_to_save):
                    os.makedirs(directory_to_save)
        for i in range(0,10):
            path = directory_path + str(i) + "/"
            for filename in os.listdir(path):
                img = cv2.imread(path+filename)
                cropped = self.crop_image(img,240)
                if not os.path.exists(directory_to_save+str(i)):
                    os.makedirs(directory_to_save+str(i))
                path_to_save = directory_to_save +str(i)+"/" +filename
                cv2.imwrite(path_to_save, cropped)

    #Resize every images of a folder
    def resize(self, src_path, dst_path):
        # Here src_path is the location where images are saved.
        for filename in os.listdir(src_path):
            try:
                img=Image.open(src_path+filename)
                new_img = img.resize((45,45))
                if not os.path.exists(dst_path):
                    os.makedirs(dst_path)
                new_img.save(dst_path+filename)
            except:
                continue

    #rename every file of a folder
    def rename(self, path,obj):
        i=0
        for filename in os.listdir(path):
            try:
                f,extension = os.path.splitext(path+filename)
                src=path+filename
                dst=path+obj+str(i)+extension
                os.rename(src,dst)
                i+=1
            except:
                i+=1

    #resize and rename every images of a folder
    def process(self, src_path , dst_path):
        for i in range(0,10):
            src_path2 = src_path + str(i) + "/"
            dst_path2 = dst_path + str(i) + "/"
            path2 = dst_path + str(i) + "/"
            obj2 = "_"+str(i)+"_"
            self.resize(src_path2, dst_path2)
            self.rename(path2,obj2)



        
        

