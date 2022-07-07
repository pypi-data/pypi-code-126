'''_4745.py

HypoidGearModalAnalysisAtASpeed
'''


from mastapy.system_model.part_model.gears import _2394
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6738
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _4687
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed', 'HypoidGearModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearModalAnalysisAtASpeed',)


class HypoidGearModalAnalysisAtASpeed(_4687.AGMAGleasonConicalGearModalAnalysisAtASpeed):
    '''HypoidGearModalAnalysisAtASpeed

    This is a mastapy class.
    '''

    TYPE = _HYPOID_GEAR_MODAL_ANALYSIS_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2394.HypoidGear':
        '''HypoidGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2394.HypoidGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6738.HypoidGearLoadCase':
        '''HypoidGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6738.HypoidGearLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None
