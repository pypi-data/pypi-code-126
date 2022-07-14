from typing import List

from rdflib import Graph, Literal

from ..ns import *
from ..Thing import Thing
from .TimeInterval import TimeInterval


class Duration(TimeInterval):
    __type__ = TI["Duration"]

    isDurationOf: List[Thing] = []
    duration: Literal = None

    def _addProperties(self, g: Graph):
        for isDurationOf in self.isDurationOf:
            g.add((self.uriRef, TI["isDurationOf"],
                  isDurationOf.uriRef))

        if self.duration:
            g.add((self.uriRef, TI["duration"], self.duration))
