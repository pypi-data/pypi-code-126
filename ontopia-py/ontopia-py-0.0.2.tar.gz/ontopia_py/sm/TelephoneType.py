from typing import List

from rdflib import Graph

from ..ns import *
from ..l0.Concept import Concept
from .Telephone import Telephone


class TelephoneType(Concept):
    __type__ = SM["TelephoneType"]

    isTelephoneTypeOf: List[Telephone] = None

    def _addProperties(self, g: Graph):
        if self.isTelephoneTypeOf:
            for isTelephoneTypeOf in self.isTelephoneTypeOf:
                g.add(
                    (self.uriRef, SM["isTelephoneTypeOf"], isTelephoneTypeOf.uriRef))
