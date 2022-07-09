"""
Hexagon provides classes for dealing with hexagonal grids.

Vec is an integer hexagonal vector, VecF is a floating one, and Grid is
a hexagonal grid indexed by Vecs.
"""
from __future__ import annotations

import itertools
from collections.abc import Iterator
from enum import Enum
from random import randint
from typing import Generic, NoReturn, TypeVar, overload
from math import sqrt

SQRT3 = sqrt(3)

__version__ = "0.0.2"


def positions(radius: int) -> Iterator[Vec[int]]:
    for x, y in itertools.product(range(-radius, radius + 1), repeat=2):
        pos = Vec(x, y)
        if abs(pos) <= radius:
            yield pos


def random(radius: int) -> Vec[int]:
    """Get a random Vec with at most a given radius."""
    while True:
        pos = Vec(randint(-radius, radius), randint(-radius, radius))
        if abs(pos) <= radius:
            return pos


N = TypeVar("N", float, int, covariant=True)


class Vec(Generic[N]):
    """A hexagonal vector."""

    __slots__ = ("x", "y")
    x: N
    y: N

    def __init__(self, x: N, y: N = 0, z: N | None = None) -> None:
        object.__setattr__(self, "x", x)
        object.__setattr__(self, "y", y)
        if z is not None and x + y + z != 0:
            raise ValueError

    @property
    def z(self) -> N:
        return -self.x - self.y

    def __setattr__(self, *_) -> NoReturn:
        raise TypeError(f"{self.__class__.__qualname__} is immutable")

    def __eq__(self, other: object, /) -> bool:
        return isinstance(other, Vec) and self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __add__(self, other: Vec[N], /) -> Vec[N]:
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vec[N]) -> Vec[N]:
        return Vec(self.x - other.x, self.y - other.y)

    def __neg__(self) -> Vec[N]:
        return Vec(-self.x, -self.y)

    @overload
    def __mul__(self: Vec[int], scalar: int) -> Vec[int]:
        ...

    @overload
    def __mul__(self: Vec[float], scalar: float) -> Vec[float]:
        ...

    def __mul__(self, scalar):
        return Vec(self.x * scalar, self.y * scalar)

    __rmul__ = __mul__

    def __truediv__(self, scalar: float) -> Vec[float]:
        return Vec(self.x / scalar, self.y / scalar)

    def __str__(self) -> str:
        return f"({self.x} {self.y} {self.z})"

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}({self.x}, {self.y}, {self.z})"

    def __bool__(self) -> bool:
        return self.x != 0 or self.y != 0

    def __abs__(self) -> N:
        return max(abs(a) for a in self.to_tuple())

    def cartesian(self, size: float = 1) -> tuple[float, float]:
        return (size * SQRT3 * (self.x - self.z) / 2, size * 1.5 * self.y)

    def to_tuple(self) -> tuple[N, N, N]:
        return (self.x, self.y, self.z)

    def rotate(self, angle: int, /) -> Vec[N]:
        """Return a copy rotated by angle sixths of a turn."""
        angle %= 6
        if angle == 1:
            return Vec(-self.y, -self.z)
        if angle == 2:
            return Vec(self.z, self.x)
        if angle == 3:
            return Vec(-self.x, -self.y)
        if angle == 4:
            return Vec(self.y, self.z)
        if angle == 5:
            return Vec(-self.z, -self.x)
        return self


class Direction(Enum):
    EA = Vec(1, 0, -1)
    NE = Vec(0, 1, -1)
    NW = Vec(-1, 1, 0)
    WE = Vec(-1, 0, 1)
    SW = Vec(0, -1, 1)
    SE = Vec(1, -1, 0)
