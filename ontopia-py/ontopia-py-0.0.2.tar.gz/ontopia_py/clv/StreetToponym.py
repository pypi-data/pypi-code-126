from typing import List

from rdflib import Graph, Literal

from ..ns import *
from .AddressComponent import AddressComponent


class StreetToponym(AddressComponent):
    __type__ = CLV["StreetToponym"]

    officialStreetName: List[Literal] = None
    toponymQualifier: List[Literal] = None

    def _addProperties(self, g: Graph):
        if self.officialStreetName:
            for officialStreetName in self.officialStreetName:
                g.add(
                    (self.uriRef, CLV["officialStreetName"], officialStreetName))

        if self.toponymQualifier:
            for toponymQualifier in self.toponymQualifier:
                g.add((self.uriRef, CLV["toponymQualifier"], toponymQualifier))
