'''_6286.py

CycloidalAssemblyCompoundDynamicAnalysis
'''


from typing import List

from mastapy.system_model.part_model.cycloidal import _2428
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6156
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6341
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_ASSEMBLY_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'CycloidalAssemblyCompoundDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalAssemblyCompoundDynamicAnalysis',)


class CycloidalAssemblyCompoundDynamicAnalysis(_6341.SpecialisedAssemblyCompoundDynamicAnalysis):
    '''CycloidalAssemblyCompoundDynamicAnalysis

    This is a mastapy class.
    '''

    TYPE = _CYCLOIDAL_ASSEMBLY_COMPOUND_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CycloidalAssemblyCompoundDynamicAnalysis.TYPE'):
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
    def assembly_analysis_cases_ready(self) -> 'List[_6156.CycloidalAssemblyDynamicAnalysis]':
        '''List[CycloidalAssemblyDynamicAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_6156.CycloidalAssemblyDynamicAnalysis))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_6156.CycloidalAssemblyDynamicAnalysis]':
        '''List[CycloidalAssemblyDynamicAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_6156.CycloidalAssemblyDynamicAnalysis))
        return value
