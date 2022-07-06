#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from .option import option
from .constant import constant
from .boussinesq import boussinesq
from .coefficients import coefficients
from .number_of_coefficients import number_of_coefficients
from .piecewise_polynomial import piecewise_polynomial
from .nasa_9_piecewise_polynomial import nasa_9_piecewise_polynomial
from .piecewise_linear import piecewise_linear
from .anisotropic import anisotropic
from .orthotropic import orthotropic
from .var_class import var_class
class struct_damping_alpha(Group):
    """
    'struct_damping_alpha' child.
    """

    fluent_name = "struct-damping-alpha"

    child_names = \
        ['option', 'constant', 'boussinesq', 'coefficients',
         'number_of_coefficients', 'piecewise_polynomial',
         'nasa_9_piecewise_polynomial', 'piecewise_linear', 'anisotropic',
         'orthotropic', 'var_class']

    option: option = option
    """
    option child of struct_damping_alpha.
    """
    constant: constant = constant
    """
    constant child of struct_damping_alpha.
    """
    boussinesq: boussinesq = boussinesq
    """
    boussinesq child of struct_damping_alpha.
    """
    coefficients: coefficients = coefficients
    """
    coefficients child of struct_damping_alpha.
    """
    number_of_coefficients: number_of_coefficients = number_of_coefficients
    """
    number_of_coefficients child of struct_damping_alpha.
    """
    piecewise_polynomial: piecewise_polynomial = piecewise_polynomial
    """
    piecewise_polynomial child of struct_damping_alpha.
    """
    nasa_9_piecewise_polynomial: nasa_9_piecewise_polynomial = nasa_9_piecewise_polynomial
    """
    nasa_9_piecewise_polynomial child of struct_damping_alpha.
    """
    piecewise_linear: piecewise_linear = piecewise_linear
    """
    piecewise_linear child of struct_damping_alpha.
    """
    anisotropic: anisotropic = anisotropic
    """
    anisotropic child of struct_damping_alpha.
    """
    orthotropic: orthotropic = orthotropic
    """
    orthotropic child of struct_damping_alpha.
    """
    var_class: var_class = var_class
    """
    var_class child of struct_damping_alpha.
    """
