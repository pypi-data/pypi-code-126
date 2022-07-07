'''_2613.py

FlexiblePinAssemblySystemDeflection
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _2315
from mastapy.system_model.analyses_and_results.static_loads import _6721
from mastapy.system_model.analyses_and_results.power_flows import _3943
from mastapy.system_model.analyses_and_results.system_deflections import (
    _2659, _2597, _2598, _2599,
    _2656, _2638, _2633, _2600,
    _2553, _2661
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'FlexiblePinAssemblySystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('FlexiblePinAssemblySystemDeflection',)


class FlexiblePinAssemblySystemDeflection(_2661.SpecialisedAssemblySystemDeflection):
    '''FlexiblePinAssemblySystemDeflection

    This is a mastapy class.
    '''

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FlexiblePinAssemblySystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pin_tangential_oscillation_amplitude(self) -> 'float':
        '''float: 'PinTangentialOscillationAmplitude' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PinTangentialOscillationAmplitude

    @property
    def pin_tangential_oscillation_frequency(self) -> 'float':
        '''float: 'PinTangentialOscillationFrequency' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PinTangentialOscillationFrequency

    @property
    def assembly_design(self) -> '_2315.FlexiblePinAssembly':
        '''FlexiblePinAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2315.FlexiblePinAssembly)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6721.FlexiblePinAssemblyLoadCase':
        '''FlexiblePinAssemblyLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6721.FlexiblePinAssemblyLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def power_flow_results(self) -> '_3943.FlexiblePinAssemblyPowerFlow':
        '''FlexiblePinAssemblyPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3943.FlexiblePinAssemblyPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults is not None else None

    @property
    def pin_analysis(self) -> '_2659.ShaftSystemDeflection':
        '''ShaftSystemDeflection: 'PinAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2659.ShaftSystemDeflection)(self.wrapped.PinAnalysis) if self.wrapped.PinAnalysis is not None else None

    @property
    def spindle_analyses(self) -> '_2659.ShaftSystemDeflection':
        '''ShaftSystemDeflection: 'SpindleAnalyses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2659.ShaftSystemDeflection)(self.wrapped.SpindleAnalyses) if self.wrapped.SpindleAnalyses is not None else None

    @property
    def separate_gear_set_details(self) -> '_2597.CylindricalGearSetSystemDeflection':
        '''CylindricalGearSetSystemDeflection: 'SeparateGearSetDetails' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2597.CylindricalGearSetSystemDeflection.TYPE not in self.wrapped.SeparateGearSetDetails.__class__.__mro__:
            raise CastException('Failed to cast separate_gear_set_details to CylindricalGearSetSystemDeflection. Expected: {}.'.format(self.wrapped.SeparateGearSetDetails.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SeparateGearSetDetails.__class__)(self.wrapped.SeparateGearSetDetails) if self.wrapped.SeparateGearSetDetails is not None else None

    @property
    def separate_gear_set_details_of_type_cylindrical_gear_set_system_deflection_timestep(self) -> '_2598.CylindricalGearSetSystemDeflectionTimestep':
        '''CylindricalGearSetSystemDeflectionTimestep: 'SeparateGearSetDetails' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2598.CylindricalGearSetSystemDeflectionTimestep.TYPE not in self.wrapped.SeparateGearSetDetails.__class__.__mro__:
            raise CastException('Failed to cast separate_gear_set_details to CylindricalGearSetSystemDeflectionTimestep. Expected: {}.'.format(self.wrapped.SeparateGearSetDetails.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SeparateGearSetDetails.__class__)(self.wrapped.SeparateGearSetDetails) if self.wrapped.SeparateGearSetDetails is not None else None

    @property
    def separate_gear_set_details_of_type_cylindrical_gear_set_system_deflection_with_ltca_results(self) -> '_2599.CylindricalGearSetSystemDeflectionWithLTCAResults':
        '''CylindricalGearSetSystemDeflectionWithLTCAResults: 'SeparateGearSetDetails' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2599.CylindricalGearSetSystemDeflectionWithLTCAResults.TYPE not in self.wrapped.SeparateGearSetDetails.__class__.__mro__:
            raise CastException('Failed to cast separate_gear_set_details to CylindricalGearSetSystemDeflectionWithLTCAResults. Expected: {}.'.format(self.wrapped.SeparateGearSetDetails.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SeparateGearSetDetails.__class__)(self.wrapped.SeparateGearSetDetails) if self.wrapped.SeparateGearSetDetails is not None else None

    @property
    def flexible_pin_shaft_details(self) -> '_2659.ShaftSystemDeflection':
        '''ShaftSystemDeflection: 'FlexiblePinShaftDetails' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2659.ShaftSystemDeflection)(self.wrapped.FlexiblePinShaftDetails) if self.wrapped.FlexiblePinShaftDetails is not None else None

    @property
    def pin_spindle_fit_analyses(self) -> 'List[_2656.ShaftHubConnectionSystemDeflection]':
        '''List[ShaftHubConnectionSystemDeflection]: 'PinSpindleFitAnalyses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PinSpindleFitAnalyses, constructor.new(_2656.ShaftHubConnectionSystemDeflection))
        return value

    @property
    def observed_pin_stiffness_reporters(self) -> 'List[_2638.ObservedPinStiffnessReporter]':
        '''List[ObservedPinStiffnessReporter]: 'ObservedPinStiffnessReporters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ObservedPinStiffnessReporters, constructor.new(_2638.ObservedPinStiffnessReporter))
        return value

    @property
    def load_sharing_factor_reporters(self) -> 'List[_2633.LoadSharingFactorReporter]':
        '''List[LoadSharingFactorReporter]: 'LoadSharingFactorReporters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadSharingFactorReporters, constructor.new(_2633.LoadSharingFactorReporter))
        return value

    @property
    def planet_gear_system_deflections(self) -> 'List[_2600.CylindricalGearSystemDeflection]':
        '''List[CylindricalGearSystemDeflection]: 'PlanetGearSystemDeflections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetGearSystemDeflections, constructor.new(_2600.CylindricalGearSystemDeflection))
        return value

    @property
    def flexible_pin_fit_details(self) -> 'List[_2656.ShaftHubConnectionSystemDeflection]':
        '''List[ShaftHubConnectionSystemDeflection]: 'FlexiblePinFitDetails' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinFitDetails, constructor.new(_2656.ShaftHubConnectionSystemDeflection))
        return value

    @property
    def bearing_static_analyses(self) -> 'List[_2553.BearingSystemDeflection]':
        '''List[BearingSystemDeflection]: 'BearingStaticAnalyses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BearingStaticAnalyses, constructor.new(_2553.BearingSystemDeflection))
        return value
