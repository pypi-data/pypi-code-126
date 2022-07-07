'''_2074.py

ElectricMachineGroup
'''


from typing import List

from mastapy.electric_machines.load_cases_and_analyses import _1272
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_GROUP = python_net_import('SMT.MastaAPI.SystemModel', 'ElectricMachineGroup')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineGroup',)


class ElectricMachineGroup(_0.APIBase):
    '''ElectricMachineGroup

    This is a mastapy class.
    '''

    TYPE = _ELECTRIC_MACHINE_GROUP

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ElectricMachineGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def electric_machine_load_case_groups(self) -> 'List[_1272.ElectricMachineLoadCaseGroup]':
        '''List[ElectricMachineLoadCaseGroup]: 'ElectricMachineLoadCaseGroups' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ElectricMachineLoadCaseGroups, constructor.new(_1272.ElectricMachineLoadCaseGroup))
        return value
