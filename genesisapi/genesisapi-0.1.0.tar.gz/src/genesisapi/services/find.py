from typeguard import typechecked

from genesisapi.datatypes import JSON, Category


class FindService:
    service_name = 'find'

    def __init__(self, client):
        self.client = client

    @typechecked
    def find(
            self,
            term,
            category: Category = None,
            page_length: int = None,
    ) -> JSON:
        """"""
        url = self.client.get_url(
            FindService.service_name,
            'find',
            term=term,
            pagelength=page_length,
            category=str(category))

        return self.client.get_json_result(url)
