'''_5644.py

TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation
'''


from mastapy.system_model.part_model.couplings import _2470
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6808
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5561
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation',)


class TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation(_5561.CouplingHalfHarmonicAnalysisOfSingleExcitation):
    '''TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    '''

    TYPE = _TORQUE_CONVERTER_TURBINE_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation.TYPE'):
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
    def component_load_case(self) -> '_6808.TorqueConverterTurbineLoadCase':
        '''TorqueConverterTurbineLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6808.TorqueConverterTurbineLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None
