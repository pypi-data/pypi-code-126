'''_4513.py

RingPinsModalAnalysisAtAStiffness
'''


from mastapy.system_model.part_model.cycloidal import _2430
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6776
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4501
from mastapy._internal.python_net import python_net_import

_RING_PINS_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'RingPinsModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('RingPinsModalAnalysisAtAStiffness',)


class RingPinsModalAnalysisAtAStiffness(_4501.MountableComponentModalAnalysisAtAStiffness):
    '''RingPinsModalAnalysisAtAStiffness

    This is a mastapy class.
    '''

    TYPE = _RING_PINS_MODAL_ANALYSIS_AT_A_STIFFNESS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RingPinsModalAnalysisAtAStiffness.TYPE'):
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
    def component_load_case(self) -> '_6776.RingPinsLoadCase':
        '''RingPinsLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6776.RingPinsLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None
