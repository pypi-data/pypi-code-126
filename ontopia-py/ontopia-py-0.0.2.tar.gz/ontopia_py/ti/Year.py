from typing import List

from rdflib import Graph, Literal

from ..ns import *
from ..Thing import Thing
from .TemporalEntity import TemporalEntity


class Year(TemporalEntity):
    __type__ = TI["Year"]

    year: Literal = None
    isYearOf: List[Thing] = []

    def _addProperties(self, g: Graph):
        for isYearOf in self.isYearOf:
            g.add((self.uriRef, TI["isYearOf"], isYearOf.uriRef))

        if self.year:
            g.add((self.uriRef, TI["year"], self.year))
