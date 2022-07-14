from typing import List

from rdflib import Graph

from ..ns import *
from ..l0.Characteristic import Characteristic
from ..l0.Entity import Entity
from ..Thing import Thing


class TemporalEntity(Entity):
    __type__ = TI["TemporalEntity"]

    hasTimeParameter: List[Characteristic] = []
    isTemporalEntityOf: List[Thing] = []

    def _addProperties(self, g: Graph):
        for hasTimeParameter in self.hasTimeParameter:
            g.add((self.uriRef, TI["hasTimeParameter"],
                  hasTimeParameter.uriRef))

        for isTemporalEntityOf in self.isTemporalEntityOf:
            g.add((self.uriRef, TI["isTemporalEntityOf"],
                  isTemporalEntityOf.uriRef))
