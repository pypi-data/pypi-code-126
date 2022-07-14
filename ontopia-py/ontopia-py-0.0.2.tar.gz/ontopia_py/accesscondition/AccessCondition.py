from typing import List

from rdflib import Graph, Literal

from ..ns import *
from ..l0.Characteristic import Characteristic
from ..Thing import Thing


class AccessCondition(Characteristic):
    __type__ = ACOND["AccessCondition"]

    isAccessConditionOf: List[Thing] = None
    description: List[Literal] = None

    def _addProperties(self, g: Graph):
        if self.isAccessConditionOf:
            for isAccessConditionOf in self.isAccessConditionOf:
                g.add((self.uriRef, ACOND["isAccessConditionOf"],
                       isAccessConditionOf.uriRef))

        if self.description:
            for description in self.description:
                g.add((self.uriRef, L0["description"], description))
