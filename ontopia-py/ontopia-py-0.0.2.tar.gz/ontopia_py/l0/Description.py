from rdflib import Graph, Literal

from ..ns import *
from .Object import Object


class Description(Object):
    __type__ = L0["Description"]

    description: Literal = None

    def _addProperties(self, g: Graph):
        if self.description:
            g.add((self.uriRef, L0["description"], self.description))
