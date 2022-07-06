import numpy as np
from pathlib import Path

from ..logger import logger
from .utils import get_available_image_libs

def image_read(path:str, img_lib: str="opencv", count: int=5) -> np.ndarray:
	assert img_lib in get_available_image_libs(), f"Image library '{img_lib}' not in {get_available_image_libs()}"
	if img_lib == "opencv":
		from .libs.opencv import image_read as f
	elif img_lib == "PIL":
		from .libs.pil import image_read as f
	elif img_lib == "lycon":
		from .libs.lycon import image_read as f
	elif img_lib == "skimage":
		from .libs.skimage import image_read as f

	path = str(path) if isinstance(path, Path) else path

	i = 0
	while True:
		try:
			return f(path)
		except Exception as e:
			logger.debug(f"Path: {path}. Exception: {e}")
			i += 1

			if i == count:
				raise Exception(e)
