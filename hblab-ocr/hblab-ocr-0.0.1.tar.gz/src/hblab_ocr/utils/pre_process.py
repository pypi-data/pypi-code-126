import math
import cv2
import numpy as np
import torch
import os

RGB_MEAN = np.array([122.67891434, 116.66876762, 104.00698793])
IMAGE_SHORT_SIDE = 736


def resize_image(img):
    height, width, _ = img.shape
    if height < width:
        new_height = IMAGE_SHORT_SIDE
        new_width = int(math.ceil(new_height / height * width / 32) * 32)
    else:
        new_width = IMAGE_SHORT_SIDE
        new_height = int(math.ceil(new_width / width * height / 32) * 32)
    resized_img = cv2.resize(img, (new_width, new_height))
    return resized_img


def load_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_COLOR).astype('float32')
    original_shape = img.shape[:2]
    img = resize_image(img)
    img -= RGB_MEAN
    img /= 255.
    img = torch.from_numpy(img).permute(2, 0, 1).float().unsqueeze(0)
    return img, original_shape

