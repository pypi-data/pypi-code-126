'''_3141.py

CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed
'''


from mastapy.system_model.connections_and_sockets.cycloidal import _2197
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3121
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed', 'CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed',)


class CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed(_3121.CoaxialConnectionSteadyStateSynchronousResponseAtASpeed):
    '''CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    '''

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2197.CycloidalDiscCentralBearingConnection':
        '''CycloidalDiscCentralBearingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2197.CycloidalDiscCentralBearingConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None
