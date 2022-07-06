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
class binary_diffusivity(Group):
    """
    'binary_diffusivity' child.
    """

    fluent_name = "binary-diffusivity"

    child_names = \
        ['option', 'constant', 'boussinesq', 'coefficients',
         'number_of_coefficients', 'piecewise_polynomial',
         'nasa_9_piecewise_polynomial', 'piecewise_linear', 'anisotropic',
         'orthotropic', 'var_class']

    option: option = option
    """
    option child of binary_diffusivity.
    """
    constant: constant = constant
    """
    constant child of binary_diffusivity.
    """
    boussinesq: boussinesq = boussinesq
    """
    boussinesq child of binary_diffusivity.
    """
    coefficients: coefficients = coefficients
    """
    coefficients child of binary_diffusivity.
    """
    number_of_coefficients: number_of_coefficients = number_of_coefficients
    """
    number_of_coefficients child of binary_diffusivity.
    """
    piecewise_polynomial: piecewise_polynomial = piecewise_polynomial
    """
    piecewise_polynomial child of binary_diffusivity.
    """
    nasa_9_piecewise_polynomial: nasa_9_piecewise_polynomial = nasa_9_piecewise_polynomial
    """
    nasa_9_piecewise_polynomial child of binary_diffusivity.
    """
    piecewise_linear: piecewise_linear = piecewise_linear
    """
    piecewise_linear child of binary_diffusivity.
    """
    anisotropic: anisotropic = anisotropic
    """
    anisotropic child of binary_diffusivity.
    """
    orthotropic: orthotropic = orthotropic
    """
    orthotropic child of binary_diffusivity.
    """
    var_class: var_class = var_class
    """
    var_class child of binary_diffusivity.
    """
