#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from .width import width
from .height import height
class field(Command):
    """
    Set the field of view (width and height).
    
    Parameters
    ----------
        width : real
            'width' child.
        height : real
            'height' child.
    
    """

    fluent_name = "field"

    argument_names = \
        ['width', 'height']

    width: width = width
    """
    width argument of field.
    """
    height: height = height
    """
    height argument of field.
    """
