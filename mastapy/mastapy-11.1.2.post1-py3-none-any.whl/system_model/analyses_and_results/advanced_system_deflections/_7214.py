'''_7214.py

StraightBevelDiffGearSetAdvancedSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model.gears import _2406
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6794
from mastapy.gears.rating.straight_bevel_diff import _368
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7212, _7213, _7122
from mastapy.system_model.analyses_and_results.system_deflections import _2669
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'StraightBevelDiffGearSetAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearSetAdvancedSystemDeflection',)


class StraightBevelDiffGearSetAdvancedSystemDeflection(_7122.BevelGearSetAdvancedSystemDeflection):
    '''StraightBevelDiffGearSetAdvancedSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearSetAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2406.StraightBevelDiffGearSet':
        '''StraightBevelDiffGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2406.StraightBevelDiffGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6794.StraightBevelDiffGearSetLoadCase':
        '''StraightBevelDiffGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6794.StraightBevelDiffGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def rating(self) -> '_368.StraightBevelDiffGearSetRating':
        '''StraightBevelDiffGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_368.StraightBevelDiffGearSetRating)(self.wrapped.Rating) if self.wrapped.Rating is not None else None

    @property
    def component_detailed_analysis(self) -> '_368.StraightBevelDiffGearSetRating':
        '''StraightBevelDiffGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_368.StraightBevelDiffGearSetRating)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis is not None else None

    @property
    def straight_bevel_diff_gears_advanced_system_deflection(self) -> 'List[_7212.StraightBevelDiffGearAdvancedSystemDeflection]':
        '''List[StraightBevelDiffGearAdvancedSystemDeflection]: 'StraightBevelDiffGearsAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearsAdvancedSystemDeflection, constructor.new(_7212.StraightBevelDiffGearAdvancedSystemDeflection))
        return value

    @property
    def straight_bevel_diff_meshes_advanced_system_deflection(self) -> 'List[_7213.StraightBevelDiffGearMeshAdvancedSystemDeflection]':
        '''List[StraightBevelDiffGearMeshAdvancedSystemDeflection]: 'StraightBevelDiffMeshesAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffMeshesAdvancedSystemDeflection, constructor.new(_7213.StraightBevelDiffGearMeshAdvancedSystemDeflection))
        return value

    @property
    def assembly_system_deflection_results(self) -> 'List[_2669.StraightBevelDiffGearSetSystemDeflection]':
        '''List[StraightBevelDiffGearSetSystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblySystemDeflectionResults, constructor.new(_2669.StraightBevelDiffGearSetSystemDeflection))
        return value
