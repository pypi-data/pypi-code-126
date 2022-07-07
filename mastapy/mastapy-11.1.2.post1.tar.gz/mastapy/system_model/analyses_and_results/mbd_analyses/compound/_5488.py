'''_5488.py

SynchroniserHalfCompoundMultibodyDynamicsAnalysis
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2464
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5349
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5489
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'SynchroniserHalfCompoundMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserHalfCompoundMultibodyDynamicsAnalysis',)


class SynchroniserHalfCompoundMultibodyDynamicsAnalysis(_5489.SynchroniserPartCompoundMultibodyDynamicsAnalysis):
    '''SynchroniserHalfCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _SYNCHRONISER_HALF_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SynchroniserHalfCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2464.SynchroniserHalf':
        '''SynchroniserHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2464.SynchroniserHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_5349.SynchroniserHalfMultibodyDynamicsAnalysis]':
        '''List[SynchroniserHalfMultibodyDynamicsAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_5349.SynchroniserHalfMultibodyDynamicsAnalysis))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5349.SynchroniserHalfMultibodyDynamicsAnalysis]':
        '''List[SynchroniserHalfMultibodyDynamicsAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_5349.SynchroniserHalfMultibodyDynamicsAnalysis))
        return value
