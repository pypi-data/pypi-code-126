from rdflib import Graph, Literal

from ..ns import *
from ..l0.Object import Object
from .OnlineContactPoint import OnlineContactPoint


class WebSite(Object):
    __type__ = SM["WebSite"]

    isWebSiteOf: OnlineContactPoint = None
    URL: Literal = None

    def _addProperties(self, g: Graph):
        if self.isWebSiteOf:
            g.add((self.uriRef, SM["isWebSiteOf"], self.isWebSiteOf.uriRef))

        if self.URL:
            g.add((self.uriRef, SM["URL"], self.URL))
