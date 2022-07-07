'''_6944.py

SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation
'''


from typing import List

from mastapy.system_model.part_model.gears import _2404
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6788
from mastapy.system_model.analyses_and_results.system_deflections import _2663
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6942, _6943, _6860
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation',)


class SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation(_6860.BevelGearSetAdvancedTimeSteppingAnalysisForModulation):
    '''SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    '''

    TYPE = _SPIRAL_BEVEL_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2404.SpiralBevelGearSet':
        '''SpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2404.SpiralBevelGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6788.SpiralBevelGearSetLoadCase':
        '''SpiralBevelGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6788.SpiralBevelGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def system_deflection_results(self) -> '_2663.SpiralBevelGearSetSystemDeflection':
        '''SpiralBevelGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2663.SpiralBevelGearSetSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def spiral_bevel_gears_advanced_time_stepping_analysis_for_modulation(self) -> 'List[_6942.SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation]':
        '''List[SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation]: 'SpiralBevelGearsAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearsAdvancedTimeSteppingAnalysisForModulation, constructor.new(_6942.SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation))
        return value

    @property
    def spiral_bevel_meshes_advanced_time_stepping_analysis_for_modulation(self) -> 'List[_6943.SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation]':
        '''List[SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation]: 'SpiralBevelMeshesAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelMeshesAdvancedTimeSteppingAnalysisForModulation, constructor.new(_6943.SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation))
        return value
