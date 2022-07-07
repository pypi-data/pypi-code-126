'''_2693.py

WormGearSystemDeflection
'''


from mastapy.system_model.part_model.gears import _2411
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6815
from mastapy.system_model.analyses_and_results.power_flows import _4013
from mastapy.gears.rating.worm import _345
from mastapy.system_model.analyses_and_results.system_deflections import _2616
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'WormGearSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSystemDeflection',)


class WormGearSystemDeflection(_2616.GearSystemDeflection):
    '''WormGearSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _WORM_GEAR_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2411.WormGear':
        '''WormGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2411.WormGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6815.WormGearLoadCase':
        '''WormGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6815.WormGearLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def power_flow_results(self) -> '_4013.WormGearPowerFlow':
        '''WormGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_4013.WormGearPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults is not None else None

    @property
    def component_detailed_analysis(self) -> '_345.WormGearRating':
        '''WormGearRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_345.WormGearRating)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis is not None else None
