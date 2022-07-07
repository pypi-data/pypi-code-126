'''_3096.py

ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
'''


from typing import List

from mastapy.system_model.part_model.gears import _2414
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3094, _3095, _2986
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _2966
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound', 'ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft',)


class ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft(_2986.BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft):
    '''ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    '''

    TYPE = _ZEROL_BEVEL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2414.ZerolBevelGearSet':
        '''ZerolBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2414.ZerolBevelGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def assembly_design(self) -> '_2414.ZerolBevelGearSet':
        '''ZerolBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2414.ZerolBevelGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def zerol_bevel_gears_compound_steady_state_synchronous_response_on_a_shaft(self) -> 'List[_3094.ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft]: 'ZerolBevelGearsCompoundSteadyStateSynchronousResponseOnAShaft' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearsCompoundSteadyStateSynchronousResponseOnAShaft, constructor.new(_3094.ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def zerol_bevel_meshes_compound_steady_state_synchronous_response_on_a_shaft(self) -> 'List[_3095.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft]: 'ZerolBevelMeshesCompoundSteadyStateSynchronousResponseOnAShaft' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelMeshesCompoundSteadyStateSynchronousResponseOnAShaft, constructor.new(_3095.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_2966.ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft]':
        '''List[ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_2966.ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_2966.ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft]':
        '''List[ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_2966.ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft))
        return value
