from typing import List
from rdflib import Graph, URIRef

from ..Thing import Thing
from ..ns import *
from .poiCategory import PointOfInterestCategory
from ..clv.Address import Address


class PointOfInterest(Thing):
    __type__ = POI["PointOfInterest"]

    hasPOICategory: List[PointOfInterestCategory] = []
    hasAddress: List[Address] = []
    hasPOINameInITime = None
    hasImage = None
    atTime = None
    hasGeometry = None
    hasPOIState = None
    isIncludedInPOI = None
    POIofficialName = None
    POIdescription = None
    POIID = None

    def _addProperties(self, g: Graph):
        for poiCategory in self.hasPOICategory:
            g.add((self.uriRef, POI["hasPOICategory"], URIRef(
                POI_CLASSIFICATION[poiCategory])))

        for address in self.hasAddress:
            g.add((self.uriRef, CLV["hasAddress"], address.uriRef))
