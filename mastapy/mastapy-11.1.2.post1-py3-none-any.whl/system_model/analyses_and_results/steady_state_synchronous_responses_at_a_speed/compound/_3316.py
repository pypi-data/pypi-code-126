'''_3316.py

RingPinsCompoundSteadyStateSynchronousResponseAtASpeed
'''


from typing import List

from mastapy.system_model.part_model.cycloidal import _2430
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3186
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3304
from mastapy._internal.python_net import python_net_import

_RING_PINS_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound', 'RingPinsCompoundSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('RingPinsCompoundSteadyStateSynchronousResponseAtASpeed',)


class RingPinsCompoundSteadyStateSynchronousResponseAtASpeed(_3304.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed):
    '''RingPinsCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    '''

    TYPE = _RING_PINS_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RingPinsCompoundSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2430.RingPins':
        '''RingPins: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2430.RingPins)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_3186.RingPinsSteadyStateSynchronousResponseAtASpeed]':
        '''List[RingPinsSteadyStateSynchronousResponseAtASpeed]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_3186.RingPinsSteadyStateSynchronousResponseAtASpeed))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3186.RingPinsSteadyStateSynchronousResponseAtASpeed]':
        '''List[RingPinsSteadyStateSynchronousResponseAtASpeed]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_3186.RingPinsSteadyStateSynchronousResponseAtASpeed))
        return value
