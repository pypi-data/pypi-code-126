#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from .method import method
from .number_of_coeff import number_of_coeff
from .function_of import function_of
from .coefficients import coefficients
from .constant import constant
from .piecewise_polynomial import piecewise_polynomial
from .piecewise_linear import piecewise_linear
class hc(Group):
    """
    'hc' child.
    """

    fluent_name = "hc"

    child_names = \
        ['method', 'number_of_coeff', 'function_of', 'coefficients',
         'constant', 'piecewise_polynomial', 'piecewise_linear']

    method: method = method
    """
    method child of hc.
    """
    number_of_coeff: number_of_coeff = number_of_coeff
    """
    number_of_coeff child of hc.
    """
    function_of: function_of = function_of
    """
    function_of child of hc.
    """
    coefficients: coefficients = coefficients
    """
    coefficients child of hc.
    """
    constant: constant = constant
    """
    constant child of hc.
    """
    piecewise_polynomial: piecewise_polynomial = piecewise_polynomial
    """
    piecewise_polynomial child of hc.
    """
    piecewise_linear: piecewise_linear = piecewise_linear
    """
    piecewise_linear child of hc.
    """
