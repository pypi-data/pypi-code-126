'''_7073.py

SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
'''


from typing import List

from mastapy.system_model.part_model.gears import _2404
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7071, _7072, _6990
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6944
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound', 'SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation',)


class SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation(_6990.BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation):
    '''SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    '''

    TYPE = _SPIRAL_BEVEL_GEAR_SET_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2404.SpiralBevelGearSet':
        '''SpiralBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2404.SpiralBevelGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def assembly_design(self) -> '_2404.SpiralBevelGearSet':
        '''SpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2404.SpiralBevelGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def spiral_bevel_gears_compound_advanced_time_stepping_analysis_for_modulation(self) -> 'List[_7071.SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation]':
        '''List[SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation]: 'SpiralBevelGearsCompoundAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearsCompoundAdvancedTimeSteppingAnalysisForModulation, constructor.new(_7071.SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation))
        return value

    @property
    def spiral_bevel_meshes_compound_advanced_time_stepping_analysis_for_modulation(self) -> 'List[_7072.SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation]':
        '''List[SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation]: 'SpiralBevelMeshesCompoundAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelMeshesCompoundAdvancedTimeSteppingAnalysisForModulation, constructor.new(_7072.SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation))
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_6944.SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation]':
        '''List[SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_6944.SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_6944.SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation]':
        '''List[SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_6944.SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation))
        return value
