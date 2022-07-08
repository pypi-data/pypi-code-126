# Imports used through the rest of the notebook.
import hashlib
from datetime import datetime
from typing import Text

import torchaudio

from ruth_tts_transformer.parser import TextToSpeech
from ruth_tts_transformer.utils.audio import load_voice


class TTS:
    def __init__(self, voice: Text = "gabby_reading"):
        self.gen = None
        self.preset = "ultra_fast"
        self.voice = voice
        self.tts = TextToSpeech()

    def generate(self, text):
        voice_samples, conditioning_latents = load_voice(self.voice)
        self.gen, _ = self.tts.tts(text, voice_samples=voice_samples,
                                   conditioning_latents=conditioning_latents,
                                   use_deterministic_seed=0,
                                   return_deterministic_state=True,
                                   num_autoregressive_samples=16,
                                   diffusion_iterations=30)

    def parse(self):
        file_name = hashlib.sha1(str(datetime.now()).encode("UTF-8"))
        torchaudio.save(file_name.hexdigest() + '.wav', self.gen.squeeze(0).cpu(), 24000)
        return file_name.hexdigest()
