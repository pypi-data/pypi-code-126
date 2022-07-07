'''_3929.py

CycloidalDiscCentralBearingConnectionPowerFlow
'''


from mastapy.system_model.connections_and_sockets.cycloidal import _2197
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _3909
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'CycloidalDiscCentralBearingConnectionPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscCentralBearingConnectionPowerFlow',)


class CycloidalDiscCentralBearingConnectionPowerFlow(_3909.CoaxialConnectionPowerFlow):
    '''CycloidalDiscCentralBearingConnectionPowerFlow

    This is a mastapy class.
    '''

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CycloidalDiscCentralBearingConnectionPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2197.CycloidalDiscCentralBearingConnection':
        '''CycloidalDiscCentralBearingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2197.CycloidalDiscCentralBearingConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None
