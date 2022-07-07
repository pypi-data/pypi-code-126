'''_3438.py

PartToPartShearCouplingHalfSteadyStateSynchronousResponse
'''


from mastapy.system_model.part_model.couplings import _2449
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6763
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3394
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'PartToPartShearCouplingHalfSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCouplingHalfSteadyStateSynchronousResponse',)


class PartToPartShearCouplingHalfSteadyStateSynchronousResponse(_3394.CouplingHalfSteadyStateSynchronousResponse):
    '''PartToPartShearCouplingHalfSteadyStateSynchronousResponse

    This is a mastapy class.
    '''

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PartToPartShearCouplingHalfSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2449.PartToPartShearCouplingHalf':
        '''PartToPartShearCouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2449.PartToPartShearCouplingHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6763.PartToPartShearCouplingHalfLoadCase':
        '''PartToPartShearCouplingHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6763.PartToPartShearCouplingHalfLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None
