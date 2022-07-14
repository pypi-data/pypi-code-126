from typing import List

from rdflib import Graph, Literal, URIRef

from ..ns import *
from ..Thing import Thing
from .TemporalEntity import TemporalEntity


class DayOfWeek(TemporalEntity):
    __type__ = TI["DayOfWeek"]

    isDayOfWeekOf: List[Thing] = []
    day: Literal = None

    def _addProperties(self, g: Graph):
        for isDayOfWeekOf in self.isDayOfWeekOf:
            g.add((self.uriRef, TI["isDayOfWeekOf"],
                  isDayOfWeekOf.uriRef))

        if self.day:
            g.add((self.uriRef, TI["day"], self.day))


class Monday(DayOfWeek):
    def __init__(self):
        self.uriRef = URIRef(TI["Monday"])


class Tuesday(DayOfWeek):
    def __init__(self):
        self.uriRef = URIRef(TI["Tuesday"])


class Wednesday(DayOfWeek):
    def __init__(self):
        self.uriRef = URIRef(TI["Wednesday"])


class Thursday(DayOfWeek):
    def __init__(self):
        self.uriRef = URIRef(TI["Thursday"])


class Friday(DayOfWeek):
    def __init__(self):
        self.uriRef = URIRef(TI["Friday"])


class Saturday(DayOfWeek):
    def __init__(self):
        self.uriRef = URIRef(TI["Saturday"])


class Sunday(DayOfWeek):
    def __init__(self):
        self.uriRef = URIRef(TI["Sunday"])
