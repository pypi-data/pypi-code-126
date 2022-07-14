from typing import List

from rdflib import Graph

from ..ns import *
from ..l0.Object import Object
from ..Thing import Thing


class Image(Object):
    __type__ = SM["Image"]

    isImageOf: List[Thing] = None

    def _addProperties(self, g: Graph):
        if self.isImageOf:
            for isImageOf in self.isImageOf:
                g.add((self.uriRef, SM["isImageOf"], isImageOf.uriRef))
