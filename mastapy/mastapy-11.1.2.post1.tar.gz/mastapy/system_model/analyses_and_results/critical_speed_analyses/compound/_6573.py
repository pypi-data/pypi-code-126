'''_6573.py

HypoidGearSetCompoundCriticalSpeedAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2395
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6571, _6572, _6515
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6444
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'HypoidGearSetCompoundCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSetCompoundCriticalSpeedAnalysis',)


class HypoidGearSetCompoundCriticalSpeedAnalysis(_6515.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis):
    '''HypoidGearSetCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    '''

    TYPE = _HYPOID_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearSetCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2395.HypoidGearSet':
        '''HypoidGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2395.HypoidGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def assembly_design(self) -> '_2395.HypoidGearSet':
        '''HypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2395.HypoidGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def hypoid_gears_compound_critical_speed_analysis(self) -> 'List[_6571.HypoidGearCompoundCriticalSpeedAnalysis]':
        '''List[HypoidGearCompoundCriticalSpeedAnalysis]: 'HypoidGearsCompoundCriticalSpeedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearsCompoundCriticalSpeedAnalysis, constructor.new(_6571.HypoidGearCompoundCriticalSpeedAnalysis))
        return value

    @property
    def hypoid_meshes_compound_critical_speed_analysis(self) -> 'List[_6572.HypoidGearMeshCompoundCriticalSpeedAnalysis]':
        '''List[HypoidGearMeshCompoundCriticalSpeedAnalysis]: 'HypoidMeshesCompoundCriticalSpeedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidMeshesCompoundCriticalSpeedAnalysis, constructor.new(_6572.HypoidGearMeshCompoundCriticalSpeedAnalysis))
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_6444.HypoidGearSetCriticalSpeedAnalysis]':
        '''List[HypoidGearSetCriticalSpeedAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_6444.HypoidGearSetCriticalSpeedAnalysis))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_6444.HypoidGearSetCriticalSpeedAnalysis]':
        '''List[HypoidGearSetCriticalSpeedAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_6444.HypoidGearSetCriticalSpeedAnalysis))
        return value
