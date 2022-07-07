'''_7195.py

PulleyAdvancedSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2450, _2447
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6773, _6690
from mastapy.system_model.analyses_and_results.system_deflections import _2648
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7144
from mastapy._internal.python_net import python_net_import

_PULLEY_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'PulleyAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('PulleyAdvancedSystemDeflection',)


class PulleyAdvancedSystemDeflection(_7144.CouplingHalfAdvancedSystemDeflection):
    '''PulleyAdvancedSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _PULLEY_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PulleyAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2450.Pulley':
        '''Pulley: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2450.Pulley.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Pulley. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6773.PulleyLoadCase':
        '''PulleyLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _6773.PulleyLoadCase.TYPE not in self.wrapped.ComponentLoadCase.__class__.__mro__:
            raise CastException('Failed to cast component_load_case to PulleyLoadCase. Expected: {}.'.format(self.wrapped.ComponentLoadCase.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentLoadCase.__class__)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def component_system_deflection_results(self) -> 'List[_2648.PulleySystemDeflection]':
        '''List[PulleySystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentSystemDeflectionResults, constructor.new(_2648.PulleySystemDeflection))
        return value
