'''_3644.py

ConceptCouplingConnectionStabilityAnalysis
'''


from mastapy.system_model.connections_and_sockets.couplings import _2206
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6672
from mastapy.system_model.analyses_and_results.stability_analyses import _3655
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'ConceptCouplingConnectionStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingConnectionStabilityAnalysis',)


class ConceptCouplingConnectionStabilityAnalysis(_3655.CouplingConnectionStabilityAnalysis):
    '''ConceptCouplingConnectionStabilityAnalysis

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_COUPLING_CONNECTION_STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptCouplingConnectionStabilityAnalysis.TYPE'):
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
