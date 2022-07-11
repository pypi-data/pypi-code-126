import os

from slack_sdk import WebClient
from typing import Optional, Union, List


class SlackNotification:
    def __init__(self, api_key: Optional[str]) -> None:
        self.api_key = api_key
        self.client = WebClient(os.environ.get("SLACK_TOKEN", self.api_key))

    def notify(self, alert: str, channel_ids: Union[List[str], str]):
        if isinstance(channel_ids, str):
            self.client.chat_postMessage(
                channel=channel_ids,
                text=alert
            )

        elif isinstance(channel_ids, list):
            for cid in channel_ids:
                self.client.chat_postMessage(
                    channel=cid,
                    text=alert
                )
        else:
            raise TypeError(f"Channel id must either be a single string or a list of strings, got: {channel_ids.__class__}")