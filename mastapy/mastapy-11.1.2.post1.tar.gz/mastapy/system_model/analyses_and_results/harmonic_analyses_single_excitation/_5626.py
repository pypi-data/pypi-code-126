'''_5626.py

SpringDamperConnectionHarmonicAnalysisOfSingleExcitation
'''


from mastapy.system_model.connections_and_sockets.couplings import _2212
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6789
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5560
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'SpringDamperConnectionHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperConnectionHarmonicAnalysisOfSingleExcitation',)


class SpringDamperConnectionHarmonicAnalysisOfSingleExcitation(_5560.CouplingConnectionHarmonicAnalysisOfSingleExcitation):
    '''SpringDamperConnectionHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    '''

    TYPE = _SPRING_DAMPER_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpringDamperConnectionHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2212.SpringDamperConnection':
        '''SpringDamperConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2212.SpringDamperConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_load_case(self) -> '_6789.SpringDamperConnectionLoadCase':
        '''SpringDamperConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6789.SpringDamperConnectionLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase is not None else None
