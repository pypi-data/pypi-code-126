'''_3478.py

TorqueConverterPumpSteadyStateSynchronousResponse
'''


from mastapy.system_model.part_model.couplings import _2468
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6807
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3394
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'TorqueConverterPumpSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterPumpSteadyStateSynchronousResponse',)


class TorqueConverterPumpSteadyStateSynchronousResponse(_3394.CouplingHalfSteadyStateSynchronousResponse):
    '''TorqueConverterPumpSteadyStateSynchronousResponse

    This is a mastapy class.
    '''

    TYPE = _TORQUE_CONVERTER_PUMP_STEADY_STATE_SYNCHRONOUS_RESPONSE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueConverterPumpSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2468.TorqueConverterPump':
        '''TorqueConverterPump: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2468.TorqueConverterPump)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6807.TorqueConverterPumpLoadCase':
        '''TorqueConverterPumpLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6807.TorqueConverterPumpLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None
