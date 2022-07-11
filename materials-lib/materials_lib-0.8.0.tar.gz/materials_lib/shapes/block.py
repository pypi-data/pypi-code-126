import logging
import numpy as np

from units import ureg


class Block:
    def __init__(self, vector = None):
        self._expected_input_size = 3
        if vector is None:
            self._dims = np.zeros(self._expected_input_size) * ureg.newton
        else:
            if np.size(vector) == self._expected_input_size:
                self._dims = vector
            else:
                logging.error(f"Incorrect input vector size (input size {np.size(vector)}, required size {self._expected_input_size})")

    def x(self):
        return self._dims[0]

    def y(self):
        return self._dims[1]

    def z(self):
        return self._dims[2]

    def volume(self):
        return self._dims[0] * self._dims[1] * self._dims[2]

    def cross_section_area(self, axis: str):
        if axis is 'x':
            return self.y() * self.z()
        elif axis is 'y':
            return self.x() * self.z()
        elif axis is 'z':
            return self.x() * self.y()

    def inertia(self, axis: str):
        if axis is 'x':
            return (self.x() * self.y()**3)/12.0
        elif axis is 'y':
            return (self.y() * self.x()**3)/12.0
        elif axis is 'z':
            return 0.0 * ureg.m**4

    # Log the current value in the cli
    def log(self, name: str = None):
        if name is None:
            logging.info(f"Block dimensions: {self._dims}")
        else:
            logging.info(f"{name} dimensions: {self._dims}")
