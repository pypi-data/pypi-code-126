# For more details,
# visit https://open.assembly.go.kr/portal/data/service/selectAPIServicePage.do/O3VTTM0010223D15681

import json
import requests

__all__ = ["send"]


class send:
    """
    Korean National Assembly Open API Service.
    Returns only JSON string ( XML disabled) on purpose.
    Usage:
        send(
            name='service_unique_string',
            blahblah='xxx',
            blablahh='yyy',
            abcdefgh='zzz'
        ).received  # This is a <class 'dict'>
    """

    def __init__(
        self,
        *,
        name: str = "npeslxqbanwkimebr",
        **kwargs,
    ):
        base_url = "https://open.assembly.go.kr/portal/openapi/"
        for k in kwargs:
            if kwargs[k] == "xml":
                kwargs[k] = "json"

        self.url: str = (
            base_url + name + "?" + "&".join([f"{k}={kwargs[k]}" for k in kwargs])
        )
        print(self.url)
        self.received: dict = json.loads(requests.get(self.url).content)
