from typing import List

from rdflib import Graph

from ..ns import *
from ..l0.Object import Object
from ..accesscondition.AccessCondition import AccessCondition


class ContactPoint(Object):
    __type__ = SM["ContactPoint"]

    available: List[AccessCondition] = None

    def _addProperties(self, g: Graph):
        if self.available:
            for available in self.available:
                g.add((self.uriRef, SM["available"], available.uriRef))
