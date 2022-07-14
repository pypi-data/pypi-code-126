from typing import List

from rdflib import Graph, Literal, URIRef

from ..ns import *
from ..cov.Organization import Organization
from ..l0.Characteristic import Characteristic


class Identifier(Characteristic):
    __type__ = CLV["Identifier"]

    issuedBy: List[Organization] = None
    identifier: URIRef = None
    identifierType: Literal = None

    def _addProperties(self, g: Graph):
        if self.issuedBy:
            for issuedBy in self.issuedBy:
                g.add((self.uriRef, CLV["issuedBy"], issuedBy.uriRef))

        if self.identifier:
            g.add((self.uriRef, L0["identifier"], self.identifier))

        if self.identifierType:
            g.add((self.uriRef, CLV["identifierType"], self.identifierType))
