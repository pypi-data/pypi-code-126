'''_1196.py

CADRotor
'''


from mastapy.electric_machines import _1245
from mastapy._internal.python_net import python_net_import

_CAD_ROTOR = python_net_import('SMT.MastaAPI.ElectricMachines', 'CADRotor')


__docformat__ = 'restructuredtext en'
__all__ = ('CADRotor',)


class CADRotor(_1245.Rotor):
    '''CADRotor

    This is a mastapy class.
    '''

    TYPE = _CAD_ROTOR

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CADRotor.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
