'''_6921.py

OilSealAdvancedTimeSteppingAnalysisForModulation
'''


from mastapy.system_model.part_model import _2327
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6759
from mastapy.system_model.analyses_and_results.system_deflections import _2639
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6878
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'OilSealAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('OilSealAdvancedTimeSteppingAnalysisForModulation',)


class OilSealAdvancedTimeSteppingAnalysisForModulation(_6878.ConnectorAdvancedTimeSteppingAnalysisForModulation):
    '''OilSealAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    '''

    TYPE = _OIL_SEAL_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'OilSealAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2327.OilSeal':
        '''OilSeal: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2327.OilSeal)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6759.OilSealLoadCase':
        '''OilSealLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6759.OilSealLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def system_deflection_results(self) -> '_2639.OilSealSystemDeflection':
        '''OilSealSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2639.OilSealSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None
