'''_6951.py

StraightBevelGearAdvancedTimeSteppingAnalysisForModulation
'''


from mastapy.system_model.part_model.gears import _2407
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6795
from mastapy.system_model.analyses_and_results.system_deflections import _2673
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6858
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'StraightBevelGearAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearAdvancedTimeSteppingAnalysisForModulation',)


class StraightBevelGearAdvancedTimeSteppingAnalysisForModulation(_6858.BevelGearAdvancedTimeSteppingAnalysisForModulation):
    '''StraightBevelGearAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    '''

    TYPE = _STRAIGHT_BEVEL_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelGearAdvancedTimeSteppingAnalysisForModulation.TYPE'):
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

    @property
    def system_deflection_results(self) -> '_2673.StraightBevelGearSystemDeflection':
        '''StraightBevelGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2673.StraightBevelGearSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None
