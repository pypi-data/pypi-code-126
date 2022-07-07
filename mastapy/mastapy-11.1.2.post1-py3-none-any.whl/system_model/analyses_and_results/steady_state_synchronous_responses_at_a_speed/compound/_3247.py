'''_3247.py

BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed
'''


from typing import List

from mastapy.system_model.part_model import _2305
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3116
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3325
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound', 'BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed',)


class BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed(_3325.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed):
    '''BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    '''

    TYPE = _BOLTED_JOINT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2305.BoltedJoint':
        '''BoltedJoint: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2305.BoltedJoint)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def assembly_design(self) -> '_2305.BoltedJoint':
        '''BoltedJoint: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2305.BoltedJoint)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3116.BoltedJointSteadyStateSynchronousResponseAtASpeed]':
        '''List[BoltedJointSteadyStateSynchronousResponseAtASpeed]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_3116.BoltedJointSteadyStateSynchronousResponseAtASpeed))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3116.BoltedJointSteadyStateSynchronousResponseAtASpeed]':
        '''List[BoltedJointSteadyStateSynchronousResponseAtASpeed]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_3116.BoltedJointSteadyStateSynchronousResponseAtASpeed))
        return value
