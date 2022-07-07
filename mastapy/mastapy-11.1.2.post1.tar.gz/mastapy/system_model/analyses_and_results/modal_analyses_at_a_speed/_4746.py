'''_4746.py

HypoidGearSetModalAnalysisAtASpeed
'''


from typing import List

from mastapy.system_model.part_model.gears import _2395
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6740
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _4745, _4744, _4688
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed', 'HypoidGearSetModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSetModalAnalysisAtASpeed',)


class HypoidGearSetModalAnalysisAtASpeed(_4688.AGMAGleasonConicalGearSetModalAnalysisAtASpeed):
    '''HypoidGearSetModalAnalysisAtASpeed

    This is a mastapy class.
    '''

    TYPE = _HYPOID_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearSetModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2395.HypoidGearSet':
        '''HypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2395.HypoidGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6740.HypoidGearSetLoadCase':
        '''HypoidGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6740.HypoidGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def hypoid_gears_modal_analysis_at_a_speed(self) -> 'List[_4745.HypoidGearModalAnalysisAtASpeed]':
        '''List[HypoidGearModalAnalysisAtASpeed]: 'HypoidGearsModalAnalysisAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearsModalAnalysisAtASpeed, constructor.new(_4745.HypoidGearModalAnalysisAtASpeed))
        return value

    @property
    def hypoid_meshes_modal_analysis_at_a_speed(self) -> 'List[_4744.HypoidGearMeshModalAnalysisAtASpeed]':
        '''List[HypoidGearMeshModalAnalysisAtASpeed]: 'HypoidMeshesModalAnalysisAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidMeshesModalAnalysisAtASpeed, constructor.new(_4744.HypoidGearMeshModalAnalysisAtASpeed))
        return value
