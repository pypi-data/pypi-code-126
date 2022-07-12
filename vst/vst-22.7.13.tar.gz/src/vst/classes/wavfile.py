import wave
from pathlib import Path


class WavFile:
    path_to_wav_file:   Path = Path()
    number_of_frames:   int = -1
    number_of_channels: int = -1
    framerate:          int = -1
    duration:           float = -1

    def open(self, path_to_wav_file: Path):
        self.path_to_wav_file = path_to_wav_file

        with wave.open(str(self.path_to_wav_file), 'r') as wav_file:
            self.number_of_frames = wav_file.getnframes()
            self.number_of_channels = wav_file.getnchannels()
            self.framerate = wav_file.getframerate()
            self.duration = self.number_of_frames / self.framerate * self.number_of_channels

    def get_file_duration(self) -> float:
        return round((self.number_of_frames / self.framerate * self.number_of_channels), 2)

    def get_formatted_length(self) -> str:
        duration_int = int(self.number_of_frames / self.framerate * self.number_of_channels)
        milliseconds = int(round(self.duration - duration_int, 3) * 1000)

        return '{:02}:{:02}:{:02}.{:03}'.format(
            duration_int // 3600,
            duration_int % 3600 // 60,
            duration_int % 60,
            milliseconds,
        )
