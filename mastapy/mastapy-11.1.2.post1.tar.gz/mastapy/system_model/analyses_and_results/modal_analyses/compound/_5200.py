'''_5200.py

StraightBevelDiffGearSetCompoundModalAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2406
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _5198, _5199, _5111
from mastapy.system_model.analyses_and_results.modal_analyses import _5054
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'StraightBevelDiffGearSetCompoundModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearSetCompoundModalAnalysis',)


class StraightBevelDiffGearSetCompoundModalAnalysis(_5111.BevelGearSetCompoundModalAnalysis):
    '''StraightBevelDiffGearSetCompoundModalAnalysis

    This is a mastapy class.
    '''

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearSetCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2406.StraightBevelDiffGearSet':
        '''StraightBevelDiffGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2406.StraightBevelDiffGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def assembly_design(self) -> '_2406.StraightBevelDiffGearSet':
        '''StraightBevelDiffGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2406.StraightBevelDiffGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def straight_bevel_diff_gears_compound_modal_analysis(self) -> 'List[_5198.StraightBevelDiffGearCompoundModalAnalysis]':
        '''List[StraightBevelDiffGearCompoundModalAnalysis]: 'StraightBevelDiffGearsCompoundModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearsCompoundModalAnalysis, constructor.new(_5198.StraightBevelDiffGearCompoundModalAnalysis))
        return value

    @property
    def straight_bevel_diff_meshes_compound_modal_analysis(self) -> 'List[_5199.StraightBevelDiffGearMeshCompoundModalAnalysis]':
        '''List[StraightBevelDiffGearMeshCompoundModalAnalysis]: 'StraightBevelDiffMeshesCompoundModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffMeshesCompoundModalAnalysis, constructor.new(_5199.StraightBevelDiffGearMeshCompoundModalAnalysis))
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_5054.StraightBevelDiffGearSetModalAnalysis]':
        '''List[StraightBevelDiffGearSetModalAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_5054.StraightBevelDiffGearSetModalAnalysis))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_5054.StraightBevelDiffGearSetModalAnalysis]':
        '''List[StraightBevelDiffGearSetModalAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_5054.StraightBevelDiffGearSetModalAnalysis))
        return value
