from typing import List

from rdflib import Graph, Literal

from ..ns import *
from .AddressComponent import AddressComponent


class AddressArea(AddressComponent):
    __type__ = CLV["AddressArea"]

    name: List[Literal] = None

    def _addProperties(self, g: Graph):
        if self.name:
            for name in self.name:
                g.add((self.uriRef, L0["name"], name))
