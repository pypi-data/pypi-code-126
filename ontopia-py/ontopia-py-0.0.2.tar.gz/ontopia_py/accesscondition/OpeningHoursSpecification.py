from typing import List

from rdflib import Graph, Literal

from ..ns import *
from ..ti.DayOfWeek import DayOfWeek
from ..ti.TimeInterval import TimeInterval
from .AccessCondition import AccessCondition
from .AdmissionType import AdmissionType


class OpeningHoursSpecification(AccessCondition):
    __type__ = ACOND["OpeningHoursSpecification"]

    atTime: List[TimeInterval] = None
    hasDayOfWeek: List[DayOfWeek] = None
    hasAdmissionType: List[AdmissionType] = None
    closes: List[Literal] = None
    opens: List[Literal] = None

    def _addProperties(self, g: Graph):
        if self.atTime:
            for atTime in self.atTime:
                g.add((self.uriRef, TI["atTime"], atTime.uriRef))

        if self.hasDayOfWeek:
            for hasDayOfWeek in self.hasDayOfWeek:
                g.add((self.uriRef, TI["hasDayOfWeek"], hasDayOfWeek.uriRef))

        if self.hasAdmissionType:
            for hasAdmissionType in self.hasAdmissionType:
                g.add(
                    (self.uriRef, ACOND["hasAdmissionType"], hasAdmissionType.uriRef))

        if self.closes:
            for closes in self.closes:
                g.add((self.uriRef, ACOND["closes"], closes))

        if self.opens:
            for opens in self.opens:
                g.add((self.uriRef, ACOND["opens"], opens))
