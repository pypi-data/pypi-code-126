'''_2949.py

StraightBevelGearSteadyStateSynchronousResponseOnAShaft
'''


from mastapy.system_model.part_model.gears import _2407
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6795
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _2856
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft', 'StraightBevelGearSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearSteadyStateSynchronousResponseOnAShaft',)


class StraightBevelGearSteadyStateSynchronousResponseOnAShaft(_2856.BevelGearSteadyStateSynchronousResponseOnAShaft):
    '''StraightBevelGearSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    '''

    TYPE = _STRAIGHT_BEVEL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelGearSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2407.StraightBevelGear':
        '''StraightBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2407.StraightBevelGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6795.StraightBevelGearLoadCase':
        '''StraightBevelGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6795.StraightBevelGearLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None
