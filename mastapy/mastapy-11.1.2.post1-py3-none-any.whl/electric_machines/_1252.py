'''_1252.py

SurfacePermanentMagnetMachine
'''


from mastapy.electric_machines import _1236
from mastapy._internal.python_net import python_net_import

_SURFACE_PERMANENT_MAGNET_MACHINE = python_net_import('SMT.MastaAPI.ElectricMachines', 'SurfacePermanentMagnetMachine')


__docformat__ = 'restructuredtext en'
__all__ = ('SurfacePermanentMagnetMachine',)


class SurfacePermanentMagnetMachine(_1236.NonCADElectricMachineDetail):
    '''SurfacePermanentMagnetMachine

    This is a mastapy class.
    '''

    TYPE = _SURFACE_PERMANENT_MAGNET_MACHINE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SurfacePermanentMagnetMachine.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
