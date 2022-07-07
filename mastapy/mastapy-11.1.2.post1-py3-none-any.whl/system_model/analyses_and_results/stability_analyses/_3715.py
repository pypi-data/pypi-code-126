'''_3715.py

ShaftStabilityAnalysis
'''


from typing import List

from mastapy.system_model.part_model.shaft_model import _2343
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6783
from mastapy.system_model.analyses_and_results.stability_analyses import _3658, _3620
from mastapy._internal.python_net import python_net_import

_SHAFT_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'ShaftStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftStabilityAnalysis',)


class ShaftStabilityAnalysis(_3620.AbstractShaftStabilityAnalysis):
    '''ShaftStabilityAnalysis

    This is a mastapy class.
    '''

    TYPE = _SHAFT_STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ShaftStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2343.Shaft':
        '''Shaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2343.Shaft)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6783.ShaftLoadCase':
        '''ShaftLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6783.ShaftLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def planetaries(self) -> 'List[ShaftStabilityAnalysis]':
        '''List[ShaftStabilityAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(ShaftStabilityAnalysis))
        return value

    @property
    def critical_speeds(self) -> 'List[_3658.CriticalSpeed]':
        '''List[CriticalSpeed]: 'CriticalSpeeds' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CriticalSpeeds, constructor.new(_3658.CriticalSpeed))
        return value
