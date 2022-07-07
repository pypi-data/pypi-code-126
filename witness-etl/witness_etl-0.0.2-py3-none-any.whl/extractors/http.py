
from datetime import datetime
from witness.core.abstract import AbstractExtractor
import requests


class HttpGetExtractor(AbstractExtractor):

    def __init__(self, uri, params: dict or None = None):
        self.params: dict or None = params
        super().__init__(uri)

    def _set_extraction_timestamp(self):
        setattr(self, 'extraction_timestamp', datetime.now())

    def extract(self):

        response = requests.get(url=self.uri, params=self.params)
        response.raise_for_status()

        setattr(self, 'output', response)
        self._set_extraction_timestamp()

        return self

    def unify(self):
        raise NotImplementedError


class JsonHttpGetExtractor(HttpGetExtractor):

    def unify(self):

        data = self.output.json()
        meta = {'extraction_timestamp': self.extraction_timestamp,
                'record_source': self.uri}

        setattr(self, 'output', {'meta': meta, 'data': data})

        return self
