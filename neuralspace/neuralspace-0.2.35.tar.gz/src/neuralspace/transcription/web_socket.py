from multiprocessing import Queue
from threading import Thread
from typing import Text

import sounddevice as sd
import websocket

from neuralspace.transcription.constants import TRANSCRIPTION_STREAMING_URL


class WebsManager:
    def __init__(self, webs_url: Text) -> None:
        self.webs_url = webs_url

        self.ws = websocket.WebSocket()

    def __enter__(self):
        self.ws.connect(
            self.webs_url,
            timeout=600,
        )
        return self.ws

    def __exit__(self, *exc):
        self.ws.close()
        self.ws.shutdown()


FLAG = True


def start_websocket_stream(  # noqa: C901
    host: str,
    client_id: int,
    chunksize: int,
    ingress: str,
    device: int,
    sample_rate: int,
    auth_token: str,
    output_queue: Queue = None,
):
    q = Queue()

    def callback(data, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        q.put(bytes(data))

    formed_url = (
        f"wss://{host}/{ingress}/{TRANSCRIPTION_STREAMING_URL}/{auth_token}/{client_id}"
    )
    global FLAG

    def listen(ws, queue: Queue):
        try:
            while FLAG:
                transcription = ws.recv()

                transcription = transcription.encode("raw_unicode_escape").decode(
                    "unicode_escape"
                )

                print("Transcription :: ", transcription)
                if queue:
                    queue.put(transcription)
        except Exception:
            print("Closing listening thread.")

    with WebsManager(formed_url) as ws:
        t = Thread(target=listen, args=[ws, output_queue], daemon=True)
        t.start()
        try:
            with sd.RawInputStream(
                samplerate=sample_rate,
                blocksize=chunksize,
                device=device,
                dtype="int16",
                channels=1,
                callback=callback,
            ):

                while True:
                    data = q.get()
                    if not data:
                        FLAG = False
                        break

                    ws.send_binary(data)

        except KeyboardInterrupt:
            print("\nDone")
