from typeguard import typechecked

from genesisapi.datatypes import JSON, Language, Area
from genesisapi.result import Variable


class MetadataService:
    service_name = 'metadata'

    def __init__(self, client):
        self.client = client

    @typechecked
    def cube(
            self,
            name,
            area: Area = None,
            language: Language = None
    ) -> JSON:
        pass

    def statistic(self):
        pass

    @typechecked
    def table(
            self,
            name,
            area: Area = None,
            language: Language = None
    ) -> JSON:
        pass

    @typechecked
    def timeseries(
            self,
            name,
            area: Area = None,
            language: Language = None
    ) -> JSON:
        pass

    @typechecked
    def value(
            self,
            name,
            area: Area = None,
            language: Language = None
    ) -> JSON:
        url = self.client.get_url(
            MetadataService.service_name,
            'value',
            name=name,
            area=area,
            language=language)

        json = self.client.get_json_result(url)
        return Variable(json)

    @typechecked
    def variable(
            self,
            name,
            area: Area = None,
            language: Language = None
    ) -> JSON:
        url = self.client.get_url(
            MetadataService.service_name,
            'variable',
            name=name,
            area=area,
            language=language)

        json = self.client.get_json_result(url)
        return Variable(json)
