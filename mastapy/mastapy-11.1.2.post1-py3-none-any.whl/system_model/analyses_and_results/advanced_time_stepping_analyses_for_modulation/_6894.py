'''_6894.py

ExternalCADModelAdvancedTimeSteppingAnalysisForModulation
'''


from mastapy.system_model.part_model import _2313
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6716
from mastapy.system_model.analyses_and_results.system_deflections import _2607
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6867
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'ExternalCADModelAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('ExternalCADModelAdvancedTimeSteppingAnalysisForModulation',)


class ExternalCADModelAdvancedTimeSteppingAnalysisForModulation(_6867.ComponentAdvancedTimeSteppingAnalysisForModulation):
    '''ExternalCADModelAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    '''

    TYPE = _EXTERNAL_CAD_MODEL_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ExternalCADModelAdvancedTimeSteppingAnalysisForModulation.TYPE'):
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
    def system_deflection_results(self) -> '_2607.ExternalCADModelSystemDeflection':
        '''ExternalCADModelSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2607.ExternalCADModelSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None
