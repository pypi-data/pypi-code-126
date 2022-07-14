from typing import List

from rdflib import Graph, Literal

from ..ns import *
from ..Thing import Thing
from .PointOfInterest import PointOfInterest


class PointOfInterestCategory(Thing):
    __type__ = POI["PointOfInterestCategory"]

    POIcategoryName: List[Literal] = None
    isPOICategoryFor: PointOfInterest = None

    def _addProperties(self, g: Graph):
        for POIcategoryName in self.POIcategoryName:
            g.add((self.uriRef, POI["hasPOICategory"], POIcategoryName))

        if self.isPOICategoryFor:
            g.add((self.uriRef, POI["isPOICategoryFor"],
                  self.isPOICategoryFor.uriRef))
