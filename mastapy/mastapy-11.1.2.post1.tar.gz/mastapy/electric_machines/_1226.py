'''_1226.py

InteriorPermanentMagnetMachine
'''


from mastapy.electric_machines import _1236
from mastapy._internal.python_net import python_net_import

_INTERIOR_PERMANENT_MAGNET_MACHINE = python_net_import('SMT.MastaAPI.ElectricMachines', 'InteriorPermanentMagnetMachine')


__docformat__ = 'restructuredtext en'
__all__ = ('InteriorPermanentMagnetMachine',)


class InteriorPermanentMagnetMachine(_1236.NonCADElectricMachineDetail):
    '''InteriorPermanentMagnetMachine

    This is a mastapy class.
    '''

    TYPE = _INTERIOR_PERMANENT_MAGNET_MACHINE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'InteriorPermanentMagnetMachine.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
