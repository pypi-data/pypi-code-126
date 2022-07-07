'''_4388.py

RootAssemblyCompoundParametricStudyTool
'''


from typing import List

from mastapy.system_model.analyses_and_results.parametric_study_tools import _4241, _4240, _4259
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.load_case_groups import (
    _5504, _5503, _5505, _5508,
    _5509, _5512, _5516
)
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2758
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4301
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'RootAssemblyCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblyCompoundParametricStudyTool',)


class RootAssemblyCompoundParametricStudyTool(_4301.AssemblyCompoundParametricStudyTool):
    '''RootAssemblyCompoundParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _ROOT_ASSEMBLY_COMPOUND_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RootAssemblyCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def results_for_reporting(self) -> '_4241.ParametricStudyToolResultsForReporting':
        '''ParametricStudyToolResultsForReporting: 'ResultsForReporting' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_4241.ParametricStudyToolResultsForReporting)(self.wrapped.ResultsForReporting) if self.wrapped.ResultsForReporting is not None else None

    @property
    def parametric_analysis_options(self) -> '_4240.ParametricStudyToolOptions':
        '''ParametricStudyToolOptions: 'ParametricAnalysisOptions' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_4240.ParametricStudyToolOptions)(self.wrapped.ParametricAnalysisOptions) if self.wrapped.ParametricAnalysisOptions is not None else None

    @property
    def compound_load_case(self) -> '_5504.AbstractLoadCaseGroup':
        '''AbstractLoadCaseGroup: 'CompoundLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5504.AbstractLoadCaseGroup.TYPE not in self.wrapped.CompoundLoadCase.__class__.__mro__:
            raise CastException('Failed to cast compound_load_case to AbstractLoadCaseGroup. Expected: {}.'.format(self.wrapped.CompoundLoadCase.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CompoundLoadCase.__class__)(self.wrapped.CompoundLoadCase) if self.wrapped.CompoundLoadCase is not None else None

    @property
    def compound_load_case_of_type_abstract_design_state_load_case_group(self) -> '_5503.AbstractDesignStateLoadCaseGroup':
        '''AbstractDesignStateLoadCaseGroup: 'CompoundLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5503.AbstractDesignStateLoadCaseGroup.TYPE not in self.wrapped.CompoundLoadCase.__class__.__mro__:
            raise CastException('Failed to cast compound_load_case to AbstractDesignStateLoadCaseGroup. Expected: {}.'.format(self.wrapped.CompoundLoadCase.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CompoundLoadCase.__class__)(self.wrapped.CompoundLoadCase) if self.wrapped.CompoundLoadCase is not None else None

    @property
    def compound_load_case_of_type_abstract_static_load_case_group(self) -> '_5505.AbstractStaticLoadCaseGroup':
        '''AbstractStaticLoadCaseGroup: 'CompoundLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5505.AbstractStaticLoadCaseGroup.TYPE not in self.wrapped.CompoundLoadCase.__class__.__mro__:
            raise CastException('Failed to cast compound_load_case to AbstractStaticLoadCaseGroup. Expected: {}.'.format(self.wrapped.CompoundLoadCase.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CompoundLoadCase.__class__)(self.wrapped.CompoundLoadCase) if self.wrapped.CompoundLoadCase is not None else None

    @property
    def compound_load_case_of_type_design_state(self) -> '_5508.DesignState':
        '''DesignState: 'CompoundLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5508.DesignState.TYPE not in self.wrapped.CompoundLoadCase.__class__.__mro__:
            raise CastException('Failed to cast compound_load_case to DesignState. Expected: {}.'.format(self.wrapped.CompoundLoadCase.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CompoundLoadCase.__class__)(self.wrapped.CompoundLoadCase) if self.wrapped.CompoundLoadCase is not None else None

    @property
    def compound_load_case_of_type_duty_cycle(self) -> '_5509.DutyCycle':
        '''DutyCycle: 'CompoundLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5509.DutyCycle.TYPE not in self.wrapped.CompoundLoadCase.__class__.__mro__:
            raise CastException('Failed to cast compound_load_case to DutyCycle. Expected: {}.'.format(self.wrapped.CompoundLoadCase.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CompoundLoadCase.__class__)(self.wrapped.CompoundLoadCase) if self.wrapped.CompoundLoadCase is not None else None

    @property
    def compound_load_case_of_type_sub_group_in_single_design_state(self) -> '_5512.SubGroupInSingleDesignState':
        '''SubGroupInSingleDesignState: 'CompoundLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5512.SubGroupInSingleDesignState.TYPE not in self.wrapped.CompoundLoadCase.__class__.__mro__:
            raise CastException('Failed to cast compound_load_case to SubGroupInSingleDesignState. Expected: {}.'.format(self.wrapped.CompoundLoadCase.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CompoundLoadCase.__class__)(self.wrapped.CompoundLoadCase) if self.wrapped.CompoundLoadCase is not None else None

    @property
    def compound_load_case_of_type_time_series_load_case_group(self) -> '_5516.TimeSeriesLoadCaseGroup':
        '''TimeSeriesLoadCaseGroup: 'CompoundLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5516.TimeSeriesLoadCaseGroup.TYPE not in self.wrapped.CompoundLoadCase.__class__.__mro__:
            raise CastException('Failed to cast compound_load_case to TimeSeriesLoadCaseGroup. Expected: {}.'.format(self.wrapped.CompoundLoadCase.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CompoundLoadCase.__class__)(self.wrapped.CompoundLoadCase) if self.wrapped.CompoundLoadCase is not None else None

    @property
    def root_assembly_duty_cycle_results(self) -> '_2758.DutyCycleEfficiencyResults':
        '''DutyCycleEfficiencyResults: 'RootAssemblyDutyCycleResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2758.DutyCycleEfficiencyResults)(self.wrapped.RootAssemblyDutyCycleResults) if self.wrapped.RootAssemblyDutyCycleResults is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4259.RootAssemblyParametricStudyTool]':
        '''List[RootAssemblyParametricStudyTool]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_4259.RootAssemblyParametricStudyTool))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4259.RootAssemblyParametricStudyTool]':
        '''List[RootAssemblyParametricStudyTool]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_4259.RootAssemblyParametricStudyTool))
        return value
