import numpy as np

from .utils import get_available_image_libs
from ..logger import logger

def image_write(file: np.ndarray, path: str, img_lib: str="opencv", count: int=5) -> None:
	path = str(path) if not isinstance(path, str) else path
	assert img_lib in get_available_image_libs(), f"Image library '{img_lib}' not in {get_available_image_libs()}"
	if img_lib == "opencv":
		from .libs.opencv import image_write as f
	elif img_lib == "PIL":
		from .libs.pil import image_write as f
	elif img_lib == "lycon":
		from .libs.lycon import image_write as f
	elif img_lib == "skimage":
		from .libs.skimage import image_write as f

	i = 0
	while True:
		try:
			return f(file, path)
		except Exception as e:
			logger.debug(f"Path: {path}. Exception: {e}")
			i += 1

			if i == count:
				raise Exception
