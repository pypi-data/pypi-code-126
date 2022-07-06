import numpy as np
import skimage.io

def image_read(path: str) -> np.ndarray:
	image = np.array(skimage.io.imread(path), dtype=np.uint8)[..., 0 : 3]
	return image
