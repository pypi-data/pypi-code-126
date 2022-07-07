import cv2
import numpy as np
from PIL import Image
import typing

class Compose():
    def  __init__(self, transforms):
        super().__init__()
        self.transforms = transforms
    def __call__(self, data) -> typing.Dict[str, typing.Any]:
        for t in self.transforms:
            data = t(data)
        return data