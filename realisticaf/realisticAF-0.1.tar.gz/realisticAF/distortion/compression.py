import cv2
import numpy as np
from PIL import Image

class JPEG_Compression():
    def __init__(self, jpeg_factor):
        super().__init__()

        self.jpeg_factor = jpeg_factor

    def __call__(self, img):
        if not isinstance(img, np.ndarray):
            img = np.array(img)
        encparam = [int(cv2.IMWRITE_JPEG_QUALITY), self.jpeg_factor] 
        result, encimg = cv2.imencode('.jpg', img, encparam)
        decimg = cv2.imdecode(encimg, 1)
        decimg = Image.fromarray(decimg)
        return decimg

class JPEG_2000():
    def __init__(self):
        super().__init__()

    def __call__(self, img):
        if not isinstance(img, np.ndarray):
            img = np.array(img)
        result, encimg = cv2.imencode('.jp2', img)
        decimg = cv2.imdecode(encimg, 1)
        decimg = Image.fromarray(decimg)
        return decimg
