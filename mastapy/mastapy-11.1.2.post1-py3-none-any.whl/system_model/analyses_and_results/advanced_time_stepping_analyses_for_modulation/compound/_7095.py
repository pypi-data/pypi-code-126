'''_7095.py

WormGearCompoundAdvancedTimeSteppingAnalysisForModulation
'''


from typing import List

from mastapy.system_model.part_model.gears import _2411
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6966
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7030
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound', 'WormGearCompoundAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearCompoundAdvancedTimeSteppingAnalysisForModulation',)


class WormGearCompoundAdvancedTimeSteppingAnalysisForModulation(_7030.GearCompoundAdvancedTimeSteppingAnalysisForModulation):
    '''WormGearCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    '''

    TYPE = _WORM_GEAR_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2411.WormGear':
        '''WormGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2411.WormGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_6966.WormGearAdvancedTimeSteppingAnalysisForModulation]':
        '''List[WormGearAdvancedTimeSteppingAnalysisForModulation]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_6966.WormGearAdvancedTimeSteppingAnalysisForModulation))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_6966.WormGearAdvancedTimeSteppingAnalysisForModulation]':
        '''List[WormGearAdvancedTimeSteppingAnalysisForModulation]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_6966.WormGearAdvancedTimeSteppingAnalysisForModulation))
        return value
