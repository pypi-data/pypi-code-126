import requests

from vunv79_utilities.libs.logger.setup import init_logging
from vunv79_utilities.libs.telegram.config import HEADERS

logger = init_logging(name="telegram_channel")


class Channel:
    def __init__(self,
                 channel_id,
                 access_token,
                 parse_mode="HTML"):
        if not channel_id:
            raise Exception("Channel ID is not provide")

        # Declare properties
        self.channel_id = channel_id
        self.access_token = access_token
        self.parse_mode = parse_mode
        self.url = f"https://api.telegram.org/bot{self.access_token}/sendMessage"

    def send(self, msg: str):
        if not msg or not msg.strip():
            raise ValueError("Message is not empty")
        payload = {
            "chat_id": f"@{self.channel_id}",
            "parse_mode": self.parse_mode,
            "text": msg
        }
        try:
            response = requests.post(self.url, json=payload, headers=HEADERS)
            result = response.json()
            if result.get("ok"):
                logger.info(f"Send message Telegram channel {self.channel_id} successful")
            else:
                logger.info(result)
        except Exception as ex:
            logger.error(f"AnomalyDetectionChannel :: send :: Ex -> {ex}")
