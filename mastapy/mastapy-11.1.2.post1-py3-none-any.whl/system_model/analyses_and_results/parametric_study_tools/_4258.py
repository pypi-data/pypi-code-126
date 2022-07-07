'''_4258.py

RollingRingParametricStudyTool
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2456
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6780
from mastapy.system_model.analyses_and_results.system_deflections import _2654
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4185
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'RollingRingParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('RollingRingParametricStudyTool',)


class RollingRingParametricStudyTool(_4185.CouplingHalfParametricStudyTool):
    '''RollingRingParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _ROLLING_RING_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RollingRingParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2456.RollingRing':
        '''RollingRing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2456.RollingRing)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6780.RollingRingLoadCase':
        '''RollingRingLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6780.RollingRingLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def planetaries(self) -> 'List[RollingRingParametricStudyTool]':
        '''List[RollingRingParametricStudyTool]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(RollingRingParametricStudyTool))
        return value

    @property
    def component_system_deflection_results(self) -> 'List[_2654.RollingRingSystemDeflection]':
        '''List[RollingRingSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentSystemDeflectionResults, constructor.new(_2654.RollingRingSystemDeflection))
        return value
