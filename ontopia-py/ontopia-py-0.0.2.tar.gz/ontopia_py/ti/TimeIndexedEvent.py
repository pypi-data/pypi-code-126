from typing import List

from rdflib import Graph

from ..ns import *
from ..l0.EventOrSituation import EventOrSituation
from .TimeInterval import TimeInterval


class TimeIndexedEvent(EventOrSituation):
    __type__ = TI["TimeIndexedEvent"]

    atTime: List[TimeInterval] = []

    def _addProperties(self, g: Graph):
        for atTime in self.atTime:
            g.add((self.uriRef, TI["atTime"], atTime.uriRef))
