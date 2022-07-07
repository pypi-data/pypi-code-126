'''_7183.py

MeasurementComponentAdvancedSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model import _2324
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6755
from mastapy.system_model.analyses_and_results.system_deflections import _2635
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7230
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'MeasurementComponentAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('MeasurementComponentAdvancedSystemDeflection',)


class MeasurementComponentAdvancedSystemDeflection(_7230.VirtualComponentAdvancedSystemDeflection):
    '''MeasurementComponentAdvancedSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _MEASUREMENT_COMPONENT_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MeasurementComponentAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2324.MeasurementComponent':
        '''MeasurementComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2324.MeasurementComponent)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6755.MeasurementComponentLoadCase':
        '''MeasurementComponentLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6755.MeasurementComponentLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def component_system_deflection_results(self) -> 'List[_2635.MeasurementComponentSystemDeflection]':
        '''List[MeasurementComponentSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentSystemDeflectionResults, constructor.new(_2635.MeasurementComponentSystemDeflection))
        return value
