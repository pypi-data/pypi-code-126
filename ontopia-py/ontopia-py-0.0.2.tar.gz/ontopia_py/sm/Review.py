from typing import List

from rdflib import Graph, Literal

from ..ns import *
from .declarations.Post import Post
from .Rating import Rating


class Review(Post):
    __type__ = SM["Review"]

    hasRating: List[Rating] = None
    reviewAspect: Literal = None

    def _addProperties(self, g: Graph):
        if self.hasRating:
            for hasRating in self.hasRating:
                g.add((self.uriRef, SM["hasRating"], hasRating.uriRef))

        if self.reviewAspect:
            g.add((self.uriRef, SM["reviewAspect"], self.reviewAspect))
