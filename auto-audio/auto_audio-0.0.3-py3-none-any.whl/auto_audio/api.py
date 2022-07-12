# -*- coding: utf-8 -*-

import os
import glob
import logging
import pyfiglet
import soundfile as sf

logger = logging.getLogger(__name__)
# C:\Users\monit\Desktop

class auto_audio:

    def __init__(self):

        self.current_path = os.getcwd()
        self.username = os.path.expanduser('~')[9:]
        self.desktop_path = os.path.join(os.path.expanduser('~'), "Desktop")

    def signature(self) -> None:
        print(pyfiglet.figlet_format("Auto-audio", font="doom"))
        print('------------------------------------------------')

    # Make a directory as 'auto_audio'
    def new_dir(self) -> None:
        dir_name = str()
        if self.username == 'monit':
            self.desktop_path = "C:\\Users\monit\Desktop"
        else:
            dir_name = os.path.join(self.desktop_path, 'auto_audio')

        if os.path.isdir(dir_name):
            logger.warning('This folder is already been.')
            return None
        os.mkdir(dir_name)
        logger.info('You got a "auto-audio" folder.')

        return None

    # Convert wav to mp3
    def converter(self) -> str:
        # collect mp3 files
        mp3_files = glob.glob(f"{self.desktop_path}\\auto_audio\*.mp3")

        for file in mp3_files:
            print(file, end='\n')

        for file in mp3_files:
            # convert mp3 to wav
            os.system(f"""ffmpeg -i {file} -codecs pcm_u8 -ar 44100 {file[:-4]}.wav""")

        return f"{len(mp3_files)} is converted as WAV file."

    # Upload to Air Force
    def run(self) -> None:
        print('########################start#################################')

        wav_files = glob.glob(f"{self.desktop_path}\\auto_audio\*.wav")

        for idx, elem in enumerate(wav_files):
            data = sf.read(elem)
            sf.write(f"\\\\10.1.7.60\RSAD_Storage\AudioD\\27000\\{os.path.basename(elem)[:-4]}.WAV", data[0], data[1])
            print(f"{os.path.basename(elem)[:-4]} is Completed!")

        return None

