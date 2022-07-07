'''_5994.py

BoltCompoundHarmonicAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _2304
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5803
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _6000
from mastapy._internal.python_net import python_net_import

_BOLT_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'BoltCompoundHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltCompoundHarmonicAnalysis',)


class BoltCompoundHarmonicAnalysis(_6000.ComponentCompoundHarmonicAnalysis):
    '''BoltCompoundHarmonicAnalysis

    This is a mastapy class.
    '''

    TYPE = _BOLT_COMPOUND_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BoltCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2304.Bolt':
        '''Bolt: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2304.Bolt)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_5803.BoltHarmonicAnalysis]':
        '''List[BoltHarmonicAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_5803.BoltHarmonicAnalysis))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5803.BoltHarmonicAnalysis]':
        '''List[BoltHarmonicAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_5803.BoltHarmonicAnalysis))
        return value
