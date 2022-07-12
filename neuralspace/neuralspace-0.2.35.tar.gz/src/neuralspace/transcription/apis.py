import logging
import uuid
from copy import copy
from multiprocessing import Queue
from threading import Thread
from typing import Any, Dict, Text

import sounddevice as sd
from rich.console import Console
from rich.table import Table

from neuralspace.apis import get_async_http_session
from neuralspace.constants import (
    AUTHORIZATION,
    COMMON_HEADERS,
    CROSS,
    DOWN_ARROW,
    ERROR,
    GREEN_TICK,
    INFO,
    RED_END,
    RED_START,
    SAD_SMILEY,
    neuralspace_url,
)
from neuralspace.transcription.constants import TRANSCRIPTION_LANGUAGE_CATALOGUE_URL
from neuralspace.transcription.language_map import LANGUAGE_MAP
from neuralspace.transcription.web_socket import start_websocket_stream
from neuralspace.utils import get_auth_token, is_success_status

console = Console()

logger = logging.getLogger("rich")


def start_transcription(
    sub_url: Text, sample_rate: int, device: int, output_queue: Queue = None
):
    HEADERS = copy(COMMON_HEADERS)
    HEADERS[AUTHORIZATION] = get_auth_token()
    client_id = uuid.uuid4().hex[:8]
    neuralspace_url_full = neuralspace_url()
    stream_url = neuralspace_url_full.replace("https://", "")
    ingress = f"stream/{sub_url}"
    blocksize = int(sample_rate / 2)
    t = Thread(
        target=start_websocket_stream,
        args=[
            stream_url,
            client_id,
            blocksize,
            ingress,
            device,
            sample_rate,
            HEADERS[AUTHORIZATION],
            output_queue,
        ],
        daemon=True,
    )
    t.start()


async def start_stream(
    suburl: str, sample_rate: int, device: int, output_queue: Queue = None
):
    HEADERS = copy(COMMON_HEADERS)
    HEADERS[AUTHORIZATION] = get_auth_token()
    client_id = uuid.uuid4().hex[:8]
    neuralspace_url_full = neuralspace_url()
    stream_url = neuralspace_url_full.replace("https://", "")
    ingress = f"stream/{suburl}"
    blocksize = int(sample_rate / 2)
    start_websocket_stream(
        stream_url,
        client_id,
        blocksize,
        ingress,
        device,
        sample_rate,
        HEADERS[AUTHORIZATION],
        output_queue=output_queue,
    )


def list_all_devices():
    print(sd.query_devices())


async def get_languages() -> Dict[Text, Any]:
    console.print(
        f"> {INFO} {DOWN_ARROW}️ Fetching all supported languages for Stream Transcription"
    )
    HEADERS = copy(COMMON_HEADERS)
    HEADERS[AUTHORIZATION] = get_auth_token()
    model_map = LANGUAGE_MAP
    async with get_async_http_session().get(
        url=f"{neuralspace_url()}/{TRANSCRIPTION_LANGUAGE_CATALOGUE_URL}",
        headers=HEADERS,
    ) as response:
        json_response = await response.json(encoding="utf-8")
        print(json_response)
        if is_success_status(response.status):
            console.print(f"> {INFO} {GREEN_TICK} Successfully Fetched Languages")
            table = Table(show_header=True, header_style="sandy_brown")
            table.add_column("Language Code", style="green")
            table.add_column("Language")
            table.add_column("Domain")
            table.add_column("SubUrl")
            for language_dict in json_response["data"]:
                language_code = language_dict["code"]
                language = language_dict["language"]
                for model in model_map[language_code]:
                    specialization = model["domain"]
                    suburl = model["suburl"]
                    table.add_row(language_code, language, specialization, suburl)
            console.print(table)
        else:
            console.print(f"> {ERROR} {CROSS} Failed to fetch languages")
            console.print(
                f'''> Reason for failure {SAD_SMILEY}: " {RED_START}{json_response['message']}{RED_END} "'''
            )
    return json_response
