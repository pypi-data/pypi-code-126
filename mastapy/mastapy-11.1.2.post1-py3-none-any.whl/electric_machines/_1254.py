'''_1254.py

SynchronousReluctanceMachine
'''


from mastapy.electric_machines import _1236
from mastapy._internal.python_net import python_net_import

_SYNCHRONOUS_RELUCTANCE_MACHINE = python_net_import('SMT.MastaAPI.ElectricMachines', 'SynchronousReluctanceMachine')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchronousReluctanceMachine',)


class SynchronousReluctanceMachine(_1236.NonCADElectricMachineDetail):
    '''SynchronousReluctanceMachine

    This is a mastapy class.
    '''

    TYPE = _SYNCHRONOUS_RELUCTANCE_MACHINE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SynchronousReluctanceMachine.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
