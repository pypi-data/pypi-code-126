import cv2
import numpy as np
from PIL import Image, ImageEnhance


class Gamma_Correction():
    def __init__(self, gamma):
        super().__init__()
        self.gamma = gamma

    def __call__(self, img):
        if not isinstance(img, np.ndarray):
            img = np.array(img)

        lookUpTable = [np.clip(((i / 255.0) ** self.gamma) * 255.0, 0, 255) for i in range(256)]
        lookUpTable = np.array(lookUpTable, np.uint8)
        img =  cv2.LUT(img, lookUpTable)
        img = Image.fromarray(img)

        return img

class Sharpness():
    def __init__(self, factor):
        super().__init__()
        self.factor = factor

    def __call__(self, img):
        if isinstance(img, np.ndarray):
            img = Image.fromarray(img)
        enhancer = ImageEnhance.Sharpness(img)
        img = enhancer.enhance(self.factor)    

        return img

class Contrast():
    def __init__(self, factor):
        super().__init__()
        self.factor = factor

    def __call__(self, img):
        if isinstance(img, np.ndarray):
            img = Image.fromarray(img)
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(self.factor)    
        return img

class Brightness():
    def __init__(self, factor):
        super().__init__()
        self.factor = factor

    def __call__(self, img):
        if isinstance(img, np.ndarray):
            img = Image.fromarray(img)
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(self.factor)    
        return img
