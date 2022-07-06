from typing import Tuple, Set
import tempfile
import subprocess
from ...logger import logger

def get_available_audio_libs() -> Set[str]:
    """Returns a set with all the available audio libraries used for reading/writing"""
    res = set()
    try:
        import librosa
        res.add("librosa")
    except:
        pass
    
    try:
        import soundfile
        res.add("soundfile")
    except:
        pass

    if len(res) == 0:
        logger.info("Warning! No image libraries available. Use 'pip install -r requirements.txt'")
    return res

def get_wav_from_video(path: str) -> Tuple[int, str]:
    """Given a video path, use ffmpeg under the hood to extract the audio, and return the audio fd and path."""
    fd, tmp_path = tempfile.mkstemp(suffix=".wav")
    logger.debug2(f"Extracting audio from '{path}'. Will be stored at '{tmp_path}'.")
    command = f"ffmpeg -loglevel panic -y -i {path} -strict -2 {tmp_path}"
    subprocess.call(command, shell=True)
    return fd, tmp_path
