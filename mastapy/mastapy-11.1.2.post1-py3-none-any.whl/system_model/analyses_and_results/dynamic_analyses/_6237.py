'''_6237.py

WormGearDynamicAnalysis
'''


from mastapy.system_model.part_model.gears import _2411
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6815
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6172
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'WormGearDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearDynamicAnalysis',)


class WormGearDynamicAnalysis(_6172.GearDynamicAnalysis):
    '''WormGearDynamicAnalysis

    This is a mastapy class.
    '''

    TYPE = _WORM_GEAR_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearDynamicAnalysis.TYPE'):
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
