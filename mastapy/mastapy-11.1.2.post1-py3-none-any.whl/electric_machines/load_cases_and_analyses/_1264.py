'''_1264.py

DynamicForceAnalysis
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.electric_machines.load_cases_and_analyses import _1265, _1269, _1268
from mastapy.electric_machines import _1203
from mastapy._internal.python_net import python_net_import

_DYNAMIC_FORCE_ANALYSIS = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'DynamicForceAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('DynamicForceAnalysis',)


class DynamicForceAnalysis(_1268.ElectricMachineAnalysis):
    '''DynamicForceAnalysis

    This is a mastapy class.
    '''

    TYPE = _DYNAMIC_FORCE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'DynamicForceAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_steps_per_operating_point(self) -> 'int':
        '''int: 'NumberOfStepsPerOperatingPoint' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.NumberOfStepsPerOperatingPoint

    @property
    def load_case(self) -> '_1265.DynamicForceLoadCase':
        '''DynamicForceLoadCase: 'LoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1265.DynamicForceLoadCase)(self.wrapped.LoadCase) if self.wrapped.LoadCase is not None else None

    @property
    def results(self) -> '_1203.DynamicForceResults':
        '''DynamicForceResults: 'Results' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1203.DynamicForceResults)(self.wrapped.Results) if self.wrapped.Results is not None else None

    @property
    def single_operating_point_analyses(self) -> 'List[_1269.ElectricMachineFEAnalysis]':
        '''List[ElectricMachineFEAnalysis]: 'SingleOperatingPointAnalyses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SingleOperatingPointAnalyses, constructor.new(_1269.ElectricMachineFEAnalysis))
        return value
