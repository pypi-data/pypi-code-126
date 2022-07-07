'''_1197.py

CADStator
'''


from mastapy.electric_machines import _1192
from mastapy._internal.python_net import python_net_import

_CAD_STATOR = python_net_import('SMT.MastaAPI.ElectricMachines', 'CADStator')


__docformat__ = 'restructuredtext en'
__all__ = ('CADStator',)


class CADStator(_1192.AbstractStator):
    '''CADStator

    This is a mastapy class.
    '''

    TYPE = _CAD_STATOR

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CADStator.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
