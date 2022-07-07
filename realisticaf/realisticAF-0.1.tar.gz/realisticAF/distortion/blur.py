import cv2
import numpy as np
from PIL import Image, ImageFilter

class Gau_Blur():
    def __init__(self, sigma):
        super().__init__()
        self.sigma = sigma

    def __call__(self, img):
        if isinstance(img, np.ndarray):
            img = Image.fromarray(img)
        img = img.filter(ImageFilter.GaussianBlur(self.sigma))    

        return img


class Med_Blur():
    def __init__(self, ks):
        super().__init__()
        self.ks = ks

    def __call__(self, img):
        if isinstance(img, np.ndarray):
            img = Image.fromarray(img)
        img = img.filter(ImageFilter.MedianFilter(self.ks))    

        return img