from typing import List

from rdflib import Graph, Literal

from ..ns import *
from ..l0.Object import Object
from .UserAccount import UserAccount


class SocialMedia(Object):
    __type__ = SM["SocialMedia"]

    socialMediaName: Literal = None
    issuesAccount: List[UserAccount] = None

    def _addProperties(self, g: Graph):
        if self.socialMediaName:
            g.add((self.uriRef, SM["socialMediaName"], self.socialMediaName))

        if self.issuesAccount:
            for issuesAccount in self.issuesAccount:
                g.add((self.uriRef, SM["issuesAccount"], issuesAccount.uriRef))
