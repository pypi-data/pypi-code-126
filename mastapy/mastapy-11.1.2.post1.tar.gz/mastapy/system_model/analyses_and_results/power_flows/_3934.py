'''_3934.py

CylindricalGearPowerFlow
'''


from mastapy.system_model.part_model.gears import _2385, _2387
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6695, _6700
from mastapy.gears.rating.cylindrical import _428
from mastapy.system_model.analyses_and_results.power_flows import _3945
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'CylindricalGearPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearPowerFlow',)


class CylindricalGearPowerFlow(_3945.GearPowerFlow):
    '''CylindricalGearPowerFlow

    This is a mastapy class.
    '''

    TYPE = _CYLINDRICAL_GEAR_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2385.CylindricalGear':
        '''CylindricalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2385.CylindricalGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to CylindricalGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6695.CylindricalGearLoadCase':
        '''CylindricalGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _6695.CylindricalGearLoadCase.TYPE not in self.wrapped.ComponentLoadCase.__class__.__mro__:
            raise CastException('Failed to cast component_load_case to CylindricalGearLoadCase. Expected: {}.'.format(self.wrapped.ComponentLoadCase.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentLoadCase.__class__)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def component_detailed_analysis(self) -> '_428.CylindricalGearRating':
        '''CylindricalGearRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_428.CylindricalGearRating)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis is not None else None
