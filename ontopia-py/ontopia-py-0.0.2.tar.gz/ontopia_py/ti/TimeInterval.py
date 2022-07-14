from typing import List

from rdflib import Graph, Literal

from ..ns import *
from .declarations.TimeInterval import TimeInterval
from .TimeInstant import TimeInstant


class TimeInterval(TimeInterval):
    __type__ = TI["TimeInterval"]

    hasTimeInstantInside: List[TimeInstant] = []
    date: List[Literal] = []
    endTime: Literal = None
    startTime: Literal = None

    def _addProperties(self, g: Graph):
        for hasTimeInstantInside in self.hasTimeInstantInside:
            g.add((self.uriRef, TI["hasTimeInstantInside"],
                  hasTimeInstantInside.uriRef))

        for date in self.date:
            g.add((self.uriRef, TI["date"], date.uriRef))

        if self.endTime:
            g.add((self.uriRef, TI["endTime"], self.endTime))

        if self.startTime:
            g.add((self.uriRef, TI["startTime"], self.startTime))
