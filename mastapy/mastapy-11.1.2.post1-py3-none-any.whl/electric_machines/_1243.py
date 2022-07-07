'''_1243.py

PermanentMagnetAssistedSynchronousReluctanceMachine
'''


from mastapy.electric_machines import _1236
from mastapy._internal.python_net import python_net_import

_PERMANENT_MAGNET_ASSISTED_SYNCHRONOUS_RELUCTANCE_MACHINE = python_net_import('SMT.MastaAPI.ElectricMachines', 'PermanentMagnetAssistedSynchronousReluctanceMachine')


__docformat__ = 'restructuredtext en'
__all__ = ('PermanentMagnetAssistedSynchronousReluctanceMachine',)


class PermanentMagnetAssistedSynchronousReluctanceMachine(_1236.NonCADElectricMachineDetail):
    '''PermanentMagnetAssistedSynchronousReluctanceMachine

    This is a mastapy class.
    '''

    TYPE = _PERMANENT_MAGNET_ASSISTED_SYNCHRONOUS_RELUCTANCE_MACHINE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PermanentMagnetAssistedSynchronousReluctanceMachine.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
