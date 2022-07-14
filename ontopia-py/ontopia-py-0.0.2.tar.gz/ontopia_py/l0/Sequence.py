from rdflib import Graph

from ..ns import *
from .Collection import Collection
from .Entity import Entity


class Sequence(Collection):
    __type__ = L0["Sequence"]

    hasFirstMember: Entity = None
    hasLastMember: Entity = None

    def _addProperties(self, g: Graph):
        if self.hasFirstMember:
            g.add((self.uriRef, L0["hasFirstMember"],
                  self.hasFirstMember.uriRef))

        if self.hasLastMember:
            g.add((self.uriRef, L0["hasLastMember"],
                  self.hasLastMember.uriRef))
