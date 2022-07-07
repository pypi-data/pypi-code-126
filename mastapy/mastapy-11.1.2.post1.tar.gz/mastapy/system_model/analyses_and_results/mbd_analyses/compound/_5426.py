'''_5426.py

ExternalCADModelCompoundMultibodyDynamicsAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _2313
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5277
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5399
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'ExternalCADModelCompoundMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ExternalCADModelCompoundMultibodyDynamicsAnalysis',)


class ExternalCADModelCompoundMultibodyDynamicsAnalysis(_5399.ComponentCompoundMultibodyDynamicsAnalysis):
    '''ExternalCADModelCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _EXTERNAL_CAD_MODEL_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ExternalCADModelCompoundMultibodyDynamicsAnalysis.TYPE'):
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
    def component_analysis_cases_ready(self) -> 'List[_5277.ExternalCADModelMultibodyDynamicsAnalysis]':
        '''List[ExternalCADModelMultibodyDynamicsAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_5277.ExternalCADModelMultibodyDynamicsAnalysis))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5277.ExternalCADModelMultibodyDynamicsAnalysis]':
        '''List[ExternalCADModelMultibodyDynamicsAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_5277.ExternalCADModelMultibodyDynamicsAnalysis))
        return value
