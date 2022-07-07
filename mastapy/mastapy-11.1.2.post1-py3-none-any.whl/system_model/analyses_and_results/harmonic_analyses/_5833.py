'''_5833.py

CylindricalGearSetHarmonicAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2386, _2402
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6699, _6766
from mastapy.system_model.analyses_and_results.system_deflections import _2597, _2598, _2599
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5831, _5832, _5860
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'CylindricalGearSetHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetHarmonicAnalysis',)


class CylindricalGearSetHarmonicAnalysis(_5860.GearSetHarmonicAnalysis):
    '''CylindricalGearSetHarmonicAnalysis

    This is a mastapy class.
    '''

    TYPE = _CYLINDRICAL_GEAR_SET_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearSetHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2386.CylindricalGearSet':
        '''CylindricalGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2386.CylindricalGearSet.TYPE not in self.wrapped.AssemblyDesign.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to CylindricalGearSet. Expected: {}.'.format(self.wrapped.AssemblyDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.AssemblyDesign.__class__)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6699.CylindricalGearSetLoadCase':
        '''CylindricalGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _6699.CylindricalGearSetLoadCase.TYPE not in self.wrapped.AssemblyLoadCase.__class__.__mro__:
            raise CastException('Failed to cast assembly_load_case to CylindricalGearSetLoadCase. Expected: {}.'.format(self.wrapped.AssemblyLoadCase.__class__.__qualname__))

        return constructor.new_override(self.wrapped.AssemblyLoadCase.__class__)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def system_deflection_results(self) -> '_2597.CylindricalGearSetSystemDeflection':
        '''CylindricalGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2597.CylindricalGearSetSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to CylindricalGearSetSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_cylindrical_gear_set_system_deflection_timestep(self) -> '_2598.CylindricalGearSetSystemDeflectionTimestep':
        '''CylindricalGearSetSystemDeflectionTimestep: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2598.CylindricalGearSetSystemDeflectionTimestep.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to CylindricalGearSetSystemDeflectionTimestep. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_cylindrical_gear_set_system_deflection_with_ltca_results(self) -> '_2599.CylindricalGearSetSystemDeflectionWithLTCAResults':
        '''CylindricalGearSetSystemDeflectionWithLTCAResults: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2599.CylindricalGearSetSystemDeflectionWithLTCAResults.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to CylindricalGearSetSystemDeflectionWithLTCAResults. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def gears_harmonic_analysis(self) -> 'List[_5831.CylindricalGearHarmonicAnalysis]':
        '''List[CylindricalGearHarmonicAnalysis]: 'GearsHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.GearsHarmonicAnalysis, constructor.new(_5831.CylindricalGearHarmonicAnalysis))
        return value

    @property
    def cylindrical_gears_harmonic_analysis(self) -> 'List[_5831.CylindricalGearHarmonicAnalysis]':
        '''List[CylindricalGearHarmonicAnalysis]: 'CylindricalGearsHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearsHarmonicAnalysis, constructor.new(_5831.CylindricalGearHarmonicAnalysis))
        return value

    @property
    def meshes_harmonic_analysis(self) -> 'List[_5832.CylindricalGearMeshHarmonicAnalysis]':
        '''List[CylindricalGearMeshHarmonicAnalysis]: 'MeshesHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeshesHarmonicAnalysis, constructor.new(_5832.CylindricalGearMeshHarmonicAnalysis))
        return value

    @property
    def cylindrical_meshes_harmonic_analysis(self) -> 'List[_5832.CylindricalGearMeshHarmonicAnalysis]':
        '''List[CylindricalGearMeshHarmonicAnalysis]: 'CylindricalMeshesHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalMeshesHarmonicAnalysis, constructor.new(_5832.CylindricalGearMeshHarmonicAnalysis))
        return value
