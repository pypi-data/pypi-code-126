#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from .mesh import mesh
from .surface import surface
from .volume import volume
from .force import force
from .lift import lift
from .drag import drag
from .moment import moment
from .flux import flux
from .injection import injection
from .user_defined import user_defined
from .aeromechanics import aeromechanics
from .expression import expression
from .custom import custom
from .compute_2 import compute
class report_definitions(Group, _ChildNamedObjectAccessorMixin):
    """
    'report_definitions' child.
    """

    fluent_name = "report-definitions"

    child_names = \
        ['mesh', 'surface', 'volume', 'force', 'lift', 'drag', 'moment',
         'flux', 'injection', 'user_defined', 'aeromechanics', 'expression',
         'custom']

    mesh: mesh = mesh
    """
    mesh child of report_definitions.
    """
    surface: surface = surface
    """
    surface child of report_definitions.
    """
    volume: volume = volume
    """
    volume child of report_definitions.
    """
    force: force = force
    """
    force child of report_definitions.
    """
    lift: lift = lift
    """
    lift child of report_definitions.
    """
    drag: drag = drag
    """
    drag child of report_definitions.
    """
    moment: moment = moment
    """
    moment child of report_definitions.
    """
    flux: flux = flux
    """
    flux child of report_definitions.
    """
    injection: injection = injection
    """
    injection child of report_definitions.
    """
    user_defined: user_defined = user_defined
    """
    user_defined child of report_definitions.
    """
    aeromechanics: aeromechanics = aeromechanics
    """
    aeromechanics child of report_definitions.
    """
    expression: expression = expression
    """
    expression child of report_definitions.
    """
    custom: custom = custom
    """
    custom child of report_definitions.
    """
    command_names = \
        ['compute']

    compute: compute = compute
    """
    compute command of report_definitions.
    """
