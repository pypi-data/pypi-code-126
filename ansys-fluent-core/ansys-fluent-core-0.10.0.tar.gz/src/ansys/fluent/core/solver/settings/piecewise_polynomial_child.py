#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from .minimum import minimum
from .maximum import maximum
from .number_of_coeff import number_of_coeff
from .coefficients import coefficients
class piecewise_polynomial_child(Group):
    """
    'child_object_type' of piecewise_polynomial.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['minimum', 'maximum', 'number_of_coeff', 'coefficients']

    minimum: minimum = minimum
    """
    minimum child of piecewise_polynomial_child.
    """
    maximum: maximum = maximum
    """
    maximum child of piecewise_polynomial_child.
    """
    number_of_coeff: number_of_coeff = number_of_coeff
    """
    number_of_coeff child of piecewise_polynomial_child.
    """
    coefficients: coefficients = coefficients
    """
    coefficients child of piecewise_polynomial_child.
    """
