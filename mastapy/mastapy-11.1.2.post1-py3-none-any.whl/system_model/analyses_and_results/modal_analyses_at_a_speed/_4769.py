'''_4769.py

PowerLoadModalAnalysisAtASpeed
'''


from mastapy.system_model.part_model import _2333
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6772
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _4804
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed', 'PowerLoadModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('PowerLoadModalAnalysisAtASpeed',)


class PowerLoadModalAnalysisAtASpeed(_4804.VirtualComponentModalAnalysisAtASpeed):
    '''PowerLoadModalAnalysisAtASpeed

    This is a mastapy class.
    '''

    TYPE = _POWER_LOAD_MODAL_ANALYSIS_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PowerLoadModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2333.PowerLoad':
        '''PowerLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2333.PowerLoad)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6772.PowerLoadLoadCase':
        '''PowerLoadLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6772.PowerLoadLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None
