'''_5403.py

ConceptGearCompoundMultibodyDynamicsAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2381
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5255
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5432
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'ConceptGearCompoundMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearCompoundMultibodyDynamicsAnalysis',)


class ConceptGearCompoundMultibodyDynamicsAnalysis(_5432.GearCompoundMultibodyDynamicsAnalysis):
    '''ConceptGearCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptGearCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2381.ConceptGear':
        '''ConceptGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2381.ConceptGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_5255.ConceptGearMultibodyDynamicsAnalysis]':
        '''List[ConceptGearMultibodyDynamicsAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_5255.ConceptGearMultibodyDynamicsAnalysis))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5255.ConceptGearMultibodyDynamicsAnalysis]':
        '''List[ConceptGearMultibodyDynamicsAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_5255.ConceptGearMultibodyDynamicsAnalysis))
        return value
