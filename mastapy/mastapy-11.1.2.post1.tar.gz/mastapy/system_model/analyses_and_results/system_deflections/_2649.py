'''_2649.py

RingPinsSystemDeflection
'''


from mastapy.system_model.part_model.cycloidal import _2430
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6776
from mastapy.system_model.analyses_and_results.power_flows import _3977
from mastapy.system_model.analyses_and_results.system_deflections import _2637
from mastapy._internal.python_net import python_net_import

_RING_PINS_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'RingPinsSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('RingPinsSystemDeflection',)


class RingPinsSystemDeflection(_2637.MountableComponentSystemDeflection):
    '''RingPinsSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _RING_PINS_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RingPinsSystemDeflection.TYPE'):
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

    @property
    def power_flow_results(self) -> '_3977.RingPinsPowerFlow':
        '''RingPinsPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3977.RingPinsPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults is not None else None
