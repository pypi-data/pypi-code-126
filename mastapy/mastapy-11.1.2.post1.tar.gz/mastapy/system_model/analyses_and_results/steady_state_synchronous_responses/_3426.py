'''_3426.py

KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse
'''


from mastapy.system_model.connections_and_sockets.gears import _2181
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6749
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3423
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse',)


class KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse(_3423.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse):
    '''KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse

    This is a mastapy class.
    '''

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2181.KlingelnbergCycloPalloidHypoidGearMesh':
        '''KlingelnbergCycloPalloidHypoidGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2181.KlingelnbergCycloPalloidHypoidGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_load_case(self) -> '_6749.KlingelnbergCycloPalloidHypoidGearMeshLoadCase':
        '''KlingelnbergCycloPalloidHypoidGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6749.KlingelnbergCycloPalloidHypoidGearMeshLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase is not None else None
