'''_7362.py

WormGearSetCompoundAdvancedSystemDeflection
'''


from typing import List

from mastapy.gears.rating.worm import _346
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2412
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7360, _7361, _7297
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7233
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound', 'WormGearSetCompoundAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetCompoundAdvancedSystemDeflection',)


class WormGearSetCompoundAdvancedSystemDeflection(_7297.GearSetCompoundAdvancedSystemDeflection):
    '''WormGearSetCompoundAdvancedSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _WORM_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearSetCompoundAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_duty_cycle_rating(self) -> '_346.WormGearSetDutyCycleRating':
        '''WormGearSetDutyCycleRating: 'GearDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_346.WormGearSetDutyCycleRating)(self.wrapped.GearDutyCycleRating) if self.wrapped.GearDutyCycleRating is not None else None

    @property
    def worm_gear_duty_cycle_rating(self) -> '_346.WormGearSetDutyCycleRating':
        '''WormGearSetDutyCycleRating: 'WormGearDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_346.WormGearSetDutyCycleRating)(self.wrapped.WormGearDutyCycleRating) if self.wrapped.WormGearDutyCycleRating is not None else None

    @property
    def component_design(self) -> '_2412.WormGearSet':
        '''WormGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2412.WormGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def assembly_design(self) -> '_2412.WormGearSet':
        '''WormGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2412.WormGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def worm_gears_compound_advanced_system_deflection(self) -> 'List[_7360.WormGearCompoundAdvancedSystemDeflection]':
        '''List[WormGearCompoundAdvancedSystemDeflection]: 'WormGearsCompoundAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearsCompoundAdvancedSystemDeflection, constructor.new(_7360.WormGearCompoundAdvancedSystemDeflection))
        return value

    @property
    def worm_meshes_compound_advanced_system_deflection(self) -> 'List[_7361.WormGearMeshCompoundAdvancedSystemDeflection]':
        '''List[WormGearMeshCompoundAdvancedSystemDeflection]: 'WormMeshesCompoundAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormMeshesCompoundAdvancedSystemDeflection, constructor.new(_7361.WormGearMeshCompoundAdvancedSystemDeflection))
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_7233.WormGearSetAdvancedSystemDeflection]':
        '''List[WormGearSetAdvancedSystemDeflection]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_7233.WormGearSetAdvancedSystemDeflection))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_7233.WormGearSetAdvancedSystemDeflection]':
        '''List[WormGearSetAdvancedSystemDeflection]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_7233.WormGearSetAdvancedSystemDeflection))
        return value
