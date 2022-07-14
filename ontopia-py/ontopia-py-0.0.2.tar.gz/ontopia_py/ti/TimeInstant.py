from typing import List

from rdflib import Graph, Literal, Namespace, URIRef

from ..ns import *
from .TemporalEntity import TemporalEntity
from .TimeInterval import TimeInterval


class TimeInstant(TemporalEntity):
    __type__ = TI["TimeInstant"]

    fallsInside: List[TimeInterval] = []
    date: Literal = None
    month: Literal = None
    year: Literal = None

    def _addProperties(self, g: Graph):
        for fallsInside in self.fallsInside:
            g.add((self.uriRef, TI["fallsInside"],
                  fallsInside.uriRef))

        if self.date:
            g.add((self.uriRef, TI["date"], self.date))

        if self.month:
            g.add((self.uriRef, TI["month"], self.month))

        if self.year:
            g.add((self.uriRef, TI["year"], self.year))
