from typing import List

from rdflib import Graph

from ..ns import *
from .declarations.Entity import Entity


class Collection(Entity):
    __type__ = L0["Collection"]

    hasMember: List[Entity] = None

    def _addProperties(self, g: Graph):
        if self.hasMember:
            for hasMember in self.hasMember:
                g.add((self.uriRef, L0["hasMember"], hasMember.uriRef))
