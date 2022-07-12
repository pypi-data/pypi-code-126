from neuralspace.transcription.apis import start_transcription
from neuralspace.transcription.utils import get_sample_rate_and_suburl_from_language


class NSStreamer:
    def __init__(self, output_queue) -> None:

        self.output_queue = output_queue

    def start_stream(self, language: str, specialization: str, device: int):
        sub_url, sample_rate = get_sample_rate_and_suburl_from_language(
            language, specialization
        )
        if not sub_url or not sample_rate:
            raise ValueError("Choose model language and specialization carefully.")
        start_transcription(sub_url, sample_rate, device, self.output_queue)
