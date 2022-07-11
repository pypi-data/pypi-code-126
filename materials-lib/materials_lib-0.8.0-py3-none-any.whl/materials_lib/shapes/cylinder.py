import logging
from math import pi

from units import ureg


class Cylinder:
    def __init__(self, diameter = None, height = None, axis: str = None):
        if diameter is None:
            self._diameter = 0.0 * ureg.m
        else:
            self._diameter = diameter
            
        if height is None:
            self._height = 0.0 * ureg.m
        else:
            self._height = height

        if axis is None:
            self._axis = 'z'
        else:
            self._axis = axis

    def height(self):
        return self._height

    def diameter(self):
        return self._diameter

    def x(self):
        if self._axis is 'x':
            return self.height()
        else:
            return self.diameter()

    def y(self):
        if self._axis is 'y':
            return self.height()
        else:
            return self.diameter()

    def z(self):
        if self._axis is 'z':
            return self.height()
        else:
            return self.diameter()

    def radius(self):
        return self._diameter/2.0

    def volume(self):
        return self._height * self.cross_section_area(self._axis)

    def cross_section_area(self, axis: str):
        if axis != self._axis:
            return 0.0 * ureg.m**2
        else:
            return pi * (self._diameter**2/4.0)

    def inertia(self, axis: str):
        if axis != self._axis:
            return 0.0 * ureg.m**4
        else:
            return pi * self._diameter**4/64.0

    # Log the current value in the cli
    def log(self, name: str = None):
        if name is None:
            logging.info(f"Cylinder: Diameter: {self._diameter}, Height: {self._height}, Axis: {self._axis}")
        else:
            logging.info(f"{name}: Diameter: {self._diameter}, Height: {self._height}, Axis: {self._axis}")
