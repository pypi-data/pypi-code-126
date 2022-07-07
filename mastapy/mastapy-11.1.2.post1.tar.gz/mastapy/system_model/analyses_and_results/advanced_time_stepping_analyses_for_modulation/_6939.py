'''_6939.py

ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2458
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6782
from mastapy.system_model.analyses_and_results.system_deflections import _2656
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6878
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation',)


class ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation(_6878.ConnectorAdvancedTimeSteppingAnalysisForModulation):
    '''ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    '''

    TYPE = _SHAFT_HUB_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2458.ShaftHubConnection':
        '''ShaftHubConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2458.ShaftHubConnection)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6782.ShaftHubConnectionLoadCase':
        '''ShaftHubConnectionLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6782.ShaftHubConnectionLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def system_deflection_results(self) -> '_2656.ShaftHubConnectionSystemDeflection':
        '''ShaftHubConnectionSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2656.ShaftHubConnectionSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def planetaries(self) -> 'List[ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation]':
        '''List[ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation))
        return value
