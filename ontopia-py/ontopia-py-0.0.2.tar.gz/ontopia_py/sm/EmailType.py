from typing import List

from rdflib import Graph

from ..ns import *
from ..l0.Concept import Concept
from .Email import Email


class EmailType(Concept):
    __type__ = SM["EmailType"]

    isEmailTypeOf: List[Email] = None

    def _addProperties(self, g: Graph):
        if self.isEmailTypeOf:
            for isEmailTypeOf in self.isEmailTypeOf:
                g.add((self.uriRef, SM["isEmailTypeOf"], isEmailTypeOf.uriRef))
