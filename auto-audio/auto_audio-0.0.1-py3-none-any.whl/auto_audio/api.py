# -*- coding: utf-8 -*-
__author__ = "hanayong"

import os
import glob
import logging
import soundfile as sf

logger = logging.getLogger(__name__)


class auto_audio:

    def __init__(self):
        self.current_path = os.getcwd()
        self.desktop_path = os.path.join(os.path.expanduser('~'), "Desktop")

        # self.weekday = [
        #     27001, 27002, 27003, 27005, 27006, 27007,  # Mon
        #     27008, 27009, 27010, 27012, 27013, 27014,  # Tue
        #     27015, 27016, 27017, 27019, 27020, 27021,  # Wed
        #     27022, 27023, 27024, 27026, 27027, 27028,  # Thu
        #     27029, 27030, 27031, 27033, 27034, 27035,  # Fri
        #                 ]
        #
        # self.weekend = [
        #     27036, 27037, 27038, 27039, 27040, 27041, 27042, 27043,
        #     27044, 27045, 27046, 27047, 27048, 27049, 27050, 27051
        # ]

        # 혹시 모를 상황을 대비해서
        # self.air_force_path = ['\\\\10.1.7.60', 'RSAD_Storage', 'AudioD', '27000']

    # Make a directory as '김근희'
    def new_dir(self) -> None:
        dir_name = os.path.join(self.desktop_path, 'auto_audio')
        if os.path.isdir(dir_name):
            return None
        os.mkdir(dir_name)

        return None

    # Convert wav to mp3
    @staticmethod
    def converter() -> str:
        # convert wav to
        mp3_files = glob.glob("C:\\Users\STudio\Desktop\\auto_audio\*.mp3")

        for file in mp3_files:
            print(file, end='\n')

        for file in mp3_files:
            # convert df
            # os.system(f"""ffmpeg -i {file} -acodec pcm_u8 -ar 22050 {file[:-4]}.wav""")
            os.system(f"""ffmpeg -i {file} -acodec pcm_u8 -ar 44100 {file[:-4]}.wav""")

        return f"{len(mp3_files)} is converted as WAV file."

    # Upload to Air Force
    @staticmethod
    def run() -> None:

        wav_files = glob.glob("C:\\Users\STudio\Desktop\\auto_audio\*.wav")
        data = []
        for idx, elem in enumerate(wav_files):
            data = sf.read(elem)
            sf.write(f"\\\\10.1.7.60\RSAD_Storage\AudioD\\27000\\{os.path.basename(elem)[:-4]}.WAV", data[0], data[1])
            f"{os.path.basename(elem)[:-4]} is Completed!"

        return None

        # x, Fs = sf.read("C:\\Users\STudio\Desktop\김근희\로제떡복이.wav")
        # sf.write("\\\\10.1.7.60\RSAD_Storage\AudioD\\27000\\27819.WAV", x, Fs)