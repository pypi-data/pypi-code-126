'''_4596.py

CycloidalAssemblyCompoundModalAnalysisAtAStiffness
'''


from typing import List

from mastapy.system_model.part_model.cycloidal import _2428
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4466
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4651
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound', 'CycloidalAssemblyCompoundModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalAssemblyCompoundModalAnalysisAtAStiffness',)


class CycloidalAssemblyCompoundModalAnalysisAtAStiffness(_4651.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness):
    '''CycloidalAssemblyCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    '''

    TYPE = _CYCLOIDAL_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CycloidalAssemblyCompoundModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2428.CycloidalAssembly':
        '''CycloidalAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2428.CycloidalAssembly)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def assembly_design(self) -> '_2428.CycloidalAssembly':
        '''CycloidalAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2428.CycloidalAssembly)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4466.CycloidalAssemblyModalAnalysisAtAStiffness]':
        '''List[CycloidalAssemblyModalAnalysisAtAStiffness]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_4466.CycloidalAssemblyModalAnalysisAtAStiffness))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4466.CycloidalAssemblyModalAnalysisAtAStiffness]':
        '''List[CycloidalAssemblyModalAnalysisAtAStiffness]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_4466.CycloidalAssemblyModalAnalysisAtAStiffness))
        return value
