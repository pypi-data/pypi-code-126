'''_6051.py

MeasurementComponentCompoundHarmonicAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _2324
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5883
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _6097
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'MeasurementComponentCompoundHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('MeasurementComponentCompoundHarmonicAnalysis',)


class MeasurementComponentCompoundHarmonicAnalysis(_6097.VirtualComponentCompoundHarmonicAnalysis):
    '''MeasurementComponentCompoundHarmonicAnalysis

    This is a mastapy class.
    '''

    TYPE = _MEASUREMENT_COMPONENT_COMPOUND_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MeasurementComponentCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2324.MeasurementComponent':
        '''MeasurementComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2324.MeasurementComponent)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_5883.MeasurementComponentHarmonicAnalysis]':
        '''List[MeasurementComponentHarmonicAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_5883.MeasurementComponentHarmonicAnalysis))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5883.MeasurementComponentHarmonicAnalysis]':
        '''List[MeasurementComponentHarmonicAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_5883.MeasurementComponentHarmonicAnalysis))
        return value
