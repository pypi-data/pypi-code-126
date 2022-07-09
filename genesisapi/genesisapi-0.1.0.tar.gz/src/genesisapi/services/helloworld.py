from typeguard import typechecked

from genesisapi.datatypes import JSON


class HelloworldService:
    service_name = 'helloworld'

    def __init__(self, client):
        self.client = client

    @typechecked
    def whoami(self) -> JSON:
        url = self.client.get_url(
            HelloworldService.service_name,
            'whoami')

        return self.client.get_json_result(url)

    @typechecked
    def logincheck(self) -> JSON:
        url = self.client.get_url(
            HelloworldService.service_name,
            'logincheck')

        return self.client.get_json_result(url)
