from typing import List

from rdflib import Graph, Literal

from ..ns import *
from .AddressComponent import AddressComponent


class AdminUnitComponent(AddressComponent):
    __type__ = CLV["AdminUnitComponent"]

    name: List[Literal] = None
    hasDirectHigherRank: List[AddressComponent] = None
    hasDirectLowerRank: List[AddressComponent] = None
    hasHigherRank: List[AddressComponent] = None
    hasLowerRank: List[AddressComponent] = None

    def _addProperties(self, g: Graph):
        if self.name:
            for name in self.name:
                g.add((self.uriRef, L0["name"], name))

        if self.hasDirectHigherRank:
            for hasDirectHigherRank in self.hasDirectHigherRank:
                g.add(
                (self.uriRef, CLV["hasDirectHigherRank"], hasDirectHigherRank))

        if self.hasDirectLowerRank:
            for hasDirectLowerRank in self.hasDirectLowerRank:
                g.add((self.uriRef, CLV["hasDirectLowerRank"], hasDirectLowerRank))

        if self.hasHigherRank:
            for hasHigherRank in self.hasHigherRank:
                g.add((self.uriRef, CLV["hasHigherRank"], hasHigherRank))

        if self.hasLowerRank:
            for hasLowerRank in self.hasLowerRank:
                g.add((self.uriRef, CLV["hasLowerRank"], hasLowerRank))
