'''_6942.py

SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation
'''


from mastapy.system_model.part_model.gears import _2403
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6786
from mastapy.system_model.analyses_and_results.system_deflections import _2664
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6858
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation',)


class SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation(_6858.BevelGearAdvancedTimeSteppingAnalysisForModulation):
    '''SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    '''

    TYPE = _SPIRAL_BEVEL_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2403.SpiralBevelGear':
        '''SpiralBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2403.SpiralBevelGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6786.SpiralBevelGearLoadCase':
        '''SpiralBevelGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6786.SpiralBevelGearLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def system_deflection_results(self) -> '_2664.SpiralBevelGearSystemDeflection':
        '''SpiralBevelGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2664.SpiralBevelGearSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None
