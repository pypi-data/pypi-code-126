import asyncio
from typing import Text

import click

from neuralspace.apis import get_async_http_session
from neuralspace.ner.constants import SUPPORTED_LANGUAGES
from neuralspace.transcription.apis import get_languages, list_all_devices, start_stream
from neuralspace.transcription.utils import get_sample_rate_and_suburl_from_language
from neuralspace.utils import setup_logger


@click.group(name="transcription")
def transcription():
    pass


@transcription.command(
    name="stream",
)
@click.option(
    "-L",
    "--language",
    type=click.STRING,
    required=True,
    help="language of the audio file",
)
@click.option(
    "-dom",
    "--domain",
    type=click.STRING,
    required=False,
    default="general",
    help="Set to the spefic domain you wish to choose."
    " If not set, a general purpose model will be used",
)
@click.option(
    "-d",
    "--device",
    type=click.INT,
    required=True,
    help="device number of microphone",
)
@click.option(
    "-l", "--log-level", type=click.Choice(["INFO", "DEBUG", "ERROR"]), default="INFO"
)
def stream(language: Text, domain: str, device: int, log_level: Text):
    setup_logger(log_level=log_level)
    if not language:
        raise ValueError(
            f"Language is mandatory. You can select from {SUPPORTED_LANGUAGES}"
        )
    if not device:
        raise ValueError(
            "Run neuralspace transription list-devices and see device number of your microphone."
            "Set -d as the device number."
        )
    sub_url, sample_rate = get_sample_rate_and_suburl_from_language(language, domain)
    if not sub_url or not sample_rate:
        raise ValueError("Choose model language and domain carefully.")
    loop = asyncio.new_event_loop()
    loop.run_until_complete(start_stream(sub_url, sample_rate, device))
    loop.run_until_complete(get_async_http_session().close())


@transcription.command(name="list-devices")
def list_devices():
    list_all_devices()


@transcription.command(name="get-languages")
@click.option(
    "-l", "--log-level", type=click.Choice(["INFO", "DEBUG", "ERROR"]), default="INFO"
)
def translation_get_languages(log_level: Text):
    setup_logger(log_level=log_level)
    loop = asyncio.new_event_loop()
    loop.run_until_complete(get_languages())
    loop.run_until_complete(get_async_http_session().close())
