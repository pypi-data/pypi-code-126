from typing import List

from rdflib import Graph, Literal

from ..ns import *
from .AdminUnitComponent import AdminUnitComponent


class Province(AdminUnitComponent):
    __type__ = CLV["Province"]

    acronym: List[Literal] = None

    def _addProperties(self, g: Graph):
        if self.acronym:
            for acronym in self.acronym:
                g.add((self.uriRef, CLV["acronym"], acronym))
