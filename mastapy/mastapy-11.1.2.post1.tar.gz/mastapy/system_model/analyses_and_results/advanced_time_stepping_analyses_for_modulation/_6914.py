'''_6914.py

KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation
'''


from typing import List

from mastapy.system_model.part_model.gears import _2399
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6750
from mastapy.system_model.analyses_and_results.system_deflections import _2627
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6912, _6913, _6911
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation',)


class KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation(_6911.KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation):
    '''KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    '''

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2399.KlingelnbergCycloPalloidHypoidGearSet':
        '''KlingelnbergCycloPalloidHypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2399.KlingelnbergCycloPalloidHypoidGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6750.KlingelnbergCycloPalloidHypoidGearSetLoadCase':
        '''KlingelnbergCycloPalloidHypoidGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6750.KlingelnbergCycloPalloidHypoidGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def system_deflection_results(self) -> '_2627.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection':
        '''KlingelnbergCycloPalloidHypoidGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2627.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_advanced_time_stepping_analysis_for_modulation(self) -> 'List[_6912.KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation]':
        '''List[KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation]: 'KlingelnbergCycloPalloidHypoidGearsAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearsAdvancedTimeSteppingAnalysisForModulation, constructor.new(_6912.KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_advanced_time_stepping_analysis_for_modulation(self) -> 'List[_6913.KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation]':
        '''List[KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation]: 'KlingelnbergCycloPalloidHypoidMeshesAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidMeshesAdvancedTimeSteppingAnalysisForModulation, constructor.new(_6913.KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation))
        return value
