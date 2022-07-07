'''_1236.py

NonCADElectricMachineDetail
'''


from mastapy.electric_machines import _1206
from mastapy._internal.python_net import python_net_import

_NON_CAD_ELECTRIC_MACHINE_DETAIL = python_net_import('SMT.MastaAPI.ElectricMachines', 'NonCADElectricMachineDetail')


__docformat__ = 'restructuredtext en'
__all__ = ('NonCADElectricMachineDetail',)


class NonCADElectricMachineDetail(_1206.ElectricMachineDetail):
    '''NonCADElectricMachineDetail

    This is a mastapy class.
    '''

    TYPE = _NON_CAD_ELECTRIC_MACHINE_DETAIL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'NonCADElectricMachineDetail.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
