'''_6536.py

ConceptCouplingConnectionCompoundCriticalSpeedAnalysis
'''


from typing import List

from mastapy.system_model.connections_and_sockets.couplings import _2206
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6404
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6547
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'ConceptCouplingConnectionCompoundCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingConnectionCompoundCriticalSpeedAnalysis',)


class ConceptCouplingConnectionCompoundCriticalSpeedAnalysis(_6547.CouplingConnectionCompoundCriticalSpeedAnalysis):
    '''ConceptCouplingConnectionCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_COUPLING_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptCouplingConnectionCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2206.ConceptCouplingConnection':
        '''ConceptCouplingConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2206.ConceptCouplingConnection)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def connection_design(self) -> '_2206.ConceptCouplingConnection':
        '''ConceptCouplingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2206.ConceptCouplingConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_6404.ConceptCouplingConnectionCriticalSpeedAnalysis]':
        '''List[ConceptCouplingConnectionCriticalSpeedAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCasesReady, constructor.new(_6404.ConceptCouplingConnectionCriticalSpeedAnalysis))
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_6404.ConceptCouplingConnectionCriticalSpeedAnalysis]':
        '''List[ConceptCouplingConnectionCriticalSpeedAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCases, constructor.new(_6404.ConceptCouplingConnectionCriticalSpeedAnalysis))
        return value
