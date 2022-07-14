from rdflib import Graph, Literal

from ..ns import *
from ..l0.Object import Object
from .OnlineContactPoint import OnlineContactPoint
from .EmailType import EmailType


class Email(Object):
    __type__ = SM["Email"]

    hasEmailType: EmailType = None
    isEmailOf: OnlineContactPoint = None
    emailAddress: Literal = None

    def _addProperties(self, g: Graph):
        if self.hasEmailType:
            g.add((self.uriRef, SM["hasEmailType"], self.hasEmailType.uriRef))

        if self.isEmailOf:
            g.add((self.uriRef, SM["isEmailOf"], self.isEmailOf.uriRef))

        if self.emailAddress:
            g.add((self.uriRef, SM["emailAddress"], self.emailAddress))
