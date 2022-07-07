'''_1266.py

EfficiencyMapAnalysis
'''


from mastapy.electric_machines.load_cases_and_analyses import _1267, _1268
from mastapy._internal import constructor
from mastapy._internal.python_net import python_net_import

_EFFICIENCY_MAP_ANALYSIS = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'EfficiencyMapAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('EfficiencyMapAnalysis',)


class EfficiencyMapAnalysis(_1268.ElectricMachineAnalysis):
    '''EfficiencyMapAnalysis

    This is a mastapy class.
    '''

    TYPE = _EFFICIENCY_MAP_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'EfficiencyMapAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def load_case(self) -> '_1267.EfficiencyMapLoadCase':
        '''EfficiencyMapLoadCase: 'LoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1267.EfficiencyMapLoadCase)(self.wrapped.LoadCase) if self.wrapped.LoadCase is not None else None
