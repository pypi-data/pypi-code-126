from typing import Union, Callable
import numpy as np
from pathlib import Path

from .mpl_video import MPLVideo
from ..utils import get_available_video_libs

def video_write(video: MPLVideo, path: Union[str, Path], apply_fn: Callable[[MPLVideo, int], np.ndarray],
    			vid_lib: str="imageio", count: int=5, **kwargs):
	path = str(path) if not isinstance(path, str) else path
	
	assert vid_lib in get_available_video_libs(), f"Video library '{vid_lib}' not in '{get_available_video_libs()}'"
	if vid_lib == "imageio":
		from ..libs.imageio import video_write as f
	elif vid_lib == "opencv":
		from ..libs.opencv import video_write as f

	i = 0
	while True:
		try:
			f(video, path, apply_fn, **kwargs)
			return
		except Exception as e:
			print(f"Path: {path}. Exception: {e}")
			i += 1

			if i == count:
				raise Exception
