'''_1203.py

DynamicForceResults
'''


from typing import List

from mastapy.math_utility import _1413
from mastapy._internal import constructor, conversion
from mastapy.electric_machines.harmonic_load_data import _1283
from mastapy._internal.python_net import python_net_import

_DYNAMIC_FORCE_RESULTS = python_net_import('SMT.MastaAPI.ElectricMachines', 'DynamicForceResults')


__docformat__ = 'restructuredtext en'
__all__ = ('DynamicForceResults',)


class DynamicForceResults(_1283.ElectricMachineHarmonicLoadDataBase):
    '''DynamicForceResults

    This is a mastapy class.
    '''

    TYPE = _DYNAMIC_FORCE_RESULTS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'DynamicForceResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def excitations(self) -> 'List[_1413.FourierSeries]':
        '''List[FourierSeries]: 'Excitations' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Excitations, constructor.new(_1413.FourierSeries))
        return value
