'''_5773.py

TorqueConverterTurbineCompoundHarmonicAnalysisOfSingleExcitation
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2470
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5644
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _5692
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound', 'TorqueConverterTurbineCompoundHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterTurbineCompoundHarmonicAnalysisOfSingleExcitation',)


class TorqueConverterTurbineCompoundHarmonicAnalysisOfSingleExcitation(_5692.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation):
    '''TorqueConverterTurbineCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    '''

    TYPE = _TORQUE_CONVERTER_TURBINE_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueConverterTurbineCompoundHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2470.TorqueConverterTurbine':
        '''TorqueConverterTurbine: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2470.TorqueConverterTurbine)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_5644.TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation]':
        '''List[TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_5644.TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5644.TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation]':
        '''List[TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_5644.TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation))
        return value
