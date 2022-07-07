import cv2
import numpy as np
from PIL import Image

class Gau_Noise():
    def __init__(self, var):
        super().__init__()

        self.mean = 0
        self.var = var

    def __call__(self, img):
        if not isinstance(img, np.ndarray):
            img = np.array(img)
        img = img/255.
        img += np.random.normal(0, self.var/255., img.shape)
        img = np.clip(img*255., 0, 255).astype(np.uint8)
        img = Image.fromarray(img)
        return img

