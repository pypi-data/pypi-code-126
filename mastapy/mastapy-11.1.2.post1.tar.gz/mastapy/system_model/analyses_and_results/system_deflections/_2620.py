'''_2620.py

HypoidGearSystemDeflection
'''


from mastapy.system_model.part_model.gears import _2394
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6738
from mastapy.system_model.analyses_and_results.power_flows import _3949
from mastapy.gears.rating.hypoid import _410
from mastapy.system_model.analyses_and_results.system_deflections import _2551
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'HypoidGearSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSystemDeflection',)


class HypoidGearSystemDeflection(_2551.AGMAGleasonConicalGearSystemDeflection):
    '''HypoidGearSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _HYPOID_GEAR_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearSystemDeflection.TYPE'):
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

    @property
    def power_flow_results(self) -> '_3949.HypoidGearPowerFlow':
        '''HypoidGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3949.HypoidGearPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults is not None else None

    @property
    def component_detailed_analysis(self) -> '_410.HypoidGearRating':
        '''HypoidGearRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_410.HypoidGearRating)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis is not None else None
