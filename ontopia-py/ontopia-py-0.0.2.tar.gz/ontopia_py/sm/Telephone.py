from rdflib import Graph, Literal

from ..ns import *
from ..l0.Object import Object
from .OnlineContactPoint import OnlineContactPoint
from .TelephoneType import TelephoneType


class Telephone(Object):
    __type__ = SM["Telephone"]

    hasTelephoneType: TelephoneType = None
    isTelephoneOf: OnlineContactPoint = None
    telephoneNumber: Literal = None

    def _addProperties(self, g: Graph):
        if self.hasTelephoneType:
            g.add((self.uriRef, SM["hasTelephoneType"],
                  self.hasTelephoneType.uriRef))

        if self.isTelephoneOf:
            g.add((self.uriRef, SM["isTelephoneOf"],
                  self.isTelephoneOf.uriRef))

        if self.telephoneNumber:
            g.add((self.uriRef, SM["telephoneNumber"], self.telephoneNumber))
