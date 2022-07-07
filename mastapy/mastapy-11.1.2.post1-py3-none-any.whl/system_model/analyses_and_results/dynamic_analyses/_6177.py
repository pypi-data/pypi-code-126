'''_6177.py

HypoidGearMeshDynamicAnalysis
'''


from mastapy.system_model.connections_and_sockets.gears import _2177
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6739
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6118
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'HypoidGearMeshDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearMeshDynamicAnalysis',)


class HypoidGearMeshDynamicAnalysis(_6118.AGMAGleasonConicalGearMeshDynamicAnalysis):
    '''HypoidGearMeshDynamicAnalysis

    This is a mastapy class.
    '''

    TYPE = _HYPOID_GEAR_MESH_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearMeshDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2177.HypoidGearMesh':
        '''HypoidGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2177.HypoidGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_load_case(self) -> '_6739.HypoidGearMeshLoadCase':
        '''HypoidGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6739.HypoidGearMeshLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase is not None else None
