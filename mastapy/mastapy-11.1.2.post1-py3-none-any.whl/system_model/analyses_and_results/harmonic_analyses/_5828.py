'''_5828.py

CycloidalDiscCentralBearingConnectionHarmonicAnalysis
'''


from mastapy.system_model.connections_and_sockets.cycloidal import _2197
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2591
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5807
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'CycloidalDiscCentralBearingConnectionHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscCentralBearingConnectionHarmonicAnalysis',)


class CycloidalDiscCentralBearingConnectionHarmonicAnalysis(_5807.CoaxialConnectionHarmonicAnalysis):
    '''CycloidalDiscCentralBearingConnectionHarmonicAnalysis

    This is a mastapy class.
    '''

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CycloidalDiscCentralBearingConnectionHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2197.CycloidalDiscCentralBearingConnection':
        '''CycloidalDiscCentralBearingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2197.CycloidalDiscCentralBearingConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def system_deflection_results(self) -> '_2591.CycloidalDiscCentralBearingConnectionSystemDeflection':
        '''CycloidalDiscCentralBearingConnectionSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2591.CycloidalDiscCentralBearingConnectionSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None
