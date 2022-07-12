# Copyright (C) 2021  Civic Hacker, LLC
#
# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation, either
# version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/>.


from typing import Tuple, List, NewType, TypeVar, Type
from typing import Union, Set
from dataclasses import dataclass, field
from cybernetickit import CoreModel
import math
import cmath
from decimal import Decimal
import operator


Location = TypeVar('Location', Tuple[int, int], complex)


class TopologicalError(Exception):
    def __init__(self, message):
        self.message = message


@dataclass(frozen=True)
class LineSegment:
    end: Location
    start: Location

    def __iter__(self):
        return iter([self.end, self.start])

    def __matmul__(self, other):
        return (self.start - other.start)*(self.end - other.end)

    def __abs__(self):
        return abs(self.end - self.start)


@dataclass(frozen=True)
class Vector(LineSegment):
    end: Location
    start: Location = complex(0, 0)

    def __matmul__(self, other):
        return (self.start - other.start)*(self.end - other.end)

    @property
    def real(self):
        return self.end.real

    @property
    def imag(self):
        return self.end.imag


class Bloom(type):
    remember: int # Band
    understand: int
    apply: int
    analyze: int
    evaluate: int
    create: int

    def __init_subclass__(cls, /, strategy, **kwargs):
        pass


@dataclass
class LearningExperience(metaclass=Bloom):
    ___points: Set[complex] = field(default_factory=set)
    software: Type[Vector] = Vector(end=complex(.5, 1))
    policy: Type[Vector] = Vector(end=complex(-.5, 1))
    data: Type[Vector] = Vector(end=complex(1, 0))

    @property
    def points(self) -> Set[complex]:
        return self.___points

    @points.setter
    def points(self, new_point: complex):
        if new_point in self:
            self.___points.add(new_point)
        else:
            raise TopologicalError("New point must be in interior")

    @property
    def area(self):
        p = self.perimeter/2
        return math.sqrt(p*(p-abs(self.software))*(p-abs(self.policy))*(p-abs(self.data)))

    @property
    def perimeter(self) -> Union[float, Decimal]:
        return abs(self.software) + abs(self.data) + abs(self.policy)

    def dot(self, vector1=None, vector2=None):
        return math.acos((vector1.real*vector2.real + vector1.imag*vector2.imag)/(abs(vector1)*abs(vector2)))

    def __len__(self):
        return len(self.points)

    def __contains__(self, other: complex):

        if any(map(lambda c: c == other,[complex(0,0), self.software.end, self.data.end])):
            # exclude vertices
            return False


        dx = other.real-self.software.end.real;
        dy = other.imag-self.software.end.imag;
        dx21 = self.software.end.real-self.data.end.real;
        dy12 = self.data.end.imag-self.software.end.imag;

        D = dy12*(self.data.start.real-self.software.real) + dx21*(self.data.start.imag-self.software.end.imag);
        s = dy12*dx + dx21*dy;
        t = (self.software.end.imag-self.data.start.imag)*dx + (self.data.start.real-self.software.end.real)*dy;
        if (D<0):
            return s<=0 and t<=0 and s+t>=D
        return s>=0 and t>=0 and s+t<=D
