'''_6505.py

WormGearSetCriticalSpeedAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2412
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6817
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6503, _6504, _6440
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'WormGearSetCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetCriticalSpeedAnalysis',)


class WormGearSetCriticalSpeedAnalysis(_6440.GearSetCriticalSpeedAnalysis):
    '''WormGearSetCriticalSpeedAnalysis

    This is a mastapy class.
    '''

    TYPE = _WORM_GEAR_SET_CRITICAL_SPEED_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearSetCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2412.WormGearSet':
        '''WormGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2412.WormGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6817.WormGearSetLoadCase':
        '''WormGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6817.WormGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def worm_gears_critical_speed_analysis(self) -> 'List[_6503.WormGearCriticalSpeedAnalysis]':
        '''List[WormGearCriticalSpeedAnalysis]: 'WormGearsCriticalSpeedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearsCriticalSpeedAnalysis, constructor.new(_6503.WormGearCriticalSpeedAnalysis))
        return value

    @property
    def worm_meshes_critical_speed_analysis(self) -> 'List[_6504.WormGearMeshCriticalSpeedAnalysis]':
        '''List[WormGearMeshCriticalSpeedAnalysis]: 'WormMeshesCriticalSpeedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormMeshesCriticalSpeedAnalysis, constructor.new(_6504.WormGearMeshCriticalSpeedAnalysis))
        return value
