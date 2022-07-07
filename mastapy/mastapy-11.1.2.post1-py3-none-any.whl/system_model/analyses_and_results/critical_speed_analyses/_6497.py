'''_6497.py

TorqueConverterConnectionCriticalSpeedAnalysis
'''


from mastapy.system_model.connections_and_sockets.couplings import _2214
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6805
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6415
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'TorqueConverterConnectionCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterConnectionCriticalSpeedAnalysis',)


class TorqueConverterConnectionCriticalSpeedAnalysis(_6415.CouplingConnectionCriticalSpeedAnalysis):
    '''TorqueConverterConnectionCriticalSpeedAnalysis

    This is a mastapy class.
    '''

    TYPE = _TORQUE_CONVERTER_CONNECTION_CRITICAL_SPEED_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueConverterConnectionCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2214.TorqueConverterConnection':
        '''TorqueConverterConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2214.TorqueConverterConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_load_case(self) -> '_6805.TorqueConverterConnectionLoadCase':
        '''TorqueConverterConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6805.TorqueConverterConnectionLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase is not None else None
