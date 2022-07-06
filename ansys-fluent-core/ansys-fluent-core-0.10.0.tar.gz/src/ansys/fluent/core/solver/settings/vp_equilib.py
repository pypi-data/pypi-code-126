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
class vp_equilib(Group):
    """
    'vp_equilib' child.
    """

    fluent_name = "vp-equilib"

    child_names = \
        ['option', 'constant', 'boussinesq', 'coefficients',
         'number_of_coefficients', 'piecewise_polynomial',
         'nasa_9_piecewise_polynomial', 'piecewise_linear', 'anisotropic',
         'orthotropic', 'var_class']

    option: option = option
    """
    option child of vp_equilib.
    """
    constant: constant = constant
    """
    constant child of vp_equilib.
    """
    boussinesq: boussinesq = boussinesq
    """
    boussinesq child of vp_equilib.
    """
    coefficients: coefficients = coefficients
    """
    coefficients child of vp_equilib.
    """
    number_of_coefficients: number_of_coefficients = number_of_coefficients
    """
    number_of_coefficients child of vp_equilib.
    """
    piecewise_polynomial: piecewise_polynomial = piecewise_polynomial
    """
    piecewise_polynomial child of vp_equilib.
    """
    nasa_9_piecewise_polynomial: nasa_9_piecewise_polynomial = nasa_9_piecewise_polynomial
    """
    nasa_9_piecewise_polynomial child of vp_equilib.
    """
    piecewise_linear: piecewise_linear = piecewise_linear
    """
    piecewise_linear child of vp_equilib.
    """
    anisotropic: anisotropic = anisotropic
    """
    anisotropic child of vp_equilib.
    """
    orthotropic: orthotropic = orthotropic
    """
    orthotropic child of vp_equilib.
    """
    var_class: var_class = var_class
    """
    var_class child of vp_equilib.
    """
