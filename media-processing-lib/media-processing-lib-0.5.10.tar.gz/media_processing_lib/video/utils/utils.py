"""Generic utility file for videos"""
from typing import Set
from ...logger import logger

def get_available_video_libs() -> Set[str]:
    """Returns a set with all the available video libraries used for reading/writing"""
    res = set()
    try:
        import decord
        res.add("decord")
    except:
        pass
    
    try:
        import pims
        res.add("pims")
    except:
        pass

    try:
        import cv2
        res.add("opencv")
    except:
        pass
    
    try:
        import imageio
        res.add("imageio")
    except:
        pass
    
    if len(res) == 0:
        logger.info("Warning! No video libraries available. Use 'pip install -r requirements.txt'")
    return res
