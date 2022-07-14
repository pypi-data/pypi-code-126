from typing import List

from rdflib import Graph, Literal

from ..ns import *
from .AccessCondition import AccessCondition


class Booking(AccessCondition):
    __type__ = ACOND["Booking"]

    name: List[Literal] = None

    def _addProperties(self, g: Graph):
        if self.isAccessConditionOf:
            for isAccessConditionOf in self.isAccessConditionOf:
                g.add((self.uriRef, ACOND["isAccessConditionOf"],
                       isAccessConditionOf.uriRef))

        if self.name:
            for name in self.name:
                g.add((self.uriRef, L0["name"], name))
