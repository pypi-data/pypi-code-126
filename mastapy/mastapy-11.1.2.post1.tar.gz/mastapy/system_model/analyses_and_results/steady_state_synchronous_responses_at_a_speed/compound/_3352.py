'''_3352.py

WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed
'''


from typing import List

from mastapy.system_model.part_model.gears import _2412
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3350, _3351, _3287
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3222
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound', 'WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed',)


class WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed(_3287.GearSetCompoundSteadyStateSynchronousResponseAtASpeed):
    '''WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    '''

    TYPE = _WORM_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2412.WormGearSet':
        '''WormGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2412.WormGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def assembly_design(self) -> '_2412.WormGearSet':
        '''WormGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2412.WormGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def worm_gears_compound_steady_state_synchronous_response_at_a_speed(self) -> 'List[_3350.WormGearCompoundSteadyStateSynchronousResponseAtASpeed]':
        '''List[WormGearCompoundSteadyStateSynchronousResponseAtASpeed]: 'WormGearsCompoundSteadyStateSynchronousResponseAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearsCompoundSteadyStateSynchronousResponseAtASpeed, constructor.new(_3350.WormGearCompoundSteadyStateSynchronousResponseAtASpeed))
        return value

    @property
    def worm_meshes_compound_steady_state_synchronous_response_at_a_speed(self) -> 'List[_3351.WormGearMeshCompoundSteadyStateSynchronousResponseAtASpeed]':
        '''List[WormGearMeshCompoundSteadyStateSynchronousResponseAtASpeed]: 'WormMeshesCompoundSteadyStateSynchronousResponseAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormMeshesCompoundSteadyStateSynchronousResponseAtASpeed, constructor.new(_3351.WormGearMeshCompoundSteadyStateSynchronousResponseAtASpeed))
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3222.WormGearSetSteadyStateSynchronousResponseAtASpeed]':
        '''List[WormGearSetSteadyStateSynchronousResponseAtASpeed]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_3222.WormGearSetSteadyStateSynchronousResponseAtASpeed))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3222.WormGearSetSteadyStateSynchronousResponseAtASpeed]':
        '''List[WormGearSetSteadyStateSynchronousResponseAtASpeed]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_3222.WormGearSetSteadyStateSynchronousResponseAtASpeed))
        return value
