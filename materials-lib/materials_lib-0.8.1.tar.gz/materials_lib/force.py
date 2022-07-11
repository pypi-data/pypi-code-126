from .units import ureg, pint

import numpy as np
import logging


class Force:
    def __init__(self, vector = None):
        self._expected_input_size = 3
        self._default_unit = ureg.newton

        if vector is None:
            self._value = np.zeros(self._expected_input_size) * self._default_unit
        else:
            if np.size(vector) == self._expected_input_size:
                # Verify that the input units are correct
                if not hasattr(vector, 'units'):
                    self._value = vector * self._default_unit
                else:
                    try:
                        _ = ureg.convert(1, vector.units, self._default_unit)
                        self._value = vector
                    except pint.DimensionalityError:
                        logging.error(f"Incorrect input vector unit: {vector.units}. Required unit must be equivalent to {self._default_unit}")
            else:
                logging.error(f"Incorrect input vector size (input size {np.size(vector)}, required size {self._expected_input_size})")

    def x(self):
        return self._value[0]

    def y(self):
        return self._value[1]

    def z(self):
        return self._value[2]

    # Return L2 norm of force vector
    def norm(self):
        return np.linalg.norm(self._value.magnitude) * self._value.units

    # Return numpy vector of value
    def vector(self, with_units: bool = True):
        if with_units:
            return self._value
        else:
            return self._value.to_base_units().magnitude

    # Return applied units
    def units(self):
        return self._value.units

    # Log the current value in the cli
    def log(self, name: str = None):
        if name is None:
            name = "Force"
            
        logging.info(f"{name}: {self._value.to(self._default_unit)}")

    # Ability to print(Force)
    def __repr__(self) -> str:
        return f"{self._value.to(self._default_unit)}"

    # Math operands
    def __add__(self, other):
        return Force(self._value + other._value)

    def __sub__(self, other):
        return Force(self._value - other._value)

    def __lt__(self, other):
        if self.norm() < other.norm():
            return True
        else:
            return False

    def __le__(self, other):
        if self.norm() <= other.norm():
            return True
        else:
            return False

    def __gt__(self, other):
        if self.norm() > other.norm():
            return True
        else:
            return False

    def __ge__(self, other):
        if self.norm() >= other.norm():
            return True
        else:
            return False

    def __eq__(self, other):
        if self._value == other._value:
            return True
        else:
            return False

    def __ne__(self, other):
        if not self._value == other._value:
            return True
        else:
            return False

    def __neg__(self):
        self._value = -self._value
