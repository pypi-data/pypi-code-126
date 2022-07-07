'''_7158.py

ExternalCADModelAdvancedSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model import _2313
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6716
from mastapy.system_model.analyses_and_results.system_deflections import _2607
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7129
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'ExternalCADModelAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ExternalCADModelAdvancedSystemDeflection',)


class ExternalCADModelAdvancedSystemDeflection(_7129.ComponentAdvancedSystemDeflection):
    '''ExternalCADModelAdvancedSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _EXTERNAL_CAD_MODEL_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ExternalCADModelAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2313.ExternalCADModel':
        '''ExternalCADModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2313.ExternalCADModel)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6716.ExternalCADModelLoadCase':
        '''ExternalCADModelLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6716.ExternalCADModelLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def component_system_deflection_results(self) -> 'List[_2607.ExternalCADModelSystemDeflection]':
        '''List[ExternalCADModelSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentSystemDeflectionResults, constructor.new(_2607.ExternalCADModelSystemDeflection))
        return value
