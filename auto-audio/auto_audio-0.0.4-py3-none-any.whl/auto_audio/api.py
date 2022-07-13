# -*- coding: utf-8 -*-

import os
import glob
import logging
import pyfiglet
import soundfile as sf

logger = logging.getLogger(__name__)
# C:\Users\monit\Desktop


class auto_audio:
    desktop_path = str()

    def __init__(self):

        self.current_path = os.getcwd()
        self.username = os.path.expanduser('~')[9:]

    def designated_path(self):
        if self.username == 'monit':
            self.desktop_path = "C:\\Users\monit\Desktop"
        else:
            self.desktop_path = "C:\\Users\STudio\Desktop"

    @staticmethod
    def signature() -> None:
        print(pyfiglet.figlet_format("Auto-audio", font="doom"))
        print('------------------------------------------------')

    # Make a directory as 'auto_audio'
    def new_dir(self) -> None:
        self.signature()
        self.designated_path()

        if os.path.isdir(self.desktop_path):
            print('This folder is already been.')
            return None
        os.mkdir(self.desktop_path)
        print('You got a "auto-audio" folder.')

        return None

    # Convert wav to mp3
    def converter(self) -> str:
        # collect mp3 files
        file_path = 'auto_audio\*.mp3'
        mp3_files = glob.glob(f"{os.path.join(self.desktop_path, file_path)}")

        print(f"starting path : {os.path.join(self.desktop_path, file_path)}", end='\n\n')

        for file in mp3_files:
            print(file, end='\n')

        print('They will be converted')

        for file in mp3_files:

            # convert mp3 to wav
            os.system(f"""ffmpeg -i {file} -acodec pcm_u8 -ar 44100 {file[:-4]}.wav""")
            print(f"{len(mp3_files)} is converted as WAV file.")
        return None

    # Upload to Air Force
    def run(self) -> None:
        print(f'Starting path : {self.desktop_path}\\auto_audio')

        wav_files = glob.glob(f"{self.desktop_path}\\auto_audio\*.wav")

        for idx, elem in enumerate(wav_files):
            data = sf.read(elem)
            sf.write(f"\\\\10.1.7.60\RSAD_Storage\AudioD\\27000\\{os.path.basename(elem)[:-4]}.WAV", data[0], data[1])
            print(f"{os.path.basename(elem)[:-4]} is Completed!")

        return None

