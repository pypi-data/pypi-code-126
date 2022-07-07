'''_3411.py

FaceGearSetSteadyStateSynchronousResponse
'''


from typing import List

from mastapy.system_model.part_model.gears import _2389
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6719
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3412, _3410, _3416
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'FaceGearSetSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetSteadyStateSynchronousResponse',)


class FaceGearSetSteadyStateSynchronousResponse(_3416.GearSetSteadyStateSynchronousResponse):
    '''FaceGearSetSteadyStateSynchronousResponse

    This is a mastapy class.
    '''

    TYPE = _FACE_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearSetSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2389.FaceGearSet':
        '''FaceGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2389.FaceGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6719.FaceGearSetLoadCase':
        '''FaceGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6719.FaceGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def face_gears_steady_state_synchronous_response(self) -> 'List[_3412.FaceGearSteadyStateSynchronousResponse]':
        '''List[FaceGearSteadyStateSynchronousResponse]: 'FaceGearsSteadyStateSynchronousResponse' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearsSteadyStateSynchronousResponse, constructor.new(_3412.FaceGearSteadyStateSynchronousResponse))
        return value

    @property
    def face_meshes_steady_state_synchronous_response(self) -> 'List[_3410.FaceGearMeshSteadyStateSynchronousResponse]':
        '''List[FaceGearMeshSteadyStateSynchronousResponse]: 'FaceMeshesSteadyStateSynchronousResponse' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceMeshesSteadyStateSynchronousResponse, constructor.new(_3410.FaceGearMeshSteadyStateSynchronousResponse))
        return value
