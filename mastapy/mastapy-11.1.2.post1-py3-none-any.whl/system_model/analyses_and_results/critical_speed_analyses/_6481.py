'''_6481.py

SpiralBevelGearSetCriticalSpeedAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2404
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6788
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6479, _6480, _6396
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'SpiralBevelGearSetCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearSetCriticalSpeedAnalysis',)


class SpiralBevelGearSetCriticalSpeedAnalysis(_6396.BevelGearSetCriticalSpeedAnalysis):
    '''SpiralBevelGearSetCriticalSpeedAnalysis

    This is a mastapy class.
    '''

    TYPE = _SPIRAL_BEVEL_GEAR_SET_CRITICAL_SPEED_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearSetCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2404.SpiralBevelGearSet':
        '''SpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2404.SpiralBevelGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6788.SpiralBevelGearSetLoadCase':
        '''SpiralBevelGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6788.SpiralBevelGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def spiral_bevel_gears_critical_speed_analysis(self) -> 'List[_6479.SpiralBevelGearCriticalSpeedAnalysis]':
        '''List[SpiralBevelGearCriticalSpeedAnalysis]: 'SpiralBevelGearsCriticalSpeedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearsCriticalSpeedAnalysis, constructor.new(_6479.SpiralBevelGearCriticalSpeedAnalysis))
        return value

    @property
    def spiral_bevel_meshes_critical_speed_analysis(self) -> 'List[_6480.SpiralBevelGearMeshCriticalSpeedAnalysis]':
        '''List[SpiralBevelGearMeshCriticalSpeedAnalysis]: 'SpiralBevelMeshesCriticalSpeedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelMeshesCriticalSpeedAnalysis, constructor.new(_6480.SpiralBevelGearMeshCriticalSpeedAnalysis))
        return value
