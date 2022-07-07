'''_5299.py

KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis
'''


from mastapy.system_model.connections_and_sockets.gears import _2181
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6749
from mastapy.system_model.analyses_and_results.mbd_analyses import _5296
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis',)


class KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis(_5296.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis):
    '''KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis.TYPE'):
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
