from typing import List

from rdflib import Graph

from ..ns import *
from .declarations.AddressComponent import AddressComponent


class AddressComponent(AddressComponent):
    __type__ = CLV["AddressComponent"]

    situatedWithin: List[AddressComponent] = None

    def _addProperties(self, g: Graph):
        if self.situatedWithin:
            for situatedWithin in self.situatedWithin:
                g.add(
                    (self.uriRef, CLV["situatedWithin"], situatedWithin.uriRef))
