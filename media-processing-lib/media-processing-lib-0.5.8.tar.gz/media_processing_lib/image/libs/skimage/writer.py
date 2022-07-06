import numpy as np
import skimage.io

def image_write(file: np.ndarray, path: str):
    assert file.min() >= 0 and file.max() <= 255
    skimage.io.imsave(path, file.astype(np.uint8))
