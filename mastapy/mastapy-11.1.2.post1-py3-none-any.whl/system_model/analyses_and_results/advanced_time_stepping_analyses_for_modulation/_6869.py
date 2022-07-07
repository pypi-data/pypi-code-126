'''_6869.py

ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation
'''


from mastapy.system_model.connections_and_sockets.couplings import _2206
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6672
from mastapy.system_model.analyses_and_results.system_deflections import _2572
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6880
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation',)


class ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation(_6880.CouplingConnectionAdvancedTimeSteppingAnalysisForModulation):
    '''ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_COUPLING_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2206.ConceptCouplingConnection':
        '''ConceptCouplingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2206.ConceptCouplingConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_load_case(self) -> '_6672.ConceptCouplingConnectionLoadCase':
        '''ConceptCouplingConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6672.ConceptCouplingConnectionLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase is not None else None

    @property
    def system_deflection_results(self) -> '_2572.ConceptCouplingConnectionSystemDeflection':
        '''ConceptCouplingConnectionSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2572.ConceptCouplingConnectionSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None
