from typing import List

from rdflib import Graph

from ..ns import *
from ..l0.Characteristic import Characteristic
from ..Thing import Thing


class MeasurementUnit(Characteristic):
    __type__ = MU["MeasurementUnit"]

    isMeasurementUnitOf: List[Thing] = None

    def _addProperties(self, g: Graph):
        if self.isMeasurementUnitOf:
            for isMeasurementUnitOf in self.isMeasurementUnitOf:
                g.add((self.uriRef, MU["isMeasurementUnitOf"],
                       isMeasurementUnitOf.uriRef))
