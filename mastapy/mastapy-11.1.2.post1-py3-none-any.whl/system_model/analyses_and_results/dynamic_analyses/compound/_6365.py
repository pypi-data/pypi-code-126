'''_6365.py

VirtualComponentCompoundDynamicAnalysis
'''


from typing import List

from mastapy.system_model.analyses_and_results.dynamic_analyses import _6236
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6320
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'VirtualComponentCompoundDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('VirtualComponentCompoundDynamicAnalysis',)


class VirtualComponentCompoundDynamicAnalysis(_6320.MountableComponentCompoundDynamicAnalysis):
    '''VirtualComponentCompoundDynamicAnalysis

    This is a mastapy class.
    '''

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'VirtualComponentCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_6236.VirtualComponentDynamicAnalysis]':
        '''List[VirtualComponentDynamicAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_6236.VirtualComponentDynamicAnalysis))
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_6236.VirtualComponentDynamicAnalysis]':
        '''List[VirtualComponentDynamicAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_6236.VirtualComponentDynamicAnalysis))
        return value
