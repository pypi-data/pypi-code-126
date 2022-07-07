'''_4990.py

CylindricalGearSetModalAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2386, _2402
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6699, _6766
from mastapy.system_model.analyses_and_results.system_deflections import _2597, _2598, _2599
from mastapy.system_model.analyses_and_results.modal_analyses import _4989, _4988, _5002
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'CylindricalGearSetModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetModalAnalysis',)


class CylindricalGearSetModalAnalysis(_5002.GearSetModalAnalysis):
    '''CylindricalGearSetModalAnalysis

    This is a mastapy class.
    '''

    TYPE = _CYLINDRICAL_GEAR_SET_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearSetModalAnalysis.TYPE'):
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
    def cylindrical_gears_modal_analysis(self) -> 'List[_4989.CylindricalGearModalAnalysis]':
        '''List[CylindricalGearModalAnalysis]: 'CylindricalGearsModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearsModalAnalysis, constructor.new(_4989.CylindricalGearModalAnalysis))
        return value

    @property
    def cylindrical_meshes_modal_analysis(self) -> 'List[_4988.CylindricalGearMeshModalAnalysis]':
        '''List[CylindricalGearMeshModalAnalysis]: 'CylindricalMeshesModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalMeshesModalAnalysis, constructor.new(_4988.CylindricalGearMeshModalAnalysis))
        return value
